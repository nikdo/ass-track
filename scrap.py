import datetime
import logging
import pprint
import re
import requests
from bs4 import BeautifulSoup

logging.getLogger().setLevel(logging.INFO)

def replaceNbsp (string):
    return string.replace(u"\xa0", " ")

def scrapMember (url):
    memberPage = requests.get(url)
    memberSoup = BeautifulSoup(memberPage.content, "html.parser", from_encoding="windows-1250")
    member = {
        "id": re.search("id=(.*)", url)[1],
        "name": replaceNbsp(memberSoup.h1.string),
        "address": replaceNbsp(memberSoup.address.get_text()),
        "assistants": [],
    }
    for assistant in memberSoup.select("ul.assistants li strong"):
        member["assistants"].append(replaceNbsp(assistant.string))
    logging.info("Scrapped member " + member["name"] + " from " + url)
    return member

def scrapSnapshot ():
    DOMAIN = "http://www.psp.cz/sqw/"
    listPage = requests.get(DOMAIN + "hp.sqw?k=192")
    listSoup = BeautifulSoup(listPage.content, "html.parser", from_encoding="windows-1250")
    snapshot = {
        "timestamp": datetime.datetime.now().strftime("%d.%m.%Y"),
        "members": [],
    }
    for memberLink in listSoup.select(".person-list .name a"):
        snapshot["members"].append(scrapMember(DOMAIN + memberLink["href"]))
    logging.info("Scrapped " + str(len(snapshot["members"])) + " members.")
    return snapshot

pprint.pprint(scrapSnapshot())
