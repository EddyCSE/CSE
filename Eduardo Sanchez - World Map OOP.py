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
                                                "Congrats, you beat the game. ")  # <-- Final Room
YOUR_CELL = Room("-Your Cell-", "HALLWAY1", None, None, None, "An abandoned cell... you don't know how you got here,"
                                                              " but you need to escape."
                                                              "Your cell door is on the north wall.")  # <-- Start Room
UNKNOWN_CELL = Room("- /= --uNkNown cEll- /=-", "OUT", None, "HALLWAY2", None, "You managed to get in and there's an "
                                                                               "escape hole")
HALLWAY1 = Room("-East Hallway-", "SHOWER_ROOM", "SECURITY_ROOM2", "YOUR_CELL", "HALLWAY2", "There is a long hallway,"
                                                                                            " breezes coming left and "
                                                                                            "right with a door north "
                                                                                            "of you.")
SHOWER_ROOM = Room("-Shower Room-", None, None, "HALLWAY1", None, "A shower room, none of the water is working.")
HALLWAY2 = Room("-West Hallway-", "UNKNOWN_CELL", "HALLWAY1", "WOMENS_CELL", "SECURITY_ROOM", "There is a long hallway,"
                                                                                              " there's more cells "
                                                                                              "north and south of you. "
                                                                                              "It looks like there "
                                                                                              "were stairs, but it's"
                                                                                              " all destroyed")
WOMENS_CELL = Room("-Women's Cell", "HALLWAY2", None, None, None, "A cell with nothing or no one in here...")
SECURITY_ROOM = Room("-West Security Office-", "WARDENS_OFFICE", "HALLWAY2", "NURSERY", "ENTRANCE", "Seems like nothing"
                                                                                                    " works in here. "
                                                                                                    "Doors north, "
                                                                                                    "south, and west.")
NURSERY = Room("-Nursery-", "SECURITY_ROOM", None, None, None, "The area the nurse would be, kinda scary like always.")
WARDENS_OFFICE = Room("-Warden's Office-", None, None, "SECURITY_ROOM", None, "The Warden's room, spoopy.")
ENTRANCE = Room("-Entrance-", None, "SECURITY_ROOM", None, None, "The exit/entrance, it's all boarded up, can't"
                                                                 " seem to ever get through.")
SECURITY_ROOM2 = Room("-East Security Room-", None, "CAFETERIA", None, "HALLWAY1", "A contraband area, nothing is "
                                                                                   "working. A cafeteria is seen east.")
CAFETERIA = Room("-Cafeteria-", "COURT_YARD", "KITCHEN", "LIBRARY", "SECURITY_ROOM2", "Lots of spoiled food is here. "
                                                                                      "Open areas north, east,"
                                                                                      " and south.")
COURT_YARD = Room("-Court Yard-", None, None, "CAFETERIA", None, "Basketball, weights, and barbed wire located here.")
KITCHEN = Room("-Kitchen-", None, None, None, "CAFETERIA", "Utensils here and a horrible smell.")
LIBRARY = Room("-Library-", "CAFETERIA", None, None, "PHONE_ROOM", "Books and 'knowledge here. One of the books have "
                                                                   "been written on it. It reads 'Open the locked"
                                                                   " cell...' ")
PHONE_ROOM = Room("-Phone Room-", None, "LIBRARY", None, None, "This is where you call your family, "
                                                               "none of the phones are working. :/")

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
