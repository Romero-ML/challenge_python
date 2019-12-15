
# add module
import csv
import os

# Creat a path to read the files
election_data = os.path.join("Resources", "election_data.csv")
election_analysis = os.path.join("Analysis", "election_analysis.txt")

# Total Votes 
total_votes = 0

# Candidate and votes list
candidate_list = []
vote_list = {}

# Top candidate and winners list
top_candidates = ""
winner_count = 0

# Read the csv and convert into a list of dictionaries
with open(election_data) as election_info:
    reader = csv.reader(election_info)

    # Read the header
    header = next(reader)

    # check info each road
    for row in reader:

        # print the road info
        #print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Select the candidate name from each row
        candidate_name = row[2]

        # Use a loop to select candidates name
        if candidate_name not in candidate_list:

            # Add it to the list of candidates in the running
            candidate_list.append(candidate_name)

            # And begin tracking that candidate's voter count
            vote_list[candidate_name] = 0

        # Then add a vote to that candidate's count
        vote_list[candidate_name] = vote_list[candidate_name] + 1

# Print the results and export the data to our text file
with open(election_analysis, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # to save the candidate info  in the text file
    txt_file.write(election_results)
    
    # Select the winner by looping through the counts
    for candidate in vote_list :

        # create the votes count and percentage
        votes = vote_list.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winner vote count and candidate
        if (votes > winner_count):
            winner_count = votes
            top_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter in the text file
        txt_file.write(voter_output)

    # Print the candidate (to terminal)
    top_candidate_summary =(
        f"-------------------------\n"
        f"Winner:{top_candidate}\n"
        f"-------------------------\n")
    print(top_candidate_summary)

    # Save the winner candidate's name to the text file
    txt_file.write(top_candidate_summary)

