import os
import platform
import subprocess

ostype = platform.system()

if ostype == "Windows":
    subprocess.call(['python', 'winmain.py'])
elif ostype == "Linux":
    subprocess.run(['python', 'linmain.py'])
elif ostype == "Osx":
    subprocess.Popen(['python','osxmain.py'])