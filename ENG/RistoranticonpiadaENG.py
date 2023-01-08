
import os
import numpy as np
import sys
import pandas as pd
import xlsxwriter


d=pd.read_excel('recensioniENG.xlsx')  

ristoranti=d.iloc[:,0]
recensioni=d.iloc[:, 1:-1]
res={}
for ristorante in ristoranti:
    i=1
    res[ristorante]="0"
    for r in recensioni.iloc[i]:
        try:
            if "piad" in r:
                res[ristorante]="1"   
                break
            i+=1
        except:
            pass
        
workbook = xlsxwriter.Workbook('ristoranticonpiadaENG.xlsx')
worksheet = workbook.add_worksheet()

row = 0
for key in res.keys():
    worksheet.write(row, 0, key)
    worksheet.write_row(row, 1, res[key])
    row += 1

workbook.close()
