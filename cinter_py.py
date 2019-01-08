# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:50:27 2019

@author: mag
"""

#Write the letters 'A' to 'Z' (in upper case) to the console, placing each letter
# on a new line.
#
#For every third letter, write it to the console in lowercase instead.
#
#For every fourth letter, write its numeric position in the alphabet to the console 
#instead (e.g. instead of outputting 'D' output '4').
#
#If a letter satisfies both rules 2 and 3, write out its numeric position followed 
#by the letter in lowercase (e.g. 'L' should be output as '12l').

#for i in range(ord("A"), ord("Z")+1):
#    print(chr(i))
#
#def alphabet():
#    for i in range(ord("A"), ord("Z")+1):
#        print(chr(i))   
#        
#        if chr(i) == 65 + 2:
#            print(str(chr(i))).lower()
#        
        
        
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alp2(string):
    for i in range(len(string)):
        if (i+1) % 3 == 0 and (i+1) % 4 == 0:
            print(string[i].lower(), str(i+1))
        elif (i+1) % 3 == 0:
            print(string[i].lower())
        elif (i+1) % 4 == 0:
            print(i+1) 
        else:
            print(string[i])
            
alp2("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


#def alp3(string):
#    for i in range(len(string)):
#        if (i) % 3 == 1 and (i) % 4 == 1:
#            print(string[i].lower(), str(i+1))
#        elif (i+1) % 3 == 0:
#            print(string[i].lower())
#        elif (i+1) % 4 == 0:
#            print(i+1) 
#        else:
#            print(string[i])
#            
#alp3("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

import string 

sA_Z = string.ascii_lowercase

for i in range(0,len(sA_Z)): 
    if i % 3 == 2:
        print(sA_Z[i].lower())
    
    else:
        print(sA_Z[i].upper())