import csv
import os

budgetpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budgetpath,'r') as budget_handler:
    budgetrows = csv.reader(budget_handler, delimiter=',')

    header = next(budgetrows)