#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:10:12 2019

@author: mag
"""

class Instrument:
    def sound(self):
        pass
    
    
class Chordophone(Instrument):
    def __init__(self, hasStringsOn):
        Instrument.__init__(self)
        self.hasStringsOn = hasStringsOn
        
    def putStringsOn(self):
        self.hasStringsOn = True


class Violin(Chordophone):
    def __init__(self, hasStringsOn, hasBow):
        Chordophone.__init__(self, hasStringsOn)
        self.hasBow = hasBow
        
    def sound(self):
        if not self.hasStringsOn:
            print("Missing strings!")
        elif not self.hasBow: 
            return "Play pizzicato."
        else:
            return "Play Bach."
        
class Guitar(Chordophone):
    def __init__(self, hasStringsOn, hasPlectrum):
        Chordophone.__init__(self, hasStringsOn)
        self.hasPlectrum = hasPlectrum
        
    def sound(self):
        if not self.hasStringsOn:
            print("Missing strings!")
        elif not self.hasPlectrum: 
            return "Play using fingers."
        else:
            return "Play using plectrum."
        

if __name__ == "__main__":
    chooseInstrument = input("Which instrument are you going to play? V for violin or g for guitar. ").lower()
#    hasString == yes -> True, otherwise False:
    hasStrings = input("Does your instrument have strings on? Y/N ").lower() == "y"
    instrument = None
    
    if chooseInstrument == "v":
        hasBow = input("Do you have a bow? Y/N ").lower() == "y"
        instrument = Violin(hasStrings, hasBow)
    elif chooseInstrument == "g":
        hasPlectrum = input("Do you use plectrum? Y/N ").lower() == "y"
        instrument = Guitar(hasStrings, hasPlectrum)
        
    if instrument != None:
        music = instrument.sound()
        if music == None:
            wantStrings = input("Do you need strings? Y/N ").lower() == "y"
            if wantStrings:
                instrument.putStringsOn()
                print(instrument.sound())
            else:
                print("You can't play without strings.")
        else:
            print(music)
            
        