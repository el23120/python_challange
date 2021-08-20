import os
import csv
input_file = os.path.join('Resoursces', 'budget_data.csv')

total_months = 0
total_profit = 0
monthly_profit_change = []
with open(input_file, newline='') as cvsfile:
    cvsreader = csv.reader(cvsfile, delimiter=',')
    csvheader = next(cvsreader)
    for row in cvsreader: 
        total_months = total_months +1 
        total_profit = total_profit+(row[1])
        print(total_profit)
        break
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        break
max_increase_value = max(monthly_profit_change)     
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
#         total_profit.append(int(row[1]))
# rows in the stored file contents
#     
#     for row in csvreader: 