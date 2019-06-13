import csv
import os

total = 0
candidates = {}
win_total = 0
winner = ''

electionpath = os.path.join('Resources', 'election_data.csv')

with open(electionpath,newline='') as elect_handler:
    electioncsv = csv.reader(elect_handler, delimiter=',')

    header = next(electioncsv)

    for row in electioncsv:
        # First task
        total += 1
        # -1 index to work with single "1" entry at end of csv
        name = row[-1]
        # Second and fourth task
        if name not in candidates:
            candidates[name] = 0
        else: 
            candidates[name] += 1

# Results
Results = ['Election Results', '-------------------------', f'Total Votes: {total}',
'-------------------------']
for person in (candidates.keys()):
    # Fifth task
    personal_result = candidates[person]
    if personal_result > win_total:
        win_total = personal_result
        winner = person
    Results.append(f'{person}: {round(((personal_result/total)*100),3)}% ({personal_result})')

Results.append('-------------------------')
Results.append(f'Winner: {winner}')
Results.append('-------------------------')

with open('analysis.txt', 'w') as written:
    writer = csv.writer(written)
    writer.writerows([row_write] for row_write in Results)

for line in Results:
    print(line)
