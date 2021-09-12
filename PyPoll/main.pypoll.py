# Import depend
import os
import csv
csvpath = os.path.join('Resoursces','election_data.csv' )

#decl vari
votes = 0
vote_count = []
candidates = []
csv_reader = ['1', '2']


#read csv
#total votes
#total candidates
#total votes per cand.
csv_reader = csv.reader(elections, delimiter=",") 
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
        votes = votes + 1
        candidates = row [2]
        if candidate in candidates 
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
            candidates.append(candidate) 
            vote_count.append(1)   
# % each cand. won
percentages = []
most_votes = vote_count[0]
most_votes_index = 0
for count in range(len(candidates)):
    vote_percentage = vote_count[count]/votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > most_votes:
        print(most_votes)
        most_votes_index = count
winner = candidates[most_votes_index]
percentages = [round (i,2)] for i in percentages]

#hopefully this is the results 
print()
print('Election Results')
print(--------------------------------------)
print(f'Total Votes; {total_votes}')
print(--------------------------------------)
print(f'Winner; {winner}')
print(---------------------------------------)



