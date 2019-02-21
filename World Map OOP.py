class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west


# Option 1 - Define as we go
R19A = Room("Mr.Wiebe's Room")
parking_lot = Room("Parking Lot", None, R19A)
R19A.north = parking_lot

# Option 2 - Set all at once, modify controller
R19A = Room("Mr.Wiebe's Room", "parking_lot")
parking_lot = Room("Parking Lot", None, "R19A")

UNKNOWN_CELL = Room("- /= --uNkNown cEll- /=-", "OUT", None, "HALLWAY2", None)
OUT = Room("-=-OUT-=-", None, None, None)
YOUR_CELL = Room("-Your Cell-", "HALLWAY1", None, None)
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
