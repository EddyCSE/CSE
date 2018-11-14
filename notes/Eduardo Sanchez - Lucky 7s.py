import random
money = 15
rounds = 0
playing = True
max_money = 15

while money > 0 and playing:
    money -= 1
    rounds += 1
    if random.randint(1, 6) + random.randint(1, 6) == 7:
        money += 5
        if money >= max_money:
            max_money += 5
    else:
        playing = True
        if money == 0:
            print("You've played %s rounds." % rounds)
            print("You should've stopped at %s dollars." % max_money)
