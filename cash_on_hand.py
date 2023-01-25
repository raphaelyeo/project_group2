from pathlib import Path
import csv
import diff

fp = Path.cwd()/"project_group2"/"csv_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF8") as file:
    reader = csv.reader(file)
    next(reader)
    day_and_cash = []
    for row in reader:
        row[0] = int(row[0])
        row[1] = int(row[1])
        day_and_cash.append([row[0],row[1]])
    for sublist in day_and_cash:
        if day_and_cash[0][0] < day_and_cash[1][0]:

            # If difference is positive, calculate difference
            if day_and_cash[0][1] - day_and_cash[1][1] > 0:
                difference1 = diff.diff(day_and_cash[0][1],day_and_cash[1][1])
            
            # If not, assign None to variable, repeat process for subsequent days
            else:
                difference1 = None
        if day_and_cash[1][0] < day_and_cash[2][0]:
            if day_and_cash[1][1] - day_and_cash[2][1] > 0:
                difference2 = diff.diff(day_and_cash[1][1],day_and_cash[2][1])
            else:
                difference2 = None
        if day_and_cash[2][0] < day_and_cash[3][0]:
            if day_and_cash[2][1] - day_and_cash[3][1] > 0:
                difference3 = diff.diff(day_and_cash[2][1],day_and_cash[3][1])
            else:
                difference3 = None
        if day_and_cash[3][0] < day_and_cash[4][0]:
            if day_and_cash[3][1] - day_and_cash[4][1] > 0:
                difference4 = diff.diff(day_and_cash[3][1],day_and_cash[4][1])
            else:
                difference4 = None
        if day_and_cash[4][0] < day_and_cash[5][0]:
            if day_and_cash[4][1] - day_and_cash[5][1] > 0:
                difference5 = diff.diff(day_and_cash[4][1],day_and_cash[5][1])
            else:
                difference5 = None

print(difference1)
print(difference2)
print(difference3)
print(difference4)
print(difference5)