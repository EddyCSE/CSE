import csv

Total = 0

with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Snacks":
            Total += int(row[13])
            print(row[2])
            print(row[13])
            print()
print(Total)
