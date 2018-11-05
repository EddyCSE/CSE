Guess2 = input("2st guess=")


def random_guess2(guess2):
    if guess2 == random.randint:
        return "Correct!"
    elif guess2 > random.randint:
        return "Lower"
    elif guess2 < random.randint:
        return "Greater"


your_2guess = random_guess2
print(your_2guess)



def random_guess1(guess1):
    if guess1 == random.randint:
        return "Correct!"
    elif guess1 > random.randint:
        return "Lower"
    elif guess1 < random.randint:
        return "Greater"
    else:
        return "boi"