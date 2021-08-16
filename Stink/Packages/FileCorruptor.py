import random
import string
import time

x = 'y'

while x == 'y':
    Passlength = int(input('Enter the length of the file : '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    x = lower + upper + num + symbols

    v = ''.join([random.choice(x) for _ in range(Passlength)])
    print (v)
    time.sleep(5)
    x=input("Do you wanna corrupt a file again y/n:")
    print("\n")
else:
    print('This isn\'t an option')