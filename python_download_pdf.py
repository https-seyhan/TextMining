#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:15:19 2018

@author: saul
"""

from urllib.parse import urlparse
import scrapy 

from scrapy.http import Request
from scrapy.http import TextResponse
from scrapy.selector import Selector
from scrapy import *
import subprocess

class pwc(scrapy.Spider):
    name = "pwc2"

    allowed_domains = ["financialservices.royalcommission.gov.au",]
    #start_urls = ["http://www.pwc.com/us/en/tax-services/publications/research-and-insights.html"]
    start_urls = ["https://financialservices.royalcommission.gov.au/pages/results.aspx?k=munich re"]

    def parse(self, response):
        #subprocess.call(["rm output.csv","/home/saul/asic/asic/spiders"])
        
        query = '//div[@class="srch-Title3"]/a/@href'
        urls = response.xpath(query).extract()
        print ("URLLLL :", urls)
        for url in urls:
            absolute_url = response.urljoin(url)
            #yield Request(absolute_url,
                   #self.parse_article) # recursively calls parse_article at each href containing pdf
            print ("Absolute_URLLLL :", absolute_url)
            yield scrapy.Request(absolute_url, self.parse_article)
            print ("SECOND RUN   :\n",)
            filename = absolute_url.split('/')[-1] #PDF file name
            print("FILE NAME      :\n", filename)
            self.logger.info('Saving PDF %s', filename )
            with open(filename , 'wb') as f:
                f.write(response.body) 
            f.close()