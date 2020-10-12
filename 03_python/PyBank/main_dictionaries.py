#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:53:54 2020

@author: mikenlee
"""

import os
import csv

#defining a function to convert value into currency format
def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

#define path to the csv file
csv_path = os.path.join("Resources", "budget_data.csv")

#initialize variables
month_count = 1 #starts at 1 because when the two lists zip (line 42) it shortens 1 month because of the short shifted list
total = 0
monthly_change = []
total_monthly_change = 0
greatest_increase = 0
change_dict = dict()

# Open the CSV
with open(csv_path) as csvfile:
    bank_csv = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(bank_csv)
    
    #convert csv to list to be able to use the enumerate function
    bank_list = list(bank_csv)    
    
    #create list with profits shifted left to calculate the differences
    profits_shifted = bank_list[1:]
    
    for row, profit in zip(bank_list, profits_shifted):
        month_count += 1 
        total = total + float(row[1])
        change_dict[profit[0]] = float(profit[1]) - float(row[1])

    greatest_increase = -1
    greatest_month = None
    greatest_decrease = None
    smallest_month = None
    
    #find greatest increase and decrease using the change dictionary tuple
    for key, value in change_dict.items():
        total_monthly_change = total_monthly_change + value
        
        if value > greatest_increase:
            greatest_increase = value
            greatest_month = key
        if greatest_decrease is None or value < greatest_decrease:
            greatest_decrease = value
            smallest_month = key
    
    avg_change = total_monthly_change/(month_count - 1) #minus 1 because there's no change in the first month
        
    print(f'''
Financial Analysis
------------------
Total Months: {month_count}
Total: {as_currency(total)}
Average Change: {as_currency(avg_change)}
Greatest Increase in Profits: {greatest_month}   {as_currency(greatest_increase)}
Greatest Decrease in Profits: {smallest_month}  {as_currency(greatest_decrease)}
''')
