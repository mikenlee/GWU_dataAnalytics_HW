#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:49:08 2020

@author: mikenlee
"""

#%%
n_num = int(input("How many numbers? "))
x = 0
while n_num > 0:

    print(x)
    x += 1
    n_num = n_num - 1
    
choice = str(input("Enter [Y]es to play again and [N]o to stop: ")).lower()

if choice in ["y", "yes"]:
    n_num2 = int(input("How many numbers? "))
    n_num = x
    
    for numbers in range(n_num, n_num + n_num2):
        print(numbers)
       
elif choice in ["n", "no"]:
    print("Goodbye")