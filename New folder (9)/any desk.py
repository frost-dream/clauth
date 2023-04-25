from pyautogui import click
from PIL.ImageGrab import grab
from time import sleep
while True:
    sleep(10)
    try:
        grab()
        click('accept.png')
    except:
        pass
