from pynput.keyboard import Controller,Key
from time import sleep
while True:
    sleep(120)
    Controller().press(Key.up)
    Controller().press(Key.enter)
