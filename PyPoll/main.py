import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
voter_ID = []
county = []
candidate = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        totVote = len(voter_ID)
    print("Election Results")
    print("-----------------------------------------")
    print('total votes: ', totVote)
