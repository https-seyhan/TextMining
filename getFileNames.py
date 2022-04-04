#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""

import pandas as pd
import os
from os import listdir
from os.path import isfile, join

os.chdir('/home/saul/pythontraining')
simple_list=[['','']]
onlyfiles = [f for f in listdir('/home/saul/pythontraining') if isfile(join('/home/saul/pythontraining', f))]
#for line in onlyfiles:
    #Type = line.split(".")
    #print(Type[0])
    #print(Type[1])
    #simple_list.append([Type[0], Type[1]])
df=pd.DataFrame(simple_list,columns=['fileName','extension'])	
df.to_csv('filedetails.csv', sep=',', index=False)
