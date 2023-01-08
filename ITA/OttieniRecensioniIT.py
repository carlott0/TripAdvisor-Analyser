from bs4 import BeautifulSoup
import os
import urllib.request
from requests_html import HTMLSession
import numpy as np
import sys
import pandas as pd
from string import digits
import xlsxwriter

session = HTMLSession()

session.headers.update({
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
})
d=pd.read_excel('risultatiIT.xlsx')  
r=d['LINK']
n=d['NOME']
links=[]
for el in r:
    links.append(el)
    

i=0
k=0
diz={}
for l in links:
    print("Obtaining reviews from: "+l)
    pre=l.split("-Reviews-")[0]
    post=l.split("-Reviews-")[1]
    nome=n[k]
    k+=1
    nuovi_links=[]
    #nuovi_links.append(l)
    for x in np.arange(10,100,10):
        t=pre+"-Reviews-or"+str(x)+"-"+post
        nuovi_links.append(t)
    diz[nome]=[]
    
    for nl in nuovi_links:
        r=session.get(nl)
        try:
            soup= BeautifulSoup(r.content, "html.parser")
            for div in soup.find_all("p", {'class':'partial_entry'}):
                diz[nome].append(div.text)
                i+=1      
        except:
            pass

workbook = xlsxwriter.Workbook('recensioniIT.xlsx')
worksheet = workbook.add_worksheet()



row = 0
for key in diz.keys():
    worksheet.write(row, 0, key)
    worksheet.write_row(row, 1, diz[key])
    row += 1

workbook.close()
