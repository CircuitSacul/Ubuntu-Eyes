import os

OLD_COMMANDS = []
COMMANDS = ['@reboot python3 /bin/UbuntuEyes/main.py &']


os.system('git pull')

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
