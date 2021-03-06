class Item(object):
    def __init__(self, name):
        self.name = name


class Player(object):
    def __init__(self, starting_location, health, shield, name, weapon):
        self.name = name
        self.current_location = starting_location
        self.inventory = []
        self.health = health
        self.shield = shield
        self.weapon = weapon

    def move(self, new_location):
        self.current_location = new_location

    def find_next_room(self, direction):
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]

    def take_damage(self, damage: int):
        if self.shield.defense > damage:
            print("But no damage is done because of armor overpowering the weak weapon.")
        elif self.health <= 0:
            print("You have died")
            return
        else:
            self.health -= damage - self.shield.defense
            print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage." % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, description=(), items=None, enemy=None):
        if items is None:
            items = []
        if enemy is None:
            enemy = []
        self.character = Enemy
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


class LegendaryPistol(Weapon):
    def __init__(self):
        super(LegendaryPistol, self).__init__("Legendary Pistol", 150, 10)


class EnemyFists(Weapon):
    def __init__(self):
        super(EnemyFists, self).__init__("Fists", 10, 100000000)


class WardenSword(Weapon):
    def __init__(self):
        super(WardenSword, self).__init__("Warden's Sword", 50, 100000000)


class EnemySword(Weapon):
    def __init__(self):
        super(EnemySword, self).__init__("Enemy Sword", 25, 100000000)


class Potion(Item):
    def __init__(self, name, heal, shield, amount):
        super(Potion, self).__init__(name)
        self.heal = heal
        self.shield = shield
        self.amount = amount


class HealthPotion(Potion):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", 50, 0, 3)

    def drink_health_potion(self):
        self.amount -= 1
        print("You drink a health potion and feel regenerated.")


class ShieldPotion(Potion):
    def __init__(self):
        super(ShieldPotion, self).__init__("Shield Potion", 0, 50, 3)

    def drink_shield_potion(self):
        self.amount -= 1
        self.shield += 50
        print("You drink a defense potion and feel protected.")


class LifePotion(Potion):
    def __init__(self):
        super(LifePotion, self).__init__("Life Potion", 50, 50, 3)

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


class Tool(Item):
    def __init__(self, name):
        super(Tool, self).__init__(name)


class Pickaxe(Tool):
    def __init__(self):
        super(Pickaxe, self).__init__("Pickaxe")


class Crowbar(Tool):
    def __init__(self):
        super(Crowbar, self).__init__("Crowbar")


class Screwdriver(Tool):
    def __init__(self):
        super(Screwdriver, self).__init__("Screwdriver")


class Enemy(object):
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
rock = Weapon("A Rock", 5, 15)  # Added
metalbeam = Weapon("A Metal Beam", 20, 50)  # Added
dagger = Weapon("A Dagger", 25, 30)  # Added
makeshiftsword = Weapon("MakeshiftSword", 40, 10)  # Added
legendary_pistol = Weapon("Golden Pistol", 150, 10)  # Added
fists = Weapon("Fists", 1, 100000000)  # Added
enemy_fists = Weapon("Fists", 10, 100000000)  # Added
warden_sword = Weapon("Warden's sword", 50, 100000000)  # Added
enemy_sword = Weapon("Sword", 25, 100000000)  # Added

# Armor
chestpiece = Armor("A Metal Chestpiece", 100)  # Added
helmet = Armor("A Metal Helmet", 50)  # Added
leggings = Armor("Metal Leggings", 100)  # Added
boots = Armor("Metal Boots", 50)  # Added
arm_shield = Armor("A Metal Arm Shield", 25)  # Added

# Potions
healthpotion = Potion("Health Potion", 50, 0, 3)  # Added
shieldpotion = Potion("Shield Potion", 0, 50, 3)  # Added
lifepotion = Potion("Life Potion", 50, 50, 3)  # Added

# Tools
pickaxe = Tool("A Sturdy Pickaxe")  # Added
crowbar = Tool("A Crowbar")  # Added
screwdriver = Tool("A Screwdriver")  # Added

# Characters
Demon = Enemy("Demon", 50, enemy_sword, helmet)  # Added
Demon1 = Enemy("Demon", 50, enemy_sword, helmet)  # Added
Demon2 = Enemy("Demon", 50, enemy_sword, helmet)  # Added
Demon3 = Enemy("Demon", 50, enemy_sword, helmet)  # Added
Demon4 = Enemy("Demon", 50, enemy_sword, helmet)  # Added
Slug = Enemy("Slug", 10, enemy_fists, None)  # Added
Slug1 = Enemy("Slug", 10, enemy_fists, None)  # Added
Slug2 = Enemy("Slug", 10, enemy_fists, None)  # Added
Slug3 = Enemy("Slug", 10, enemy_fists, None)  # Added
Slug4 = Enemy("Slug", 10, enemy_fists, None)  # Added
Warden = Enemy("Warden", 300, warden_sword, Chestpiece)  # Added

OUT = Room("-=-OUT-=-", None, None, None, None, "- You've made it out through skill and intelligence."
                                                " You now just need to find civilization and get your way back home. "
                                                "Congrats, you beat the game.", None, None)
YOUR_CELL = Room("-Your Cell-", "HALLWAY1", None, None, None, "- For command list, type 'commands', An abandoned cell"
                                                              "... you don't know how you got here,"
                                                              " but you need to escape."
                                                              " Your cell door is on the north wall."
                                                              "", Rock(), Slug)
UNKNOWN_CELL = Room("- /= --uNkNown cEll- /=-", "OUT", None, "HALLWAY2", None, "- You managed to get in and there's an "
                                                                               "escape hole."
                                                                               "", Chestpiece(), Demon)
HALLWAY1 = Room("-East Hallway-", "SHOWER_ROOM", "SECURITY_ROOM2", "YOUR_CELL", "HALLWAY2", "- There is a long hallway,"
                                                                                            " breezes coming left and "
                                                                                            "right with a door north "
                                                                                            "of you."
                                                                                            "", Dagger(), Slug)
SHOWER_ROOM = Room("-Shower Room-", None, None, "HALLWAY1", None, "- A shower room, none of the water is working."
                                                                  "", MetalBeam(), Slug1)
HALLWAY2 = Room("-West Hallway-", "UNKNOWN_CELL", "HALLWAY1", "WOMENS_CELL", "SECURITY_ROOM", "- There is a long"
                                                                                              " hallway,there's more"
                                                                                              " cells north and south"
                                                                                              " of you. "
                                                                                              "It looks like there "
                                                                                              "were stairs, but it's"
                                                                                              " all destroyed."
                                                                                              "", None, Slug2)
WOMENS_CELL = Room("-Women's Cell", "HALLWAY2", None, None, None, "- A cell with nothing or no"
                                                                  " one in here..."
                                                                  "", LegendaryPistol(), Warden)
SECURITY_ROOM = Room("-West Security Office-", "WARDENS_OFFICE", "HALLWAY2", "NURSERY", "ENTRANCE", "- Seems like"
                                                                                                    " nothing"
                                                                                                    " works in here. "
                                                                                                    "Doors north, "
                                                                                                    "south, and west."
                                                                                                    "", None, Demon2)
NURSERY = Room("-Nursery-", "SECURITY_ROOM", None, None, None, "- The area the nurse would be, "
                                                               "kinda scary like always. "
                                                               "", ArmShield(), Slug3)
WARDENS_OFFICE = Room("-Warden's Office-", None, None, "SECURITY_ROOM", None, "- The Warden's "
                                                                              "room, looks like a strong entity"
                                                                              " lived here. "
                                                                              "", MakeshiftSword(), Demon1)
ENTRANCE = Room("-Entrance-", None, "SECURITY_ROOM", None, None, "- The exit/entrance, it's all boarded up, can't"
                                                                 " seem to ever get through. "
                                                                 "", Screwdriver(), Slug)
SECURITY_ROOM2 = Room("-East Security Room-", None, "CAFETERIA", None, "HALLWAY1", "- A contraband area, nothing is "
                                                                                   "working. A cafeteria is seen"
                                                                                   " east. "
                                                                                   "Helmet nearby.", Helmet(), None)
CAFETERIA = Room("-Cafeteria-", "COURT_YARD", "KITCHEN", "LIBRARY", "SECURITY_ROOM2", "- Lots of spoiled food is here. "
                                                                                      "Open areas north, east,"
                                                                                      " and south.", None, Slug4)
COURT_YARD = Room("-Court Yard-", None, None, "CAFETERIA", None, "- Basketball, weights, "
                                                                 "and barbed wire located here."
                                                                 "", Pickaxe(), Demon3)
KITCHEN = Room("-Kitchen-", None, None, None, "CAFETERIA", "- Utensils here and a horrible smell. "
                                                           "", Leggings(), None)
LIBRARY = Room("-Library-", "CAFETERIA", None, None, "PHONE_ROOM", "- Books and 'knowledge here. One of the books have "
                                                                   "been written on it. It reads 'Open the locked"
                                                                   " cell...'", Boots(), None)
PHONE_ROOM = Room("-Phone Room-", None, "LIBRARY", None, None, "- This is where you call your family, "
                                                               "none of the phones are working. :/ "
                                                               "", Crowbar(), Demon4)

playing = True
directions = ['north', 'east', 'south', 'west']
inventory = ['inventory', 'i']
pick_up = ['pick up', 'grab']
attack = ['attack', 'hit', 'slash']

player = Player(YOUR_CELL, 100, 0, "You", Fists())

while playing:
    print("---------------------------")
    print(player.current_location.name)
    print("You have %s health" % player.health)
    print("You have %s shields" % player.shield)
    print("You have %s equipped" % player.weapon.name)
    print(player.current_location.description)
    print("---------------------------")

    try:
        print("There is a %s nearby." % player.current_location.items.name)
    except AttributeError:
        pass

    if player.current_location.enemy is not None:
        print("There is a %s wanting to fight." % player.current_location.enemy.name)

    command = input(">_")

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False

    elif command.lower() in ['commands']:
        print("Commands")
        print("---------------------------")
        print("Moving= North, East, South, West")
        print("Actions= Pick up, Grab, attack, hit, slash, inventory, i ")

    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")

    elif command.lower() in inventory:
        print("---------------------------")
        print("Your inventory:")
        print(list(player.inventory))
        print("---------------------------")

    elif command.lower() in pick_up:
        if player.current_location.items is None:
            print("---------------------------")
            print("There is nothing to pick up here.")
            print("---------------------------")
            pass
        else:
            print("---------------------------")
            print("You picked up %s" % player.current_location.items.name)
            player.inventory.append(player.current_location.items.name)
            print(list(player.inventory))
            print("---------------------------")
            player.current_location.items = None

    else:
        print("Command Not Found")
