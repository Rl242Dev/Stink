import sys

myListOfShortCuts = ['...''...''...''...''...''...''...''...']
#If you dont remember all of your shortcuts, You gotta type them, if you dont understand Check the Github page | https://github.com/Rl242Dev/Stink |


print('The version that you are currently using is Version 0.1')
print('Hey welcome to ShortCuts, if you haven\'t set up ShortCuts already then go to the Githup Page to see | https://github.com/Rl242Dev/Stink | if you have already set up then type \"Pass\'')
Shortcuts = input('Type the name of your shortcut')
if Shortcuts == ('YouChoose'):
#Name of your Shortcut
    dir = 'C:\\...\\...\\'
    #Location of your file
    import os
    os.startfile(dir)
    os.system(dir)

    import subprocess
    subprocess.Popen([dir])
    subprocess.call(dir)
    sys.exit
    #Eveything to start a file
if Shortcuts == ('YouChoose'):
#Name of your Shortcut
    dir = 'C:\\...\\...\\'
    #Location of your file
    import os
    os.startfile(dir)
    os.system(dir)

    import subprocess
    subprocess.Popen([dir])
    subprocess.call(dir)
    sys.exit
    #Eveything to start a file
    #Just Copy and Paste for more ShortCuts
else:
    ListOfShortCuts = input('Type \"List\" if you want the list of shortcuts that you\'ve made')
    if ListOfShortCuts == ('List'):
        print(myListOfShortCuts)