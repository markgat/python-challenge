# python-challenge
Using python, this assignment will process massive CSVs of election and finance data to summarize their respective results.
![vote](Images/vote.jpg)
## Getting Started
### Installing
1) Git clone the repository to your local machine:
    ````
    $ git clone https://github.com/markgat/python-challenge.git
    ````
## Running
1) Within the local repository, enter either PyBank or PyPoll folder, and run the respective ````main.py```` program to allow for summary analysis of entries within ````Resources````. The summary will be returned within the terminal where the program is executed.
2) A text folder ````analysis.txt```` will also be saved in the same folder as ````main.py```` that contains the same text as the returned summarization.
## Data
### Original Data (Finance)
86 Entries of net monthly profit/loss preceded by date of record. Entries recorded in monthly periods.

![profit-loss](Images/profit-loss.png)
### Original Data (Election)
A whopping collection of 460,997 votes for an election of 4 candidates. Votes listed by voter ID, regional county, and candidate voted for.

![vote_entries](Images/vote_entries.png)
### Output Data (Finance)
Output is a financial analysis with a count of total months, total dollar amount at the end of the time period, the average change in amount, and the greatest increase and decrease in profits with date and amount stated. This ultimately gives us a sense of our financial performance, length of duration, and critical periods to note. 
![Financial-Analysis](Images/fin_analysis.png)
### Output Data (Election)
Output is the election results containing the count of total votes, candidates with their percentage and amount of votes, and the winner of the overall poll. The analysis gives a sense of the size and influence of the election, significant differences of candidate preferences, and a quick view of the winner of the election.

![Poll-Analysis](Images/elect_analysis.png)