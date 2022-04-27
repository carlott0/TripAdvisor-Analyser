
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
input_link=input()
geocode=input_link.split("-g")[1].split("-")[0]

while(giro):
    
    offsett=i*30
    i+=1
    
    
    link="https://www.tripadvisor.it/RestaurantSearch?Action=PAGE&ajax=1&availSearchEnabled=true&sortOrder=popularity&geo="+geocode+"&itags=10591&eaterydate=2022_04_11&date=2022-04-12&time=20:00:00&people=2&o=a"+str(offsett)
    r=session.get(link)

    soup= BeautifulSoup(r.content, "html.parser")
    div=soup.find("div", )
    
    div=soup.find("div", {'class':'OhCyu'})
    value=str(div).split('_blank">')[1].split("<")[0]
    print("Analisi primi",offsett, "ristoranti")
    if fine==1 and value=="1":
        giro=False
        break
    if fine==0 and value=="1":
        fine=1
    for div in soup.find_all("div", {'class':'OhCyu'}): 
        remove_digits = div.text.maketrans('', '', digits)
        remove_point = div.text.maketrans('','','.')
        s = div.text.translate(remove_digits).translate(remove_point)
        
        nomi.append(s)
        links.append("https://www.tripadvisor.it"+str(div).split("href=\"")[1].split(" target=")[0])
    for div in soup.find_all("div", {'class':'bhDlF bPJHV'}): 
        try:
            stelle.append(str(div).split("Punteggio ")[1].split(" su")[0])
        except Exception as e:
            pass
    for div in soup.find_all("span", {'class':'NoCoR'}): 
        s= str(div.text).replace('recensioni','')
        recensioni.append(s)
    

print("Totale ristoranti: ",str(len(links)))



diz=[]
for n in zip(nomi,links,stelle, recensioni):
    diz.append(n)


d=pd.DataFrame.from_records(diz, columns=['NOME', 'LINK', 'STELLE', 'RECENSIONI'])


d.to_excel('risultati.xlsx')

print("Salvati i risultati in risultati.xlxs")
