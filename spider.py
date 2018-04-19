import datetime
import logging
import re
import requests
from bs4 import BeautifulSoup

import config

def replace_nbsp (string):
    return string.replace(u"\xa0", " ")

def scrap_member (url):
    member_page = requests.get(url)
    member_soup = BeautifulSoup(member_page.content, "html.parser", from_encoding="windows-1250")
    member = {
        "id": re.search("id=(.*)", url).group(1),
        "name": replace_nbsp(member_soup.h1.string),
        "assistants": [],
    }
    if member_soup.address is not None:
        member["address"] = replace_nbsp(member_soup.address.get_text())
    for assistant in member_soup.select("ul.assistants li strong"):
        member["assistants"].append(replace_nbsp(assistant.string))
    logging.debug("Scrapped member " + member["name"] + " from " + url)
    return member

def scrap_snapshot ():
    DOMAIN = "http://www.psp.cz/sqw/"
    list_page = requests.get(DOMAIN + "hp.sqw?k=192")
    list_soup = BeautifulSoup(list_page.content, "html.parser", from_encoding="windows-1250")
    snapshot = {
        "timestamp": datetime.datetime.now(),
        "members": [],
    }
    links = list_soup.select(".person-list .name a")
    links = links if config.IS_PRODUCTION else links[0:3]
    for link in links:
        snapshot["members"].append(scrap_member(DOMAIN + link["href"]))
    logging.info("Scrapped " + str(len(snapshot["members"])) + " members.")
    return snapshot
