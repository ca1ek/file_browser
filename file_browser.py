__author__ = 'ca1ek'


import curses
import time


def main(screen): #screen is a curses window

    window = curses.newwin(10, 10, 2, 3)

    #for i in range(0,10):
    #   screen.addstr("kruruurururururkowce")
    #  screen.refresh()
    # time.sleep(5)

    window.addstr("jajaja")
    time.sleep(5)


if __name__ == '__main__':
    curses.wrapper(main)