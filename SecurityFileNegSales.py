import pandas as pd
import numpy
import openpyxl
import xlrd
import xlwt
import xlsxwriter
import re
import os, sys
import glob
from datetime import datetime
import datetime as dt



#start = datetime.strptime('05:15:00', '%H:%M:%S').time()
#end = datetime.strptime('11:45:00', '%H:%M:%S').time()

# set working directory to the folder on drop box that has the files stored in it.


os.chdir('/Users/paulf/Dropbox/BACK OFFICE SECURITY FILE/')
#print (os.getcwd())
FileList = glob.glob('*.rtf')
#print (FileList)


newdf=[]

for x in FileList:
    inputfilename=x
    excel_file=inputfilename
    store_number=x
    a=str(store_number)
    b=re.search('\d+', a).group()
    df=pd.read_csv(excel_file, sep='\t', header=None)
    df.columns=['Text']
    df['Date'] = df['Text'].str.extract('(.. ... ..)', expand=False).copy()
    
    df2=df[df['Text'].str.contains('NEGATIVE',na=False)].copy()
    
    if df2.empty:
        continue

    df2['Store']=b
    print (df2)
    newdf.append(df2)

    
    
newdf=pd.concat(newdf)

newdf['Date'] = pd.to_datetime(newdf['Date'], dayfirst=True)#.dt.strftime('%d %m %Y')

newdf['Time'] = newdf['Text'].str.extract(r"([\d]{1,2}\:[\d]{1,2}\:[\d]{1,2})")
newdf['Time'] = pd.to_datetime(newdf['Time'], format='%H:%M:%S').dt.time
newdf.set_index('Date', inplace=True)


newdf.to_excel("Negative Sales" + ".xlsx", engine='xlsxwriter')
print (newdf.dtypes)
