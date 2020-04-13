import PyPDF2
import os
import subprocess
from PyPDF2 import PdfFileReader

#os.chgdir()

print (os.getcwd())

file_name = '65231mar312020.pdf'


file = open(file_name, 'rb')

pdfreader = PyPDF2.PdfFileReader(file)

print(pdfreader.getNumPages())

pageobj = pdfreader.getPage(2)

print(pageobj.extractText())





