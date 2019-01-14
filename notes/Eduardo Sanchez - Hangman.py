import random

print("Guess out my word...")

words = ["thigh", "computer", "mouse", "chair", "shirt", "o'clock", "concatenation", "pajama", "soccer", "sweater",
         "goldfish", "human", "haphazard", "wildebeest", "pixel", "Wiebe"]

randword = (random.choice(words))
wordlist = len(randword)
print(wordlist)
