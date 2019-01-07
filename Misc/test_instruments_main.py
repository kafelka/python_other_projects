#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:51:33 2019

@author: mag
"""
import instruments_oop

if __name__ == "__main__":
    guitar = instruments_oop.Guitar(True, True)
    print(guitar.sound())
    violin = instruments_oop.Violin(True, False)
    print(violin.sound())
