import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
Date = []
ProfitLoss = []
total = 0
plOld = 0
plNew = 0
average = plNew-plOld
moneyChange = []
totChange = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        Date.append(row[0])
        totMonth = len(Date)
        ProfitLoss.append(row[1])
        if ProfitLoss.count(ProfitLoss) > 1:
            plOld = plNew
            plNew = int(row[1])
            moneyChange.append(average)
            
        else:
            plNew = int(row[1])
            
        
        total += int(row[1])
    for row in moneyChange:
        totChange += row[0]
    print(totChange)
    print("Total months: " + str(totMonth))
    print("Total: $" + str(total))
    print("Average change: $" + str(average))

    