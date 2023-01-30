from pathlib import Path
import csv

# Define function to find highest overhead
def overhead():
    """
    - This function finds the highest overhead type
    - No parameters required.
    """
    # Instantiate file path to current working directory
    fp_readoverhead = Path.cwd()/"project_group2"/"csv_reports"/"Overheads.csv"
    fp_write = Path.cwd()/"summary_report.txt"

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
            percentage.append(float(row[1]))
        
        # Use max() function and set key=float to find highest percentage
        max_percentage = max(percentage, key=float)
        
        # Find the index of the highest percentage from percentage list
        # Assign max_overhead_type variable to the highest percentage's overhead type by using the same index
        max_overhead_type = overhead_type[percentage.index(max_percentage)]

    # Use mode "w" to write data into file because overheads goes first    
    with fp_write.open(mode="w", encoding="UTF-8") as file2:

        # Write data into file, and convert overhead type to uppercase letters
        file2.writelines(f"[HIGHEST OVERHEADS] {max_overhead_type.upper()}: {max_percentage}%")
