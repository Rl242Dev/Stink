import sys
import time

myList = ['NoRecoil']

print('The version that you are currently using is Version 0.2')
AppChoose = input('Hey Welcome to AppChoose, if you want the list of Application type \"List\", or just type the name or the application/file ')
if AppChoose == ('List'):
    print(myList)
    time.sleep(5)
    AppList = input('Which app/file do you want to execute')
    if AppList == ('NoRecoil'):
        dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\NoRecoil.ahk'
        time.sleep(3)
        print('The NoRecoil Started, you can close this Window')
else:
    print('This isn\'t an file or Application avalable on Stink')
