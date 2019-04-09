class Item(object):
    def __init__(self, name):
        self.name = name


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        self.current_location = new_location

    def find_next_room(self, direction):
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


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

    def die(self):
        if self.health >= 0:
            print("Your enemy has died has died")
            Room.enemy = None


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
Demon = Character("Demon", 100, makeshiftsword, helmet)
Slug = Character("Slug", 10, rock, None)
