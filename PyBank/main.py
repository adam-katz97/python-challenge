import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
Date = []
ProfitLoss = []
total = 0
maxGain = 0
maxLoss = 0
prevValue = 0
moneyChange = []
totChange = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        Date.append(row[0])
        totMonth = len(Date)
        ProfitLoss.append(row[1])
        change = int(row[1]) - prevValue
        if change > 0 and change > maxGain:
            maxGain = change
        if change < 0 and change < maxLoss:
            maxLoss = change
        total += int(row[1])
        
    final_day = int(ProfitLoss[-1])
    (first_day) = int(ProfitLoss[0])
    average = float((final_day-first_day)/(totMonth-1))
    moneyTime = dict(zip(Date, ProfitLoss))

    
    print max(ProfitLoss)
    print("Total months: " + str(totMonth))
    print("Total: $" + str(total))
    print("Average change: $" + str(average))
    print("Greatest increase: " + str(maxGain))
    print("Greatest decrease: " + str(maxLoss))
    