from pyautogui import hotkey as b
from time import sleep
sleep(3)
import pynput as a
from os import system
with open('F:/--others--/old laptop/everything/امیرصدرا/موسیقی بی کلام/غمگین/باد.mp3','rb')as c:
    while True:
        system('echo '+str(c.read(1000))[2:-1]+'| clip')
        b('ctrl','v')
