import random
import string
guesses = 6
output = []
AllLetters = string.ascii_letters
words = ["thigh", "computer", "mouse", "chair", "shirt", "o'clock", "concatenation", "pajama", "soccer", "sweater",
         "goldfish", "human", "haphazard", "wildebeest", "pixel", "Wiebe"]

print("Guess out my word...")
randword = (random.choice(words))
wordlist = []
wordlist = list(randword)
length = len(randword)


output = len(list(randword))
print(output)



