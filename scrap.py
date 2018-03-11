import re
import requests
import datetime
from bs4 import BeautifulSoup

DOMAIN = "http://www.psp.cz/sqw/"
page = requests.get(DOMAIN + "hp.sqw?k=192")
soupList = BeautifulSoup(page.content, "html.parser", from_encoding="windows-1250")
timestamp = datetime.datetime.now().strftime("%d.%m.%Y")

print(soupList.title.string)

#print header
print("\"poradi\";\"casova_znamka\";\"poslanec_odkaz\";\"poslanec_jmeno\";\"poslanec_adresa\";\"asistent_jmeno\"")

i = 1
for memberLink in soupList.find_all("span", "name"):
    detailPage = requests.get(DOMAIN + memberLink.a['href'])
    soupMember = BeautifulSoup(detailPage.content, "html.parser", from_encoding="windows-1250")
    for memberAssistantCollection in soupMember.find_all("ul", "assistants"):
        for memberAssistant in memberAssistantCollection.find_all("strong"):
            # Adresa
            addressMember = str(soupMember.address)
            #print addressMember
            address = "Neuvedena"
            #print type(addressMember)
            if (addressMember != "None"):
                addressReg = re.search('^<address.*?>([^<]*)', addressMember)
                address = str(addressReg.group(1))

            # Record
            print("\"" + str(i) + "\";\"" + timestamp + "\";\"" + DOMAIN + memberLink.a['href'] + "\";\"" + soupMember.h1.string + "\";\"" + address + "\";\"" + memberAssistant.string + "\"")
    i += 1
