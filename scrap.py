import requests
import datetime
import pprint
from bs4 import BeautifulSoup

DOMAIN = "http://www.psp.cz/sqw/"
listPage = requests.get(DOMAIN + "hp.sqw?k=192")
listSoup = BeautifulSoup(listPage.content, "html.parser", from_encoding="windows-1250")
timestamp = datetime.datetime.now().strftime("%d.%m.%Y")

def replaceNbsp (string):
    return string.replace(u"\xa0", " ")

for memberLink in listSoup.select(".person-list .name a"):
    memberPage = requests.get(DOMAIN + memberLink["href"])
    memberSoup = BeautifulSoup(memberPage.content, "html.parser", from_encoding="windows-1250")
    member = {
        "name": replaceNbsp(memberSoup.h1.string),
        "address": replaceNbsp(memberSoup.address.get_text()),
        "assistants": [],
        "url": memberLink["href"],
        "timestamp": timestamp
    }
    for assistant in memberSoup.select("ul.assistants li strong"):
        member["assistants"].append(replaceNbsp(assistant.string))

    pprint.pprint(member)
