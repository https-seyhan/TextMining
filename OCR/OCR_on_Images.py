#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
# This code performs OCR on images using Python modules
# This code employs pytesseract
# Crawl in a directory and obtain each file name of the direcrory
# That will recognize and “read” the text embedded in images
"""
# Scrap text of images.
import os
import pytesseract # Python-tesseract is an optical character recognition (OCR) tool for python. NN based.
from pytesseract import image_to_string # convert image to text.
import PyPDF2

from PIL import Image as PI # Python image library
from os import listdir
from os.path import isfile, join

tesseract_cmd = 'tesseract'
os.chdir('/home/saul/pythontraining')

# get file names in the directory
onlyfiles = [f for f in listdir('/home/saul/pythontraining') if isfile(join('/home/saul/pythontraining', f))]

#loop through files
for file in onlyfiles:
    fileReader = PyPDF2.PdfFileReader(open(file,'rb')) # read pdf files in the directory
    count = 0

    # read first 2 pages of the pdf files
    while count < 3: 
        pageObj = fileReader.getPage(count)
        count +=1
        text = pageObj.extractText() 

def convertImageString():
    a = PI.open("first.jpg") # sample image
    print(image_to_string(a)) # scrap text in the images
