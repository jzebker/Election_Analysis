# Election_Analysis
[Deliverable 1](https://github.com/jzebker/Election_Analysis/blob/main/PyPollterminaloutput.png)

[Deliverable 2](https://github.com/jzebker/Election_Analysis/blob/main/analysis/election_analysis.txt)
## Resources
- Data Source: election_results.csv
- Software: Python 3.7.4, VS Code 1.38.0

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1.  Calculate the total number of votes cast.
2.  Get a complete list of candidates who received votes.
3.  Calculate the total number of votes each candidate received.
4.  Calculate the percentage of votes each candidate won.
5.  Determine the winner of the election based on popular vote.
6.  Determine the voter turnout for each county.
7.  Calculate the percentage of votes from each county out of the total count.
8.  Determine the county with the highest turnout.

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
### Results by Candidate
- The candidates were:
    - (1) Charles Casper Stockham
    - (2) Diana DeGette
    - (3) Raymon Anthony Doane
- The candidate results were:
    - (1) Charles Casper Stockham received **23.0%** of the vote and **85,213** votes.
    - (2) Diana DeGette received **73.8%** of the vote and **272,892** votes.
    - (3) Raymon Anthony Doane received **3.1%** of the vote and **11,606** votes.
- The winner of the election was:
    - (2) Diana DeGette, who received **73.8%** of the vote and **272,892** votes.
### Results by County
- The number of voters by county was:
    - (1) Jefferson with **10.5%** of the total vote and **38,855** voters.
    - (2) Denver with **82.8%** of the total vote and **306,055** voters.
    - (3) Arapahoe with **6.7%** of the total vote and **24,801** voters.
- The county with the most voters was:   
    - (2) Denver with **82.8%** of the total vote and **306,055** voters.
### Computation Method:
[Python Script](https://github.com/jzebker/Election_Analysis/blob/main/PyPoll_Challenge.py)

## Election-Audit Summary
This code can work for other elections as long as the input data matches the format of the data source.  It doesn't matter if it is an election in another country, another year, or on another planet as long as the voting data is formatted as it is below:
<p align="center">
  <img width="727" alt="electiondataformat" src="https://user-images.githubusercontent.com/84994321/124547200-a2e10200-dde0-11eb-8261-276d3955c815.png">
</p>
Examples for modifying the script to fit different elections follow.

(1) For an electoral college-type election, this data could also be used to determine winners of individual counties using some type of group by statement.  Sample output for the suggested code follows:
<p align="center">
    <img width="398" alt="electoraloutput" src="https://user-images.githubusercontent.com/84994321/124654771-d01ac800-de53-11eb-9ec1-2713a73b681f.png">
</p>
(2) If the voting data is formatted in a different order, then the appropriate column index must be assigned.
<p align="center">
    <img width="415" alt="columnindex" src="https://user-images.githubusercontent.com/84994321/124980132-db532c80-dfe8-11eb-8a38-cadc8b940932.png">
</p>
(3) If the voting data is not in csv format, use the appropriate function that reads in the file.
<p align="center">
    <img width="522" alt="csvreader" src="https://user-images.githubusercontent.com/84994321/124981481-7993c200-dfea-11eb-85f6-0cd6fd62d39a.png">
</p>
