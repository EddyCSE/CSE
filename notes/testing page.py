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


'''
import csv
Item_List = ['"Fruits"', '"Clothes"', '"Meat"', '"Beverages"', '"Office Supplies"', '"Cosmetics"', '"Snacks"',
             '"Personal Care"', '"Household"', '"Vegetables"', '"Baby Food"', '"Cereal"']
Total = 0
Div = 0
with open("Sales Records.csv", 'r') as o_csv:
    reader = csv.reader(o_csv)
    if Item_List == ():
        for row in reader:
            if row[2] == Item_List[0]:
                Total += float(row[13])
                Div += 1
        Average = Total / Div
        print("Average = %s" % Average)
        Total = 0
        Div = 0
        Item_List.pop(0)
    else:
        print("Done")

'''

# Total = 0
# Div = 0
#
# with open("Sales Records.csv", 'r') as o_csv:
#     reader = csv.reader(o_csv)
#     for row in reader:
#         if row[2] == "Fruits":
#             Total += float(row[13])
#             Div += 1
# Average = Total / Div
# print("Fruits Average = %s" % Average)
