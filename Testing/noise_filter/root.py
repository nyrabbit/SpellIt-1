#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs

    # Change the file address here
CPATH = os.getcwd()  # current
FILE_ENUS_AFF = os.path.join(CPATH, "en_US.aff")
FILE_EN_CSV = os.path.join(CPATH, "en.csv")
ENCODING = "utf-8"
    # Define the second column "class/paradigm" in the future 
def whatParadigm(paradigm):
    return paradigm
    
    # Identify the first column is SFX or PFX
def qualified(condition, category, inputword):
    if category not in ('PFX', 'SFX'):  
        raise TypeError('invalid argument')
    elif category == 'PFX':
        return True
    elif category == 'SFX':
        return True
def isEnglish(unknown):
    for letter in unknown:
        try:
            i = 0
            while unknown[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkkmnopqrstuvwxyz-\'':
                i += 1
            return False
        except IndexError:
            return True


def main():
    # open noise file
    noises = list()
    with codecs.open(FILE_EN_CSV, "r", encoding=ENCODING) as f:
        noises = [pair.split(',')[1].replace('\r\n', '') for pair in f.readlines()[1:]]
    print noises[:10]
    noises = [noise for noise in noises if isEnglish(noise)]
    print noises


    # define the open file
    with codecs.open(FILE_ENUS_AFF, "r", encoding=ENCODING) as f:
        lines = f.readlines()
    
    
    rules = {'PFX': dict(), 'SFX': dict()}
    for line in lines:
        entities = line.split()
        # print entities
        if any(entities):
            category = entities[0]
            paradigm = whatParadigm(entities[1])
            if category in ('PFX', 'SFX'):
                if paradigm not in rules[category]:
                    rules[category][paradigm] = list()
                try:
                    number_of_rules = int(entities[3])
                    print '!!!{}'.format(entities)
                except ValueError:
                    print '{}'.format(entities)
                    rules[category][paradigm].append(entities[2:])
    print rules

                
if __name__ == "__main__":
    main()
