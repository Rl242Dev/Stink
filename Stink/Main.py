import  time

myHelp = ["To run an app type the name of the app/file, if there's any error(s) you can message me on Github Name:Rl242Dev (Same for suggestions just message me). You gotta type the exact name of the file/app to execute it."]

TotalChoose = input("Welcome to Stink, if you want help to see Commands type \"Help\'.To Choose an App type \"AppChoose\".") 
if TotalChoose == ('Help'):
    print(myHelp)
    time.sleep(10)
    print('The app will close, you just gotta restart it')
    time.sleep(5)
    quit()
if TotalChoose == ('AppChoose'):
        print('This is gonna start another Window')
        exec(open("Stink\AppChoose.py").read())
else:
    print('This isn\'t an option')
    quit()
