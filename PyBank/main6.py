#Import modules
import os
import csv

#Set up the path of csv
data_csv = os.path.join("Resources", "budget_data.csv")
#print(data_csv)


with open(data_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    # To skip Header
    csv_header = next(csv_reader)
    #print(csv_header)

# Total amount = data_csv 
    total_months = 0
    #row_count = sum(1 for row in csv_reader)
    print("Finantial Analysis")
    print("..................")
    #print(f"{total_months} : {row_count}")
    #print(row_count)

    #The Total Net amount of "Profit/ Losses" over the entire period
    # create lists

    total_net = 0
    sum_loss = 0
    sum_profit = 0
    profit = 0

    months =[]
    date = [] 
    total_Net = []
    revenue_change =[]
    #total_months = []

    #create lists to store Profit/Loss change
    avgChng = []
    linenum = 0
    first_mnth = 0
    last_mnth = 0
    prev_mnth = 0
    
    #read through each row of data after header
    for row in csv_reader:
          #total_net.append((int(rows[1]))
          #total_months.append(row[0])
        total_months = total_months + 1
        total_net = total_net + int(row[1])
    #print(total_months)
    #print(total_net)
    #print("Total Months is: " + int(total_months) )
    #print("Total Net is: " + int(total_net)  )


    # for x in range(1, len(total_net_profit)):
    #        revenue_change.append((int(total_net_profit[x]) - int(total_net_profit[x-1])))
    # print(f"total_Net: {sum(row_count}")

#The average of the changes in Profit/ Losses over the entire period

    #revenue_average = sum(revenue_change)/ len(revenue_change)

    #print (revenue_average)
#

   # This means we are at the beginning of the file
        if (linenum == 0):
            first_mnth = float(row[1])
            prev_mnth = float(row[1]) 

   # This means we are at the end of the file
        elif (linenum == total_months-1):
            last_mnth = float(row[1])

   # this means we are comparing previous month to current month
        if  (linenum > 0):
            avgChng.append((row[0] , float(row[1]) - prev_mnth))
            prev_mnth = float(row[1])

        linenum = linenum + 1

print(total_months) 
print(total_net)           
avg_Chng = (last_mnth - first_mnth)/ (total_months-1)
print(avg_Chng)
# Average Change :-2315.1176470588234
# Greatest Increase in Revenue:('Feb-2012', 1926159.0):
# Greatest decrease in Revenue:('Sep-2013', -2196167.0):
max_avgChng = max(avgChng, key=lambda item: item[1])
min_avgChng = min(avgChng, key=lambda item: item[1])
print(max_avgChng)
print(min_avgChng)