from pathlib import Path
import csv

# Define function to calculate profit deficit
def profit_loss():
   """
   - This function calculates net profit deficit based on net profits over multiple days
   - No parameters required
   """

   # Declare profit_deficit1-5 as global variables
   global profit_deficit1, profit_deficit2, profit_deficit3, profit_deficit4, profit_deficit5

# Instantiate file path to current working directory
   fp_readpl = Path.cwd()/"project_group2"/"csv_reports"/"Profit and Loss.csv"
   fp_write = Path.cwd()/"summary_report.txt"

# Use mode "r" to read file
   with fp_readpl.open(mode="r", encoding="UTF8") as file:

    # Read csv file to append day and net profit to their respective empty lists
       reader = csv.reader(file)

    # Skip header
       next(reader)

    # Create empty lists to store day and net profit
       net_profit = []
       dayp = []

    # Convert values to int/float and append day and net profit to each empty list 
       for row in reader:
            row[4] = int(row[4])
            row[0] = float(row[0])
            net_profit.append(row[4])
            dayp.append(row[0])

      # Calculate the differences in net profit between consecutive days
       profit_deficit1 = net_profit[0] - net_profit[1]
       profit_deficit2 = net_profit[1] - net_profit[2]
       profit_deficit3 = net_profit[2] - net_profit[3]
       profit_deficit4 = net_profit[3] - net_profit[4]
       profit_deficit5 = net_profit[4] - net_profit[5]

   # Using mode "a" to append data so as to not overwrite overhead data   
   with fp_write.open(mode="a", encoding="UTF-8") as file2:

      # Use if/else statements to check whether profit difference is positive
      # If it is positive, append the deficit and its respective day into the .txt file
      if profit_deficit1 >= 0:
         file2.writelines(f"\n[PROFIT DEFICIT] DAY: {dayp[1]}, AMOUNT: USD{profit_deficit1}")
      if profit_deficit2 >= 0:
         file2.writelines(f"\n[PROFIT DEFICIT] DAY: {dayp[2]}, AMOUNT: USD{profit_deficit2}")
      if profit_deficit3 >= 0:
         file2.writelines(f"\n[PROFIT DEFICIT] DAY: {dayp[3]}, AMOUNT: USD{profit_deficit3}")
      if profit_deficit4 >= 0:
         file2.writelines(f"\n[PROFIT DEFICIT] DAY: {dayp[4]}, AMOUNT: USD{profit_deficit4}")
      if profit_deficit5 >= 0:
         file2.writelines(f"\n[PROFIT DEFICIT] DAY: {dayp[5]}, AMOUNT: USD{profit_deficit5}")
      if profit_deficit1 < 0 and profit_deficit2 < 0 and profit_deficit3 < 0 and profit_deficit4 < 0 and profit_deficit5 < 0:
         file2.writelines("\n[PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
