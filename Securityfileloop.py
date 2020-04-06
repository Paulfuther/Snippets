import pandas as pd
import numpy
import openpyxl
import xlrd
import xlwt
import xlsxwriter
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename , asksaveasfile
import re
import os, sys
import glob
from datetime import datetime
import datetime as dt

start = datetime.strptime('07:15:00', '%H:%M:%S').time()
end = datetime.strptime('23:45:00', '%H:%M:%S').time()

os.chdir('/Users/paulf/Dropbox/BACK OFFICE SECURITY FILE/')
print (os.getcwd())
FileList = glob.glob('*.rtf')
print (FileList)

newdf=[]

for x in FileList:
    inputfilename=x
    excel_file=inputfilename
    store_number=x
    a=str(store_number)
    print(a)
    b=re.search('\d+', a).group()
    print(b)
    print (store_number)

    df=pd.read_csv(excel_file, sep='\t', header=None)
    df.columns=['Text']
    print(df.dtypes)
    print(df.head)

    df2=df[df['Text'].str.contains('Pump',na=False)].copy()
    print(df2)

    if df2.empty:
        continue


    df2['Time'] = df2['Text'].str.extract('(..:..:..)', expand=True)
    df2['Time'] = pd.to_datetime(df2['Time'],format= '%H:%M:%S' ).dt.time
    df2 = df2[df2['Time'].between(start, end)]

    df2['Date'] = df2['Text'].str.slice(start=0, stop =9)
    df2['Date'] = pd.to_datetime(df2['Date'], format='%d %b %y').dt.date
    #df2['Date']=df2['Date'].datetime.strptime(b1, "%d %m %y").strftime("%b-%Y")


    df2['Store']=b
    print (df2)
    newdf.append(df2)

newdf=pd.concat(newdf)

newdf.to_excel("Pumps to Prepay" + ".xlsx", engine='xlsxwriter')
print (newdf.dtypes)
