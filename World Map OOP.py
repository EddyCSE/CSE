class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, description=()):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room exists in that direction.

        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not exist
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


OUT = Room("-=-OUT-=-", None, None, None, None, "You've made it out through skill and intelligence."
                                                " You now just need to find civilization and get your way back home. "
                                                "Congrats, you beat the game. ")  # <-- Exit Room
YOUR_CELL = Room("-Your Cell-", "HALLWAY1", None, None, None, "An abandoned cell... you don't know how you got here,"
                                                              "but you need to escape."
                                                              "Your cell door is on the north wall.")  # <-- Start Room
UNKNOWN_CELL = Room("- /= --uNkNown cEll- /=-", "OUT", None, "HALLWAY2", None, "You managed to get in and there's an "
                                                                               "escape hole")
HALLWAY1 = Room("-East Hallway-", "SHOWER_ROOM", "SECURITY_ROOM2", "YOUR_CELL", "HALLWAY2")
SHOWER_ROOM = Room("-Shower Room-", None, None, "HALLWAY1", None)
HALLWAY2 = Room("-West Hallway-", "UNKNOWN_CELL", "HALLWAY1", "WOMENS_CELL", "SECURITY_ROOM")
WOMENS_CELL = Room("-Women's Cell", "HALLWAY2", None, None, None)
SECURITY_ROOM = Room("-West Security Office-", "WARDENS_OFFICE", "HALLWAY2", "NURSERY", "ENTRANCE")
NURSERY = Room("-Nursery-", "SECURITY_ROOM", None, None, None)
WARDENS_OFFICE = Room("-Warden's Office-", None, None, "SECURITY_ROOM", None)
ENTRANCE = Room("-Entrance-", None, "SECURITY_ROOM", None, None)
SECURITY_ROOM2 = Room("-East Security Room-", None, "CAFETERIA", None, "HALLWAY1")
CAFETERIA = Room("-Cafeteria-", "COURT_YARD", "KITCHEN", "LIBRARY", "SECURITY_ROOM2")
COURT_YARD = Room("-Court Yard-", None, None, "CAFETERIA", None)
KITCHEN = Room("-Kitchen-", None, None, None, "CAFETERIA")
LIBRARY = Room("-Library-", "CAFETERIA", None, None, "PHONE_ROOM")
PHONE_ROOM = Room("-Phone Room-", None, "LIBRARY", None, None)

player = Player(YOUR_CELL)

playing = True
directions = ['north', 'east', 'south', 'west']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")

    else:
        print("Command Not Found")
