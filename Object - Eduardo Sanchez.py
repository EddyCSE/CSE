class Balloon(object):
    def __init__(self):
        self.hole = False
        self.obtained = True
        self.water_filled = False
        self.air_filled = False
        self.shiny = True

    def fill_with_water(self):
        if self.hole:
            print("You can't, it's broken.")
            return
        if self.water_filled:
            print("It has already been done.")
        if self.air_filled:
            print("You can't do that.")
        else:
            print("You can't")

    def fill_with_air(self):
        if self.hole:
            print("You can't, it's broken.")
            return
        if self.water_filled:
            print("You can't do that")
        if self.air_filled:
            print("It has already been done.")

    def let_go(self):
        if self.hole:
            print("You can't, it's broken.")
            return
        if self.water_filled and self.air_filled == False:
            print("It dropped to the floor.")
            self.obtained = False
        if self.water_filled:
            print("The balloon splashed on the floor.")
            self.water_filled = False
            self.obtained = False
        if self.air_filled:
            print("The balloon flew away.")
            self.obtained = False

    def throw(self):
        if self.hole:
            print("You can't, it's broken.")
            return
        if self.water_filled and self.air_filled == False:
            print("It dropped to the floor.")
            self.obtained = False
        if self.water_filled:
            print("The balloon went flying and splatted.")
            self.water_filled = False
            self.obtained = False
        if self.air_filled:
            print("The balloon flew away.")
            self.obtained = False

    def squeak(self):
        if self.hole:
            print("You can't, it's broken.")
            return
        if self.shiny:
            print("You squeaked the balloon... great.")
            self.shiny = False
        if self.shiny == False:
            print("It's not shiny.")

    def get_new_balloon(self):
        if self.obtained == False:
            print("You got a new balloon.")
            self.obtained = True

    def shine_balloon(self):
        if self.hole:
            print("You can't, it's broken.")
            return
        if self.shiny == False:
            print("You shined it.")


my_balloon = Balloon()

my_balloon.fill_with_air()
