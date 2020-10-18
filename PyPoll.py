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

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options List
candidate_options = []
# Declare a the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load,"r") as election_data:

     #To do : read and analyze the data here.
     file_reader = csv.reader(election_data)

     # Read the header row.
     headers = next(file_reader)
     
     #Print each row in the csv file
     for row in file_reader:
         #2 . Add to the total vote count
         total_votes +=1
         
         #Print the candidate name from each row
         candidate_name = row[2]

         #If the candidate does not match any existing candidate
         if candidate_name not in candidate_options:
             #Add candidate to the list of candidates
             candidate_options.append(candidate_name)

             #Begin tracking that candidate's vote count.
             candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
         candidate_votes[candidate_name] += 1

#Iterate through the candidate list
for candidate_name in candidate_votes:
    # 2. Retrive vote count of a candidate.
    votes = candidate_votes[candidate_name] 
    # 3. Calculate the percentage of votes
    vote_percentage = float(votes)/float(total_votes)*100

    # To do : print out each candidate's name, voter count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent = voter_percent.
        winning_count = votes
        winning_percentage = vote_percentage
        #And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
# To do : print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (f"--------------------------\n"
                             f"Winner: {winning_candidate}\n"
                             f"Winning Vote Count: {winning_count:,}\n"
                             f"Winning Percentage: {winning_percentage:.1f}%\n"
                             f"--------------------------\n")
print(winning_candidate_summary)
    
        

#Print the candidate list
#print(candidate_options)
#print(candidate_votes)

# 3. Print the total votes.
#print(total_votes)
# 4 Print voter names and %
#print(f"{candidate_name}: received {vote_percentage}% of the vote.")
     





