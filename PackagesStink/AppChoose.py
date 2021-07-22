import sys
import time

myList = ['NoRecoil','ShortCuts','PasswordGenerator']

print('The version that you are currently using is Version 0.3')
AppChoose = input('Hey Welcome to AppChoose, if you want the list of Application type \"List\", or just type the name or the application/file. ')
if AppChoose == ('List'):
    print(myList)
    time.sleep(5)
    AppList = input('Which app/file do you want to execute.')
    if AppList == ('NoRecoil'):
        dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\NoRecoil.ahk'
        import os
        os.startfile(dir)
        os.system(dir)

        import subprocess
        subprocess.Popen([dir])
        subprocess.call(dir)
        time.sleep(3)
        print('The NoRecoil Started, you can close this Window.')
    if AppList == ('ShortCuts'):
        dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\ShortCuts.py'
        import os
        os.startfile(dir)
        os.system(dir)

        import subprocess
        subprocess.Popen([dir])
        subprocess.call(dir)
        time.sleep(3)
        sys.exit
if AppList == ('PasswordGenerator'):
     dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\PasswordGenerator.py'
     import os
     os.startfile(dir)
     os.system(dir)

     import subprocess
     subprocess.Popen([dir])
     subprocess.call(dir)
if AppChoose == ('ShortCuts'):
    dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\ShortCuts.py'
    import os
    os.startfile(dir)
    os.system(dir)

    import subprocess
    subprocess.Popen([dir])
    subprocess.call(dir)
    time.sleep(3)
    sys.exit
if AppChoose == ('NoRecoil'):
        dir = 'C:\\Users\\Robin\\Desktop\\GithubStink\\Stink\\PackagesStink\\Dir\\NoRecoil.ahk'
        import os
        os.startfile(dir)
        os.system(dir)

        import subprocess
        subprocess.Popen([dir])
        subprocess.call(dir)
        time.sleep(3)
        print('The NoRecoil Started, you can close this Window.')
else:
    time.sleep(3)
    print('This isn\'t an file or Application avalable on Stink')
