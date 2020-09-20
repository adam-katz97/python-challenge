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
    win_num = 0
    winner = ""
    for i in result:
        if candidate.count(i) > win_num:
            win_num = candidate.count(i)
            winner = i

    print("Election Results")
    print("-----------------------------------------")
    print('Total Votes: ', totVote)
    print("-----------------------------------------")
    for i in result:
        print(i + ": " + str(round(((candidate.count(i)/totVote)*100), 2))+ "% " + str(candidate.count(i)))
    print("-----------------------------------------")
    print("Winner: " + winner)
    print("-----------------------------------------")
txtpath = os.path.join("Analysis", "poll_output.txt")
with open(txtpath, 'w') as f:
    f.write("Election Results" + '\n')
    f.write("-----------------------------------------" + '\n')
    f.write("Total Votes: " + str(totVote) + '\n')
    f.write("-----------------------------------------" + '\n')
    for i in result:
        f.write(i + ": " + str(round(((candidate.count(i)/totVote)*100), 2))+ "% " + str(candidate.count(i)) + '\n')
    f.write("-----------------------------------------" + '\n')
    f.write("Winner: " + winner + '\n')
    f.write("-----------------------------------------" + '\n')
