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
month_count = 0
total = 0
monthly_change = []
total_monthly_change = 0
greatest_increase = 0

# Open the CSV
with open(csv_path) as csvfile:
    bank_csv = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(bank_csv)
    #convert csv to list to be able to use the enumerate function
    bank_list = list(bank_csv)    
    
    for index, row in enumerate(bank_list):
        month_count += 1 
        total = total + float(row[1])
        
        if index > 0: 
            monthly_change.append(float(row[1]) - float(bank_list[index - 1][1]))
            total_monthly_change = total_monthly_change + monthly_change[index - 1]
        if index > 0 and row[1] == max(monthly_change):
            greatest_increase = monthly_change[index]
            greatest_month = row[0]
            print(row[0])
    # print(monthly_change)
    # print(total_monthly_change)
    avg_change = total_monthly_change/(month_count - 1)
    # greatest_increase = max(monthly_change)
    print(greatest_increase)
    # print(greatest_month)

         
        
    print(f'''
Financial Analysis
------------------
Total Months: {month_count}
Total: {as_currency(total)}
Average Change: {as_currency(avg_change)}
Greatest Increase in Profits:  {as_currency(greatest_increase)}
Greatest Decrease in Profits:
''')
        
        # if float(row[7]) >= 5:
        #     print(row)
        #     # print(f"{row[0]} {row[7]}")
    
    
