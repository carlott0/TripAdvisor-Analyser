from bs4 import BeautifulSoup
import os
import urllib.request
from requests_html import HTMLSession

import sys
import pandas as pd
from string import digits


session = HTMLSession()

session.headers.update({
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
})
d=pd.read_excel('risultati.xlsx', index_col=1)  
r=d['LINK']
links=[]
for el in r:
    links.append(el)
    
f=open("./recensioni.txt", "a", encoding="utf-8")
i=0
for l in links:
    print("Obtaining reviews from: "+l)
    r=session.get(l)

    soup= BeautifulSoup(r.content, "html.parser")
    for div in soup.find_all("div", {'class':'entry'}):
        try:
            f.write(str(div).split("<p class=\"partial_entry\">")[1].split("</span>")[0])
            i+=1
            f.write("\n")        
        except Exception as e:
            pass
f.close()


print("Scritte "+str(i)+" recensioni su file: recensioni.txt")