import pyscreenshot as screen
import os
from numpy import random
from time import sleep
from os.path import expanduser


TMP_SCREEN_PATH = expanduser('~') + '/.UE/tmp.png'
LOG_FILE_PATH = expanduser('~') + '/.UE/log.txt'
GRAB_DELAY_RANGE = (1, 10)


def screenshot(save_path=TMP_SCREEN_PATH):
    img = screen.grab()
    img.save(save_path)


def delay(delay_range):
    sleep_time = random.randint(delay_range[0], delay_range[1])
    print(f"Sleeping for {sleep_time} seconds")
    sleep(sleep_time)


def main():
    try:
        while True:
            screenshot()
            delay(GRAB_DELAY_RANGE)
    except KeyboardInterrupt:
        print("Nope")
        main()
    except Exception as e:
        print(e)
        with open(LOG_FILE_PATH, 'a') as f:
            f.write(str(type(e))+str(e)+'\n')
        sleep(5)
        main()

f = open(LOG_FILE_PATH, 'w+')
f.write('Startup')
f.close()
main()
