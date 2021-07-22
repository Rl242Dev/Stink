import  sys
import  time

myHelp = ["To run an app type the name of the app/file, if there's any error(s) you can message me on Github Name:Rl242Dev (Same for suggestions just message me). You gotta type the exact name of the file/app to execute it."]
myList = ["NoRecoil"]


print('The version that you are currently using is Version 0.3')
time.sleep(5)
TotalChoose = input("Welcome to Stink, if you want help to see Commands type \"Help\'.To Choose an App type \"AppChoose\".") 
if TotalChoose == ('Help'):
    print(myHelp)
    time.sleep(15)
    print('The app will close, you just gotta restart it')
    time.sleep(5)
    sys.exit
if TotalChoose == ('AppChoose'):
        print('This is gonna start another Window')
        time.sleep(3)
        dir = 'C:\\Users\\Robin\\Desktop\\PackagesStink\\AppChoose.py'
        import os
        os.startfile(dir)
        os.system(dir)

        import subprocess
        subprocess.Popen([dir])
        subprocess.call(dir)
        sys.exit



    




