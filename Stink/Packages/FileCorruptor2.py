import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

x = lower + upper + num + symbols
y = 450

v = ''.join([random.choice(x) for _ in range(y)])

f = open('Work.txt', 'w')
f.write(v)
f.close()

f = open("Work.txt", "r")
print(f.read())

print('Remember to delete the file after using it, in case if you don\'t delete it the program won\'t work !')
