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
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers=next(file_reader)
    print(headers)