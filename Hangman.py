# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:16:02 2021

@author: viraj
"""
import random

name = input('Enter your name')
print('Welcome', name)
print(' _ _ _ _ _ _ _')
print('Try to guess the word in less than 10 attempts')
word = random.choice(['apple', 'car', 'mouse', 'cpu', 'tree', 'motherboard', 'laptop', 'computer'])
validLetter = 'abcdefghijklmnopqrstuvwxyz'
guessmade=''
turns=10

while len(word) > 0:
    main = ''
    missed = 0
    for letter in word:
        if letter in guessmade:
            main = main + letter
        else:
            main = main + "_" + ""
    if main == word:
        print(main)
        print('You Won!')
        break
    print("Guess the word:", main)
    guess = input()          
        
    
    if guess in validLetter:
        guessmade = guessmade + guess
    else:
        print("Enter a valid character")
        guess = input()
    if guess not in word:
        turns= turns-1
        if turns == 9:
            print("9 turns left")
            print("----------")
        
        if turns == 8:
            print("8 turns left")
            print("----------")
            print("     O    ")
            
        if turns == 7:
            print("7 turns left")
            print("----------")
            print("     O    ")
            print("     |    ")

            
        if turns == 6:
            print("6 turns left")
            print("----------")
            print("     O    ")
            print("     |    ")
            print("    /  ")

            
        if turns == 5:
            print("5 turns left")
            print("----------")
            print("     O    ")
            print("     |    ")
            print("    / \ ")
            
        if turns == 4:
            print("4 turns left")
            print("----------")
            print("   \ O   ")
            print("     |    ")
            print("    / \ ")
                    
        if turns == 3:
            print("3 turns left")
            print("----------")
            print("   \ O /   ")
            print("     |    ")
            print("    / \ ")
            
        if turns == 2:
            print("2 turns left")
            print("----------")
            print("   \ O_/   ")
            print("     |    ")
            print("    / \ ")
            
        if turns == 1:
            print("1 turns left")
            print("LAST CHANCE LEFT. THINK CAREFULLY")
            print("----------")
            print("   \ O_|/   ")
            print("     |    ")
            print("    / \ ")
        if turns == 0:
            print("YOU LOOSE")
            print("YOU LET A KIND PERSON DIE")
            print("1 turns left")
            print("----------")
            print("     0_|   ")
            print("    /|\    ")
            print("    / \ ")
            break;
        