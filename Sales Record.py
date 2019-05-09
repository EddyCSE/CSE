import csv
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for column in reader:
        column = column[13]
        print(column)

# roww = row[2]
# if roww = ("Snacks"):
