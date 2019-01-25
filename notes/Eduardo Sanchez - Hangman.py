import random
import string
guesses = 6
output = []
AllLetters = string.ascii_letters
words = ["thigh", "computer", "mouse", "chair", "shirt", "o'clock", "concatenation", "pajama", "soccer", "sweater",
         "goldfish", "human", "haphazard", "wildebeest", "pixel", "Wiebe"]

print("".join(output))

randword = (random.choice(words))
wordlist = list(randword)
length = len(randword)

# Takes the randword into blanks
for i in range(length):
    output.append("_ ")
print("".join(output))
print(randword)

# Takes the guess and checks it in the word list
# The "\n" is a full line space

while guesses > 0 and length > 0:
    guess = input("Guess out my word, letter = ")
    print("\n" * 20)
    if guess in randword:
        print("Nice, that's a letter.")
        print(guesses)
        for i in range(length):  # Testing lines from this one
            if guess in wordlist:
                wordlist.pop(i)
                wordlist.insert(i)
        for i in range(length):
            if randword[i] == guess:
                output.pop(i)
                output.insert(i, guess)  # To this one
        print("".join(output))
        if wordlist == 0:  # Checks if you won
            print("\n" * 10)
            print("Congrats, you won!")
            print("The word was %s" % randword)
    else:
        print("Wrong, guess again.")
        guesses = (guesses - 1)
        print(guesses)
        print("".join(output))
    if guesses <= 0:
        print("\n" * 10)
        print("You ran out of guesses, you failed, he's dead, shame on you")
    if len(wordlist) == 0:  # Checks if you won
        print("\n" * 10)
        print("Congrats, you won!")
        print("The word was %s" % randword)

print(wordlist)
print(randword)
print(length)
print(output)
