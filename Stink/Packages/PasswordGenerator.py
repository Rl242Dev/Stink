import random
import string
import time

print('Hey welcome to PasswordGenerator, type the lenght of the password that you want.')

x = 'y'

while x == 'y':
    Passlength = int(input('Enter the length of password: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all,Passlength)
    password = "".join(temp)

    print(password)
    time.sleep(5)
    x=input("Do you wanna create a password again y/n:")
    print("\n")
else:
    print('This isn\'t an option')


