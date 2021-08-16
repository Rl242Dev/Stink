import random as r

x = 'y'

while x == 'y':
    n = r.randint(1, 3)
    GetFirstPlay = input('What do you play ? :')
    if GetFirstPlay == 'Paper':
        if n == 1:
            print('Rock')
            print('You won!')
        if n == 2:
            print('Paper')
            print('Nul')
        if n == 3:
            print('Scissors')
            print('You losed.')
    if GetFirstPlay == 'Rock':
        if n == 1:
            print('Rock')
            print('Nul')
        if n == 2:
            print('Paper')
            print('You losed.')
        if n == 3:
            print('Scissors')
            print('You won!')
    if GetFirstPlay == 'Scissors':
        if n == 1:
            print('Rock')
            print('You losed.')
        if n == 2:
            print('Paper')
            print('You won!')
        if n == 3:
            print('Scissors')
            print('Nul')
    x = input("Do you wanna play again y/n:")