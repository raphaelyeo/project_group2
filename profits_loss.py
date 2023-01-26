from pathlib import Path
import csv

def profit_loss():

# Instantiate file path to current working directory
   fp = Path.cwd()/"project_group2"/"csv_reports"/"Profit and Loss.csv"

# Use mode "r" to read file
   with fp.open(mode="r", encoding="UTF8") as file:

    # Read csv file to append day and net profit to empty list
       reader = csv.reader(file)

    # Skip header
       next(reader)

    # Create empty list to store day and net profit
       net_profit = []

    # Append day and net profit as a list to each empty list 
       for row in reader:
            row[4] = int(row[4])
            net_profit.append(row[4])
        
        # Use if/else statements to check whether net profit difference between days is positive

       if net_profit[0] > net_profit[1]:
            print(net_profit[0] - net_profit[1])
       if net_profit[1] > net_profit[2]:
            print(net_profit[1] - net_profit[2])
       if net_profit[2] > net_profit[3]:
            print(net_profit[2] - net_profit[3])
       if net_profit[3] > net_profit[4]:
            print(net_profit[3] - net_profit[4])
       if net_profit[4] > net_profit[5]:
            print(net_profit[4] - net_profit[5])

print(profit_loss())

