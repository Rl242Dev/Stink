import random
import string

print('Hey welcome to PasswordGenerator, type the lenght of the password that you want.')

Passlength = int(input('Enter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,Passlength)
password = "".join(temp)

print(password)

