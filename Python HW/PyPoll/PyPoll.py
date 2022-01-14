import csv



csvpath ="PyPoll/Resources/election_data.csv"
cand = set()
cand2 = []

totalVotes = 0

cand_dict = {"Li": 0, "O'Tooley": 0, "Khan": 0,"Correy": 0}


with open(csvpath, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
       # print(row)

       totalVotes += 1
       cand.add(row[2])

      

       if row[2] not in cand2:
           cand2.append(row[2])

       if row[2] == "Khan":
           cand_dict["Khan"] += 1

       elif row[2] == "Correy":
           cand_dict["Correy"] += 1

       elif row[2]== "Li":
           cand_dict["Li"] += 1
       else:
           cand_dict["O'Tooley"] += 1
           
        
        

       
      
# https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
khan_perc = round(((cand_dict["Khan"] / totalVotes) * 100), 4)
correy_perc = round(((cand_dict["Correy"] / totalVotes) * 100), 4)
li_perc = round(((cand_dict["Li"] / totalVotes) * 100), 4)
tooley_perc = round(((cand_dict["O'Tooley"] / totalVotes) * 100), 4)

# https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
winner = max(cand_dict, key=cand_dict.get)

print("Election Results")
print("-----------------------")       
print(f'Total Votes: {totalVotes}')
print("-----------------------")
print(f'Khan: {khan_perc}% ({cand_dict["Khan"]})')
print(f'Correy: {correy_perc}% ({cand_dict["Correy"]})')
print(f'Li: {li_perc}% ({cand_dict["Li"]})')
# https://stackoverflow.com/questions/68461626/how-to-fix-unterminated-expression-in-f-string-missing-close-brace-in-python
print(f"""O'Tooley: {tooley_perc}% ({cand_dict["O'Tooley"]})""")
print("------------------------")
print(f'Winner: {winner}')
print("------------------------")
