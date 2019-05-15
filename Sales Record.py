import csv

Fruits = 0
Clothes = 0
Meat = 0
Beverages = 0
Office_Supplies = 0
Cosmetics = 0
Snacks = 0
Personal_Care = 0
Household = 0
Vegetables = 0
Baby_Food = 0
Cereal = 0
Item_List = []

with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    for row in reader:
        if row[2] == "Fruits":
            Fruits += float(row[13])
        if row[2] == "Clothes":
            Clothes += float(row[13])
        if row[2] == "Meat":
            Meat += float(row[13])
        if row[2] == "Beverages":
            Beverages += float(row[13])
        if row[2] == "Office Supplies":
            Office_Supplies += float(row[13])
        if row[2] == "Cosmetics":
            Cosmetics += float(row[13])
        if row[2] == "Snacks":
            Snacks += float(row[13])
        if row[2] == "Personal Care":
            Personal_Care += float(row[13])
        if row[2] == "Household":
            Household += float(row[13])
        if row[2] == "Vegetables":
            Vegetables += float(row[13])
        if row[2] == "Baby Food":
            Baby_Food += float(row[13])
        if row[2] == "Cereal":
            Cereal += float(row[13])

print("Fruits Total = %s" % Fruits)
print("Clothes Total = %s" % Clothes)
print("Meat Total = %s" % Meat)
print("Beverages Total = %s" % Beverages)
print("Office_Supplies Total = %s" % Office_Supplies)
print("Cosmetics Total = %s" % Cosmetics)
print("Snacks Total = %s" % Snacks)
print("Personal_Care Total = %s" % Personal_Care)
print("Household Total = %s" % Household)
print("Vegetables Total = %s" % Vegetables)
print("Baby_Food Total = %s" % Baby_Food)
print("Cereal Total = %s" % Cereal)

Item_List.append(Fruits)
Item_List.append(Clothes)
Item_List.append(Meat)
Item_List.append(Beverages)
Item_List.append(Office_Supplies)
Item_List.append(Cosmetics)
Item_List.append(Snacks)
Item_List.append(Personal_Care)
Item_List.append(Household)
Item_List.append(Vegetables)
Item_List.append(Baby_Food)
Item_List.append(Cereal)


def max_num(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


max_num(Item_List)

print(Item_List)
