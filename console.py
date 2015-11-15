'''
Released under The MIT License.
Copyright (c) 2015 Rene Tanczos
https://github.com/gravmatt/py-console
'''
import sys

off='\033[0m\033[27m'
bold='\033[1m'
underscore='\033[4m'
blink='\033[5m'
reverse='\033[7m'
hide='\033[8m'

black='\033[30m'
red='\033[31m'
green='\033[32m'
yellow='\033[33m'
blue='\033[34m'
magenta='\033[35m'
cyan='\033[36m'
white='\033[37m'

bgblack='\033[40m'
bgred='\033[41m'
bggreen='\033[42m'
bgyellow='\033[43m'
bgblue='\033[44m'
bgmagenta='\033[45m'
bgcyan='\033[46m'
bgwhite='\033[47m'

def send(cmd):
    sys.stdout.write(cmd)
    sys.stdout.flush()

def position(line, column):
    send('\033[%s,%sf' % (line, column))

def up(value):
    send('\033[%sA' % value)

def down(value):
    send('\033[%sB' % value)

def right(value):
    send('\033[%sC' % value)

def left(value):
    send('\033[%sD' % value)

def saveCursor():
    send('\033[s')

def restoreCursor(value):
    send('\033[u')

def clear():
    send('\033[2J')

def clearLine():
    send('\033[K')

def write(text, *style):
    if(style):
        send('%s%s%s' % (''.join(style), text, off))
    else:
        send(text)

def writeLine(text, *style):
    write(text+'\n', *style)
