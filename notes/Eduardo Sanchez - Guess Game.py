import random
(random.randint(0, 10))
guesses_taken = 5

print("Guess a number from 1 to 10")
Guess1 = input("1st guess=")
Guess1 = int(Guess1)

while guesses_taken < 5:
    if Guess1 > random.randint:
        print("Lower")
    elif Guess1 < random.randint:
        print("Greater")
    else:
        print("Correct")

print(random.randint)
