# 1. Does it gave 16 digits - Working
# 2. Drop the last digit from the number. The last digit is what we want to check against - Working
# 3. Reverse the numbers - Working
# 4. Multiply the digits in odd positions by 2 and subtract 9 to all any result higher than 9 - Not Working
# 5. Add all the numbers together - Not Working
# 6. The taken out num is the amount that you would need to add to get a multiple of 10 - Not Working

Taken_out_num = []


def v(num: str):
    print("------------------------------")
    print(num)
    if not has_16_digits(num):
        return False
    new_list = take_last_digit(num)
    reverse_it(new_list)
    # multiply_odds(new_new_list)


def has_16_digits(num: str):                    # Works
    if len(num) == 16:
        print("1. Num Is 16 Digits.")
        print("------------------------------")
        return True
    else:
        print("ERROR. Num Is NOT 16 Digits.")
        print("------------------------------")


def take_last_digit(num: str):                  # Works
    list_num = list(num)
    Taken_out_num.append(list_num[15])
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])
    list_num.pop(15)
    print(list_num)
    print("2. Last Number Taken Out.")
    print("------------------------------")
    return list_num


def reverse_it(list_num: str):                  # Works
    list_num = (list_num[::-1])
    print(list_num)
    print("3. Number Is Reversed.")
    print("------------------------------")
    return list_num


def multiply_odds(new_num: str):         # Not working
    for i in (len(new_num)):
        if not div_by_2(new_num):
            i = i * 2
            if new_num > 9:
                new_num -= 9
            return len(new_num)


def div_by_2(list_num: str):              # Not working
    if list_num % 2 == 0:
        return True
    return False


# pre_odd_num = int(list_num)             # Not Working
#      if pre_odd_num == [1, 3, 5, 7, 9]:
#          odd_num = pre_odd_num * 2
#          if odd_num == [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
#              odd_num -= 9
#              print(odd_num)
#              return list_num
#      else:
#          pass

print("------------------------------")
numb = input("Enter a 16 digit credit card number here. --->")
print(v(numb))
