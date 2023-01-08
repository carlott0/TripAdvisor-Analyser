
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
i=1
offsett=0
fine=0
giro=True

nomi=[]
stelle=[]
links=[]
recensioni=[]




print("Inserire un link di una città su tripadvisor per ottenere i suoi ristoranti.")
print("Es: https://www.tripadvisor.it/Restaurants-g187807-Rimini_Province_of_Rimini_Emilia_Romagna-Vacations.html")
#input_link=input()
input_link="https://www.tripadvisor.com/Restaurants-g194878-Riccione_Province_of_Rimini_Emilia_Romagna.html"
geocode=input_link.split("-g")[1].split("-")[0]

while(giro):
    
    offsett=i*30
    i+=1
    items=[]
    
    link="https://www.tripadvisor.com/RestaurantSearch?Action=PAGE&ajax=1&availSearchEnabled=true&sortOrder=popularity&geo="+geocode+"&itags=10591&eaterydate=2022_04_11&date=2022-04-12&time=20:00:00&people=2&o=a"+str(offsett)
    r=session.get(link)
    
    soup= BeautifulSoup(r.content, "html.parser")
    try:
        if soup.find("span",{"class","nav next disabled"})!=None:
            print("esco")
            break
    except:
        continue
    items=soup.find_all("div",{"class", "YHnoF Gi o"})
    print("Analisi primi",offsett, "ristoranti")
    for it in items:
        #stelle:
        stelle.append(str(it.find("svg", {"class","UctUV d H0"})['aria-label']).split(" of")[0])
        #nomi
        nomi.append(str(it.find("a",{"class","Lwqic Cj b"}).text))
        #links
        links.append("https://www.tripadvisor.com"+str(it.find("a",{"class","Lwqic Cj b"})['href']))
        recensioni.append(it.find("span", {'class':'IiChw'}).text.replace("reviews","")) 
print("Totale ristoranti: ",str(len(links)))

diz=[]
for n in zip(nomi,links,stelle, recensioni):
    diz.append(n)


d=pd.DataFrame.from_records(diz, columns=['NOME', 'LINK', 'STELLE', 'RECENSIONI'])


d.to_excel('risultatiENG.xlsx')

print("Salvati i risultati in risultatiENG.xlxs")