# -*- coding: utf-8 -*-
#import pdfminer.six
#import pdfminer3k
#import pdfminer
import os
import sys, getopt
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
#import pdfminer.six
from pdfminer.pdfpage import PDFPage

os.chdir('/home/saul/pdfwork')
path = 'sample.pdf'

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    print("FP :", fp)

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, 
                                  password=password,
                                  caching=caching, 
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
        print(interpreter.process_page(page))
        
    print(converter)
    infile.close() 
    converter.close()
    text = output.getvalue()
    output.close
    #Save pdf file to text
    with open('texted.txt','w') as f:
        f.write(text)   
    return text 
if __name__ == '__main__':
     #convert_pdf_to_txt(path)
     convert('sample.pdf')
