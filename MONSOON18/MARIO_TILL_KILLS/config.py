from __future__ import print_function
import signal,copy,sys,time
from random import randint
import os ,signal

class GetchUnix:
    def __init__(self):
        import tty 

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

getch = GetchUnix()

class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException

def input_char(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

def print_screen(level, bd, mario, enemies, objects, scene):
    os.system('clear')
    bd.init_board(mario)
    for sc in scene:
        sc.draw(bd)
    mario.drawPlayer(bd)
    for en in enemies:
        en.drawEnemy(bd)
    # print ("SCORE: ", mario.score)
    # print ("TIME LEFT: ", timelimit[level] - mario.play_time(), end=' ')
    # print ("\t\t\tLIVES: ", mario.lives)
    bd.render(mario, enemies)