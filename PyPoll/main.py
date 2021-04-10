import os
import csv

csvpath = os.path.join('Resources','PyPoll_Resources_election_data.csv')
total_votes = 0
khan_count= 0
correy_count = 0
li_count = 0
tooley_count = 0

with open(csvpath,newline="",encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if(row[2] == "Khan"):
            khan_count += 1
        elif(row[2] == "Correy"):
            correy_count += 1
        elif(row[2] == "Li"):
            li_count += 1
        elif(row[2] == "O'Tooley"):
            tooley_count += 1

    khan_per = round(((khan_count / total_votes) * 100),4)
    correy_per = round(((correy_count / total_votes) * 100),4)
    li_per = round(((li_count / total_votes) * 100),4)
    tooley_per = round(((tooley_count / total_votes) * 100),4)

    if(khan_count > correy_count and   khan_count > li_count and khan_count > tooley_count):
        winner = "Khan"
    elif(correy_count > khan_count and correy_count > li_count and correy_count > tooley_count ):
        winner = "Correy"
    elif(li > khan_count and li > correy_count and li > tooley_count):
        winner = "Li"
    else: winner = "O'Tooley"

    print("Election Results")
    print("-------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------")
    print(f"Khan: {khan_per}% ({khan_count}) ")
    print(f"Correy: {correy_per}% ({correy_count}) ")
    print(f"Li: {li_per}% ({li_count}) ")
    print(f"O'Tooley: {tooley_per}% ({tooley_count}) ")
    print("-----------------------")
    print(f"Winner: {winner}")
    print("-----------------------")

    f = open("Analysis.txt", "w")
    f.write("Election Results\n")
    f.write("----------------------\n")
    f.write(f"Total votes: {total_votes} \n")
    f.write("--------------------------\n")
    f.write(f"Khan: {khan_per}% ({khan_count}) \n" )
    f.write(f"Correy: {correy_per}% ({correy_count}) \n")
    f.write(f"Li: {li_per}% ({li_count}) \n")
    f.write(f"O'Tooley: {tooley_per}% ({tooley_count}) \n")
    f.write("-----------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")
