import os

import csv

csvpath = os.path.join('D:\GitRepo\RiceBootCamp\python-challenge', 'Resources', 'budget_data.csv')

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

# print ("Financial Analysis")
# print ("----------------------------")
# print('Total Months: ' + str(RowCount))
# print ('Total: ' + str(sum(PnLVal)))
# print ('Average Change: ' + str(round(sum(ChangeValue)/len(ChangeValue),2)))
# print ('Greatest Increase in Profits: ' + str(MonthVal[MonthValMax]) + ' ' + str(max(ChangeValue)))
# print ('Greatest Decrease in Profits: ' + str(MonthVal[MonthValMin]) + ' ' +  str(min(ChangeValue)))

line1 = 'Financial Analysis'
line2 = '----------------------------'
line3 = 'Total Months: ' + str(RowCount)
line4 = 'Total: ' + str(sum(PnLVal))
line5 = 'Average Change: ' + str(round(sum(ChangeValue)/len(ChangeValue),2))
line6 = 'Greatest Increase in Profits: ' + str(MonthVal[MonthValMax]) + ' ' + str(max(ChangeValue))
line7 = 'Greatest Decrease in Profits: ' + str(MonthVal[MonthValMin]) + ' ' +  str(min(ChangeValue))

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)

text_file = open("PyBank.txt", "w")

#Enter list of products
lines = [line1, line2, line3, line4, line5, line6, line7] #Formerly "lines" variable

#Enter each product on a new line
for l in lines:
    text_file.writelines(l)
    text_file.writelines('\n')

#Close text file for writing
text_file.close()




