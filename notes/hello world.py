"""
print("hello world")

# This is a comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. Make notes to myself.
# 2. Comment pieces of code that do not work.
# 3. Make by my code easier to read.

print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple of blank lines here.")

# Math
print(3 + 5)
print(5 - 2)
print(3 + 4)
print(6 / 2)

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)  # Modulus (Remainder)

# powers
# What is 2^20?
print(2 ** 100)

# Taking input
name = input("What is your name?")
print("Hello %s." % name)

age = input("How old are you? >_")
print("%s?!? You belong in a museum." % age)
print()
print("%s is really old. They are %s years old." % (name, age))

# Variable assignments
car_name = "Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 16
car_miles_per_gallon = 0.01

# Make it print "I have a car called Wiebe Mobile. It is a Tesla.
print("I have a car called %s. It is a %s." % (car_name, car_type))

# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print("This is your real age: %d" % hidden_age)
"""
"""
This is a multi-line comment
Anything between the "s is not a run.
"""


# Functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


# Distance Formula
def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)


# For Loops
for i in range(5):  # This gives the numbers 0 through 4
    say_it()

for i in range(10):
    print(i + 1)

for i in range(5):
    f(i)

# While loops
a = 1
while a < 10:
    print(a)
    a += 2  # This is the same as saying a = a + 1


"""
At the moment you START the loop:
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
"""

# Control Structures (If statements)
sunny = False
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return"F"


your_grade = grade_calc(82)
print(your_grade)

# "Random" Notes
import random  # This should be on line 1
print(random.randint(0, 100))


# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3  # A is set to 3
a == 3 # Is A equal to 3?
"""

# Creating a list # USE SQUARED BRACKETS
colors = ["blue", "turquoise", "pink", "orange", "black", "red", "yellow", "green", "white", "brown"]
print(colors)
print(colors[0])
print(colors[1])

# Length of the list
print("There are %d things in the list." % len(colors))

# Changing Elements in a list
colors[1] = "purple"
print(colors)

# Looping through lists
for blahblahblah in colors:
    print(blahblahblah)

'''
1. Make a list with 7 items
2. Change the 3rd thing in the list
3. Print the item
4. Print the full list
'''

food = ["hamburger", "cupcake", "fries", "cake", "sandwich", "cookie", "rice"]
food[2] = "french fries"
print(food[2])
print(food)
print("The last thing in the list is %s" % food[len(food) - 1])

# Slicing a list
print(food[1:3])
print(food[1:4])
print(food[1:])
print(food[:4])
