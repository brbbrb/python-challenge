# PyPoll Challenge

# Import the os module
# This will allow us to create file path to budget data
import os

# Import the module for reading csv files
import csv

# Create lists
#voter_ids = 
#counties = 
#candidates = 

# os.path.join would not work, so I used this
csvpath = '/Users/bradleybarker/Documents/GT_Boot_Camp/GT_Homework/Week_03_Python/python-challenge/PyPoll/Resources/election_data.csv'
#path=os.path.join("Resources","election_data.csv")
print(csvpath)

with open(csvpath) as csvfile:

    # Use CSV reader to specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        print row
