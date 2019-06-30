import os

import csv

#csvpath = os.path.join('D:\GitRepo\RiceBootCamp\python-challenge', 'Resources', 'budget_data.csv')
csvpath = os.path.join('../', 'Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    RowCount = sum(1 for row in csvreader)

with open(csvpath, newline='') as csvfile:    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #variables
    vChange, vCounter, LastValue = 0, 0, 0
    MonthVal, PnLVal, ChangeValue = [], [], []

    for i in csvreader:

        # keep tracke of the previos value to calc change
        if vCounter == 0:
            LastValue = float(i[1])
            vChange = 0

        else:
            vChange =  float(i[1]) - LastValue
            LastValue = float(i[1])
            ChangeValue.append(vChange)

        vCounter += 1
        MonthVal.append(i[0])
        PnLVal.append(float(i[1]))

MonthValMin = ChangeValue.index(min(ChangeValue)) +1    # add 1 my ChangeList has one less element
MonthValMax = ChangeValue.index(max(ChangeValue)) +1


line1 = 'Financial Analysis'
line2 = '----------------------------'
line3 = 'Total Months: ' + str(RowCount)
line4 = 'Total: $' + str(round(sum(PnLVal), 0))
line5 = 'Average Change: $' + str(round(sum(ChangeValue)/len(ChangeValue),2))
line6 = 'Greatest Increase in Profits: ' + str(MonthVal[MonthValMax]) + ' ($' + str(round(max(ChangeValue), 0)) + ')'
line7 = 'Greatest Decrease in Profits: ' + str(MonthVal[MonthValMin]) + ' ($' +  str(round(min(ChangeValue), 0)) + ')'

#print(type(max(ChangeValue)))
# TODO not sure why round is not working in some case above, type is float

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)

text_file = open("PyBank.txt", "w")

#Enter list of lines
lines = [line1, line2, line3, line4, line5, line6, line7] #Formerly "lines" variable

#Enter each line on a new line
for l in lines:
    text_file.writelines(l)
    text_file.writelines('\n')

#Close text file for writing
text_file.close()




