#!/usr/bin/env python

import random

def get_word(fname):#gets random word from given list of words
    lines = open(fname).read().splitlines()
    return random.choice(lines)

file = open("Title.txt")
print(file.read())
file.close()
while True:
    print("What difficulty level would you like to play on? (enter a number below):\n")
    print("1.) Easy(4-5 letter words)\n2.) Medium(6-7 letter words)")
    print("3.) Hard(8-9 letter words)\n4.) ???Extreme???\n")
    inp = input()
    if (inp=="1" or inp=="2" or inp=="3" or inp=="4"): break
if inp=="1":
    word = get_word("EasyWords.txt")
elif inp=="2":
    word = get_word("MediumWords.txt")
elif inp=="3":
    word = get_word("HardWords.txt")
print(word)
exit()