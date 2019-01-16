import random
import string

print("Guess out my word...")

words = ["thigh", "computer", "mouse", "chair", "shirt", "o'clock", "concatenation", "pajama", "soccer", "sweater",
         "goldfish", "human", "haphazard", "wildebeest", "pixel", "Wiebe"]

randword = (random.choice(words))
randword = '-' * len(randword)
wordlist = []
wordlist.append(randword)
print(wordlist)

guess1 = input("Guess a letter")

if guess1