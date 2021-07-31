import random

x = 'y'

while x == 'y':

    GetDiceRoll = random.randint(1,3)

    if GetDiceRoll == 1:
        print('You\'ve Got Rock')
    if GetDiceRoll == 2:
        print('You\'ve Got Paper')
    if GetDiceRoll == 3:
        print('You\'ve got Scissors')

    x=input("Do you wanna play again y/n:")
    print("\n")
else:
    print('This isn\'t an option')


