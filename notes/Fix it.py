print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()

print("So, you're %s old, %s tall and %s heavy." % (age, height, weight))


print("Let's practice everything.")
print("You'd need to know 'bout escapes")
print("with \\ that do \n newlines and \t tabs.")

poem = " The lovely world " \
       " with logic so firmly planted" \
       " cannot discern the needs of love" \
       " nor comprehend passion from intuition" \
       " and requires an explanation" \
       " where there is none."

print("--------------")
print(poem)
print("--------------")


five = (10 - 5)
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars * 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: %d" % start_point)
# it's just like with an f"" string
print("We'd have %d beans, %d jars, and %d crates." % (jelly_beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
