# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:08:25 2019

@author: LLakhi
"""

#Write a program to check the validiti of the password
''' criteria
    1. Atleast 1 character from [$@#]
    2. min length :6
    3. max length: 12
    
    Display valid password if all conditions are correct else invalid pwd
    
    '''
    
string_1 = input (" Ener password : ")
count_len = len(string_1)
cond_1 = 0
cond_2 = 0

if count_len > 5 and count_len <13 :
    cond_1 = 1
    
for item in string_1 :
    if item == "$" or item == "#" or item == "@":
        cond_2 =1 


if cond_1 == 1 and cond_2 == 1:
    print("Valid Password ")
else:
    print("invalid password")