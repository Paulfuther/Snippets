from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter  # process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

#from cStringIO import StringIO

import io
from io import BytesIO
import pandas


file_name = '65231mar312020.pdf'

def pdf_to_text(pdfname):

    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()
    #print(text)
    # Cleanup
    device.close()
    sio.close()

    print(text)

    return text

pdf_to_text(file_name)

f=open("text2.txt",'w')
#f.write(text)

#print(f)
