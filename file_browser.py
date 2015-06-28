__author__ = 'ca1ek'


import curses


def main(screen): #screen is a curses window
    while True:
        screen.addstr("kruruurururururkowce")
        screen.refresh()
    #window = curses.newwin(10,10,2,3)
    #window.addstr("jajaja")


if __name__ == '__main__':
    curses.wrapper(main)