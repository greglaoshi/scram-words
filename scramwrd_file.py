# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:02:17 2019

@author: english teacher
"""

import random

def scram(wrd):
    wrdlst = list(wrd)
    random.shuffle(wrdlst)
    result = ''.join(wrdlst)
    return result


def abcsort(wrd):
    wrdlst = list(wrd)
    wrdlst.sort()
    result = ''.join(wrdlst)
    return result


def scram_word_file():
    with open("toscramlist.txt") as f_obj:
        for line in f_obj:
            owrd = line.rstrip()
            print(owrd, scram(owrd))
            



mywrd=input("input a word to scramble or sort, type file: ")

if mywrd == "file":
    scram_word_file()
    
else:
    print(scram(mywrd), abcsort(mywrd))
    
