from pathlib import Path
import csv
import write

# Define function to calculate cash deficit
def cash_hand():
    """
    - This function calculates cash on hand deficit based on cash amounts over multiple days
    - No parameters required
    """

    # Declare cash_deficit1-5 as global variables
    global cash_deficit1, cash_deficit2, cash_deficit3, cash_deficit4, cash_deficit5

    # Instantiate file path to current working directory
    fp_readcash = Path.cwd()/"project_group2"/"csv_reports"/"Cash on Hand.csv"

    # Use mode "r" to read file
    with fp_readcash.open(mode="r", encoding="UTF8") as file:
        reader = csv.reader(file)

        # Skip header
        next(reader)

        # Create empty list to store cash and day values
        cash = []
        dayc = []

    # Convert day and cash to float/int respectively and append them to their empty list 
        for row in reader:
            row[1] = int(row[1])
            row[0] = float(row[0])
            cash.append(row[1])
            dayc.append(row[0])
        
        # Calculate cash difference between consecutive days
        cash_deficit1 = (cash[0] - cash[1])
        cash_deficit2 = (cash[1] - cash[2])
        cash_deficit3 = (cash[2] - cash[3])
        cash_deficit4 = (cash[3] - cash[4])
        cash_deficit5 = (cash[4] - cash[5])
    
    # Use mode "a" to append data so as to not overwrite overheads data
    with write.fp_write.open(mode="a", encoding="UTF-8") as file2:

        # Use if statements to check if cash deficit is positive
        # If positive, append the cash deficit and its day into the .txt file
        if cash_deficit1 > 0:
            file2.writelines(f"\n[CASH DEFICIT] DAY: {dayc[1]}, AMOUNT: USD{cash_deficit1} ")
        if cash_deficit2 > 0:
            file2.writelines(f"\n[CASH DEFICIT] DAY: {dayc[2]}, AMOUNT: USD{cash_deficit2} ")
        if cash_deficit3 > 0:
            file2.writelines(f"\n[CASH DEFICIT] DAY: {dayc[3]}, AMOUNT: USD{cash_deficit3} ")
        if cash_deficit4 > 0:
            file2.writelines(f"\n[CASH DEFICIT] DAY: {dayc[4]}, AMOUNT: USD{cash_deficit4} ")
        if cash_deficit5 > 0:
            file2.writelines(f"\n[CASH DEFICIT] DAY: {dayc[5]}, AMOUNT: USD{cash_deficit5} ")
        if cash_deficit1 < 0 and cash_deficit2 < 0 and cash_deficit3 < 0 and cash_deficit4 < 0 and cash_deficit5 < 0:
            file2.writelines("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")


