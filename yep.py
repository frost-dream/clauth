from time import sleep
from pyautogui import hotkey
from pynput.keyboard import Controller,Key
from pyperclip import copy
with open(input()+'.mp3','rb')as a:
    a,b=a.read(),0
sleep(3)
try:
    while True:
        copy(str(a[b:b+100000])[2:-1])
        hotkey('ctrl','v')
        b+=100000
except:
    Controller().type(str(a[b:])[2:-1])
