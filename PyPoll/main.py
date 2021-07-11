#PyPoll

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Create Lists & Dictionaries
voter_ids = []
counties = []
candidates = []

# Set all votes to 0
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0
all_votes = 0

# Assign name with vote counters
vote_count_names = {"Khan":votes_khan,"Correy":votes_correy,"Li":votes_li,"O'Tooley":votes_otooley}

# Locate csv file data
csvpath = '/Users/bradleybarker/Documents/GT_Boot_Camp/GT_Homework/Week_03_Python/python-challenge/PyPoll/Resources/election_data.csv'

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Loop through rows add add data to lists
    for row in csvreader:
        voter_ids = int(row[0])
        counties = str(row[1])
        candidates = str(row[2])
        #print(row)
        
        # Count candidate votes
        if candidates == "Khan":
            votes_khan = votes_khan + 1
        elif candidates == "Correy":
            votes_correy = votes_correy + 1
        elif candidates == "Li":
            votes_li = votes_li + 1
        elif candidates == "O'Tooley":
            votes_otooley = votes_otooley + 1

# Count all votes
all_votes = votes_khan + votes_correy + votes_li + votes_otooley

# Calculate percentage votes per candidate
percent_khan = round((votes_khan/all_votes)*100)
percent_correy = round((votes_correy/all_votes)*100)
percent_li = round((votes_li/all_votes)*100)
percent_otooley = round((votes_otooley/all_votes)*100)

# Test outputs by printing

#print(votes_khan)
#print(percent_khan) 
#print(votes_correy)
#print(percent_correy)   
#print(votes_li)
#print(percent_li)   
#print(votes_otooley)
#print(percent_otooley)   
#print(all_votes)
        
# Determine Winner  
winner = max(vote_count_names, key=vote_count_names.get)
#print(winner)

# Open and write to file for displaying results
with open ("election_results.txt", "w") as file:
    file.write("Election Results\n")
    file.write("--------------------\n")
    file.write(f'Total Votes: {all_votes} \n')
    file.write("--------------------\n")
    file.write(f'Khan: {percent_khan}% ({votes_khan})\n')
    file.write(f'Correy: {percent_correy}% ({votes_correy})\n')
    file.write(f'Li: {percent_li}% ({votes_li})\n')
    file.write(f'O\'Tooley: {percent_otooley}% ({votes_otooley})\n')
    file.write("--------------------\n")
    file.write(f'Winner: {winner}\n')
    file.write("--------------------\n")

# Read contents of file
file = open("election_results.txt", "r")
print(file.read())