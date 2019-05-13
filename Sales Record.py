import csv
Total = 0
Div = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Snacks":
            Total += float(row[13])
            Div += 1
Average = Total / Div
print("Average = %s" % Average)

aTotal = 0
aDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Fruits":
            aTotal += float(row[13])
            aDiv += 1
aAverage = aTotal / aDiv
print("Average = %s" % aAverage)

bTotal = 0
bDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Clothes":
            bTotal += float(row[13])
            bDiv += 1
bAverage = bTotal / bDiv
print("Average = %s" % bAverage)

cTotal = 0
cDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Meat":
            cTotal += float(row[13])
            cDiv += 1
cAverage = cTotal / cDiv
print("Average = %s" % cAverage)

dTotal = 0
dDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Beverages":
            dTotal += float(row[13])
            dDiv += 1
dAverage = dTotal / dDiv
print("Average = %s" % dAverage)

eTotal = 0
eDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Office Supplies":
            eTotal += float(row[13])
            eDiv += 1
eAverage = eTotal / eDiv
print("Average = %s" % eAverage)

fTotal = 0
fDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Cosmetics":
            fTotal += float(row[13])
            fDiv += 1
fAverage = fTotal / fDiv
print("Average = %s" % fAverage)

gTotal = 0
gDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Personal Care":
            gTotal += float(row[13])
            gDiv += 1
gAverage = gTotal / gDiv
print("Average = %s" % gAverage)

hTotal = 0
hDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Household":
            hTotal += float(row[13])
            hDiv += 1
hAverage = hTotal / hDiv
print("Average = %s" % hAverage)

iTotal = 0
iDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Vegetables":
            iTotal += float(row[13])
            iDiv += 1
iAverage = iTotal / iDiv
print("Average = %s" % iAverage)

jTotal = 0
jDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Baby Food":
            jTotal += float(row[13])
            jDiv += 1
jAverage = jTotal / jDiv
print("Average = %s" % jAverage)

kTotal = 0
kDiv = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Cereal":
            kTotal += float(row[13])
            kDiv += 1
kAverage = kTotal / kDiv
print("Average = %s" % kAverage)



