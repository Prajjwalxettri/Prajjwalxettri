import platform
import os

global arch

def check_python_architecture():
    global arch
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arch = "32BIT"
    elif architecture[0] == '44bit':
        arch = "44BIT"
    else:
        arch = "INVALID"

def main():
    global arch
    print("\x1b[37m •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES")
    os.system("git pull --quiet")
    print(f"\x1b[37m •\x1b[38;5;196m ->\x1b[37m {arch} DETECED")
    print("\x1b[37m •\x1b[38;5;196m ->\x1b[37m STARTING PRAJJWALv6")
    os.system("python data/PRAJJWALv6-PyProtected-xD.so")

if __name__ == "__prajjwal__":
    check_python_architecture()
    main()
####Logo####
llogo1=1
l
____________  ___     ___   ___  _    _  ___   _     
| ___ \ ___ \/ _ \   |_  | |_  || |  | |/ _ \ | |    
| |_/ / |_/ / /_\ \    | |   | || |  | / /_\ \| |    
|  __/|    /|  _  |    | |   | || |/\| |  _  || |    
| |   | |\ \| | | |/\__/ /\__/ /\  /\  / | | || |____
\_|   \_| \_\_| |_/\____/\____/  \/  \/\_| |_/\_____/

OOWNER❤️❤️❤️PRAJJWAL KC
GITHUB❤️❤️❤️PR(KC)
FACEBOOK❤️❤️❤️prajjwal xettry
