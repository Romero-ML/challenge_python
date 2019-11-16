# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
elect_data = os.path.join("Resources", "election_data.csv")

# Total Vote Counter
votes_total = 0

# Candidate Votes Counters
votes_candidates = {}

# Candidate options Counters
options_candidates = []

# Winning Candidate and winning counter 
winning_candidate_summary = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(elect_data) as election_info:
    election_reader = csv.reader(election_info)

    #read the header
    header = next(election_reader)

    #read each row
    for row in election_reader:

        #print the list
        print(". ", #end="")
    
        # Add to the total vote count
        #votes_whole = votes_total  + 1
        
        #Candidate name from each row
        candidate_name = row[2]

        #use a loop to discovwer candidates
        if candidate_name not in  options_candidates:

            #add to the candidates list 
            options_candidates.append(candidate_name)

            #to track the candidarte votes
            votes_candidates[candidates_name] = 0

        #add a vote to that candidate's count"
        votes_candidates[candidate_name] = votes_candidates[candidate_name] + 1

#print the result
election_results =(
    f"Election Results"
    f"----------------------"
    f"Total Votes: {votes_whole}"
    f"----------------------")   
print(election_results, end="")    

#Using loop to find the winner and percentage
for candidate in votes_candidates:
    votes = votes_candidates.get(candidate)
    percentaje_vote = float(votes)/ float(votes_whole)*100

    #determine winning vote and candidates count
    if (vote > winning_count):
        winning_count = votes   
        winning_candidate_summary = candidate
        winning_candidate = candidate

    voter_output = f"{candidate}: {percentaje_vote:.3f}% ({votes})"
    print(voter_out, end="")

#print the winner candidate
winning_candidate_summary =(
    f"--------------------"
    f"winner: {winning_candidate}"
    f"---------------------")
print(winning_candidate_summary)

