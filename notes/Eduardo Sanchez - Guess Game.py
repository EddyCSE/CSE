import random
r = (random.randint(0, 10))
guesses_left = 5
playing = True

print("Guess a number from 1 to 10")

while guesses_left > 0 and playing:
    guess = int(input("Guess="))
    if guess > r:
        print("Lower")
        guesses_left -= 1
    elif guess < r:
        print("Greater")
        guesses_left -= 1
    else:

        print("Correct!!!")
        playing = False
