#data we need:
#1) total votes cast
#2) list of all aandidates who received votes
#3) percentage of votes each candidate won
#4) number of votes each candidate won
#5) winner of the election based on popular vote
import os
import csv
#assign variable to csv
file_to_load = "../Resources/election_results.csv"
#assign variable to written filename
file_to_save = os.path.join("..","analysis", "election_analysis.txt")

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#initialize counters
total_votes=0
candidate_options=[]
candidate_votes={}

#open results and read
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers=next(file_reader)
    #count votes
    for row in file_reader:
        total_votes+=1
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

#write results to txt
with open(file_to_save,'w') as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    #print(election_results, end="")
    txt_file.write(election_results)
    #find the winner, print the results
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        vote_percentage=round((float(votes)/total_votes)*100,1)
        candidate_results=(f"{candidate}: {vote_percentage}% ({votes:,})\n")
        txt_file.write(candidate_results)
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate

    #print the winner
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    txt_file.write(winning_candidate_summary)
