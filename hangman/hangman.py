#!/usr/bin/env python

import random
import string

def get_word(fname):#gets random word from given list of words
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def check_guess(letter, word):#checks if guessed letter is correct
    x = 0
    flag = True
    global check
    global num_wrong
    for i in word:
        if letter == i:
            flag = False
            corr_guess[x] = letter
            check+=1
        x+=1
    if flag:
        num_wrong+=1

def display(num_wrong):#displays ascii art hangman
    if num_wrong == 0:
        file = open("HangmansCross.txt")
        print(file.read())
        file.close()
    if num_wrong == 1:
        file = open("Head.txt")
        print(file.read())
        file.close()
    if num_wrong == 2:
        file = open("Body.txt")
        print(file.read())
        file.close()
    if num_wrong == 3:
        file = open("LeftArm.txt")
        print(file.read())
        file.close()
    if num_wrong == 4:
        file = open("RightArm.txt")
        print(file.read())
        file.close()
    if num_wrong == 5:
        file = open("LeftLeg.txt")
        print(file.read())
        file.close()
    if num_wrong == 6:
        file = open("RightLeg.txt")
        print(file.read())
        file.close()

while True:
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
    elif inp=="4":
        word = ""
        for i in range(10):
            word+=random.choice(string.ascii_letters)
        word = word.lower()

    corr_guess = ['_'] * len(word)
    used_letters = []
    check = 0
    num_wrong = 0

    while True:
        display(num_wrong)
        print("What is your guess?")
        for k in corr_guess:
            print(k, end = '')
            print(' ', end = '')
        print("\nYou have used the following letters:")
        for x in used_letters:
            print(x, end = '')
            print(' ', end = '')
        print('\n')
        while True:
            flag = True
            inp = input()
            for i in used_letters:
                if inp == i:
                    flag = False
            if flag == True:
                used_letters.append(inp)
                break
            else:
                print("You have already used that letter!")
        check_guess(inp, word)
        if (check == len(word) or num_wrong == 6):
            break
    if num_wrong == 6:
        print("Sorry, the word was: \"", end = '')
        print(word, end = '')
        print("\". You Lose :(\n")
    else:
        print("Congratulations!! The word was: \"", end = '')
        print(word, end = '')
        print("\". You Win!!!")
    print("Do you want to play again?(Type yes or no)\n")
    while True:
        inp = input()
        if(inp == "no" or inp == "yes"):
            break
    if inp == "no":
        exit()
