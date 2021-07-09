# PyPoll Challenge

# Import the os module
# This will allow us to create file path to budget data
import os

# Import the module for reading csv files
import csv

# os.path.join would not work, so I used this
csvpath = '/Users/bradleybarker/Documents/GT_Boot_Camp/GT_Homework/Week_03_Python/python-challenge/PyPoll/Resources/election_data.csv'

with open(csvpath) as csvfile:

    # Use CSV reader to specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)