import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
Date = []
ProfitLoss = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        Date.append(row[0])
        ProfitLoss.append(row[1])
        totMonth = len(Date)-1
        
    print("Total months: " + str(totMonth))

  


    
      
    

