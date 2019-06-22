import os
import csv
import numpy as np

# DEFINE VARIABLES

#net_total = 

# PRINT INTRODUCTION TO ANALYSIS

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

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    net_total = 0

    for rows in csvreader:

        net_total += float(rows[1])

    print("Total: $ " + str(round(net_total)))

# TASK THREE - CALCULATE AVERAGE P/L

    def mean(net_total):
        return float(sum(net_total)) / max(len(net_total), 1)
        
        print np.mean(net_total)

# TASK FOUR - CALCULATE GREATEST INCREASE IN PROFIT

# TASK FIVE - CALCULATE GREATEST DECREASE IN LOSS

#df.groupby('A').agg(['min', 'max'])