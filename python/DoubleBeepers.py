"""
File: DoubleBeepers.py
Name:
-------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """

    move()
    double_beepers()
    return_beepers()
    karel_goes_home()


def turn_around():
    turn_left()
    turn_left()


def double_beepers():
    while on_beeper():
        #old beepers, facing East
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


def return_beepers():
    move()
    while on_beeper():
        turn_around()
        pick_beeper()
        move()
        put_beeper()
        turn_around()
        move()


def karel_goes_home():
    turn_around()
    move()
    move()
    turn_around()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)



