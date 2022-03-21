#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
import os,time,PythonMagick,subprocess,shutil
import os
from PIL import Image, ImageChops
from optparse import OptionParser

def get_image_list_from_pdf(pdf_file):
    #Return a list of images that resulted from running convert on a given pdf
    pdf_name = pdf_file.split(os.sep)[-1].split('.pdf')[0]
    print("PDF Name :", pdf_name)
    #pdf_dir = pdf_file.split(pdf_name)[0]
    jpg = pdf_file.split('.pdf')[0]+'.jpg'
    # Convert the pdf file to jpg file
    call_convert(pdf_file,jpg)
    #Get all the jpg files after calling convert and store it in a list
    image_list = []
    file_list = os.listdir(pdf_dir)

    for f in file_list:
        if f[-4:]=='.jpg' and pdf_name in f:
            #Make sure the file names of both pdf are not similar
            image_list.append(f)
         
    print('Total of %d jpgs produced after converting the pdf file: %s'%(len(image_list),pdf_file))
    return image_list

def call_convert(src,dest):
    #Call convert to convert pdf to jpg
    print('About to call convert on %s'%src)

    try:
        subprocess.check_call(["convert",src,dest], shell=True)
    except Exception as e:
        print('Convert exception ... could be an ImageMagick bug')
        print(e)
    print('Finished calling convert on %s'%src)

def get_pdf_diff(pdf1, cleanup=True):
    #Create a difference pdf by overlaying the two pdfs and generating an image difference.Returns True if the file matches else returns false
    #Get the list of images using get_image_list_from_pdf which inturn calls convert on a given pdf  
    pdf1_list = get_image_list_from_pdf(pdf1)
    #pdf2_list = self.get_image_list_from_pdf(self.pdf2)
    #If diff directory already does exist - delete it 
    #Easier to simply nuke the folder and create it again than to check if its empty
#    diff_image_dir = self.download_dir + os.sep+'diff_images
#    if os.path.exists(diff_image_dir):
#        print('diff_images directory exists ... about to nuke it')
#        shutil.rmtree(diff_image_dir)
#    #Create a new and empty diff directory
#    os.mkdir(diff_image_dir)
#    print('diff_images directory created')
#    print('Total pages in pdf2: %d'%len(pdf2_list))
#    print('Total pages in pdf1 : %d'%len(pdf1_list))
#
#    #Verify that there are equal number pages in pdf1 and pdf2
#    if len(pdf2_list)==len(pdf1_list) and len(pdf2_list) !=0:
#        print('Check SUCCEEDED: There are an equal number of jpgs created from the pdf generated from pdf2 and pdf1')
#        print('Total pages in images: %d'%len(pdf2_list))
#        pdf1_list.sort()
#        pdf2_list.sort()
#
#        #Create the diffed images
#        result_flag = self.create_diff_image(pdf1_list,pdf2_list,diff_image_dir)
#    else:
#        print('Check FAILED: There are an unequal number of jpgs created from the pdf generated from pdf2 and pdf1')
#        print('Total pages in image2 : %d'%len(pdf2_list))
#        print('Total pages in image1: %d'%len(pdf1_list))
#        print('ERROR: Skipping image comparison between %s and %s'%(self.pdf1,self.pdf2))
#
#    if cleanup:
#        #Delete all the image files created
#        self.cleanup(diff_image_dir,pdf1_list,pdf2_list)            
#
#    return result_flag
if __name__== '__main__':
    get_pdf_diff('RCD.0001.0075.0002.pdf')
    #get_image_list_from_pdf('RCD.0001.0075.0002.pdf')
