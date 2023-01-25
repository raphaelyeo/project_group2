from pathlib import Path
import csv
import diff

# Instantiate file path to current working directory
fp = Path.cwd()/"project_group2"/"csv_reports"/"Profit and Loss.csv"

# Use mode "r" to read file
with fp.open(mode="r", encoding="UTF8") as file:

    # Read csv file to append day and net profit to empty list
    reader = csv.reader(file)

    # Skip header
    next(reader)

    # Create empty list to store day and net profit
    day_and_profit = []

    # Append day and net profit as a list to each empty list 
    for row in reader:
        row[0] = int(row[0])
        row[4] = int(row[4])
        day_and_profit.append([row[0],row[4]])
    
    # Use if/else statements to check whether net profit difference between days is positive
    for sublist in day_and_profit:
        if day_and_profit[0][0] < day_and_profit[1][0]:

            # If difference is positive, calculate difference
            if day_and_profit[0][1] - day_and_profit[1][1] > 0:
                difference1 = diff.diff(day_and_profit[0][1],day_and_profit[1][1])
            
            # If not, assign None to variable, repeat process for subsequent days
            else:
                difference1 = None
        if day_and_profit[1][0] < day_and_profit[2][0]:
            if day_and_profit[1][1] - day_and_profit[2][1] > 0:
                difference2 = diff.diff(day_and_profit[1][1],day_and_profit[2][1])
            else:
                difference2 = None
        if day_and_profit[2][0] < day_and_profit[3][0]:
            if day_and_profit[2][1] - day_and_profit[3][1] > 0:
                difference3 = diff.diff(day_and_profit[2][1],day_and_profit[3][1])
            else:
                difference3 = None
        if day_and_profit[3][0] < day_and_profit[4][0]:
            if day_and_profit[3][1] - day_and_profit[4][1] > 0:
                difference4 = diff.diff(day_and_profit[3][1],day_and_profit[4][1])
            else:
                difference4 = None
        if day_and_profit[4][0] < day_and_profit[5][0]:
            if day_and_profit[4][1] - day_and_profit[5][1] > 0:
                difference5 = diff.diff(day_and_profit[4][1],day_and_profit[5][1])
            else:
                difference5 = None
        
# Print to check the differences
print(difference1)
print(difference2)
print(difference3)
print(difference4)
print(difference5)





