import pyscreenshot as screen
import os
from numpy import random
from time import sleep
from os.path import expanduser
from datetime import datetime

os.environ["DISPLAY"] = ':0'

TMP_SCREEN_PATH = expanduser('~') + '/.UE/'
LOG_FILE_PATH = expanduser('~') + '/.UE/log.txt'
GRAB_DELAY_RANGE = (5, 20)


def screenshot(save_path=TMP_SCREEN_PATH+str(datetime.now().time())):
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
        main()
    except Exception as e:
        print(e)
        with open(LOG_FILE_PATH, 'a') as f:
            f.write(str(type(e))+str(e)+'\n')
        sleep(5)
        main()


if __name__ == '__main__':
    f = open(LOG_FILE_PATH, 'w+')
    f.write('Startup\n')
    f.close()
    main()
