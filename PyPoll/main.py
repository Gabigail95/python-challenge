# import the csv file to begin scripting

import os
import csv

# defining the file path
election_data_csv = os.path.join("Resources", "election_data.csv")

# create lists to store the data
Total_Votes = 0
Candidate_Votes = {}
Candidate = []
Candidates = set()

# with open csv file 
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        # add the number of votes that were cast
        Total_Votes += 1

        # reviewing each candidate
        Candidate_name = row[2]
        Candidates.add(Candidate_name)

        if Candidate_name in Candidate_Votes:
            Candidate_Votes[Candidate_name] += 1
        else:
            Candidate_Votes[Candidate_name] = 1

# vote count 
Total_Votes = sum(Candidate_Votes.values())

# percentage of votes for each candidate
Candidate_percentages = {}
for candidate, votes in Candidate_Votes.items():
    percentage = (votes/Total_Votes)*100
    Candidate_percentages[candidate] = percentage

# calculating the winner
winner = max(Candidate_Votes, key=Candidate_Votes.get)

       
# Print total number of votes
print("Total Votes:", Total_Votes)

# The total number of votes each candidate won
# A complete list of candidates who received votes and percentage
print("Candidate Results:")
for candidate, percentage in Candidate_percentages.items():
    print(f"{candidate}: {percentage:.3f}% ({Candidate_Votes[candidate]:,} votes)")

# The winner of the election based on popular vote
print("Winner:", winner)

# added the text file 
# python main.py > ElectionResults.txt



