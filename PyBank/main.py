# PyBank Challenge

# Import the os module
# This will allow us to create file path to budget data
import os

# Import the module for reading csv files
import csv

# os.path.join would not work, so I used this
csvpath = '/Users/bradleybarker/Documents/GT_Boot_Camp/GT_Homework/Week_03_Python/python-challenge/PyBank/Resources/budget_data.csv'



with open(csvpath) as csvfile:

    # Use CSV reader to specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Define last month number
    last_month = 0 

    # Read each row of data after the header
    for row in csvreader:
        month = row[0]
        profit = row[1]
        #print(month)
        #print(profit)
        # Assign columns to type classes

        month_string = str(month)
        #print(type(month_string))

        profit_integer = int(profit)
        #print(type(profit_integer))

    # Count total number of months in dataset
    month_count = len(month)
    print(month_count)

    # Determine total net profit/loss over entire period
    net_profit = sum(profit)
    print(net_profit)

        # Determine change in profit
        #change = 
