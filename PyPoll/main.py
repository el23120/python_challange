# Import depend
import os
import csv
input_file = os.path.join('Resoursces','election_data.csv' )

#decl vari
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

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

