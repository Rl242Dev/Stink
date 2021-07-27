import sys
import time

class myDirOs:
    def my_function():
        import os
        os.startfile(dir)
        os.system(dir)

        import subprocess
        subprocess.Popen([dir])
        subprocess.call(dir)

myList = ['NoRecoil','ShortCuts','PasswordGenerator','Calculator','DiskCleaner','RPASimulator','DiceSimulator']

print('The version that you are currently using is Version 0.5')
AppChoose = input('Hey Welcome to AppChoose, if you want the list of Application type \"List\", or just type the name or the application/file. ')
if AppChoose == ('List'):
    print(myList)
    time.sleep(5)
    AppList = input('Which app/file do you want to execute.')
    if AppList == ('NoRecoil'):
        dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\NoRecoil.ahk'
        myDirOs
        time.sleep(3)
        print('The NoRecoil Started, you can close this Window.')
    if AppList == ('ShortCuts'):
        dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\ShortCuts.py'
        myDirOs
        time.sleep(3)
        sys.exit
    if AppList == ('PasswordGenerator'):
     dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\PasswordGenerator.py'
     myDirOs
    if AppList == ('Calculator'):
     dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\Calculator.py'
     myDirOs
     time.sleep(3)
     sys.exit
    if AppList == ('DiskCleaner'):
     dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\DiskCleaner.py'
     myDirOs
     time.sleep(3)
     sys.exit
    if AppList == ('DiceSimulator'):
     dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\DiceSimulator.py'
     myDirOs
     time(3)
     sys.exit
    if AppList == ('RPASimulator'):
     dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\RPASimulator'
     myDirOs
     time.sleep(3)
     sys.exit
if AppChoose == ('ShortCuts'):
    dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\ShortCuts.py'
    myDirOs
    time.sleep(3)
    sys.exit
if AppChoose == ('NoRecoil'):
        dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\NoRecoil.ahk'
        myDirOs
        time.sleep(3)
        print('The NoRecoil Started, you can close this Window.')
if AppChoose == ('Calculator'):
     dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\Calculator.py'
     myDirOs
     time.sleep(3)
     sys.exit
if AppChoose == ('PasswordGenerator'):
    dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\PasswordGenerator.py'
    myDirOs
    time.sleep(3)
    sys.exit
if AppChoose == ('DiskCleaner'):
    dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\DiskCleaner.py'
    myDirOs
    time.sleep(3)
    sys.exit
if AppChoose == ('DiceSimulator'):
    dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\DiceSimulator.py'
    myDirOs
    time(3)
    sys.exit
if AppChoose == ('RPASimulator'):
    dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\RPASimulator'
    myDirOs
    time.sleep(3)
    sys.exit
else:
    time.sleep(3)
    print('This isn\'t an file or Application avalable on Stink')