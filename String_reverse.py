# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:21:06 2019

@author: LLakhi
"""

#write a program to  accept a string and reverse the string


string = input ("Type String")

alist=list(string)
alist.reverse()

#conveting to string
finalstring="".join(alist)
print(finalstring)

# find number of alpha and digit numbers in string

name = input("ENter string  :")
alpha=0
digit=0
for item in name:
    if item.isalpha():
        alpha= alpha+1
    if item.isdigit():
           digit = digit+1
           
           
print (" No of alphas :" ,alpha)
print (" No of digits :" ,digit)
