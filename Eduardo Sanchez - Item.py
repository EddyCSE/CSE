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
        super(MetalBeam, self).__init__("Metal_Beam", 20, 50)


class MakeshiftSword(Weapon):
    def __init__(self):
        super(MakeshiftSword, self).__init__("MakeshiftSword", 40, 10)


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

    def drink_defense_potion(self):
        self.amount -= 1
        self.shield += 50

    def drink_strength_potion(self):
        self.amount -= 1
        self.health += 0


class HealthPotion(Potion):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", 50, 0, 2, 0)


class ShieldPotion(Potion):
    def __init__(self):
        super(ShieldPotion, self).__init__("Shield Potion", 0, 50, 2, 0)


class StrengthPotion(Potion):
    def __init__(self):
        super(StrengthPotion, self).__init__("Health Potion", 0, 0, 2, 0)


class Armor(object):
    def __init__(self, name, defense):
        super(Armor, self).__init__(name)
        self.defense = defense


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self).__init__("Helmet", 10)