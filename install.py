import os

COMMAND = '@reboot python3 /bin/UbuntuEyes/main.py &'

os.system('mkdir ~/.UE')
os.system('sudo cp -r UbuntuEyes /bin')
os.system('crontab -l > tmpcron')
with open('tmpcron', 'r') as f:
    contents = f.read()
    if COMMAND not in contents:
        print("Installing UbuntuEyes")
        os.system(f'echo "{COMMAND}" >> tmpcron')
        os.system('crontab tmpcron')
    else:
        print("Reinstalling UbuntuEyes")
os.system('rm tmpcron')

print("Installed UbuntuEyes")

y_or_n = input("The computer must restart in order to complete the installation; do you want to restart now?")

if y_or_n.lower() in ['yes', 'y']:
    os.system('sudo reboot')
