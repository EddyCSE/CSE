class Item(object):
    def __init__(self, name):
        self.name = name


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []


class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, description=(), items=None, enemy=None):
        if items is None:
            items = []
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description
        self.items = items
        self.enemy = enemy


class Weapon(Item):
    def __init__(self, name, damage, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = durability

    def attack(self, durability):
        self.durability = durability
        print("You attack with your weapon.")
        self.durability -= 5
        print("You %s had %s durability left" % (durability, Weapon))


class Rock(Weapon):
    def __init__(self):
        super(Rock, self).__init__("Rock", 5, 10)


class MetalBeam(Weapon):
    def __init__(self):
        super(MetalBeam, self).__init__("Metal Beam", 20, 50)


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__("Small Dagger", 25, 30)


class MakeshiftSword(Weapon):
    def __init__(self):
        super(MakeshiftSword, self).__init__("Makeshift Sword", 40, 10)


class Fists(Weapon):
    def __init__(self):
        super(Fists, self).__init__("Fists", 1, 100000000)


class Potion(Item):
    def __init__(self, name, heal, shield, amount):
        super(Potion, self).__init__(name)
        self.heal = heal
        self.shield = shield
        self.amount = amount


class HealthPotion(Potion):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", 50, 0, 0)

    def drink_health_potion(self):
        self.amount -= 1
        print("You drink a health potion and feel regenerated.")


class ShieldPotion(Potion):
    def __init__(self):
        super(ShieldPotion, self).__init__("Shield Potion", 0, 50, 0)

    def drink_shield_potion(self):
        self.amount -= 1
        self.shield += 50
        print("You drink a defense potion and feel protected.")


class LifePotion(Potion):
    def __init__(self):
        super(LifePotion, self).__init__("Life Potion", 50, 50, 0)

    def drink_life_potion(self):
        self.amount -= 1
        self.shield += 50
        print("You drink a life potion and feel revived.")


class Armor(Item):
    def __init__(self, name, defense):
        super(Armor, self).__init__(name)
        self.defense = defense


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self).__init__("Helmet", 50)


class Chestpiece(Armor):
    def __init__(self):
        super(Chestpiece, self).__init__("Chestpiece", 100)


class Leggings(Armor):
    def __init__(self):
        super(Leggings, self).__init__("Leggings", 50)


class Boots(Armor):
    def __init__(self):
        super(Boots, self).__init__("Boots", 25)


class ArmShield(Armor):
    def __init__(self):
        super(ArmShield, self).__init__("An Arm Shield", 100)


class Character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.defense > damage:
            print("But no damage is done because of armor overpowering the weak weapon.")
        elif self.health <= 0:
            print("%s boi died" % self.name)
            return
        else:
            self.health -= damage - self.armor.defense
            print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage." % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Weapons
rock = Weapon("A Rock", 5, 10)
metalbeam = Weapon("A Metal Beam", 20, 50)
dagger = Weapon("A Dagger", 25, 30)
makeshiftsword = Weapon("MakeshiftSword", 40, 10)
legendary_pistol = Weapon("Golden Pistol", 150, 10)
fists = Weapon("Fists", 1, 100000000)

# Armor
chestpiece = Armor("A Metal Chestpiece", 100)
helmet = Armor("A Metal Helmet", 50)
leggings = Armor("Metal Leggings", 100)
boots = Armor("Metal Boots", 50)
arm_shield = Armor("A Metal Arm Shield", 25)

# Potions
healthpotion = Potion("Health Potion", 50, 0, 0)
shieldpotion = Potion("Shield Potion", 0, 50, 0)
lifepotion = Potion("Life Potion", 50, 50, 0)


# Characters
Demon = Character("Demon", 100, makeshiftsword, helmet)
Slug = Character("Slug", 10, rock, None)

OUT = Room("-=-OUT-=-", None, None, None, None, "You've made it out through skill and intelligence."
                                                " You now just need to find civilization and get your way back home. "
                                                "Congrats, you beat the game.", None)  # <-- FRoom
YOUR_CELL = Room("-Your Cell-", "HALLWAY1", None, None, None, "An abandoned cell... you don't know how you got here,"
                                                              " but you need to escape."
                                                              "Your cell door is on the north wall.", None)  # <-- SRoom
UNKNOWN_CELL = Room("- /= --uNkNown cEll- /=-", "OUT", None, "HALLWAY2", None, "You managed to get in and there's an "
                                                                               "escape hole", None)
HALLWAY1 = Room("-East Hallway-", "SHOWER_ROOM", "SECURITY_ROOM2", "YOUR_CELL", "HALLWAY2", "There is a long hallway,"
                                                                                            " breezes coming left and "
                                                                                            "right with a door north "
                                                                                            "of you.", None)
SHOWER_ROOM = Room("-Shower Room-", None, None, "HALLWAY1", None, "A shower room, none of the"
                                                                  " water is working.", None)
HALLWAY2 = Room("-West Hallway-", "UNKNOWN_CELL", "HALLWAY1", "WOMENS_CELL", "SECURITY_ROOM", "There is a long hallway,"
                                                                                              " there's more cells "
                                                                                              "north and south of you. "
                                                                                              "It looks like there "
                                                                                              "were stairs, but it's"
                                                                                              " all destroyed", None)
WOMENS_CELL = Room("-Women's Cell", "HALLWAY2", None, None, None, "A cell with nothing or no"
                                                                  " one in here...", None)
SECURITY_ROOM = Room("-West Security Office-", "WARDENS_OFFICE", "HALLWAY2", "NURSERY", "ENTRANCE", "Seems like nothing"
                                                                                                    " works in here. "
                                                                                                    "Doors north, "
                                                                                                    "south, and west."
                                                                                                    "", None)
NURSERY = Room("-Nursery-", "SECURITY_ROOM", None, None, None, "The area the nurse would be, "
                                                               "kinda scary like always.", None)
WARDENS_OFFICE = Room("-Warden's Office-", None, None, "SECURITY_ROOM", None, "The Warden's "
                                                                              "room, spoopy.", None)
ENTRANCE = Room("-Entrance-", None, "SECURITY_ROOM", None, None, "The exit/entrance, it's all boarded up, can't"
                                                                 " seem to ever get through.")
SECURITY_ROOM2 = Room("-East Security Room-", None, "CAFETERIA", None, "HALLWAY1", "A contraband area, nothing is "
                                                                                   "working. A cafeteria is seen"
                                                                                   " east.", None)
CAFETERIA = Room("-Cafeteria-", "COURT_YARD", "KITCHEN", "LIBRARY", "SECURITY_ROOM2", "Lots of spoiled food is here. "
                                                                                      "Open areas north, east,"
                                                                                      " and south.", None)
COURT_YARD = Room("-Court Yard-", None, None, "CAFETERIA", None, "Basketball, weights, "
                                                                 "and barbed wire located here.")
KITCHEN = Room("-Kitchen-", None, None, None, "CAFETERIA", "Utensils here and a horrible smell.", None)
LIBRARY = Room("-Library-", "CAFETERIA", None, None, "PHONE_ROOM", "Books and 'knowledge here. One of the books have "
                                                                   "been written on it. It reads 'Open the locked"
                                                                   " cell...' ", None)
PHONE_ROOM = Room("-Phone Room-", None, "LIBRARY", None, None, "This is where you call your family, "
                                                               "none of the phones are working. :/")

playing = True
directions = ['north', 'east', 'south', 'west']
actions = ['attack', 'a', 'block', 'b']

player = Player(YOUR_CELL)

Demon.attack(Slug)

'''
while playing:
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in actions:
        try:
            attack = Character.take_damage
        except KeyError:
            print("I can't do that")
    else:
        print("Command Not Found")

while playing:
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in pick_up:
        try:
            if Item in player.current_location:
                
        except KeyError:
            print("I can't do that")
    else:
        print("Command Not Found")
'''

# 1. Put items in room - Done
# 2. Show items in room - Done
# 3. Pick up item -
# 4. Use item -
