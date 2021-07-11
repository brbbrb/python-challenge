# PyBank

# Import the os module
# This will allow us to create file path to budget data
import os

# Import the module for reading csv files
import csv

# os.path.join would not work, so I had to use full CPU location
#csvpath = os.path.join('Resources','budget_data.csv')
csvpath = '/Users/bradleybarker/Documents/GT_Boot_Camp/GT_Homework/Week_03_Python/python-challenge/PyBank/Resources/budget_data.csv'

# Create lists
months = []
profits = []
monthly_change = []

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Set last month to 0
    last_month = 0
    
    # Read each row of data after the header
    for row in csvreader:
        month = str(row[0])
        profit = int(row[1])
        
        #print(row)
        
        # Add data to month, profit, and montly_change lists
        months.append(month)
        profits.append(profit)
        change = profit - last_month
        monthly_change.append(change)
        last_month = profit

#Determine final calculations    
    
total_months = len(months)
#print(total_months)

total_profit = sum(profits)
#print(total_profit)

avg = round((sum(monthly_change)/len(monthly_change)),2)
#print(avg)

maxprofit = max(profits)
#print(maxprofit)

minprofit = min(profits)
#print(minprofit)

maxrow = profits.index(maxprofit)
#print(maxrow)

minrow = profits.index(minprofit)
#print(minrow)

maxmonth = str(months[maxrow])
#print(maxmonth)

minmonth = str(months[minrow])
#print(minmonth)

# Message
with open ("pybank_financial_analysis.txt","w")as file:
    file.write("Financial Analysis" "\n")
    file.write("------------------------" "\n")
    file.write(f'Total Months: {total_months}' "\n")
    file.write(f'Total: ${total_profit}' "\n")
    file.write(f'Average Change: ${avg}' "\n")
    file.write(f'Greatest Increase in Profits: {maxmonth} (${maxprofit})' "\n")
    file.write(f'Greatest Decrease in Profits: {minmonth} (${minprofit})')

file = open("pybank_financial_analysis.txt","r")
print(file.read())