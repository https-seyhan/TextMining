#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:34:17 2019

@author: saul

#This code performs OCR using Python modules
"""
# This code employs pytesseract
# Crawly in a directory

import os
from PIL import Image as PI
from pytesseract import image_to_string
import pytesseract

import PyPDF2
from os import listdir
from os.path import isfile, join

tesseract_cmd = 'tesseract'

os.chdir('/home/saul/pythontraining')

onlyfiles = [f for f in listdir('/home/saul/pythontraining') if isfile(join('/home/saul/pythontraining', f))]
for file in onlyfiles:
    fileReader = PyPDF2.PdfFileReader(open(file,'rb'))

    count = 0

    while count < 3:

        pageObj = fileReader.getPage(count)
        count +=1
        text = pageObj.extractText()

def convertImageString():
    a = PI.open("first.jpg")
    print(image_to_string(a))
    
