"""
File: Steeplechase.py
Name: Chen H,S
---------------------------------

"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
             jump()


def turn_right():
    for i in range(3):
        turn_left()

def jump():
    """
    pre-condition: Karel is on the left,facing East
    post-condition: Karel is on the right
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition: Karel is on the left,facing East
    post-condition: Karel is at the upper right, facing North
    # Comment/Un-comment:
    """
    turn_left()
    while not right_is_clear():
        move()

def cross():
    """
    pre-condition: Karel is at the upper left, facing North
    post-condition: Karel is at the upper right, facing South
    """
    turn_right()
    move()


def down():
    turn_right()
    while front_is_clear():
        move()
    turn_left()
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)




