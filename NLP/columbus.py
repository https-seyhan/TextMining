#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saul
"""
import os
import pandas as pd
from collections import Counter
import csv
import itertools
import operator

columbus = []
with open('columbus.txt') as inputfile:
    for line in inputfile:
        columbus.append(line.strip().split(' '))
   
#print(len(columbus))
#print(columbus[96])
counts = Counter(columbus[96])
#print(counts)

with open('columbus.txt', newline='') as inputfile:
    columbus = list(csv.reader(inputfile))
cnt = 0

for word in columbus:
    cnt += 1
print(cnt)

#print(columbus)
#print(len(columbus))
#counts = Counter(columbus)
#sum(x.count(x in columbus))

flat_list = [item for sublist in columbus for item in sublist] # convert multiple list to aa single list
#print(flat_list)
#print(Counter(flat_list))
singlelist = []

for i in range(len(flat_list)):
    flat_list2 = flat_list[i].split(" ")
    #print(flat_list2)
    singlelist.append(flat_list2)
#print(singlelist)
#print(len(singlelist))

flat_list = [item for sublist in singlelist for item in sublist] # convert multiple list to aa single list
print(flat_list)
counts = Counter(flat_list)
cnt = 0

for words in flat_list:
    cnt += 1

print(cnt)
counts.pop('', None) #remove '' 

print("First Item", counts.keys())
print(len(counts))
print(sum(counts.values()))

#for key, item in counts.keys():
    #print(item)

with open('wordfrequency.csv','w') as csvfile:
    fieldnames=['word','count']
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)
  
    for key, value in counts.items():
        print(key, value)
        writer.writerow([key] + [value])
