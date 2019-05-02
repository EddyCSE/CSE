# Does it gave 16 digits - Y
# Drop the last digit from the number. The last digit is what we want to check against - Y
# Reverse the numbers - Y
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10

Taken_out_word = []


def v(num: str):
    print(num)
    if not has_16_digits(num):
        return False
    take_last_digit(num)
    reverse_it(num)
    print(Taken_out_word)


def has_16_digits(num: str):
    if len(num) == 16:
        print("16 = Y")
        return True


def take_last_digit(num: str):
    list_num = list(num)
    Taken_out_word.append(list_num[15])
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])
    list_num.pop(15)
    print(list_num)
    print("Last digit = Y")


def reverse_it(list_num: str):
    list_num = (list_num[::-1])
    print(list_num)
    print("Reversing = Y")


# def multiply_odds(list_num: str):


print(v("5431709304959590"))
