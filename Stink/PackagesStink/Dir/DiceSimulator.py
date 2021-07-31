import random

x = 'y'

while x == 'y':

    getRandom = random.randint(1,6)

    if getRandom == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        print("You Rolled 1")
    if getRandom == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
        print("You Rolled 2")
    if getRandom == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        print("You Rolled 3")
    if getRandom == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        print("You Rolled 4")
    if getRandom == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        print("You Rolled 5")
    if getRandom == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
        print("You Rolled 6")
          
    x=input("Do you wanna roll again y/n:")
    print("\n")
else:
    print('This isn\'t an option')