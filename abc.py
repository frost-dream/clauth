from pygame.mixer import Sound
from pygame import init
from io import BytesIO
init()
with open('Loading Sound1.mp3','rb')as a:
    Sound(BytesIO(a.read())).play()
