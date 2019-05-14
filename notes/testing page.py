import string
'''
print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)
print(string.whitespace)


# This just see if the program gets an error and deals with it how you want it.
try:
    room_name = current_node['PATHS'][command.upper()]
    current_node = world_map[room_name]
except KeyError:
    print("I can't go that way")

    world_map = {
        'R19A': {
            'NAME': "Mr. Wiebe's Room",
            'DESCRIPTION': "This is the classroom you are in right now. "
                           "There are two doors on the north wall",
            'PATHS': {
                'NORTH': "PARKING_LOT"
            }
        },
        'PARKING_LOT': {
            'NAME': "The North Parking Lot",
            'DESCRIPTION': "There are a couple of cars parked here.",
            'PATHS': {
                'SOUTH': 'R19A'
            }
        },
    }

    # Controller   node = area
    playing = True
    current_node = world_map['R19A']
    directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

    while playing:
        print(current_node['NAME'])
        print(current_node['DESCRIPTION'])
        command = input(">_")
        if command.lower() in ['q', 'quit', 'exit']:
            playing = False
        elif command.upper() in directions:
            try:
                room_name = current_node['PATHS'][command.upper()]
                current_node = world_map[room_name]
            except KeyError:
                print("I can't go that way")

        else:
            print("Command Not Found")

'': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': "",
            'EAST': "",
            'SOUTH': "",
            'WEST': ""
        }
    },

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")

    else:
        print("Command Not Found")
'''

# aTotal = 0
# aDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Fruits":
#             aTotal += float(row[13])
#             aDiv += 1
# aAverage = aTotal / aDiv
# print("Fruits Average = %s" % aAverage)
#
# bTotal = 0
# bDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Clothes":
#             bTotal += float(row[13])
#             bDiv += 1
# bAverage = bTotal / bDiv
# print("Clothes Average = %s" % bAverage)
#
# cTotal = 0
# cDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Meat":
#             cTotal += float(row[13])
#             cDiv += 1
# cAverage = cTotal / cDiv
# print("Meat Average = %s" % cAverage)
#
# dTotal = 0
# dDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Beverages":
#             dTotal += float(row[13])
#             dDiv += 1
# dAverage = dTotal / dDiv
# print("Beverages Average = %s" % dAverage)
#
# eTotal = 0
# eDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Office Supplies":
#             eTotal += float(row[13])
#             eDiv += 1
# eAverage = eTotal / eDiv
# print("Office Average = %s" % eAverage)
#
# fTotal = 0
# fDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Cosmetics":
#             fTotal += float(row[13])
#             fDiv += 1
# fAverage = fTotal / fDiv
# print("Cosmetics Average = %s" % fAverage)
#
# gTotal = 0
# gDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Personal Care":
#             gTotal += float(row[13])
#             gDiv += 1
# gAverage = gTotal / gDiv
# print("Personal Average = %s" % gAverage)
#
# hTotal = 0
# hDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Household":
#             hTotal += float(row[13])
#             hDiv += 1
# hAverage = hTotal / hDiv
# print("Household Average = %s" % hAverage)
#
# iTotal = 0
# iDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Vegetables":
#             iTotal += float(row[13])
#             iDiv += 1
# iAverage = iTotal / iDiv
# print("Vegetables Average = %s" % iAverage)
#
# jTotal = 0
# jDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Baby Food":
#             jTotal += float(row[13])
#             jDiv += 1
# jAverage = jTotal / jDiv
# print("Baby Food Average = %s" % jAverage)
#
# kTotal = 0
# kDiv = 0
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Cereal":
#             kTotal += float(row[13])
#             kDiv += 1
# kAverage = kTotal / kDiv
# print("Cereal Average = %s" % kAverage)

'''
import csv
Item_List = ['Fruits', 'Clothes', 'Meat', 'Beverages', 'Office Supplies', 'Cosmetics', 'Snacks', 'Personal Care',
             'Household', 'Vegetables', 'Baby Food', 'Cereal']
Total = 0
Div = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    if Item_List == [""]:
        for row in reader:
            if row[2] == Item_List[0]:
                Total += float(row[13])
                Div += 1
        Average = Total / Div
        print("Average = %s" % Average)
        Total = 0
        Div = 0
        Item_List.pop(0)

'''