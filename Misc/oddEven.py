# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:22:52 2019

@author: mag
"""
def oddEven():
    
    number = int(input("Please provide a number: "))

    if number % 2 == 0:
        print(f"{number} is an even number.")
        if number % 4 == 0:
            print(f"{number} is also a multiple of 4.")
    else:
        print(f"{number} is an odd number.")
        
oddEven()


def oddEven2():
    
    number = int(input("Please provide a number: "))
    check = int(input("Please provide another number: "))

    if check % number == 0:
        print(f"{check} divides evenly into {number}.")
    else:
        print(f"{check} does not divide evenly.")
        
oddEven2()

