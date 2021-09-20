#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: ahmedlasheen
Date  : Sep 20, 2021
Purpose : file managment.
"""
#%% writing and reading file with one row
definition = """ A computer file is a computer resource for recording data discretely in a computer storage device. Just as words can be written to paper, so can information be written to a computer file. Files can be edited and transferred through the internet on that particular computer system."""

open("file_definition.txt", "w").write(definition)
text = open("file_definition.txt").read()
print(text)

#%%  reading multi lines file that contains a list of numbers.
fh = open("multi_lines.txt","r")
print(fh.read())
fh.close()
#%%  reading multi lines file that contains a list of numbers.
fh = open("multi_lines.txt","r")
print(fh.readline())
print(fh.readline())
print(fh.readlines())
fh.close()
#%%  reading multi lines file that contains a list of numbers.
fh = open("multi_lines.txt","r")
for myline in fh:
    print(myline)
fh.close()
#%%
with open("multi_lines.txt", "r") as fh: 
    for myline in fh:
        print(myline.strip())
#%%  reading multi lines file that contains a list of numbers.
year=[]
month=[]
fh = open("co2.dat","r")
for mylines in fh:
    ll=mylines.strip() # to remove whitespace & newlines
    print(ll[0:4]+' '+ll[5:8])
    year.append(ll[0:4])
    month.append(ll[5:8])
fh.close()

#%%  reading space delimited file
myyear=[]
mymonth=[]
myvar3=[]
fh = open("co2.dat","r")
for mylines in fh:
    myyear=mylines.split()[0]
    mymonth=mylines.split()[1]
    myvar3=mylines.split()[2]
    print(myyear+" "+mymonth+" "+myvar3)

fh.close()

#%% reading comma seperated file CSV
import csv
myyear=[]
mymonth=[]
myvar3=[]
fh = open("co2_csv.dat")
file_csv=csv.reader(fh,delimiter=",")

for myrow in file_csv:
    myyear=myrow[0]
    mymonth=myrow[1]
    myvar3=myrow[2]
    myvar4=myrow[3]
    print(myyear+" "+mymonth+" "+myvar3+" "+myvar4)

