import os
import csv

#creating file path for csv file
csvpath = os.path.join('Resources','election_data.csv')
csvfile = open(csvpath,encoding='utf8')

#opening/reading csv file/collecting data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    total_votes = 0
    long_candidates_list = [ ]
    for row in csvreader:
        total_votes = total_votes + 1
        long_candidates_list.append(str(row[2]))

#creating list of unique candidates
candidate_list = [long_candidates_list[0]]

for i in range(len(long_candidates_list)):
    x = long_candidates_list[i]
    if x not in candidate_list:
        candidate_list.append(x)

#creating list of unique candidates votes
can_tot_votes = [ ]

for i in range(len(candidate_list)):
    ticker = 0
    for j in range(len(long_candidates_list)):
        x = candidate_list[i]
        y = long_candidates_list[j]
        if x == y:
            ticker = ticker + 1
    can_tot_votes.append(ticker)

#calculating percent of votes won    
a = total_votes/100
percent_votes = [x / a for x in can_tot_votes]
percent_votes = [round(x,3) for x in percent_votes]

#finding the index of max votes to find the winner of popular vote
max_votes = 0
for i in range(len(can_tot_votes)):
    x = can_tot_votes[i]
    if x >= max_votes:
        max_votes = x
        index = i

#writing file path for new text file to write into
w_path = os.path.join('Analysis','Election_Results.txt')

#writing analysis into text file
with open(w_path, 'w', newline='') as csvfile1:
    csvwriter = csv.writer(csvfile1, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['--------------------']) 
    csvwriter.writerow(['Total Votes: '+ str(total_votes)])
    csvwriter.writerow(['--------------------']) 
    for i in range(len(candidate_list)):
        csvwriter.writerow([str(candidate_list[i]) + ': ' + str(percent_votes[i]) + '% ' + '(' + str(can_tot_votes[i]) +')'])
    csvwriter.writerow(['--------------------']) 
    csvwriter.writerow(['Winner: ' + candidate_list[index]])
    csvwriter.writerow(['--------------------']) 
 
#printing results in terminal
print('Election Results \n --------------------')
print(f'Total Votes: {total_votes} \n --------------------')
for i in range(len(candidate_list)):
    print(f'{candidate_list[i]}: {percent_votes[i]}% ({can_tot_votes[i]})')
print('--------------------')
print(f'Winner: {candidate_list[index]}')
print('--------------------')
