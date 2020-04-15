import pandas as pd
import numpy
import openpyxl
import xlrd
import xlwt
import xlsxwriter
import re
import os
import sys
import glob
from datetime import datetime
import datetime as dt


# set parameters for times that pumps are allowed to be on prepay.
# pumps should not be on prepay between 07:15 and 23:45.


start = datetime.strptime('07:15:00', '%H:%M:%S').time()
end = datetime.strptime('23:45:00', '%H:%M:%S').time()

os.chdir('/Users/paulf/Dropbox/BACK OFFICE SECURITY FILE/')
FileList = glob.glob('*.rtf')

newdf = []

for x in FileList:
    inputfilename = x
    excel_file = inputfilename
    store_number = x
    a = str(store_number)
    b = re.search('\d+', a).group()
    df = pd.read_csv(excel_file, sep='\t', header=None)
    df.columns = ['Text']
    
    #use regular expresssions re to find character sets in a string of data
    #in a dataframe.
    
    df['Date'] = df['Text'].str.extract(r"([\d]{1,2} [ADJFMNOS]\w* [\d]{2})" ).copy()
    df2 = df[df['Text'].str.contains('Pump', na=False)].copy()
    
    if df2.empty:
        continue

    df2['Store'] = b
    print(df2)
    newdf.append(df2)

newdf = pd.concat(newdf)


newdf['Date'] = pd.to_datetime(newdf['Date'], dayfirst=True)
newdf['Time'] = newdf['Text'].str.extract(r"([\d]{1,2}\:[\d]{1,2}\:[\d]{1,2})")
newdf['Time'] = pd.to_datetime(newdf['Time'], format='%H:%M:%S').dt.time
newdf = newdf[newdf['Time'].between(start, end)]


newdf.set_index('Date', inplace=True)

newdf.to_excel("Pumps to Prepay" + ".xlsx", engine='xlsxwriter')
#print(newdf.dtypes)
