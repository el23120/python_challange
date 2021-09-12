# Import depend
import os
import csv
input_file = os.path.join('Resoursces','election_data.csv' )

#decl vari
votes = 0
vote_count = []
cabidates = []
csv_reader = ['1', '2']


#read csv
csvreader = csv.reader(elections,delimiter=",") 

for row in csvreader:
    total_votes = +1

    if row[2] = "Khan":
        khan_votes = +1
    elif row[2] = "Correy":
        correy_votes = +1
    elif row[2] = "Li":
        li_votes = +1
    elif row[2] = "O'Tooley":
        otooley_votes = +1

canidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

