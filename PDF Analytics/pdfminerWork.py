#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
import pdfminer
import nltk
import nltk.tokenize
import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
import os
os.chdir('/home/saul/royal/royal/spiders/')

# convert pdf file to text
# then store the text in to a .txt file
# useful for text scraping off pdf files.

def readfiles(firstFile, secondFile):
    pdfdetails = {}
    print("READINNG PDF FILE :",firstFile)
    pdfReader1 = PyPDF2.PdfFileReader(open(firstFile, "rb"))  # PdfFileReader object
    pdfReader2 = PyPDF2.PdfFileReader(open(secondFile, "rb"))  # PdfFileReader object
    print("PDF Reader :", pdfReader1.numPages)
    pdfdetails[firstFile] = pdfReader1.numPages
    pdfdetails[secondFile] = pdfReader2.numPages
    num_pages = pdfReader1.numPages
    count = 0
    text1 = ""
 
    # The while loop will read each page
    while count < num_pages:
        pageObj = pdfReader1.getPage(count)
        count += 1
        text1 += pageObj.extractText()
    tokens = word_tokenize(text1)
   
    with open('firstfile.txt', 'w') as f:
        f.write(text1)
   
    num_pages = pdfReader2.numPages
    count = 0
    text2 = ""
    # The while loop will read each page
    while count < num_pages:
        pageObj2 = pdfReader2.getPage(count)
        count += 1
        text2 += pageObj.extractText()

    # for word in pageObj.extractText():  # #if word in keyword:  # print("Page Number : ", count)
    tokens = word_tokenize(text2)
    with open('secondfile.txt', 'w') as f:
        f.write(text2)

def readpdfFile(secondFile):
    pdfReader2 = PyPDF2.PdfFileReader(open(secondFile, "rb"))  # PdfFileReader object
    num_pages = pdfReader2.numPages
    count = 0
    text2 = ""
    # keyword = stopwords.words('Google')
    # The while loop will read each page
    while count < num_pages:
        pageObj2 = pdfReader2.getPage(count)
        count += 1
        text2 += pageObj2.extractText()
        
    # for word in pageObj.extractText():  # #if word in keyword:  # print("Page Number : ", count)
    tokens = word_tokenize(text2)
    wordtokens = sent_tokenize(text2)
    with open('secondfile.txt', 'w') as f:
        f.write(text2)
      
if __name__ == "__main__":
    #readfiles('EXHIBIT-6.124.8.pdf', 'EXHIBIT-6.126.24.26.pdf')
    readpdfFile('EXHIBIT-6.126.24.26.pdf')
