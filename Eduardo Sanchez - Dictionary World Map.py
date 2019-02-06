world_map = {
    'YOUR_CELL': {
        'NAME': "Your Cell",
        'DESCRIPTION': "An abandoned cell... you don't know how you got here, but you need to escape."
                       "Your cell door is on the north wall.",
        'PATHS': {
            'NORTH': "HALLWAY1"
        }
    },
    'HALLWAY1': {
        'NAME': "Hallway",
        'DESCRIPTION': "There is a long hallway, breezes coming left and right with a door north of you.",
        'PATHS': {
            'NORTH': "SHOWER_ROOM",
            'EAST': "SECURITY_ROOM",
            'WEST': "HALLWAY2"
        }
    },
    'SHOWER_ROOM': {
        'NAME': "Shower Room",
        'DESCRIPTION': "A shower room, none of the water is working.",
        'PATHS': {
            'SOUTH': "HALLWAY1",
        }
    },
    'HALLWAY2': {
        'NAME': "Hallway",
        'DESCRIPTION': "There is a long hallway, there's more cells north and south of you."
                       "IT looks like there were stairs, but it's all destroyed",
        'PATHS': {
            # 'NORTH': "Locked Cell",
            'EAST': "HALLWAY1",
            'SOUTH': "WOMENS_CELL",
            'WEST': "SECURITY_ROOM"
        }
    },
    'WOMENS_CELL': {
        'NAME': "Women's Cell",
        'DESCRIPTION': "A cell with nothing or no one in here...",
        'PATHS': {
            'NORTH': "HALLWAY2",
        }
    },
    'UNKNOWN_CELL': {
        'NAME': "Unknown Cell",
        'DESCRIPTION': "You managed to get in and there's an escape hole",
        'PATHS': {
            'NORTH': "OUT",
            'SOUTH': "HALLWAY2",
        }
    },
    'SECURITY_ROOM': {
        'NAME': "Security Room",
        'DESCRIPTION': "Seems like nothing works in here."
                       "Doors on the north, south, ans west.",
        'PATHS': {
            'NORTH': "WARDENS_OFFICE",
            'EAST': "HALLWAY2",
            'SOUTH': "NURSERY",
            'WEST': "ENTRANCE"
        }
    },
    'NURSERY': {
        'NAME': "Nursery",
        'DESCRIPTION': "The area the nurse would be, kinda scary like always.",
        'PATHS': {
            'NORTH': "SECURITY_ROOM",
        }
    },
    'WARDENS_OFFICE': {
        'NAME': "Warden's Office",
        'DESCRIPTION': "The Warden's room, spoopy.",
        'PATHS': {
            'SOUTH': "SECURITY ROOM",
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
