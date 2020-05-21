import pyscreenshot as screen
import os
from numpy import random
from time import sleep


TMP_SCREEN_PATH = 'tmp.png'
GRAB_DELAY_RANGE = (1, 10)


def screenshot(save_path=TMP_SCREEN_PATH):
    try:
        img = screen.grab()
        img.save(save_path)
    except Exception as e:
        print(f"Error occurred while capturing screen:\n{e}")


def delay(delay_range):
    sleep_time = random.randint(delay_range[0], delay_range[1])
    print(f"Sleeping for {sleep_time} seconds")
    sleep(sleep_time)


def main():
    while True:
        screenshot()
        delay(GRAB_DELAY_RANGE)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error occurred:\n{e}")
