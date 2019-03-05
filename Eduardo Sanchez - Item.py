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
        super(Rock, self).__init__("Rock", 5)


class MetalBeam(Weapon):
    def __init__(self):
        super(MetalBeam, self).__init__("Metal_Beam", 20)


class MakeshiftSword(Weapon):
    def __init__(self):
        super(MakeshiftSword, self).__init__("MakeshiftSword", 40)


class Potion(object):
    def __init__(self, name, heal):
        super(Potion, self).__init__(name)
        self.heal = heal


class Armor(object):
    def __init__(self, name, defence):
        super(Armor, self).__init__(name)
        self.defence = defence


class
