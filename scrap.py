import datetime
import logging
import pprint
import re
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

logging.getLogger().setLevel(logging.INFO)

def replaceNbsp (string):
    return string.replace(u"\xa0", " ")

def scrapMember (url):
    memberPage = requests.get(url)
    memberSoup = BeautifulSoup(memberPage.content, "html.parser", from_encoding="windows-1250")
    member = {
        "id": re.search("id=(.*)", url)[1],
        "name": replaceNbsp(memberSoup.h1.string),
        "assistants": [],
    }
    if memberSoup.address is not None:
        member["address"] = replaceNbsp(memberSoup.address.get_text())
    for assistant in memberSoup.select("ul.assistants li strong"):
        member["assistants"].append(replaceNbsp(assistant.string))
    logging.info("Scrapped member " + member["name"] + " from " + url)
    return member

def scrapSnapshot ():
    DOMAIN = "http://www.psp.cz/sqw/"
    listPage = requests.get(DOMAIN + "hp.sqw?k=192")
    listSoup = BeautifulSoup(listPage.content, "html.parser", from_encoding="windows-1250")
    snapshot = {
        "timestamp": datetime.datetime.now(),
        "members": [],
    }
    for memberLink in listSoup.select(".person-list .name a"):
        snapshot["members"].append(scrapMember(DOMAIN + memberLink["href"]))
    logging.info("Scrapped " + str(len(snapshot["members"])) + " members.")
    return snapshot

def saveSnapshot(snapshot):
    client = MongoClient("mongodb://localhost")
    db=client.ass_track
    db.snapshots.insert_one(snapshot)
    logging.info("Snapshot persisted in database.")

snapshot = scrapSnapshot()
saveSnapshot(snapshot)
