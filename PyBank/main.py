import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
Date = []
ProfitLoss = []
total = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        Date.append(row[0])
        totMonth = len(Date)
        ProfitLoss.append(row[1]) 
        total += int(row[1])
    
    print("Total months: " + str(totMonth))
    print("Total: $" + str(total))