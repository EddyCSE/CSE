class Item(object):
    def __init__(self, name):
        self.name = name


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


class Potion(Item):
    def __init__(self, name, heal, shield, amount):
        super(Potion, self).__init__(name)
        self.heal = heal
        self.shield = shield
        self.amount = amount


class HealthPotion(Potion):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", 50, 0, 0)

    def drink_potion(self):
        self.amount -= 1
        print("You drink a health potion and feel regenerated.")


class ShieldPotion(Potion):
    def __init__(self):
        super(ShieldPotion, self).__init__("Shield Potion", 0, 50, 0)

    def drink_potion(self):
        self.amount -= 1
        self.shield += 50
        print("You drink a defense potion and feel protected.")


class LifePotion(Potion):
    def __init__(self):
        super(LifePotion, self).__init__("Life Potion", 50, 50, 0)

    def drink_potion(self):
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


class Shield(Armor):
    def __init__(self):
        super(Shield, self).__init__("An Arm Shield", 100)


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
        if self.health <= 0:
            print("%s boi died" % self.name)
            return
        else:
            self.health -= damage - self.armor.defense
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage." % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
rock = Weapon("A Rock", 5, 10)
metalbeam = Weapon("A Metal Beam", 20, 50)
dagger = Weapon("A Dagger", 25, 30)
makeshiftsword = Weapon("MakeshiftSword", 40, 10)

chestpiece = Armor("A Metal Chestpiece", 100)
helmet = Armor("A Metal Helmet", 50)
leggings = Armor("Metal Leggings", 100)
boots = Armor("Metal Boots", 50)
shield = Armor("A Metal Arm Shield", 25)

healthpotion = Potion("Health Potion", 50, 0, 0)
shieldpotion = Potion("Shield Potion", 0, 50, 0)
lifepotion = Potion("Life Potion", 50, 50, 0)


# Characters
orc1 = Character("Orc", 100, makeshiftsword, helmet)
Eddie = Character("Eddie", 1000, makeshiftsword, helmet)

orc1.attack(Eddie)
Eddie.attack(orc1)
Eddie.attack(orc1)
Eddie.attack(orc1)
Eddie.attack(orc1)
Eddie.attack(orc1)
Eddie.attack(orc1)

