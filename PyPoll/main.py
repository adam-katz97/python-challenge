import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
voter_ID = []
county = []
candidate = []
result = []
totVote = 0
vote_num = 0
percenCount = {"name": "percentage"}
voteCount = {"name": "votes"}

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        totVote = len(voter_ID)
    
    result = set(candidate)
    


      
    
        



    print("Election Results")
    print("-----------------------------------------")
    print('Total Votes: ', totVote)
    for i in result:
        print(i + ": " + str(round(((candidate.count(i)/totVote)*100), 2))+ "% " + str(candidate.count(i)))
