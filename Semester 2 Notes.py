"""
print("Hello World")

# single-line comment

Cars = 5
Driving = True

print("I have %d cars." % Cars)
print("I have " + str(Cars) + " cars.")

Age = input("How old are you?")
print(Age + "? lmao, weak.")


Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
Colors.append("Purple")

print(Colors)
Colors.pop(0)
print(Colors)

print(Colors[2])

print(len(Colors))

"""
# Dictionary Notes

states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000  # 39,500,000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000  # 21,300,000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000    # 737,000
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000  # 10,500,000
    }
}

print(nested_dictionary["GA"]["POPULATION"])
print(nested_dictionary["FL"]["NAME"])

georgia = (nested_dictionary["GA"])
print(georgia)

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Fransisco",
            "Los Angeles"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": [
            "Anchorage",
            "Fairbanks",
            "Juneau"
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }
}

print(complex_dictionary["AK"]["CITIES"][0])
print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())

for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("- - " * 20)

# This makes it look pretty
print()
for state, info in complex_dictionary.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 20)
    print("=" * 20)
