import os
import csv


csvpath = os.path.join('D:\GitRepo\RiceBootCamp\python-challenge', 'Resources', 'election_data.csv')

# with open(csvpath, newline='') as csvfile:    
#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvreader)

#     #variables
    
#     VoterVal, CountyVal, CandidateVal = [], [], []

#     CandidateDict = {rows[2]:1 for rows in csvreader}
#     print(CandidateDict)

with open(csvpath, newline='') as csvfile:    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #variables
    KhanVote, LiVote, CorreyVote, TooleyVote = 0, 0, 0, 0
    VoterVal, CountyVal, CandidateVal = [], [], []    
    # print("Total Votes:" + str(len(list(csvfile))))
    for i in csvreader:
        VoterVal.append(i[0])
        CountyVal.append(i[1])
        CandidateVal.append(i[2])

        if i[2] == 'Khan':
            KhanVote +=1
        elif i[2] == "O'Tooley":
            TooleyVote +=1
        elif i[2] == 'Li':
            LiVote +=1
        elif i[2] == 'Correy':
            CorreyVote += 1


TotalVote = len(CountyVal)

line1 = 'Election Results'
line2 = '----------------------------'
line3 = 'Total Votes: ' + str(TotalVote)

# line5 = 'Khan: ' + '{:.0%}'.format(str(math.ceil((KhanVote/TotalVote)*100.000))) + '(' + str(KhanVote) + ')'

line5 = 'Khan: ' + '{0:.3f}%'.format(round(((KhanVote/TotalVote)*100),3)) + ' (' + str(KhanVote) + ')'
line6 = 'Correy: ' + '{0:.3f}%'.format(round(((CorreyVote/TotalVote)*100),3)) + ' (' + str(CorreyVote) + ')'
line7 = 'Li: ' + '{0:.3f}%'.format(round(((LiVote/TotalVote)*100),3)) + ' (' + str(LiVote) + ')'
line8 = "O'Tooley: " + "{0:.3f}%".format(round(((TooleyVote/TotalVote)*100),3)) + " (" + str(TooleyVote) + ")"

winner = max(KhanVote, CorreyVote, LiVote, TooleyVote)
if winner == KhanVote:
    winnerName = 'Khan'
elif winner == CorreyVote:
    winnerName = 'Correy'
elif winner == LiVote:
    winnerName = "Li"
elif winner == TooleyVote:
    winnerName = "O'Tooley"
else:
    winnerName = 'N/A'

line9 = "Winner: " + winnerName

print(line1)
print(line2)
print(line3)
print(line2)
print(line5)
print(line6)
print(line7)
print(line8)
print(line2)
print(line9)
print(line2)

text_file = open("PyPoll.txt", "w")

#Enter list of lines
lines = [line1, line2, line3, line2, line5, line6, line7, line8, line2, line9, line2] #Formerly "lines" variable

#Enter each line on a new line
for l in lines:
    text_file.writelines(l)
    text_file.writelines('\n')

#Close text file for writing
text_file.close()
