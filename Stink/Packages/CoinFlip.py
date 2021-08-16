import random

x = 'y'

while x == 'y':

    n = random.randint(1,2)

    if n == 1:
        print('You flipped heads')
    if n == 2:
        print('You flipped tails')
        
    x=input("Do you wanna play again y/n:")
    print("\n")
else:
    print('This isn\'t an option')