# The data we need to retrive
# 1. The total number of votes cast
# 2. A Complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# import csv file 
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = "election_results.csv"

#Assign a variable to save the file to path
file_to_save = "election_analysis.txt"

#Open the election results and read the file
with open(file_to_load,"r") as election_data:

     #To do : read and analyze the data here.
     file_reader = csv.reader(election_data)

     #Print each row in the csv file
     #for row in file_reader:
     #   print(row)
     # Read and print the header row.
     headers = next(file_reader)
     print(headers)

     





