import os
import csv

# PRINT INTRODUCTIO TO ANALYSIS

print("Financial Analysis")

print("--------------------------")

# TASK ONE - CALCULATE TOTAL MONTHS IN DATASET

budget_csv = os.path.join('..', "python-challenge", 'budget_data.csv')

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    data = list(csvreader)
    
    row_count = len(data)
    
    print("Total Months: " + str(row_count - 1))

# TASK TWO - CALCULATE NET TOTAL P/L ENTIRE PERIOD

    net_total = 0

    for row in csv.reader(csvfile):
        for col in row[1]:
            net_total += int(col)
    print("Total: $" + str(net_total))

# TASK THREE - CALCULATE AVERAGE P/L

# TASK FOUR - CALCULATE GREATEST INCREASE IN PROFIT

# TASK FIVE - CALCULATE GREATEST DECREASE IN LOSS