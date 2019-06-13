import csv
import os

row_list = []
total = 0
greatest = (0, None)
least = (0, None)

budgetpath = os.path.join('Resources', 'budget_data.csv')

with open(budgetpath,'r') as budget_handler:
    budgetcsv = csv.reader(budget_handler, delimiter=',')

    header = next(budgetcsv)

    for row in budgetcsv:
        change = int(row[1])
        # Second task
        total += change
        row_list.append(row)
        # Fourth task
        if change > greatest[0]:
            greatest = (change, len(row_list) - 1)
        # Fifth task
        if change < least[0]:
            least = (change, len(row_list) - 1)

# First task
total_months = len(row_list)
# Third task 
avg_change = round(total/total_months, 2)

# Results
print(total_months)
print(total)
print(avg_change)
print(greatest)
print(least)
print(row_list[greatest[1]])
print(row_list[least[1]])