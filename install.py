import os

os.system('sudo cp -r UbuntuEyes /bin')
os.system('crontab -l > tmpcron')
with open('tmpcron', 'r') as f:
    contents = f.read()
    if 'reboot python3 /bin/UbuntuEyes/main.py' not in contents:
        print("Installing UbuntuEyes")
        os.system('echo "@reboot python3 /bin/UbuntuEyes/main.py" >> tmpcron')
        os.system('crontab tmpcron')
        os.system('rm tmpcron')
    else:
        print("Reinstalling UbuntuEyes")

print("Installed UbuntuEyes")
