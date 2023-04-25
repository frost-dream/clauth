from shutil import copy,rmtree
from os import scandir,mkdir
from time import sleep
while True:
    for i in scandir(r'C:\Users\lenovo\AppData\Local\FortniteGame\Saved\PersistentDownloadDir\CMS\Files\C28FF1DE0C661DAF01E118A30B3F21B897A7A6E2'):
        copy(i.path,'F:/--others--/others/FortniteGame/0')
    rmtree(r'C:\Users\lenovo\AppData\Local\FortniteGame\Saved\Demos')
    mkdir(r'C:\Users\lenovo\AppData\Local\FortniteGame\Saved\Demos')
    sleep(86400)
