import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
Date = []
ProfitLoss = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    For row in csvreader:
        Date.append(row[1])
        ProfitLoss.append(row[2])
    
