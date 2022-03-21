
import PyPDF2
import os
import glob
from tika import parser

os.chdir('/home/saul/pythontraining/NLP')
print(glob.glob("*.pdf"))

pdfFileObj = open('GassBill2.pdf','rb')     
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)        #'0' is the page number
pageObj.extractText()
raw = parser.from_file('GassBill2.pdf')
print(raw['content'])
