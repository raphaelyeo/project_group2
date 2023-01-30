from pathlib import Path
import csv
import write

# Define function to find highest overhead
def overhead():
    """
    - This function finds the highest overhead type
    - No parameters required.
    """

    # Instantiate file path to current working directory
    fp_readoverhead = Path.cwd()/"project_group2"/"csv_reports"/"Overheads.csv"

    # Use mode "r" to read file
    with fp_readoverhead.open(mode="r", encoding="UTF8") as file:
        reader = csv.reader(file)

        # Skip header
        next(reader)

        # Create empty lists to append overhead type and its percentage
        overhead_type = []
        percentage = []
        for row in reader:
            overhead_type.append(row[0])
            percentage.append(row[1])
        
        # Use max() function and set key=float to find highest percentage
        max_percentage = max(percentage, key=float)
        # Use if statements to assign the highest to max_overhead_type variable
        if max_percentage == percentage[0]:
            max_overhead_type = overhead_type[0]
        if max_percentage == percentage[1]:
            max_overhead_type = overhead_type[1]
        if max_percentage == percentage[2]:
            max_overhead_type = overhead_type[2]
        if max_percentage == percentage[3]:
            max_overhead_type = overhead_type[3]
        if max_percentage == percentage[4]:
            max_overhead_type = overhead_type[4]
        if max_percentage == percentage[5]:
            max_overhead_type = overhead_type[5]
        if max_percentage == percentage[6]:
            max_overhead_type = overhead_type[6]
        if max_percentage == percentage[7]:
            max_overhead_type = overhead_type[7]
        if max_percentage == percentage[8]:
            max_overhead_type = overhead_type[8]
        if max_percentage == percentage[9]:
            max_overhead_type = overhead_type[9]

    # Use mode "w" to write data into file because overheads goes first    
    with write.fp_write.open(mode="w", encoding="UTF-8") as file2:

        # Write data into file, and convert overhead type to uppercase letters
        file2.writelines(f"[HIGHEST OVERHEADS] {max_overhead_type.upper()}: {max_percentage}%")
