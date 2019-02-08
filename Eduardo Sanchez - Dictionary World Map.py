world_map = {
    'UNKNOWN_CELL': {
        'NAME': "- /= --uNkNown cEll- /=-",
        'DESCRIPTION': "You managed to get in and there's an escape hole",
        'PATHS': {
            'NORTH': "OUT",
            'SOUTH': "HALLWAY2",
        }
    },
    'OUT': {
        'NAME': "-=-OUT-=-",
        'DESCRIPTION': "You've made it out through skill and intelligence. "
                       "You now just need to find civilization and get your way back home. "
                       "Congrats, you beat the game. ",
        'PATHS': {
        }
    },
    'YOUR_CELL': {
        'NAME': "-Your Cell-",
        'DESCRIPTION': "An abandoned cell... you don't know how you got here, but you need to escape. "
                       "Your cell door is on the north wall.",
        'PATHS': {
            'NORTH': "HALLWAY1",
        }
    },
    'HALLWAY1': {
        'NAME': "-East Hallway-",
        'DESCRIPTION': "There is a long hallway, breezes coming left and right with a door north of you.",
        'PATHS': {
            'NORTH': "SHOWER_ROOM",
            'EAST': "SECURITY_ROOM2",
            'WEST': "HALLWAY2",
            'SOUTH': "YOUR_CELL",
        }
    },
    'SHOWER_ROOM': {
        'NAME': "-Shower Room-",
        'DESCRIPTION': "A shower room, none of the water is working.",
        'PATHS': {
            'SOUTH': "HALLWAY1",
        }
    },
    'HALLWAY2': {
        'NAME': "-West Hallway-",
        'DESCRIPTION': "There is a long hallway, there's more cells north and south of you. "
                       "IT looks like there were stairs, but it's all destroyed",
        'PATHS': {
            'NORTH': "UNKNOWN_CELL",
            'EAST': "HALLWAY1",
            'SOUTH': "WOMENS_CELL",
            'WEST': "SECURITY_ROOM"
        }
    },
    'WOMENS_CELL': {
        'NAME': "-Women's Cell-",
        'DESCRIPTION': "A cell with nothing or no one in here...",
        'PATHS': {
            'NORTH': "HALLWAY2",
        }
    },
    'SECURITY_ROOM': {
        'NAME': "-West Security Office-",
        'DESCRIPTION': "Seems like nothing works in here. "
                       "Doors on the north, south, and west.",
        'PATHS': {
            'NORTH': "WARDENS_OFFICE",
            'EAST': "HALLWAY2",
            'SOUTH': "NURSERY",
            'WEST': "ENTRANCE"
        }
    },
    'NURSERY': {
        'NAME': "-Nursery-",
        'DESCRIPTION': "The area the nurse would be, kinda scary like always.",
        'PATHS': {
            'NORTH': "SECURITY_ROOM",
        }
    },
    'WARDENS_OFFICE': {
        'NAME': "-Warden's Office-",
        'DESCRIPTION': "The Warden's room, spoopy.",
        'PATHS': {
            'SOUTH': "SECURITY_ROOM",
        }
    },
    'ENTRANCE': {
        'NAME': "-Entrance-",
        'DESCRIPTION': "The exit/entrance, it's all boarded up, can't seem to ever get through.",
        'PATHS': {
            'EAST': "SECURITY_ROOM",
        }
    },
    'SECURITY_ROOM2': {
        'NAME': "-East Security Room-",
        'DESCRIPTION': "A contraband area, nothing is working. "
                       "A cafeteria is seen east.",
        'PATHS': {
            'EAST': "CAFETERIA",
            'WEST': "HALLWAY1"
        }
    },
    'CAFETERIA': {
        'NAME': "-Cafeteria-",
        'DESCRIPTION': "Lots of spoiled food is here. "
                       "Open areas north, east, and south.",
        'PATHS': {
            'NORTH': "COURT_YARD",
            'EAST': "KITCHEN",
            'SOUTH': "LIBRARY",
            'WEST': "SECURITY_ROOM2"
        }
    },
    'COURT_YARD': {
        'NAME': "-The Court Yard-",
        'DESCRIPTION': "Basketball, weights, and barbed wire located here.",
        'PATHS': {
            'SOUTH': "CAFETERIA",
        }
    },
    'KITCHEN': {
        'NAME': "-The Kitchen-",
        'DESCRIPTION': "Utensils here and a horrible smell.",
        'PATHS': {
            'WEST': "CAFETERIA"
        }
    },
    'LIBRARY': {
        'NAME': "-The Library-",
        'DESCRIPTION': "Books and 'knowledge here. "
                       "One of the books have been written on it. "
                       "It reads 'Open the locked cell...' ",
        'PATHS': {
            'NORTH': "CAFETERIA",
            'WEST': "PHONE_ROOM"
        }
    },
    'PHONE_ROOM': {
        'NAME': "-The Phone Room-",
        'DESCRIPTION': "This is where you call your family, none of the phones are working. :/",
        'PATHS': {
            'EAST': "LIBRARY",
        }
    },
}

# Controller   node = area
playing = True
current_node = world_map['YOUR_CELL']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
actions = ['PICK UP']
items = []

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