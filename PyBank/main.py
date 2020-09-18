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
gainDate = "Waiting input"
lossDate = "waiting input"
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
            gainDate = str(row[0])
        if change < 0 and change < maxLoss:
            maxLoss = change
            lossDate = str(row[0])
        total += int(row[1])
        
    final_day = int(ProfitLoss[-1])
    (first_day) = int(ProfitLoss[0])
    average = float((final_day-first_day)/(totMonth-1))
    moneyTime = dict(zip(Date, ProfitLoss))

    
    print("Total months: " + str(totMonth))
    print("Total: $" + str(total))
    print("Average change: $" + str(average))
    print("Greatest Increase in Profits: " + gainDate + "  $" + str(maxGain))
    print("Greatest Decrease in Profits: " + lossDate + "  $" + str(maxLoss))
txtpath = os.path.join("Analysis", "budget_output.txt") 
line1 = "Total months: " + str(totMonth)
line2 = "Total: $" + str(total)
line3 = "Average change: $" + str(average)
line4 = "Greatest Increase in Profits: " + gainDate + "  $" + str(maxGain)
line5 = "Greatest Decrease in Profits: " + lossDate + "  $" + str(maxLoss)
with open(txtpath, 'w') as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("--------------------------------")
    f.write("\n")
    f.write(line1)
    f.write("\n")
    f.write(line2)
    f.write("\n")
    f.write(line3)
    f.write("\n")
    f.write(line4)
    f.write("\n")
    f.write(line5)