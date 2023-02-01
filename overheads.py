# import csv module
import csv                                 
# import Path module from pathlib library
from pathlib import Path                   
# define a function named 'find_highest_overhead'
def find_highest_overhead():              
  
# create a variable 'csv_file' and store the path to the Overheads.csv file
    csv_file = Path.cwd() / "csv_reports" / "Overheads.csv"

# create a variable 'txt_file' and store the path to the summary_report.txt file                                         
    txt_file = Path.cwd() / "summary_report.txt"
                                           
 # create two empty lists, 'overhead_type' and 'percentage'    
    overhead_type, percentage = [], []   
  # open the csv file in read mode and encode in UTF8, store the file object in 'f'
    with csv_file.open(mode="r", encoding="UTF8") as f:
        
 # create a reader object from the csv file 'f'       
        reader = csv.reader(f)             
# skip the header row       
        next(reader)                      
        for row in reader: 
# loop through each row in the csv file
            overhead_type.append(row[0])   
# add the first column value (overhead type) to the 'overhead_type' list
            percentage.append(float(row[1]))
# add the second column value (percentage) as a float to the 'percentage' list

# find the maximum value in the 'percentage' list and store it in 'max_percentage'
            max_percentage = max(percentage)  
# find the corresponding overhead type for the 'max_percentage' and store it in 'max_overhead'
            max_overhead = overhead_type[percentage.index(max_percentage)]


# open the txt file in write mode and encode in UTF8, store the file object in 'f'   
    with txt_file.open(mode="w", encoding="UTF-8") as f:

 # write the highest overhead type and its percentage in the format '[HIGHEST OVERHEADS] OVERHEAD_TYPE: PERCENTAGE%' to the txt file
        f.write(f"[HIGHEST OVERHEADS] {max_overhead.upper()}: {max_percentage}%")
                                           
