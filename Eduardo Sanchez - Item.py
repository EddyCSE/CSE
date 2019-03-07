class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(object):
    def __init__(self, name, damage, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = durability

    def attack(self, durability):
        self.durability = durability
        print("You attack with your weapon.")


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


class Potion(object):
    def __init__(self, name, heal, shield, amount, health):
        super(Potion, self).__init__(name)
        self.heal = heal
        self.shield = shield
        self.amount = amount
        self.health = health

    def drink_health_potion(self):
        self.amount -= 1
        self.health += 50
        print("You drink a health potion and feel regenerated.")

    def drink_defense_potion(self):
        self.amount -= 1
        self.shield += 50
        print("You drink a defense potion and feel protected.")

    def drink_life_potion(self):
        self.amount -= 1
        self.health += 50
        self.shield += 50
        print("You drink a life potion and feel revived.")


class HealthPotion(Potion):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", 50, 0, 2, 0)


class ShieldPotion(Potion):
    def __init__(self):
        super(ShieldPotion, self).__init__("Shield Potion", 0, 50, 2, 0)


class LifePotion(Potion):
    def __init__(self):
        super(LifePotion, self).__init__("Life Potion", 50, 50, 2, 0)


class Armor(object):
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


class WorldObjects(object):
    def __init__(self):
        super(WorldObjects, self).__init__()