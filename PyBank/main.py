import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
Date = []
ProfitLoss = []

total = 0
plOld = 0
plNew = 0

moneyChange = []
totChange = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        Date.append(row[0])
        totMonth = len(Date)
        ProfitLoss.append(row[1])
        
        total += int(row[1])
        
    final_day = int(ProfitLoss[-1])
    (first_day) = int(ProfitLoss[0])
    average = float((final_day-first_day)/(totMonth-1))
    moneyTime = dict(zip(Date, ProfitLoss))

    gain = max(moneyTime, key=moneyTime.get)
    loss = min(moneyTime, key=moneyTime.get)
    
    print("Total months: " + str(totMonth))
    print("Total: $" + str(total))
    print("Average change: $" + str(average))
    print("Greatest increase: " + str((gain, moneyTime[gain]))) 
    print("Greatest decrease: " + str((loss, moneyTime[loss])))
