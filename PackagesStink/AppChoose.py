import sys
import time
from Index import myDir

myList = ['NoRecoil']

AppChoose = input('Hey Welcome to AppChoose, if you want the list of Application type \"List\", or just type the name or the application/file ')
if AppChoose == ('List'):
    print(myList)
    time.sleep(5)
    AppList = input('Which app/file do you want to execute')
    if AppList == ('NoRecoil'):
        dir = 'C:\\Users\\Robin\\Desktop\\PackagesStink\\Dir\\NoRecoil.ahk'
        time.sleep(3)
        print('The NoRecoil Started, you can close this Window')
        myDir