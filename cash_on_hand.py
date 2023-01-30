from pathlib import Path
import csv

# Define function to calculate cash_difference
def cash_hand():
    """
    - This function calculates cash on hanh_difference based on cash amounts over multiple days
    - No parameters required
    """

    # Instantiate file path to current working directory
    fp_readcash = Path.cwd()/"project_group2"/"csv_reports"/"Cash on Hand.csv"
    fp_write = Path.cwd()/"summary_report.txt"

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

        # Initialise counter to 0
        i = 0 

        # Create for loop to iterate over the number of values of cash
        # -1 from the length of cash to skip the last value because future values are unknown
        for values in range(len(cash)-1):

            # Calculate cash_difference by subtracting next value from current value
            cash_difference = cash[values] - cash[values+1]

            # Use mode "a" so that overheads data will not be overwritten
            with fp_write.open(mode="a", encoding="UTF-8") as file2:
                
                # If cash_difference is positive, write its respective data into the .txt file
                if cash_difference > 0:
                    file2.writelines(f"\n[CASH DEFICIT] DAY: {dayc[values+1]}, AMOUNT: USD{cash_difference} ")

                    # Add 1 to counter
                    i +=1 
        with fp_write.open(mode="a", encoding="UTF-8") as file2:

            # If counter is 0, all cash differences are negative
            # This means that each day's cash on hand value is greater than the previous day's
            # If such, report cash surplus
            if i == 0:
                file2.writelines(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    