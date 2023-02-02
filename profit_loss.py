from pathlib import Path
import csv

# File will be used as module
# Define function to calculate profit deficit
def profit_loss():
   """
   - This function calculates net profit deficit based on net profits over multiple days
   - No parameters required
   """

# Instantiate file path to current working directory
   fp_readpl = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
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

        # Initialise counter to 0.
      i = 0 

        # Create for loop to iterate over the number of values of net_profit.
        # -1 from the length of net_profit to skip the last value because future values are unknown.
      for values in range(len(net_profit)-1):

            # Calculate net_profit_difference by subtracting next value from current value
            net_profit_difference = net_profit[values] - net_profit[values+1]

            # Use mode "a" so that overheads data will not be overwritten
            with fp_write.open(mode="a", encoding="UTF-8") as file2:
                
                # If net_profit_difference is positive, write its respective data into the .txt file.
                if net_profit_difference > 0:
                    file2.writelines(f"\n[PROFIT DEFICIT] DAY: {dayp[values+1]}, AMOUNT: USD{net_profit_difference} ")

                    # Add 1 to counter
                    i +=1 
      with fp_write.open(mode="a", encoding="UTF-8") as file2:

         # If counter is 0, all net profit differences are negative.
         # This means that each day's net profit value is greater than the previous day's.
         # If such, report net profit surplus.
         if i == 0:
            file2.writelines(f"\n[PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")


    
