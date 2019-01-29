# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:24:16 2019

@author: LLakhi
"""

''' write a program to capture any string count and count the occurances
 of each character to any dictionary the count of each character
 
 Enter any string : hello
 dictionary : {'o':1,'e':1,'l':2,'h':1}
 occurances : 
     '''
     

mystring = input(" Enter string :-" )
mydict = {}

for char in mystring :
    temp = mystring.count(char)
    mydict[char] = temp
    
print (mydict)
for mykey in mydict.keys():
    print(mykey,mydict[mykey])
    
    
    
     