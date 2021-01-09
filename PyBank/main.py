import os
import csv

#writing the file path to the csv file with the data
csvpath = os.path.join('Resources','budget_data.csv')
csvfile = open(csvpath,encoding='utf8')

#opening the csv file, collecting the data and storing them in lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    total_vol = 0
    ticker = 0
    next(csvreader)
    date = [ ]
    profit = [ ]
    for row in csvreader:
        ticker = ticker + 1
        total_vol = total_vol + int(row[1])
        date.append(str(row[0]))
        profit.append(int(row[1]))

#calculating the change in profit from month to month
change_list = [ ]

for i in range(1,len(profit)):
    change =  profit[i] - profit[i-1]
    change_list.append(change)

#calculating the greatest increase in profit
max_change = 0
for i in range(len(change_list)):
    if change_list[i] >= max_change:
        max_change = change_list[i]
        index1 = i+1
        
#calculating the greatest decrease in profit
min_change = 0
for i in range(len(change_list)):
    if change_list[i] <= min_change:
        min_change = change_list[i]
        index2 = i+1

#calculating average change in profit
ave_change = round(sum(change_list)/len(change_list),2)

#writing file path for new text file
w_path = os.path.join('Analysis','Financial_Analysis.txt')

#writing analysis into text file
with open(w_path, 'w', newline='') as csvfile1:
    csvwriter = csv.writer(csvfile1, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Total Months: ' + str(ticker)])
    csvwriter.writerow(['Total: $' + str(total_vol)])
    csvwriter.writerow(['Average Change: $' + str(ave_change)])
    csvwriter.writerow(['Greatest Increase in Profits: ' + str(date[index1]) + ' ($ ' + str(max_change) + ')']) 
    csvwriter.writerow(['Greatest Decrease in Profits: ' + str(date[index2]) + ' ($ ' + str(min_change) + ')'])

#printing analysis in terminal
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {ticker}')
print(f'Total: ${total_vol}')
print(f'Average Change: ${ave_change}')
print(f'Greatest Increase in Profits: {date[index1]} (${max_change})')
print(f'Greatest Decrease in Profits: {date[index2]} (${min_change})')

