#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:54:22 2020

@author: mikenlee
"""

import os
import csv
   
# Define the function and have it accept the 'wrestlerData' as its sole parameter    
def print_percentages(wrestlerData):
    total_matches = float(wrestlerData[1]) + float(wrestlerData[2]) + float(wrestlerData[3])
    win_percentage = float(wrestlerData[1]) / total_matches
    loss_percentage = float(wrestlerData[2]) / total_matches
    draw_percentage = float(wrestlerData[3]) / total_matches
    
    print(f'''
{name_to_check} Stats:
Total Matches:   {total_matches}
Win Percentage:  {round(win_percentage * 100, 1)}%
Loss Percentage: {round(loss_percentage * 100, 1)}%
Draw Percentage: {round(draw_percentage * 100, 1)}%
''')


csv_path = os.path.join("..", "Resources", "WWE-Data-2016.csv")

with open(csv_path) as csv_file:
    wwe_csv = csv.reader(csv_file, delimiter = ",")
    next(wwe_csv)
    
    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in wwe_csv:
        if name_to_check == row[0]:    
            print_percentages(row)
    
    
        
 


