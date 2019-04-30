# Does it gave 16 digits - Y
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10


def reverse_it(string):
    print(string[::-1])


reverse_it(num)


def take_last_digit(num: str):
    list_num = list(num)
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])
    last_digit = list_num[15]
    list_num.pop(15)
    print("Last digit = Y")


def has_16_digits(num: str):
    if len(num) == 16:
        print("16 = Y")
        return True


def v(num: str):
    if not has_16_digits(num):
        return False
    take_last_digit(num)


print(v("5431709304959590"))
