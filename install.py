import os
import sys

OLD_COMMANDS = []
COMMANDS = ['@reboot python3 /bin/UbuntuEyes/main.py &']


def install():
    os.system('mkdir ~/.UE')

    os.system('sudo cp -r UbuntuEyes /bin')

    os.system('crontab -l > tmpcron')
    with open('tmpcron', 'r') as f:
        contents = f.read()
        for command in COMMANDS:
            if command not in contents:
                os.system(f'echo "{command}" >> tmpcron')
                os.system('crontab tmpcron')
            else:
                pass
        for command in OLD_COMMANDS:
            if command in contents:
                contents.replace(command, '')
    os.system('rm tmpcron')


    print("UbuntuEyes Installed")

    y_or_n = input("The computer must restart in order to complete the installation; do you want to restart now?")

    if y_or_n.lower() in ['yes', 'y']:
        os.system('sudo reboot')


def uninstall():
    print("Not implemented")


def menu():
    print("Do you want to")
    print("0. Quit")
    print("1. Install LinuxEyes")
    print("2. Uninstall LunuxEyes")
    try:
        option = int(input(">"))
    except ValueError:
        print("Please choose a valid option")
        menu()
        return
    if option == 0:
        print("Exiting")
        sys.exit()
    if option == 1:
        print("Installing")
        install()
        sys.exit()
    elif option == 2:
        print("Uninstalling")
        uninstall()
        sys.exit()
    else:
        print("Please choose a valid option")
        menu()


if __name__ == '__main__':
    menu()
