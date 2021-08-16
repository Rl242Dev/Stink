import sys

dir = 'C:\\Windows\\System32\\cleanmgr.exe'
        
import os
os.startfile(dir)
os.system(dir)

import subprocess
subprocess.Popen([dir])
subprocess.call(dir)
