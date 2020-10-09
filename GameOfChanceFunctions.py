import random

money = 100


# Write your game of chance functions here

def coin_flip(guess, bet):
    num = random.randint(1, 2)
    if money < bet:
        print("You cant bet more than you own!")
        return

    elif guess == "Heads" and num == 1:
        new_total = money + bet
        print("Heads! You won! You bet $" + str(bet) + " and your new total is $" + str(new_total))

    elif guess == "Tails" and num == 2:
        new_total = money + bet
        print("Tails! You won! You bet $" + str(bet) + "and your new total is $" + str(new_total))
        return new_total

    elif guess != "Tails" and num == 2:
        new_total = money - bet
        print("Sorry! You lost and your new total is $" + str(new_total))
        return new_total

    elif guess != "Heads" and num == 1:
        new_total = money - bet
        print("Sorry! You lost and your new total is $" + str(new_total))
        return new_total

### end dice game ###
money2 = 100

def cho_han(guess, bet2):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    dice_mod = dice_sum % 2
    print("The sum of both sides is: " +str(dice_sum))
    print("Your guess is: "+str(guess))

    if money2 < bet2:
       return print("You cant bet more than you own!")


    elif guess == "Even" and dice_mod == 0:
        print("You are correct! It's even!")
        new_total = money2 + bet2
        print("Your new total is: $"+str(new_total))
    elif guess == "Odd" and dice_mod == 1:
        print("You are correct! Its odd!")
        new_total = money2 + bet2
        print("Your new total is: $" + str(new_total))
    else:
        print("Sorry, you're wrong.")
        new_total = money2 - bet2
        print("Your new total is: $"+str(new_total))




My_money = 200
their_money = 100
def card_game(bet):
    mine = random.randint(1,12)
    theirs = random.randint(1,12)
    print("Your card value is: " + str(mine))
    print("Their card value is: " + str(theirs))
    if mine > theirs:
        print("I win!")
        new_value1 = My_money + bet
        print("My new total is: $" + str(new_value1))
        return bet
    elif mine < theirs:
        print("They win!")
        new_value2 =  My_money - bet
        new_value3 = their_money + bet
        print("You lost! Your new total is: $" + str(new_value2))
        print("Their new total is : $" + str(new_value3))
        return -bet
    else:
        print("It was a tie, no one lost!")
        return 0

def roulette(guess, bet):
    if bet <= 0:
        print("You must place a bet higher than 0.")
        return 0
    result = random.randint(0,37)
    if result == 37:
        print("The wheel landed on: 00.")
    else:
        print("The wheel landed on: "+str(result))

    if guess == "Even" and result % 2 == 0 and result != 0:
        print(str(result) + " is an even number.")
        print("You won " + str(bet) + " dollars!")
        return bet
    if guess =="Odd" and result % 2 == 1 and result != 37:
        print(str(result) + " is an odd number.")
        print("You won " + str(bet) + " dollars!")
        return bet
    else:
        print("You lost.")



### call games here ###
