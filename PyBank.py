import os

import csv

csvpath = os.path.join('python_challenge', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

