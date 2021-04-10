import os
import csv
from statistics import mean

csvpath = os.path.join('Resources','budget_data.csv')
months = []
total = []
monthly_change = []



with open(csvpath,newline="",encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)


    for row in csvreader:
        months.append(row[0])
        total.append(int(row[1]))

    total_months = len(months)
    final_total = sum(total)

    for i in range(total_months - 1):
        monthly_change.append(total[i+1] - total[i])

    average_change = round(mean(monthly_change),2)
    greatest_inc = max(monthly_change)
    greatet_dec = min(monthly_change)

    for x in range(len(monthly_change)):
        if(greatest_inc == monthly_change[x]):
            index = x
        if(greatet_dec == monthly_change[x]):
            index1 = x


print("Financial Analysis")
print("--------------------")
print(f"Total Mnoths:{total_months}")
print(f"Total: ${final_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {months[index]}: ${greatest_inc}")
print(f"Greatest Decrease in Profits: {months[index1]}: ${greatet_dec}")
print("filed saved")

f = open("Analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("--------------------\n")
f.write(f"Total Months:{total_months}\n")
f.write(f"Total: ${final_total}\n")
f.write(f"Average Change: ${average_change}\n")
f.write(f"Greatest Increase in Profits: {months[index]}: ${greatest_inc}\n")
f.write(f"Greatest Decrease in Profits: {months[index1]}: ${greatet_dec}\n")
