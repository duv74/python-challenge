import os
import csv

budget_csv = os.path.join('..', "python-challenge", 'budget_data.csv')

month_total = []
net_total = []
average_total = []

with open(budget_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        month_total.append(row[0])

        net_total.append(int(row[1]))

    for i in range(len(net_total)-1):

        average_total.append(net_total[i+1]-net_total[i])

max_increase = max(average_total)

max_decrease = min(average_total)

max_increase_month = average_total.index(max(average_total)) + 1

max_decrease_month = average_total.index(min(average_total)) + 1

print("Financial Analysis")

print("--------------------------")

print(f"Total Months: {len(month_total)}")

print(f"Total: ${sum(net_total)}")

print(f"Average Change: ${round(sum(average_total)/len(average_total),2)}")

print(f"Max Increase: {month_total[max_increase_month]} ${(str(max_increase))}")

print(f"Max Decrease: {month_total[max_decrease_month]} ${(str(max_decrease))}")

output_path = os.path.join('..', "python-challenge", "Summary.txt")

with open(output_path, 'w', newline='') as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(month_total)}")
    file.write("\n")
    file.write(f"Total: ${sum(net_total)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(average_total)/len(average_total),2)}")
    file.write("\n")
    file.write(f"Greatest Increase: {month_total[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease: {month_total[max_decrease_month]} (${(str(max_decrease))})")