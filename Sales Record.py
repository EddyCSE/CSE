import csv

Total = 0
Div = 0

with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Fruits":
            Total += float(row[13])
            Div += 1
Average = Total / Div
print("Fruits Average = %s" % Average)
