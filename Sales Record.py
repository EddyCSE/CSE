import csv


with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        row = row[13]
        print(row)

# with open("MyNewFile.csv", 'w', newline='') as new_csv:
