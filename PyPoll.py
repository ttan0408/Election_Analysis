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

#Initialize County Vote
county_votes_total = 0

#County Option List
county_options = []
# Declare a empty county dictionary
county_votes = {}
#County count and county winning tracker
county_count = 0
county_winning_percentage = 0

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
         #    Add to the county vote count
         county_votes_total +=1

         #Print the candidate name from each row
         candidate_name = row[2]
         county_name = row[1]
         
         # If county name does not match any existing county name
         if county_name not in county_options:
             #Add county to the list of county
             county_options.append(county_name)

             #Begin tracking county votes count
             county_votes[county_name] = 0
        
        #Add a voute to that county's count
         county_votes[county_name] +=1

         #If the candidate does not match any existing candidate
         if candidate_name not in candidate_options:
             #Add candidate to the list of candidates
             candidate_options.append(candidate_name)

             #Begin tracking that candidate's vote count.
             candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
         candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as text_file:
    #Print the final count to the terminal.
    election_results = (f"\nElection Results\n"
                        f"-------------------------\n"
                        f"Total Votes: {total_votes:,}\n"
                        f"--------------------------\n"
                        f"\nCounty Votes:\n")
    print(election_results, end="")
    #Save the final vote count to the text file.
    text_file.write(election_results)

    #Iterate through the county list
    for county_name in county_votes:
        # Retrive vote count of county
        votes_of_county = county_votes[county_name]
        # Calculate the percentage of votes_of_county
        votes_of_county_percentage = float(votes_of_county)/float(county_votes_total)*100

        #Print county and save to txt file.
        county_results = (f"{county_name}: {votes_of_county_percentage:.1f}% ({votes_of_county:,})\n")
             
        print(county_results)
        #Save the county results to out text file
        text_file.write(county_results)

    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. Retrive vote count of a candidate.
        votes = candidate_votes[candidate_name] 
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100

        # To do : print out each candidate's name, voter count, and percentage of votes to the terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Save the final vote count to the text file.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #Save the candidate results to our text file.
        text_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
           #if true then set winning_count = votes and winning_percent = voter_percent.
           winning_count = votes
           winning_percentage = vote_percentage
        
    # To do : print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (f"--------------------------\n"
                                 f"Winner: {winning_candidate}\n"
                                 f"Winning Vote Count: {winning_count:,}\n"
                                 f"Winning Percentage: {winning_percentage:.1f}%\n"
                                 f"--------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file.
    text_file.write(winning_candidate_summary)
        

#Print the candidate list
#print(candidate_options)
#print(candidate_votes)

# 3. Print the total votes.
#print(total_votes)
# 4 Print voter names and %
#print(f"{candidate_name}: received {vote_percentage}% of the vote.")
     





