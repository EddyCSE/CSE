import Special_Random


class Phone(object):
    def __init__(self, carrier, charge_left=50):
        # These are attributes that a phone has.
        # These should all be relevant to our program.
        self.screen = True
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

    def make_call(self, duration):
        if not self.screen:
            print("You can't make a phone call.")
            print("Your screen is broken.")
            return
        battery_loss_per_minute = 5
        if self.battery_left <= 0:
            print("You can't. Your phone is dead.")
            return
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
            self.battery_left = 0
            print("Your phone dies during the conversation.")
        elif self.battery_left == 0:
            print("Your phone dies at the end of the conversation.")
        else:
            print("You successfully make the phone call.")
            print("Your phone is now at %s percent." % self.battery_left)

    def smash_phone(self):
        print("HULK SMASHHH!!!!")
        print("it broke.")
        self.screen = False

    def repair_phone(self):
        print("You put toothpaste on your screen.")
        print("It work now.")
        self.screen = True


# Initialize Objects
my_phone = Phone("ATT", 100)
your_phone = Phone("Bell", 0)
default_phone = Phone("Verizon")

my_phone.make_call(60)
my_phone.make_call(10)
my_phone.charge(100)
my_phone.make_call(10)
my_phone.smash_phone()
my_phone.make_call(10)
my_phone.repair_phone()
my_phone.make_call(10)

print(Special_Random.RandomWiebe.my_random())
