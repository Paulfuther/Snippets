import tabula
from tabula import read_pdf, convert_into
import os
import subprocess
print(os.getcwd())

file_name = '65231mar312020.pdf'


#df = read_pdf(file_name, guess='false', encoding='utf-8')
#
# print(df)

df2= tabula.read_pdf(file_name, pages = 'all')

tabula.convert_into(file_name, "output.csv", output_format="csv", pages = 'all')
print(df2)
