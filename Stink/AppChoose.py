import time

myList = ['NoRecoil','ShortCuts','PasswordGenerator','Calculator','DiskCleaner','RPASimulator','DiceSimulator','CoinFlip']

AppChoose = input('Hey Welcome to AppChoose, if you want the list of Application type \"List\", or just type the name or the application/file. ')
if AppChoose == ('List'):
    print(myList)
    time.sleep(5)
    AppList = input('Which app/file do you want to execute.')
    if AppList == ('NoRecoil'):
        exec(open('Stink\Packages\NoRecoil.ahk').read())
        time.sleep(3)
    if AppList == ('CoinFlip'):
        exec(open("Stink\Packages\CoinFlip.py").read())
        time.sleep(3)
    if AppList == ('ShortCuts'):
        exec(open("Stink\Packages\ShortCuts.py").read())
        time.sleep(3)
    if AppList == ('PasswordGenerator'):
     exec(open("Stink\Packages\PasswordGenerator.py").read())
    if AppList == ('Calculator'):
     exec(open("Stink\Packages\Calculator.py").read())
     time.sleep(3)
    if AppList == ('DiskCleaner'):
     exec(open("Stink\Packages\DiskCleaner.py").read())
     time.sleep(3)
    if AppList == ('DiceSimulator'):
     exec(open("Stink\Packages\DiceSimulator.py").read())
     time(3)
    if AppList == ('RPASimulator'):
     exec(open("Stink\Packages\RPASimulator.py").read())
     time.sleep(3)
if AppChoose == ('ShortCuts'):
    exec(open("Stink\Packages\ShortCuts.py").read())
    time.sleep(3)
if AppChoose == ('NoRecoil'):
        exec(open("Stink\Packages\NoRecoil.ahk").read())
        time.sleep(3)
if AppChoose == ('Calculator'):
     exec(open("Stink\Packages\Calculator.py").read())
     time.sleep(3)
if AppChoose == ('PasswordGenerator'):
    exec(open("Stink\Packages\PasswordGenerator.py").read())
    time.sleep(3)
if AppChoose == ('DiskCleaner'):
    exec(open("Stink\Packages\DiskCleaner.py").read())
    time.sleep(3)
if AppChoose == ('DiceSimulator'):
    exec(open("Stink\Packages\DiceSimulator.py").read())
    time.sleep(3)
if AppChoose == ('RPASimulator'):
    exec(open("Stink\Packages\RPASimulator.py").read())
    time.sleep(3)
if AppList == ('CoinFlip'):
    exec(open("Stink\Packages\CoinFlip.py").read())
else:
    print('This isn\'t an file or Application avalable on Stink')