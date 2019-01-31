import string
print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)
print(string.whitespace)


# This just see if the program gets an error and deals with it how you want it.
try:
    room_name = current_node['PATHS'][command.upper()]
    current_node = world_map[room_name]
except KeyError:
    print("I can't go that way")