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
        date = row[0]
        # Second task
        total += change
        row_list.append(row)
        # Fourth task
        if change > greatest[0]:
            greatest = (change, date)
        # Fifth task
        if change < least[0]:
            least = (change, date)

# First task
total_months = len(row_list)
# Third task 
avg_change = round(total/total_months, 2)

# Results
Results = ['Financial Analysis', '----------------------------', 
f'Total Months: {total_months}',
f'Total: ${total}', f'Average Change: ${avg_change}', 
f'Greatest Increase in Profits: {greatest[1]} (${greatest[0]})',
f'Greatest Decrease in Profits: {least[1]} (${least[0]})']

with open('analysis.txt', 'w') as written:
    writer = csv.writer(written)
    writer.writerows([row_write] for row_write in  Results)

for line in Results:
    print(line)