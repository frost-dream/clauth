#1.12.3
from os import remove,rename,scandir
from os.path import isfile,getsize,expanduser
from math import ceil,log10,factorial,fabs,sqrt,sin,cos,tan,log,radians
from sys import argv,exit
from urllib.request import urlopen
from tkinter.filedialog import askopenfilenames,askopenfilename,asksaveasfile,askdirectory
from time import sleep,time
from pystray import Icon,MenuItem
from random import randint,choice
from webbrowser import open as op
from PIL.ImageGrab import grab
from cv2 import VideoCapture,CAP_PROP_FPS,VideoWriter,VideoWriter_fourcc,cvtColor,COLOR_RGB2BGR
from numpy import array
from turtle import*
from winsound import MessageBeep,Beep
from PIL import ImageTk,Image
from shutil import copy
from pynput.keyboard import Listener as li
from pynput.mouse import Listener as lis,Controller
from pygame import draw,init,display,FULLSCREEN,quit
from pygame.mixer import Sound,stop
from moviepy.editor import VideoFileClip
from io import BytesIO
from threading import Thread,Timer
from send2trash import send2trash
from plyer import notification
from tkinter import Tk,Menu,Button,Label,Text,Checkbutton,Listbox,Entry,DISABLED,NORMAL,IntVar,StringVar,OptionMenu,RIGHT,LEFT,Scrollbar,Y,Frame
from tkinter.colorchooser import askcolor
from PIL import Image,ImageTk
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip,ffmpeg_merge_video_audio
from tkinter.messagebox import showerror,showinfo,askyesno,askyesnocancel
a36,a37,a38,a39,a40,a41=[0,0,0,0,0,0]
b65=expanduser("~")+'\\desktop'
a,b81=Tk(),Tk()
b81.attributes('-fullscreen',True)
b81.withdraw()
u=1
a.geometry('600x350+430+220')
a.resizable(False,False)
c78=Image.open(BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00^\x00\x00\x00\\\x08\x06\x00\x00\x00\xe7\x1a\x02e\x00\x00\x00\tpHYs\x00\x00\x12t\x00\x00\x12t\x01\xdef\x1fx\x00\x00#\xaaIDATx\x9c\xed\x9dk\xacd\xd9U\xdf\x7fk\xefsNU\xddg\xbf\xa7g\xba\xa7g<\x8f\xf6L\xdb3\xc6\xe3\xc7\x18{P\x14\x82\x0c\x08\x9c\x90 0\xc1! @\x11\x8a\x12A\x84\x92/QP\x94("\x12"R\x12!\x05"\x14\x11\xc8\x07\x14\xa4\x90\x10D\xc8\x83\xa0\xd8&`c{\xc6\x83\xafgz\xde==\xef~\xdd\xee{oU\x9d\xb3\xf7^\xf9\xb0\xf69U\xb7n\xdd\xdb\xb7{z\xc6\x96\xc2\x92\xeaV\xdd\xaaS\xe7\xec\xb3\xf6\xda\xff\xb5\xd6\x7f\xaf\xbdKT\x95?\x97w_\xdc7\xba\x01\xff\xbfJ\xd1\xbd\x92\xf7}\x03\x9bqc"\xac\rg\xdfS\xce\x0c\xb6\xfd\x7f\xed\x0b\xdd\xbd\xc9\xf2G\xc3\xbb\xd1\xae}\x8b~mJ\xf1s>\x04\xbei:d\x8e\xb2\xfbS\xafG\xc2\xda\xd0\x01\xa5H\xf2\x08\x1b\xe3\xf1Q`\x13\x91E\xbd\xf6\'\xc8\xf2\xa3\xdfT\xca\x97\x0e\xe3\xa7\x15\xdc*}\xdb\x91\xef|\x07\x08k\xc3+w\xde\x7fN\x01\xc9\x0f\'\x02"\t \xa9>\xa0\xaaDU\x92*\t\xc5)\x888\xfa\x02\xc5\xe2"~i\x19\x8e\x1eC\x7f\xf4\xd3 \x82\x1c\xbf\r\x16\x16\x1f\xa2W\xd5\'\x1e\xf9\xe0\x97\x86\xaan\xfd\xda\xc6\xb2,~8\xbd\xe37\xb4\x9b\xe8\xd7\xe6(~\x9e\xd2[\xb9\xc5\xca\x17\xd6\x86\xd7\xeez\xef\x8b3o?@\xe7\xf0\xc5\xb4\x9f%\xa9\xd2*^\x01U\xc5\xa9\xa2\xce\xb1 B5X\xa2\xf9\x8eO\xa0\xab\x87`y\x00\x08r\xf0 r\xe402\x18 \xab\xabH\x7f\x11\xbc{\x10Q\xee\xfe\xf0\x87\xbf\x18\x81W_}\xf5\x04\xfd\xfeHV?V\xdf\xd2\x1b\xdcMv@\xcd^J\xbf\x85\xd2\xc2FV\xfa\x03\xf3\x8e\x98~\x02@M\xd1\xb31\x98\x02\x85\x08\x1e\x08:&]\xae\xd1\xad7H\xc3\x05\x00\xfcx\x8c\x0b\x11]Y\xc2\xa5\x04\xab\t\xbc\xff\xba\x14%/\xfe\xa7\xff\x8c\x8e\xc6\x9c\xbc\xe3\x8e\xf5\xf3\xaf\xbc\xb2\xaa\x97>\xe7\xe4\xd0c\xa3[|\xbbse\xbb\xc5_O\xf1o\xd3\xe2\xaf\x9d\nO\x0b\xb4\xd01G\xe1\xbbKg\xe9\xad\xb5\xe7\xf7\x92*\x8a\xb0\xac\tWT\x8c\x8f\x1e\x86\xd5e8\xb2jM\xf6\x15\x0c*\\\xbf\x8f\x1c;\x86;~\x07\xb2\xb0\x80;t\x08R\x84:\xc2p\x13\x11\x81\x98>]|\xf7\'\xff\x1b\xbdj$\x07>\xfe\xceY\xff\x9e\xce\xf5\x16\x8a\xb06\\\xbf\xf3\xf49w\x13\n\x07@\'0\xa3\xdb\xdf\xb6\xf3\xa7H\xed\x1c\xa4H\xb1\xd5\x10\xe2\x05\xf0\xde\x8e\x19\xf4\x91\xd1\x98\xe8\xb7\x90\xad!\xba\xb1\x81,\xac\xc0\xed\x9b\xb8\xc5E\x08\r\x94=C\xb7\xd5\x95\xdf\x8cO>\xc9\xa9\xef\xfc\xce\x8dW.\xbfuT\x0e~\xe2\x1d\xb3\xfe\xfdc\xfcMZ\xfb\xe5;\x9b\xa7\x05\xf0"\xa7E\xe4\xba\xc7\xcf\x13U%$e\x16h\x92*G_y\x8e7o\x7f\x0f\xa5*\xa5\x14\xa8s\x84B`\xe5v(\xae\xc1\xcaaXZ0G\xeb=\xf4{\x88x\xfc\x91\xa3\xf8\xbbn\x87\xe8\x90\xa3\x87\x11_B\xbf\x84\x85\x01\x88\xe7=\xdf\xf7\xa9\x8d\xf3\x17\xde:JU\xd5\xb2\xf8\x91[\xeb\x88\xe7:\xd7\xfc\xc1\x0e\xb9\x01\xc5\x0bk\xc3K\'\xef;\xefD\x927e\x9f\x16\x91\x1d\xf8\xbc_I\xaa\x84\xb4\xf3\xde\x158\xbc\xf6,\xb2\x02W\xee\xbc\x0fb\xc2\xa7\x84\xa8\xd2\xa4|\x84w0X\x80\xe5E\xe8\r\xa0\x02\xa2"UAq\xf8 \x14\x15r\xfc\x0edu\x15\x96\x07\xb8\xa3\xc7\xa0\xac\x90\xaaBb\x84\x03\x07\xff\xe2\xf1\xef\xfd\xee\xdf\xbdp\xf5\xea\xb2,\xdd\xa2\x0e\xd8\x15j\xa6\xf1\xfe&,\xfd\xd2\x9d\xf7\x9f\x138-\x80s\x0eD@\x15\xe68\xc7\xfd\xc8n\xe3Df\xfe\xf3\xbe@\t\x90\x12B\xb0k\xa9\x83\xad!\xd4#8\xb0\x0cq\x00\x8d\x83\xd8\x90.\x1f\x01\x7f\tW\xf6\xd0\xd0 \xfe\x08\xe9\xca:2XB\x06\x01\x9c\x87\xf1\xd6\xff\xee\x89\xc0x\xdc\xd7\x8d/\x8en\x95\xf2\xe7[\xfc\xcd\x9e\x8c\xb5\xe1\x95S\xa7\xcf9\xc0\xc1i\xef=\xae(\xa0\x8d\xbbc\x9c\x1b\x99\\Ov\xb3\xf8\xc3\xe7\x9fE\xaf\xda\xeb+\xef?M\x01\x14\xaa\x88*\xc3\x18(\xf1\xa8&\xa2\x98\x03V"B\x05EB\xcaet\xb0\x88\xc8&z\xe8 ZVH\xb5\x88;\xb8\x82T}\x8a\xd5U\xfcJ\x1f\xa4D\xee:\x01\xbd\x01\xb2\xbc\xfa\x9d\xfe\xb1G?GQ\x05Y}\xf4\xe6\x9d\xef\xadr\xae\xc2\xda\xf0\xea\xa9\xd3\xe76\xdd\x03/\n\xf2\x808ADpE\x81 \xa8*\x92\xe2\xcd\xb51w\xda\x9c\x8b2\xed2\x0e\xbd|\x96\x8b\'\xef\'\x02^\x84\xbe/@ \xa5\x02\x8f\x92\x04R\x12\x02\t\x89\xa0i\x83\xc2\x05\x82\x14\xa4K\x1b\xc4^\t\xee\n\xee\xd2\x9b\xa8.\x10\x8b\x86\xf2\xc8\x11|\x7f\x01w\xf1-\xf4\xc0!d\xd0\xff\xfd{\xbe\xff\xaf\x90`\xe3\xe5\x0b\xaf\xdf&G\xbem\xeb\xe64\xc6\xad\x8bj\n\xefO;\xe7\x10\x11$\xc3\x8bx\x0f\n\xa2j\xa1\x9bu\xc3\rY\xbc\x85\x8d3o\x8a\xbd\x9f\xd6\'\x9aw\x0e\x92&\x1cB\x00D\x84\xa4\x8a\'\x01B\xa1J\xe3\n\nr{H\xd0\x8c)\xd2\x88\xc6/\xa2\xe2\x80\x86Q\xd8\xc2\xab@o\x0b_\x14\xa4\xa5\x86\xa2\xf2HH\x88\x14<\xfb\x0f\x7f\x0e\x9c_:q\xdbmo\xbc\xca\xe9\xe5\x9b\xd5\xd7\xdb\x82\x1aam\xb8y\xea\xf49W\x94\xc1{w\x06gd\xa7dx\x11@S2\xabm"1\x05\x83\xfa\xfd\xa8>\x1f\x17\xa7->\xebY\x1d\xdc\xf1\xdas\x8c\xde\x12T\xedM\x11\xe5\xad\x87\xee\xc6\xab\xb5\xc1\'P\x01\x8d\x892\x7fwP\xf4P"A\x15Q!" \r\xa9\xe8S\xfb@r\x05\x1b1\xe2T\xf1E\x8f\xaarT\xfd\x01\xe5\x81\x13\xc8R\x81\x14\x03\xe4\xc4a\xb8\xbc\x89\x1c\\\xfd\xe7\xe5?\xf8\xe9_\x90\xc5\x85\x8d\x1b\x8e\xf9w\x8dj\xf6!\xc2\xdap\xf3=\x0f>\xef\xcb\xf2\x8c/K\x04\x07\x92\xa3\x08U\x88\tR2\\\x074Fb\x8c\xfbV|L\xc9\xaczF\xe98\x88=8\xf4\'/\x91\xd4\xa3\xc9\x83("\x89\x8b\xdfz\x027T\x1be\t\x92B\x13\x13\x0e\xa5\x12\x18\xf8\x92\n\x05\x1c\xea\x12\x11o0\x88\xe5\x08\xc3\xa2`TV\xc4\xe4hp\x88\xdfD|\xc1\xf2\xeaa\x8a\xc1a\xca\xbe\xa0\x07\x16\xc1\x97\xb8\xa6\x868\xe6\xde\xdf\xfe\xed\x8dW/\\8*\x07?\xbe\xff\x98_\xbfvs||\x9b\xf2{\xef\xcf\xb8\xa2@\n\x0f^\x90\xaaD\x10\xbbc2L$EcD;\xe7x}\xa5w\xd9\xe9,\xc6x\xc0\xc1\xfb/\xbfD\xd2\x92\x18+\x9a\xd8#\x84\x1e)\x95|\xe8\xea\xcb$/$\x81Z\x13\x8d&F\x9ah\x80\xb1B\x08\r\xb5b8\x8fC5\xe1H\xa8&\x10\xa1\xaf\x91B\x03\x15\x81"\\Ab\xc2\xc7D=\xde\xa2\x19_d\x14\xb6\xe0*\xb0Y\x936#\xac\x8fx\xee\x93\x9fZ\xd2+W\x0e\xe8\xfa\x1fW7\xa2\xc3\x9b\xc2\xf8\xd1\xe9\x87\xcf:\xe7\x1eve\tU\x89x\x8f\xb8\x9c)\xa6\x08\x9bC\xb3z1\xeb\xd6\x98H\xec\xcc<\xe7\x89\xaa\x12r\x96\xbaM\x04(A\xbdpb\xb9G]\xf7hB\x9f\x18+\x10\xa5,\xc6<\xffd\xe2\xf2c\xa0c\x88\xc1\xbaX\x04\xd6U)Q6\x15\xbc6,\x88cY"\xe2<\x11P\x841Jh"\xfd&\x10\xf1l\x89\xf9+Ue<\xaa\xa9\xc7\xca\xc2\xe6\x90\xb0\x12\x91\xd2\xa1I\x90q\x8d\xaf<\xa3\x7f\xf6\xf3\xaf=\xf0\x1b\xff\xfe\xca\x0b\xcf\xad\xbd\xcf\x1d9tAV\xbf\xf5\xba\xd0sS\x16\xef0\xe7\x85\x13\x04A\xc4\x81\xb3\xff-\xd4\xc8JK\xa6t5\xc0\xbe\xbe\xad\xb7\xc7\xec5\x1d\xe9\x84?\xfa_\x82\xaaG\xd5\x91\xd4\xa1\xea2\xd6\xcb\x84\xc7!\xd1\x82Z\x85\xd2\x00#l$\x04\x8d\x8c\x14\xa2&P%\xa2\x14\xaa\x94\x88\xc1%\x8a\xd7\x06\xb4FT\xcc\x98hH\xd1\x1c\xb2\xd6\x114B\x82\x98"\x8c@T\x0f\xb0\xb9\xf1\nM\xd8\x971\xdf\xb0\xe2\x85\xb5\xa1\x14E\xa0\xaa\x90\xa2D\xbc3\\\x97L\xe1\x86\xd8)\xceB\xc1\x94i\xdc}@\x0c-\xe95\xbf\xa5Z\t\xf4-D\x8c\xa9 \xa6\xb2\xeb\x00U\x07*\xa8(\x11\x88*D\xcdq\x94L\xe2\xa9\x84p\x01XO\x91k\xaa\\\xd1D\xc8\xb0T\x03\xeb\xc9\x94\xb2\x88P\xa8\xc7\x91\x88QH\xb5\xb21\x0e\\\xdb\xdc`\xb4\xb9I\xa8k4\x05\xd2hL\xbap\x89\xa7\x7f\xf4\xc78\xfdm\x8f\x91\xde|\xf3\xd8\xbe\xf4\xb8_\xe7*\xac\r\xc7\xf7?t\xd6\r\xfa#7\x18|\x14\xc4\xb0]\xb5\xb3r\x1d\x8e\xd1\xd0\xa0!v\xb8\xde\xd45\xb4t\xc1\x1e\x96\xbc+\xc4\xd8\xc5\xd1\x05!\x9dp\xfc\xf5\xf4\x06\xbf\xf9k\x07I\xad\xa2\x11\x9c$\xcarH\xbfw\x95\xdb\xee\x19\xf1\x95\x83\'Hcs\tI!e\x8b\xaf\x15\xea\x940\xeeHq8D`\t\xc1\x89\xd0G\xf1\xe2A\xa0$\x818\xa8J\xea~\xc5\xb0\t4\xc9\x11$RH\xc5`\xb1\xa4\xbf\xb0\x8a6P\xa4!~e\x15\xb7\xb4\xc4#_\xfc\xec\xb9\xaf\x7f\xe5\xf1\x0f\xca\x81\xd5+\xbbr<7\xe2\\\xc7\xf7=\xf4\xacx\xff\xb08\xffQ\xca\n)\x0b\xa6\xb3\x18\x8d\xd3\xf0b\xc9\x92f\'kQ\xc6\x1e\x16\xbf/\x88\x81\xef\x1f\xbd\xc6\xa1C%!\x9a\xa5\xb7v,b\xdfk\x81\xe6\xc1\xd7^\xc63\x816\xc5\xf8z\x8f57\t\x0c\x05T\x14\xaf\x10\x99t\x0e\xa8A)>\x9f\xb7\xa0\'\x15\xceW8Q\xcc\xf5F\x08\x15!\x05\xcb\t"\xa4\x10\xd0\xf1\x06O|\xe2\x93\xa7\x18\x8f/jJ{\xeav_\x8a\x17\xd6\x86~iq\xc3\x1f=\x84;~\x149v\x0c\x8e\xdd\x06K\x8bP\x96\x16:6\x01\r\xcd\x04f\xa6#\x19\xb1\x98z\xae\xe8u FLcz\xc4\xf1\x1d\xdf~\x80_\xfa\xc5UR*I\xc9#.\xe1|\x83s5\xde\xd5\x88\x8b\\~YII\xcd\xd2\x15\xea<\x92\xa2B\x81\xb2\xe0\x1c\x8b\xce\xb1\x88\xc7\x8b\xeb\x92\xbd\xa0\xd0(\x042E\x81\xe2\xd4\xe1CD\x86\x9b\xac\xa4\xc0\xaa/h\x08l\xaa2\x0c\xeb\xd4\xc3!M\xb3\xc9(\x8c\xd0\xf5\xab\xc4\xf5\r\xc6\x1bo\xf1\x81\xbf\xf4\xed\xa4s\xe7N\xc5\x0b\x9f]\xb8i\xc5\x0bk\xc3\xe6\xcc#k\xee\x8e\xe3\x1f\x93\x83\x87au\x15\xaa\xc2\x1e\x0b\x0b\xe0\x9c\xc5\xe61@L\xa4\x10H1f\xfe<M\x08\xb2]\xf5\xae\x1d\xd7\xbeK\x03\xd0B\x88\xf7x~\xea\xc7\x07\xc4T\x82(\xde7\x88D\x9c$\xbc\x0fx\xdf\xe0\x9c\xc5(\xf5\xa5\xc9\xb9RN\xc2"\x9a#\x18\x1b\x15\xae}_\x13\x90H\x0e\xd49\xc6(\xd7\xd4FB\xa3J\xa3\r\xbe\x0e0\xdc\xc2\r\x87,\xa4\xc0bL\xa4\x14(H9b+\x18\t4M\x84\xcd\x11\x7f\xf2\xa9\x1f\xe0[\x7f\xf0\xd3\xcf\xc5\xcd\x8d\xa5\x9bV\xbc\xdd\xbc{\x04\xef\xb7\x93#\x93\xcf\xb2\x87\x9f\xe2bT\xbbX\xfe\x96\x88\x03\xfa-\xad,3\xac\xe4>\xaf\xd3\xc1Y~\xee\x883k\xae\xd3D\xd4D\x93\x13\xaa\xd0\x86\x0311$\xe2R\x01\x9a\xf0j\xcd)\xb4@c\x81\x8a\xa7Q\xb5!\xedM\x0f\xa1\x19\x124\xa1Q\\\xda\xfc\xe2\\\x1d\xef\xa9xam\x18\xce|h\xcd\x1d>\x04\x0b\x8b0\xe8\x9b\xa2[\x19\x8d\xedN\xc4u\xd6\xae\x99\x81\x04\xd0l\xed{\xa9F\xa7\x1e3\x17\xb7G!\xb0(\xfc\xca\xb1\x8d\x1c\xc1\x08\xce\x05\x9c\x8b\x08\x8as\t\xefB\x1e\x01\x9amC8}\xe1\x1c\xef\xbdp.W)L8\x9f\x04\xa8\n\xaa\x0e\x97!h\x04\xd4I\xa83D\x8dU\x19\x02\xde9\n\xe7\x90\x04\xe3\xd4\x90R\xe2\xb6\x108\x16\x03\x8b!\x015QkF\xa1d\x18\xc7\xd4\xc3\n\x8d\xc0\xabW\xf9?\x7f\xf5\x07\xf9\x9e\xcf|\xfa5\x1d\x0e\xfb\xb3\xb7v]\xc5\xd7\x0f|\xcbS\xb2\xba\xfc\x88,\xee\x06Uj\xda\t\xc1\xe0"\xf32\x13\xd3\xdaG\x10\xb9\xdb\x01-\xb6\xf7@\x0f\t?\xf5\xe3\xa5\x85\x8c\x08\x92ct\xc90#>\x00JJBJ\x9e\x94<\xcd%\xa1W\t\xa5\x17\x9b\x0c\x9f*X\xf0X\xe6X\x8a\xd0sP\xe6\xd7^dR\xc1\x80a\xbd\x13A\x9c\x10\xc4\xc2\xd3:\t>\xc1\x828\xca\xa2"\x89g\x9c\xd6I\xa9\xa1\x96\xabDu\xc8x\x1dY\xbf\xc8\xef\xfc\xf0\x8f\xf0\xb3?\xf3\xf7\xfee\xbc\xf4\xf9\x1d\xca\xbf\x0e\xd4\\o\xaa\xee\x16\xc2\xc9\x1eMP\xd9eT\xb42\x15=M\xb7\xb9E\xc6\xd9\t\x93iq\x19\xba\xe6\xde\xa98&\xe4G+\xd6\x12%u\t\xa3HB\xb5\xa2+Gi/\xec\x85\xa0\xe9\'Iq\x87\x9ewU\xbc\xb06t\xfd\xdeH\x0e\xacB\xaf\xb7\xb3e[C\xa8\x03\xba\xb9i\xe1c\x9c`\xbc\xe4\x8b\xefg\x8eu\xc7\x98h\xbfR\x08Z\t\xba\xea\xf8\xc9\xde[\xa4T\xb6\x83\xc8\x8eQc$\x85`nF=)U\x84h\xc9UJ\x05\xeb\xaf\x14\xf8J\xa8\xbc\xd0s\x8e\x9e\x13\xfa"\x94NX\x10{]!\x0c\xc4\x99\xf5\x8bP8\xb3\xfcF\x95\xb1&\xc61\xe2\xc5\xb3R\x14\xf4\xbd\x91j\xa3d\x19\xafn\xd6T*\x1cp\x15"%HA\xe3\x13\xd1+\xf2\xe6:\xe9\xa5\x97\xf8\x85\xef\xf8n>\xf37~\xe4?\xc4\x8d/l\xd3\xf5\xdc\xf4VX\x1b\xd6g\x1eY\x93^\xf91\xbc\x87r\xe6\xb0:@\xd3\xc0xl\x9a\x08\xb9:.\'S\xe2\xda\xa9\xbe\x89+\x9c\x1b\xb5d%n\x0b5\xb3\xf9i\x85q3\x8bp\xe2\x8e^\x17\xb7\xd3\xc6\xec\xa2\x80\xa5\x99\xd29L\xc9\xe4\x97U\x99\t\xf0\xc8\x95\xf3<\xbet\x12A\xf1\xc9\xe1Er\x85\xdaT\xa7O\xd1\x19%\xe4\xa4\xccx\xfb\xe4\x9c\xf5\xb3*\xdey\xaa\x94\x10\x04\x1f\x952\x8dI\xc3\x1a_\x08\x9e1\x1a\x12\xae\x19 \xc3\x86 c\x8a\xb7\xde\x82#o\xf1\xc2k\xaf~\x9f^^?\x04\\\xd8S\xf1\xf5\x99G\xd6\x04\x1e\xc1\x15P\x146\xf78GT\x13\x8ckSj\xa6q\xad\xe2\xce\xd2sq\x18N\xe7\x9b\xd9\x11V*\x93\xc8\xa2\xab\xd9\xcb\xdfY\x14\xf0\x02\x07\x1c\xff\xf4\xe7*\xc6ci\xcf\xd2\xf5Y\xab\x1cu\x86\xc5v\xc2\x16\xcc\xed\xbc\xbe\x80\xa2p\xa4\xc6\x1c\xaf\x9f\x1a\x85\xdbZ\xd3r\xfd\xb8\x0ez\xda\x87\xaa\x92\x9c\xc7\x01\xa5\xf7\x08\xd08\xa1H\x82w\xca\x96\x08\xde\x15$<MSS\r\xaf!\x0c\x8c\xc5|\xf35\xfe\xf0\x07~\x88t\xed\xeaR\xba\xf2GW]\xe6\xeew(^X\x1b6\xf2\xa1?\x93\xcc<RU;af8\x84\x94\xa0i\x8c}\xd4D\xac\xd4\xce\x16\x05\xcd\x94|\xaa\x84T\xe58\xdf)\x12\xbb\xbb\xb3s&H>\xa1\xa2hK\xb2\x95\xa0\x1eX0\xa8\xf9\'\x87\xd6\xf9Ga\xd9B\xbe\xcc\xbb\x8b$S\xab\xc4\x0c7\x13\x0f\xa0\xe4\x11\x90\x15\xfc\xfa3\x8e\x8b\x1fu\xd6^\x91v\xc0l\x9fN\x94\xc9\xc8\xcc}f\x1d\x99G\x82\xe6NM\xd2R\x14\x82\xd7\x84OB\x10G\x9f\x12*%\xa4\x86":\x9a\xba\xa1L\xaf\x13\x8a%\n\'P\xd7|\xfbg~\xf8\x85?\xfc\xbd\xdf[u0_\xf1\xf9\xba\x1fF\xb0\x04Ivq\x03\x9a\x8c\x10K\x11\xd5\x88.\t\xda\x03\xd7\xe4\x10\xd2\t\xa9\xafh\xcf\x99b\xf3WHX\x8e\xeeLC\xdfu\xf1U\x9c\x07\x9f\xa3\x8f"\x1a\xc6.&\xc7\x828\xde\xb3:\xb0\xc9\x0eZ\x1e\xae\x8d\xe6[\x1f6\xcf\xe5\xca\xa4s\x81\xfb\xdfx\x81\xf1X\xa9\xeb47\x97{\xed\x8e{\xa6\xce)\xdd9\xdak\xb5\x84K\xa9\x90r\x179\xb0\xd9\x16u\x08\x11B\x1f\xe7\x1a\x1a\x97\xe855A\x17)\xc7\x11F\n[#\xea\xf1\x18\xea\xa6\xe3\xec\xe7S\x98\xbd\xca&5\xcabb\x02\xdbn0\xe1\xfe\xfb\x7f\xcd3\xfcB\n=\xc6[GH)s\xd8\x19tU=)\x16\x9d.&\xc0\x92\xfb\x0e\xe1w\xf5x\x86!\xfb\x7f\xc7\x95\xd4\xa1\xeaq\x92pRw\xcav.\xf7\xa0\xec\xd4\xa4\xe9\xdc\x86]\xc2q\xe9\x9c\xe2$\xce\xcd\xffL\x9e\xdf\xed\x83\xddE\x81 T\x8d0~\xdd\xf3\xe0G\x1cO>\xfc\x11\x12#$.\xd9}lEH\xaf"\xe9\x10\x9f\xfd\xd8c0\x1cvq\xf9\x0ev2}p\xf5\xf3\xf4\xca\x8f\xe3=r\xe2\x84\xf11\x00\xe3\xcc\xed\x87\x06\xdex\xcb\xa2\x99\xad\x11J\xe2\xde\xab_\xe3\x89\xff{\x84\x18+\x9b\x8eSORGJ~\xc6s\xea6\xd8\xca\x9cf\xf7\x9am\xdd\xd2j\xd0>\xf1\xae\xb6\x92KQ\n_S\x16\xc6\xcf8\xd7t$\xd9<\x11I8\x898\x97p.pKC`\x85b\x15\xb6N\xbf\x9f\xe8=u9 \xb9\n-\x1a\xe8U\x94\xce\xe3#\xe0\x12\xc5\xc1U\x1e\xf8\xc3?x\xf3\xf9kw\xde\xb6{y\x87\x02\x83\xc5\xed\xd8\xbe\xbc\x02\xd7r\x11K\x8c\xd0X\xe1\x10\x9a\xb8\xb2\x1e\xa9\xca!c-H\xd1\xe7\xfcI\xba\x1b\xdf\xae\t\xed\xacZ\xf2\x08\xe8,\xb1\x8b.\xb2[\x936P\xd2\xec\xb4\xed0G\xca\xb8\xd5\x9d\x94\xbd31i\xeb\xa9\xf6\xb0\xfa\x1b\x17Y\x85t\xfa[\x08\x92\x90\xa0\x88\x1b\xd9T"%\x92\xac\x9e\xc7G\x874\r\xd4J3\xae\xbbDj\x9b\xe2\x85\xb5at\x1f\xffS\x19\xf4\xa1\xdf3\x8c\x07\xa8\x06@\x02\xf16\x033\x1cY\xec\x9e\x1d\xe4\x85\x13\xef#}\x8f\xf2\x97\xab\x17\xf8\xdd\xdfZb4^\x9eR\xa0\xd1\xb6\xce\x85\xae\x13\xec9g\xa038-@R\x81\\-\xa0\xdaj<\xe1\xb2cu.".e\x1a`&=\x9a\xb5\xfe\xe9@\xe7\x16\x89\xac\xd8s|\xe8#h\xbf\xa2\x18\x8e\xa1\xae\xe9\xa90\x1e\xd7\x88\x14H\x99p\xbd\x15$\xd5\xe6&\x87C\xea8I\xa4vz\xce\xb2|\x8c\xa5\x15XY\xca\xb5\x86\x03+\xe6\x04\x18T\xe6Lc4ko%\x814\xf0?\xca\xbb\xf9k\x9f\xd9\xa4*\x87\xc6\x9d\xa09\xb1\xf1\xa4d}\xbc-\x98\x13\x10\x92u\x8c$\x9c\x04D"\xdeE\xc4G\xc4E\x9c\x0f\x88k(2\x1f\xe3}\x83\xb8\xd8\x9dcz\xfa\xcf,{6\x0f\x95\x1d\x19\xed\xdb\x11Y\x81\xe1=\xef\xa3\xf9\xc0G\x91\x85\x01R\r\xa0p\xc8\xe2\x12\xce;D\x1a\x88C\x18;\xa4p\xc8\xd2\x02r`\x19F5\xaf\x9e\xf9\x96\xb5\xf6<;\xc3\xc9\xc5EX\x9e\x13\xcd\x8c\xadW\x19\rAS\xe7\x08\xdb{\x93Z\xe1j\xe2\xbf\x1c8I\xfaY\xe1o\xeb\x1b\xfc\xd2/.f\xeb7\x0eE\xb5\x0fb\xa4\x16`\xcfN\xb3%G\x9cL\x11\x032IQ5G\x18\xed\x08\xb1pr\xbbbs\x91\xc6\x14\x8f#\xdb\xcf%\xfa\xb6`FV\xe0\xea\x9d\xf7\xb3u\x97\xc3\xa1\x96D.W\x86\x02\x8b\x07\xf0)\x90\x82\xd0+z4\xde\xe1\x0f\x1cF\x16\n\x18\xd6H\xb2%CI\xb5\xcb\x88\xb6)\xbe\xf9\xc0\xa3\x8fs\xf0\xc0\xc7X9\xd0\xe6\xfd\x13k\xaf\x1b\xcbV\xa3\xcd\xce\xe3r\xe1\x8aw\x16V\x02\xb2i\x96\xefk\xe5\xdf.\x1d#\xfe\x0c\xfc\xe3\xd57Y])\xf8\xfb?\xbdD\x13{\x90<M*\x0cR\\\xc0\xfb\x1a\x95h\xc5\xad\xce:@\\\xa0\x90\x98\x1d\xef\x8cs\xdeKT\xb0\xf9\xa3\x9c\xd5"\xe6Te\xd2!7\xa3\xf07\xeex\x0fo\xdd!\xc4\x98p\xce\xa11R\x86\x80\x86\x88,\xf4\xa0pP\x07\x9c\x96\xb8fD\xd1\xeb\x93\xe2\x186\x03\xd2\xeb!E\x05u\x8d\x84\xa6\x06[C\xd7\x99\xb5\xb06\xb4\xc8q\x8eYL;\xb2\xdd\xda\x9e\xefU\x020\xb6\x87\x8c\xe1\xca\x95\xc8\x85\x0b\r\xbe\xa8\xb3\xc5\xb6\xd9\xa7v\x93\xd4\xcaT\xc5@\x92\xac\xc0\x9b\x97\x0eY:\xffqs\xd6\xdeby\xeb\x98#\xdaE\xaf\n\xa6\xbd\x94\xe7"\x923Ct\x05\x88\xe0\xa2"adH\x10\x02\x92$G\x05&\xdb,^U?fW\x9c\xb1\xf6\xcc\xb7\xa3\x18\x85 \x13o\xa51M\xa8\x00\x05\x1a\x90k\xa6t\xd9J\xfc\xdb#\xc7P\x85\xbf\xf9S\xaf\xf3k\xbf\x1c\x89\xa9\xa0i\x069\xa1\xf2\x84\xd0C\\\xa4\xf0 \x1aQ\xb1\x0e\xa0\x98v\xa8{r\x93S\x9a\xda\xf6\xd4u\xf0\xbe\xbf?}\xaa\x15x\xf9\xf8]\x04L\xe1\xaa\n\xe2\xac\xd4\xa3(l\xa4G5\x14\xd0\x12\xf0\xd0\x8b\xd0\x17\xa4\xac,\xc5\x18;`d\x9dR8\x88\xda\xe9{{T\x93\x14\n\xbf]\xe9{H\x97\xa4OGs\n\x04\x90\xa8H\x03R$\xa8\x84__9\xce\xdf\xfa\x997\x19\xf4\x1d\xbf\xf8\xf3V\xd88\xae\x97\xcc\xe2\x93\'RR\x14V\x0e"\x14\xa4\x08"\x91\xe4"\x92;\xe0\xfa\xcak\xc3S3\xd1\xd6\xf2-\x8c\xdc\x9f\xc9\xb7V\xfe\xf2\xf1\xbb\x19\xb7E\xb0\xaa\x14"\xb4\x1a\x91\x96\xa7\x97l\x8cA\x01gdb\xd5\x83\xa2\x07\xb1\x86~a0\xdc\xef\xc3hD\xe7\xdc\x98u\xae\xa2\x96(\xf5fH1\x9d\x8a\x9b\xa7r\xee]\xa3g\xcd_\x89\x8a\\\x02q\x8a\x0e\x95_9v\x0cM\xf0\x13\x7f\xf7u\x04\xf8\xe5\x7f\r\xe3\xf1\xa2\xb9D\xf5\x84XR\xf8\xc6\xb8\x1f\xf5\xa0\x1e\xaf\r\xde\x07T\xd2\x9epa\xdc\xcd\x94\x03\xde\xd6J\x87\xea^\x99k>r\x05\xce\x1e;\x85`\xb3P\xedY\x1a\xb1\x99)\x97\x12\x95\x88\xb1\x96\xaa\xf8&\'d\xae0T\x10\x0f\x8b\xa5\x91{\xbe\xb2d3&\xd8\xda\xca#\xd8 ]a\xb0\x1dj\x10l\xeejF\x9ah\xf8\x15\x13p}\xcb\xb1\x04*gCc\xfb\x8a\x85\xee\t<\xfc\xea\xeaq\x10\xf8\x89\xbf\xf3\x06\xff\xe6_9b\xb0\x8c7%O\x92D\xe1\x15M\xe6$\xd5\x1b\xde;\xd2$\xaf\x9d\xd3\xe3-\x9c\xcc\xc6\xf1\xfb\x05\x18Y\x81\'\x8e\x9cd\x8b\x88\xe0(\x92\xd2sV\x87\x99\xd3\x8e\xee\xce\x9d*>\xe4\x15\x83^\x8c\x16\xf7\x80\xefAj,\x10\x01\xb3\xbe\x98\x1dD\xa8I!>\x86\xcd4\xceX|J\x10\x12\x8c\x1bK\xa0vW\xab\xe1\\\xacg\xdf\xcd\xffLMo\xb4\xeed\x04\xf2fv\x1f\x17\xec\xcd\x7f\xb7p\x8c\xbf\xf0\xa9\xf3\xdcq{\xc9o\xfc\xeab\xc6~GLbIRf#\x9d$\x9c\x9b\xc1\xfa\x1d\xe6;\xab\xe2i\xec\x9b\xef\\[X\xf9\xe3#\'\xf8\xdcQ\xb8\x86R(T$\x9c\x08WU\x91\x04=\x84B\x8c$s-\xbb\t\xb8f\x8c\x15\xe3\xd8\xa26B\x82\x8d\xa1\x15n\xe2\xcd\x0f\xb4s\x19\xb5\xda:\xdb,3\xc1\xba\x9aBg\xc5\xc9\xfc\xd77*\xdbu\x01\x11\xfe\xe0\xc8IFc\xedx\x18\xcd3\xf69\xd1\xcfV\x96\xa6\xbe4{\xb2\xb7/#\xb1L\xa1\xe8\xe0er\xe5v\xfc\xef\xcc4\xe7utn\xa7b\xc3\xa4%\x18\xb5\xeb\xb1/\xb4G\xcfhY`8b\x07\x9c\xf8\xe9\xba,\x01\xef\x90\x90P\x99\xb0\x89\xd3\xcf\xb6\xe0ng\xea\xde\xb5-\xbb\x18\xa9\x15W\xc3o\x15\xc7h~\xcc\xe1\x7fuH\x8c\x8bVDJ=\xe1\xdaw\xed\xeb\x99\x8e\xe8BU\xa6F\xc7tT3\xc1(Y\x81\xcf\x1e9\x89\xc3x\xfeB!\x8a\xa3\x87\xa1\xc6(/\xefL\x90\xab%r`"\xd8\xe2\xb6\xba\xce\x1d\x05\x14j\xf5\x81\xae2 I\t\x8a\x92.\xa5/+l\x19\xa2\xa3\xdded{G\nf\xd1\xf3\xd6+y\x0f\xe3\x91\x9d\xb4u&]\xa7\xd8\x97\xbb\\v?\xd5\x05\xad\xae\xa2B\x82\xef\xbap>g\xb7d\xa3\xc9\xc5\xa8\x1d\r\xb0\xf7\x89\x8cv\x98L\x94\x90s\x86\xed\x03t\xd2*\xbdj\x91N@\t\xd98{X\xb1\xaaj\xe7\x0b\xbbt\xc0\xb5\xff\xb5A}J\x84\x98\x08S\xa3\x84\xe8\x0cn\xda`$\xe69\x8b\x10\xcc\xd8\xa6\xfc\xcf6\xc5k\x13\x1e\'D\x8bM\xa7e\x9c\xe7W\x9d\xdb\x1dj\xdaN\xbb\x11\x11\xb3&-\xa0\xdfw\xdd\xf0\x161\xa2,\xa56\x13\xdd\xefy[j@gf\xa6\xe6\x9bA\xd2DD\xadl\x0f\xed\xea-\x17DX\x91\\k\x99\x8f\x8dSg\xd2\xeeO\xca\xe8"9\xaa\xc1\xdek\xa7\xe0\xda\xc2\xae\xcc\xe2NS\xb5\x9d\xe2\x953\x03\r\xb1\xd0\xcd-\x9b\xda\x9b\x95^\xcf\xea$\x9dC\xbc\xe4\xb9\xd8\x19f0km\xdf\xe8\xeb\xb0\xba\x99%\xe1\xf7\x7f\xbb-D\xb5hFHyP\xe9\xf5\xd5\x9e3\xd4iewH\xbdG\x02\xb6N\xe2\xb2Z\xb1j\x85\xd0G\xe8;\xabB\xf08\n\x11*\x91\xdc"e\x94\xac.\xd3x\xb8l\x10\xa29\xa2qP:\x9b\xe4m\x1b\xdcF\x88)A\x8aD&H\xb2\xcd\xe2{\xcf\xfd\xd9}\xd4c\xd8\x1aY\xf9\xc6\xb4x\x07\xa5\xb7\x133e\x83\xd3\xe1B[9\xbcW\xd5\xef\x8c\xc2tA\xf8\xe4\xf0\x15B\xa8H\xa90$\xce\xca2\xc5ED\xf6\xb1T\xb3\x85\x86\x0en\xe2d~Vv\x86\x99\x00\x9f\xba\xf0\x1a=\xc1BX\xb2\x17\xd0\x89.K\x84\x02\x08\xb9\x96\xb2\'J\xe9\x1c\xbd\xb6\xc2\xcc\xb9\xa9\xaa\xe94\xc9\xf0i\x1f\xedM\xe6WIw\xa7\x85\xb5n\xf2:\x96\xf9\xa5\xdd\xb6\x08\xc1\xe5\x0c\x97\xce\x89j[x\xaa\xfb\xb0\xd0\xf6Z^\xd0\n\x0e\x1ch\x17\x19X#;+\xbd\x01\xba@\xba\xc7${\x9dv\xb0\xbb\xc9\xf7^x\x8d~\xb2\xc2\xa6\x9eH7\x1d\x1c\xb1-\xa0\xdaoVb>TPJq\x88x\xbcwx\xd7*\xbe%\xe7Z\x8f\x90U\xab9\th\xb6g\xde;\x15\x1f\xc2\x9f\xb2~\x15\xde\xb88\xe7\xee\xf2\xca\x8f\xc2w\xbd\xdbE\x88\xda\xae\xdc6\xa7\xb5\xa7\xf2[-\xf5\xe0\x87\xaa\xd7\xf9\xad__\xa4i\x16\x00A:\x862\xe1%N\xea$\xf7\x88l:,\xef,<m\xb3\xf6]\xbfy\xd5\x1e\x87\\aELv#\x04U\x1a\xb5\xea\xe2\xbe\x18\xfc8\xe3\xa3\xa9|\t"\xf8\x9e\x87\xb2g~\xcf\x0b\xe0\xf3D~\xa4]v\n\xae\xad/\x01_P<\xf9\xa5\x87\xe7*^93P\x14\r\x11F[\x067\xa3\x19G\x8b@Hh\xd3\x98\xd2C\xe8,\xbd\xfdX\xf6[EV\xc1\x7f\xfc\xf5>!\xf4-\xa2\xc1\xe8\x0c!!\xe4\x89\x10[\x8d\xca\xaeV;\xcd@\xee\x91,\xed%Qm\x19\xbe\xe8\xb4E\xaa\xd5Sb\xd1N\x89A\x0f$\xc3x\xc3D\xd3`\xe9r\x9c>\x95aA\xc6-gk\x07f\x10d\xa7\xc5\'u4\xb5\x85@\x17.O\xe6Yw\xc8\xee\x96\xb4\xaf\xfbv@!\xc4X\x12\x93\r\xd7ig\xd8bu\x07\xba\xbb^k\x9e\xa2o,\xb9\xfa\xe0\x85\xf3\x1dHL\x9ag\xff\x15\xd3\xef\xe6N.\x84\xa9\xa3\x1dha\x91M\xcaqi\x17\xbc8\xd0`NV\xe4s\xb3\xb7\xbfMz_\xff\xca\x19\x1d\xd9\n\x07\x86[\x10jS\xfeTm$E\xbb\xda\xcf\x86\x1f;\x16\x16\xc8\xdep\xe3-\xe2\xfa^\xff\nu\xb3\x90\x9d\xaa\xe2}\x9d\xa1%\xaf\xf4\x90\x80\xf7qf\xc6\xa9\x95\xed1\xbb{\x9b\xb3L5J\x10\xa1r\x9e\xd29*g\xe5~%\xd0\x13\xa1t\x8e\x02\xa1\xc0\xe5D\xd0x\xa7)"\xcax\x9av1\xae8\xcb\x87\xc6\x01\xc6\ri8\\\x98\xde\xa2qn\xb5\x92\x86\xe6q\x1d\x8d\xd0k\xd7\xe0\xf2\x95\x9c\xcdN\xb7\xd2\x16\x98\xe1\x04\xe7\xe7\x9c"\x13Js\xe1FL\xe98\xe1\xd4\x9d\xfd<Wj\xd9\xe3\x84\x9f\x89\xf8<\xf7\xca6\'\xd9\xb5\x10\x11\xe5\xfd\x8f&\xd6\xbf\xeb\x14\xf7>\xb4\x1djnT\xf4\xaa\xb5\xcb\xb2V\xc5\xe7\x90\xb8\xc8\x89`O\x1cE\x1b\xa7w\xa1\xa2\xda\xf4_\x8a\xd9\x81F\x90b\x92y\x91,H\x19\x8fI\xc3-\xca\xb5/\x9d\x99\xbe\xe6N\xa8\xe1\xcc@S~?\x84\x9c9\xa81q`QM\xb7gAiu\x957\x9c8Y\xcf\xfc\xd2\xbf(&w\xd2\x85\x909\xaa\xe9f\xab\xe6+\xfd\xa1G\x95?:r\n\x12|\xf9\xf8\xdd\x1c\xbf\xef\xc6\x9a0+\x0f\xbdy~b(m\xa4\xc6T\xd6*\xe0\xdb\xd8\x1d\x05\xf1\x99\xb1m\x97\x97J.\xe6\xcc\x81GSC\x13H\xa9ASz|\xf6z\xbb\xd5\xe7\xd9S\x13\xc0O\xddtV\xbe:\x07\xbd\xd2zWd\x17#3\xb8i\xc3L\x9dp\x01\xb4K\xf0R,\xd0m\xf57\n\xd8\xba&qY\xf9;\xf8\x18x\xe8Q\xe5\xf3G\xee\xec\xd2II\xf0\xd4\xf1\xbb\xe9\x1d\xb9qk\x9f\x16OK\x8aM\x92\xc0\xd2\x99\x99{\xc0\x89\x9b\xc0J^+\x08\xc9\xb8\xf7V\xe1d*8\n1\x04t\x1cHM]\xcd\xee\x04;W\xf1\xd53O\x9eN\x9a\xbe\xac(l\x8dass\xea\x1b\xadU`\x0e%W\xcf\xee\x90\xa97\xb7G\xd3\xda]9u\x97\xd7\x99\xf8;M\x8d\x80.`\xe5C\xdf\xa6<\xf2\t\xe5\xf3GOm\',\xf3H\x7f\xfd\x8e{\x91\x15:\xba\xf7F%`Ks\xe2tK\'!\x8c=\xb7\x06\xd4bf\xcbY\xb5U\x11R\x9aCM)\xe7%:w9\xd8\xdcJ2\xe5\xcc\xa0\t\xf1\tF#\x14Az\xbd\x89\xc2pH\x99\x17\t\x84\xc6. \xc2\xdc\x9dh2U\xa1\x9aK\xb8][\x9b\xae9\x080v\xa4-R"\xe3\xbc\xf7\x81\xc2\xd9\xd6VN\x14U\xb8\xf7\x11\xe5Kw\xdcm#\'h\xa7t\x89\xd8:\xc9\xc6:\xe0\xe2I\xc3\x1cYy\xd6\x9a\xb0[P6{\xcfWAV\xce\xf1\xf2\xb1S \xed\x06\x13\xd2\xf5\xaboW0J\x8fv\xd9=^\xac\xa2:\xe5TW\x14\xb41\x8bO\rb\xab\n\xd7\x06/|\xfd\x1ee\x1b\xc4\xef\xbe"\xa4:\xfb\xd5\xd3\xaa\xfaem\xc6\xe8\xb5u\x8bp\xc0f\xa3\xfa}\xe8Wh\x13\xd0\xc6.\xd0\xc6\xef\xdbn\xa6\x8d\xb1\xa5]]gSfA\x94\x90\x13_\xe7\x02EQ\xe3]\x83w\r\x85\xafst\x13q\x12X\xba=\xb0\xfe\x91\xbb\xf8\xd2\xe2)\x18)2\xc6\xfcX~P\x9b\xd2%n\xef\xf4\x8b\'\xef\xe3\xe2\xc9\xfbn\xd8\xfaU\x841\xa6\xbb-l\xf7\x0f[|,6\tO\xcaIS\t\xfd\x01\x14\xd5$\x87Qo\xd3}I3Q\x96\xe8?\xbfv\xcf,\xcc\xec\xa9\xf8\xee\xe04\xe5X[\xe5/\x0c&NU\xa7\xcaN\xe7p4mX)\xd0\xcd\x06>x\xe1E>x\xf1E\x04\xc5\xbb\x88w5EQg\xa5781\xfc\x1c\x1cU\xce\xdfv\xafQ\xaa\xed\x9a\xf8\xa0VB\xd2Zz\xc8\x1d\xb0\xcb\\\xf8\x8d(_\xafZ]|a\n\xb0\x05g\xf92I\xc8\x96\x9e\xc3\xc9*[\xbb\xc3,L\x9d\xc5\xeb1Z\xe3\x8cA\xf8\xean\xd7\xdaU\xf1\x00\xe5\xda\x97\xcf\xa0\xfa\xa7\x8a\xc2\xb5\r\x9bK\x1cn\x19M\xec\x04q\xde&\tbN\x1c\x9c\xa3\xad*o\x17\rwa\xe5TI\xc8\xa9\x93\x15w\xdf\xd5GD\xf3\x1e\x04\x1b\xf4\xaakT\xd5&\x85\x1f\xb1rG\xe0\xf2\xfb\xef\xe5\xb5\xe3Y\xe9\x11\xa4Qd\x042\x04\x86j\x8f\x91\xbd\xdfA\xcf.r\xf1\xe4}\\:\xb3\xbf\x0ep\xceQ\xe5\xb6\xf6\x81\x81s\xf4\x8a\x82\x9es\xb6\xcf\x81\x93\xccB\xe6ua\xbd\x81\x15w\xd9\xba\xfa\x0c3@\xd2/\x97\xcf<yz\x9e\xb5\xc3u\xf6\xab1\xac\x0f_q\x18\x9e\x0b@l\'s\xd5\x14\xed\x1c\xea\xc4\xeak\x04\xdb\x18\x08\xcd\xcf\x13\x1f+\xd8H\xd4J\xf8\x9f\xbfce\x1d1E\xfa\xbdu\xcab\x8cHb\xf168\x7f\xfc\x1e^>\xd25`\xf2l7c\xe7\x92\x99\xcfg_\xef"\xd6\x01\xdbw\xef\x9b\x95\x12\xdb\xed\xa3t6\x1bU\xe5$\xca\xb7\x17.\n\x83\x1aq6!T7\xf6\x7f\xcc\x0e-\x02NII\xddnJ\x87}\xac\xec\xae\x9e~\xe2\x81\x14\xe2\xe3:\x1a\x93\x86C\xf4\xda&z\xe5\n:\x1a\xa1MM^#\x83\xb8\x1c:2\xd9b\xbc\xdd,eZ\'w\xbf\xfa|G\xdb\xf6J+p\xad\x0e\x07\x8a\x83\x89\xf3G\xef\xd9>\xe30-\xd3\xa1Q\xcb\xba\xea.\xc7^G.\x9e\xbc\x8f+\xef\xbb\x7f\xee\x088\xfa\xeas\x80\x91c\xa5\xb8\xbc$K\x89\xb8\xbc\x8a%\x03\xa7\x06+\x85\x89\r\xb8\xd2`&\x98\x87OQ\x1f/\x9e~|\xcf\xad|\xaf\xabx\xe5\xcc\xa0z\xfa\xf1\x07H\xe9\x0b\x96,d\x1eb4\x9e$\x1a\x99\xb5\x9c\x17V\xea\xcc?1\xd8\xc2\x82\xc27x_\x03JJ\xf0\xd6\x89\xb7\x99\x01\xdd\xa4\xccS\xbe\xd2\xc2c\x8bt\x06\xd8ef(\xbb|\x84`q\xbd66\xe5ga\xdc\xe3\xc5S_~`/k\x87}n\x8d\xa5\x9c\x194\xe3\xf1W\x9c/l\x91Xi\xd4\xa8$[\xeb\xe4"$\xb1\xed\x0e]Jh\xdeD"u\xdf\x07T9\xfcR;\xc4\xd7Q\x85\xf2\x10\xbcy\xfb\xbd\\8\xc1\r[\xed\xdb\x15U\xe5\xea\xa9\xd3\x00\\{\xbf\xb0r\xee\xe9\x8e&\x96\x95\xe7\xd98y?\xb5\xa6<\xa1\xad\x99b\xf79\xa2\xc9d\x93wV9\xb6\xb9A\x885\xc4\x88S)\xae\xa7t\xb8\x81=\xc9\xaa\xa7\x9fx\x00\x18\x853\x1f\xeaK\x8a\x16\xeb&\xab;\xe9\x082U\x9b\x95I\xc9\xb2\xd6\x94\xb6\xc3p\xc6\xd5Kg\xee\x05\xe0\xcd\xdb\xf7{\xf5[/\x8a\xcd,\xb5\x94\xf3\xa5;\xef\xe7\xca\x19\xe5`\xc6\xff\xad\xf7\t\x1e\xb1l\xd59\xdb@\xb4\xf0\xb6\n\xd2a\xbcLY\x81\xf7\xc4:\x91\x9a\x80(k\xc5\x0b_\xbbo6f\x9f\'\xd7\x85\x9aIC\xad\x175\xc5\xc7\xe9\x86\\V\xae\xd2-T\xd0\xcc[\xcc\xe3\xe4\xdfNV\xf9\x8e\xc84\x9d1]\x9a\xb8B&\xfaZ\xb6\xafu\xa6\x92C\xc7\x96\xafI\xb6^ 4\x99\xb9V\xf6c\xed\xc0\x8d\xef;)\xac\r\xc3\xc3\x1f\xf9*\xf0Q\r\xd1v\xech\x1a\x94I\xb8\xd8F6Q\x95\x10\xe3\xbb\x8d"7,m\xc8\xebE(\xbdQ\xd4\xb4\xcb\xe6\x81\xc2\x97\x94\x85\x98\xb5\x97\x95)^\x12\x84@\x8c\x890\x1e\xaf\r\x9e_\xbb\x07\xd8\x9f\xe2ofoa\xe5\xcc\xa0\x1e\x8e\x9e\x10\x91\xaf\xaa\xea\xc3\xed\xa6@"\xed|E\xcb\xc5\xdbl\r.o\xac\xcc\x14$}\x93\x88\xeb\x96\xd7\xdb\xa2a\xdb\xf9\xbb\xb5t\x01\xb1=\xcbl\x86)\xcf\xa3\x8ej\xb3\xfc\xd00\xb6m\xd3\xd7\x06/\xcc\xcfN\xf7\x92\x9b\xdaw\xb2z&~@X\x1b\x0e\xdf\xf3\xe0\xe4\x97\x0cT\'Yj\xcb\xf4\x8aX{s\x01j\xd4\x1dl\xce7L\x04&\xfb\x1a8\x97\x97\xe4O//2n\xd4\xd4-\xc4\x94\x10m\x0c\x91B\xb0\xfd\xd6BbL\xda\x973\x9d\x95}c\xfc<QX\x03\x9e\x9a\xcesfcw\xd9\xf6|\x9dI\xf0wQ&T\xc6\xcc\xd4^[\x17\x94o \xe5\x19\xb6$\x992KV\xdb\xaf\xaakJ:\xbb|\xee\xec\xa9\x9b\xba\xfe\xdb\xdd?~\xea\'\x85\x1e\xd8\xfe\xbe\xc9\xb6\xa8F\x8di\x8c9\x17\xf8FX\xff4\x9e{\xd7\xce~I7L\x9d\x08\x9a\x94\x98\xa2}\xde\x06\tJ\xde\x03?\xb4\x84\xdf\xd9\xa5\x97\xcb\xf7\xdeT#nvo\xe1m\xe7h\x87\x99rv\xda\xd4\xe7%\x94-\x0c\xed\xb7\n\xe1\x1d\x91\x19K\x9f\xb6x#\xf2\x8c\xb2n\xf9\xa5\xf6\'6b\xca\xb9IR4\xe9\xb3\xcb/?sS\x96\xde\xca\xdbV<\xc0\xd2K\xfe\xc1\x84\x924\x9dM\xedd\xc1<s\xce7\xe2D\xbaY\xfcwS\xdai<[F\xd3\x1a\x00\x93\xac{\x8a\xbe\x9e~\xa4`\xfb\xac\xa5\x14\xcf.\x9f\x7ff\xb4|\xfe\x99\x937\x83\xeb\xd3r\xcb6\xee_9W\xbcWX\x1b^\xbe\xf3\xfe\xb3\x88\xe0\xd0\xd3\xec\xa2\xdcv\x0eSv\xe9\x9fwJ\xdaNo\xa3\x96m6\x9f\x8db\xb2u\xa3\xd5\xd9\x98\xf2\xd3\xd9\x04\xa4\x94\xf6$\xben\xa8-\xb7\xf27B\xba\x93\xb26\xbct\xe7\xfd}\xe3\x94\xa4\xc3\xd5Yi\x7fT\xab}\xdd}\x7f\xea\xd8nG\xbf\x1d\xd7\x98\x9c\x1b\xda\xdd\xf5\xe6wc{l[)\xd0E2\xed\xa4\xfd\xd4\xdcp\x08\xa1\xab\xefw\xf9\xe0\xe5sgG\xb7J\xe1v3\xb7\x00\xe3w?9\xcf*\x9c\xbd\xdea\xd7\x05\x9c\xfd\xae\xd6{\xbb\xd7\x99+z\x96}\xdc\xc3\xcd\xc8;b\xf1\xdd\xc9\xf3\xefA\x89H\xcaI\xca\xe9\x1d\x07u\xcex\xc2\xdfO;\xbc6\xf2\x9f\xdd{~\x02\x19t\x9f\xb7y\xc2\xac\x92].\xb5fj\xf49\xe7\xf0ys\xb7\xe9Gc\xfbf\x9eEq\x07n\x01\x96\xcf\x95\xb7\xf3S\x157*\xf9\'C\xfb\xd2*aJi\xb7J\xda{\x91\xa9\xbf\xed\x9co+\x0e\xc09\ng\xbbf+\xa0)u\xb8\xbe\xf4\xe2S\x00\xb7\x16Zv4\xf4]\xfa\xad\xbf\xeezp\x16\xd5\\\x95\xb0\xbb\xf3\xbdY\xd9\x16\x18vz\xdf\xed\x1a\xb6\xe5D7g\xac\xfaT\xfe\xe0\xee[\xda\xa8]\xe4]\xb3\xf8m\x17m\x7fV\xf4\xd4{\xcf!\xec\x84\x9fwB\xf2m\xb6\xc9\x928!\x19\xa3\xfa\xd4\xd2\x8bO\xddm\x87\xbc\x83V\xbe\xad-\xef"\xd4\xcc\x13amx\xed\xd4\xe9s\xd9<O\xcf|x\xe32\xed\x04\xa6\xbf?\xe5\x1f2\xc6?\x05\xb0\xf4\xd2\xd3w\xdb\xd7\xde%\x85w\xed\xf9\x06+\xbe\x95v\x04\\\xb9\xf3\xfes\xdd{\xe6\x08O\xdb\xe7\xdb{a\x1e\xd5\xd6&>\xad\xb8\t\xae\x9fM\x138q\x07\xcf?{\xd2\x8e\x7f\x97\x95=-\xdf,\x8a\x9f\'\xb3?\x8e>\xdd)Y\xc9\xd3#\xe4\xd9\xf6\xfd\xc3Y\xb1\xd3\xf2\rU\xf2<\xf9fV\xfc^2\xe7\x17\xeb\xbf\xf9\x94\xbb\x97lS\xfc\x9f\xcb\xbb*\xef\\\xe6\xfa\xe7\xb2\xa7\xfc?\xb6cd\x17i\x1d\x84*\x00\x00\x00\x00IEND\xaeB`\x82'))
a.wm_iconphoto(False,ImageTk.PhotoImage(c78))
a.title('clauth app')
c=Menu(a)
b=Menu(c,tearoff=False)
def a91():
    global u
    b03=[0,1,2,3,4,5,6,7,8,9,".","=","sin","cos","C","-","+","÷","×","<=","√","yX","n!","log","tan","cot"]
    b04=[10,410,10,330,75,330,140,330,10,250,75,250,140,250,10,170,75,170,140,170,140,410,400,330,270,250,335,250,270,170,205,410,205,330,205,170,205,250,335,170,270,410,270,330,400,170,400,250,335,330,335,410]
    b05=[125,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60]
    b06=[75,75,75,75,75,75,75,75,75,75,75,155,75,75,75,75,75,75,75,75,75,75,75,75,75,75]
    b07=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,"yellow",None,None,None,None,None,None,None,None,None,None,None]
    b08=[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,25,20,20,20,20,20,20,20,20,20,20]
    b09=["<Key-^>","<Key-minus>","<Key-+>","<Key-*>","<Key-/>","<Key-.>","<Key-0>","<Key-1>","<Key-2>","<Key-3>","<Key-4>","<Key-5>","<Key-6>","<Key-7>","<Key-8>","<Key-9>","<Key-Delete>","<Key-BackSpace>","<Key-Return>"]
    global b00
    b00="  "
    b02=Tk()
    b02.resizable(0,0)
    b01=Label(b02,font=(None,30))
    b02.title('calculator')
    b01.place(x=15,y=60)
    b02.geometry("475x500+{}+{}".format(str(int(500*u)),str(int(150*u))))
    def b1():
        b2("0")
    def b3():
        b2("1")
    def b4():
        b2("2")
    def b5():
        b2("3")
    def b6():
        b2("4")
    def b7():
        b2("5")
    def b8():
        b2("6")
    def b9():
        b2("7")
    def b10():
        b2("8")
    def b11():
        b2("9")
    def b12():
        b2(".")
    def b13():
        global b00
        try:
            if b00[-2]=="(":
                b00=b00[:-6]
            elif b00[-1]in["÷","×","+","-","^","."]:
                b00=b00[:-1]
            b00=b00[2:]
            b14=""
            b15=""
            b16=""
            b17=0
            for b18 in range(len(b00)):
                if b17==0:
                    if b00[b18]in["÷","×","+","-","^"]:
                        if b15!="":
                            if b16=="÷":
                                if float(b15)==0:
                                    b00="0"
                                else:
                                    b14=str(float(b14)/float(b15))
                                b15=""
                            elif b16=="×":
                                b14=str(float(b14)*float(b15))
                                b15=""
                            elif b16=="+":
                                b14=str(float(b14)+float(b15))
                                b15=""
                            elif b16=="-":
                                b14=str(float(b14)-float(b15))
                                b15=""
                            else:
                                b14=str(float(b14)**float(b15))
                                b15=""
                        b16=b00[b18]
                    elif b00[b18]in["s","c","t","l","n","√"]:
                        if b00[b18]=="n":
                            b18+=3
                            b17=3
                        elif b00[b18]=="√":
                            b18+=2
                            b17=2
                        else:
                            b18+=4
                            b17=4
                        b36=""
                        while True:
                            b36+=b00[b18]
                            b18+=1
                            if b00[b18]==")":
                                break
                        b17+=len(b36)
                        if b00[b18-len(b36)-2]=="n":
                            if b00[b18-len(b36)-3]=="i":
                                b36=sin(radians(float(b36)))
                            else:
                                b36=tan(radians(float(b36)))
                        elif b00[b18-len(b36)-2]=="t":
                            b36=cos(radians(float(b36)))/sin(radians(float(b36)))
                        elif b00[b18-len(b36)-2]=="s":
                            b36=cos(radians(float(b36)))
                        elif b00[b18-len(b36)-2]=="!":
                            if float(b36)==int(float(b36)):
                                b36=factorial(int(float(b36)))
                            else:
                                0/0
                        elif b00[b18-len(b36)-2]=="g":
                            b36=log(int(float(b36)))
                        else:
                            b36=sqrt(float(b36))
                        if b14=="":
                            b14=str(b36)
                        else:
                            b15=str(b36)
                    else:
                        if b16=="":
                            b14+=b00[b18]
                        else:
                            b15+=b00[b18]
                else:
                    b17-=1
            if b15=="":
                b00=b14
            elif b16=="÷":
                if float(b15)==0:
                    b00="0"
                else:
                    b00=str(float(b14)/float(b15))
            elif b16=="×":
                b00=str(float(b14)*float(b15))
            elif b16=="-":
                b00=str(float(b14)-float(b15))
            elif b16=="+":
                b00=str(float(b14)+float(b15))
            else:
                b00=str(float(b14)**float(b15))
            if float(b00)==int(float(b00)):
                b00=str(int(float(b00)))
            b00="  "+b00
            if len(b00)>20:
                b01.configure(text=b00[len(b00)-20:])
            else:
                b01.configure(text=b00)
        except:
            b00="  "
            b01.configure(text="  Error")
    def b19():
        b2("sin()")
    def b20():
        b2("cos()")
    def b21():
        global b00
        b00="  "
        b01.configure(text="  ")
    def b22():
        b2("-")
    def b23():
        b2("+")
    def b24():
        b2("÷")
    def b25():
        b2("×")
    def b26():
        global b00
        if len(b00)!=2:
            if b00[-1]==")"and b00[-2]!="(":
                b00=b00[:-2]+")"
            else:
                b00=b00[:-1]
            if len(b00)>20:
                b01.configure(text=b00[len(b00)-20:])
            else:
                b01.configure(text=b00)
    def b27():
        b2("√")
    def b28():
        b2("yX")
    def b29():
        b2("n!()")
    def b30():
        b2("log()")
    def b31():
        b2("tan()")
    def b32():
        b2("cot()")
    u=[b1,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32]
    def c4(k):
        if k.char=="*":
            k.char="×"
        elif k.char=="/":
            k.char="÷"
        b2(k.char)
    def b2(k):
        global b00
        if k in["÷","×","+","-","^"]:
            if b00[-1]==")":
                if b00[-2]=="(":
                    b00=b00[:-6]+k
                else:
                    b00+=k
            elif b00[-1]in["÷","×","+","-","^","."]:
                b00=b00[:-1]+k
            else:
                b00+=k
        elif k in["sin()","cos()","tan()","cot()","log()","n!()","√"]:
            if b00[-2]=="(":
                b00=b00[:-5]
            if b00[-1]in["÷","×","+","-","^"]or len(b00)==2:
                b00+=k
            else:
                b00+="×"+k
        elif k==".":
            if b00[-1]in["0","1","2","3","4","5","6","7","8","9"]:
                b00+="."
            elif b00[-1]not in[".",")"]or b00[-1]==")"and b00[-2]!=".":
                b00+="0."
        elif b00[-1]==")":
            b00=b00[:-1]+k+")"
        else:
            b00+=k
        if len(b00)>20:
            b01.configure(text=b00[-20:])
        else:
            b01.configure(text=b00)
    for b18 in range(26):
        Button(b02,text=b03[b18],bg=b07[b18],font=(None,b08[b18]),command=u[b18]).place(x=b04[b18*2],y=b04[b18*2+1],width=b05[b18],height=b06[b18])
        if b18<19:
            b02.bind(b09[b18],c4)
    def b33(a):
        b26()
    def b34(a):
        b21()
    def b35(a):
        b13()
    b02.bind("<Key-Delete>",b34)
    b02.bind("<Key-BackSpace>",b33)
    b02.bind("<Key-Return>",b35)
def a8():
    if a2.get('1.0','end')!='\n':
        try:
            s=a2.get('1.0','end')
        except:
            a6.place(x=250,y=13)
            return False
    else:
        s=open(askopenfilename(initialdir=b65,title='choose file'),'rb')
    with open(s,'rb')as r:
        a2.insert('end',int.from_bytes(r.read()))
    s.close()
def d():
    b36()
    a2.delete('1.0','end')
    a2.place(x=90*u,y=50*u,height=200*u,width=400*u)
    a9.place(x=260*u,y=270*u,height=26*u)
def e():
    try:
        with open((asksaveasfile(initialdir=b65,title='choose location')).name,'wb')as s:
            s.write(int(c73.get('1.0')).to_bytes(ceil(len(format(int(c73.get('1.0')),'b'))/8),'little'))
        notification.notify('Completed','successful')
    except:
        notification.notify('Error','didn\'t run successfuly')
def c74():
    b36()
    c72.place(x=270*u,y=270*u)
    c73.place(x=40*u,y=30*u,width=500*u,height=230*u)
def f():
    b36()
    a2.delete('1.0','end')
    a2.pack()
    try:
        with open(askopenfilename(initialdir=b65,title='choose file'),'rb')as s:
            try:
                t=0
                while True:
                    a2.insert('end',format(s.read(1)[0],'08b'))
                    if t%100==0:
                        a.update()
                        t=0
                    t+=1
            except:
                pass
    except:
        pass
def g():
    if urlopen('https://clauth.net/version').read().decode()!=open('clauth.py','r').raedline[1:]:
        with open('clauth','wb')as a:
            a.write(urlopen('https://clauth.net/download').read())
        open('clauth.py','r').close()
def j():
    b36()
    a27.place(x=40*u,y=40*u,width=270*u,height=250*u)
    a11.place(x=350*u,y=50*u,width=50*u,height=25*u)
    a14.place(x=350*u,y=100*u,width=50*u,height=25*u)
    a16.place(x=350*u,y=150*u,width=50*u,height=25*u)
    a16.config(text='next',state=DISABLED)
    a18.place(x=350*u,y=200*u,width=50*u,height=25*u)
    a20.place(x=350*u,y=250*u,width=50*u,height=25*u)
    a22.place(x=420*u,y=50*u,width=50*u,height=25*u)
    a24.place(x=420*u,y=100*u,width=50*u,height=25*u)
    a26.place(x=420*u,y=150*u,width=50*u,height=25*u)
    a00.place(x=420*u,y=200*u,width=50*u,height=25*u)
    b75.place(x=420*u,y=250*u,width=50*u,height=25*u)
    c75.place(x=490*u,y=50*u,width=50*u,height=25*u)
def b76():
    b77,b78=[askdirectory()],0
    while len(b77)!=b78:
        for i in scandir(b77[b78]):
            if isfile(i.path):
                a28.append(i.path)
            else:
                b77.append(i.path)
        b78+=1
    a29()
def a1():
    b36()
    a2.place(x=25*u,y=45*u,height=280*u,width=550*u)
    a3.place(x=20*u,y=10*u,height=26*u)
    a4.place(x=520*u,y=10*u,height=26*u)
def a5():
    a7=a2.get('1.0','end')
    try:
        s=[' 'in a7,','in a7,'\n'in a7,'/'in a7,'\\'in a7]
        if s==[0,0,0,0,0]:
            a7=int(a7,2).to_bytes(len(a7)//8)
        elif s==[1,0,0,0,0]:
            a7=a7.split(' ')
        elif s==[0,1,0,0,0]:
            a7=a7.split(',')
        elif s==[0,0,1,0,0]:
            a7=a7.splitlines()
        elif s==[0,0,0,1,0]:
            a7=a7.split('/')
        elif s==[0,0,0,0,1]:
            a7=a7.split('\\')
        else:
            0/0
        if type(a7)==list:
            s=len(a7[0])
            if s is 2:
                a7=bytes([int(i,16)for i in a7])
            if s is 3:
                a7=bytes(a7)
            if s is 8:
                a7=int(''.join(a7),2).to_bytes(len(a)//8)
    except ZeroDivisionError:
        pass
    except:
        Thread(target=b37).start()
def b37():
    a6.place(x=420*u,y=11*u)
    sleep(5)
    a6.pack_forget()
def a10():
    j()
    a16.config(text='secure',state=NORMAL,command=a35)
def a29():
    a27.delete(0,'end')
    for i in a28:
        a27.insert('end',i.rsplit('/',1)[1])
    if a28:
        a16.config(state=NORMAL)
    else:
        a16.config(state=DISABLED)
def a35():
    if not a28:
        showerror('Error','No file')
        return False
    b36()
    a42.place(x=70*u,y=255*u)
    a43.place(x=70*u,y=210*u)
    a43.select()
    a44.place(x=70*u,y=165*u)
    a45.place(x=70*u,y=120*u)
    a46.place(x=70*u,y=75*u)
    a47.place(x=70*u,y=30*u)
    a54.place(x=500*u,y=200*u,width=70*u)
    a57.place(x=190*u,y=280*u)
def a12():
    a28.extend(askopenfilenames(initialdir=b65,title='choose file'))
    a29()
def a13():
    try:
        for i in a28:
            if i.endswith(a27.selection_get()):
                a28.remove(i)
                0/0
    except ZeroDivisionError:
        pass
    except:
        a28.clear()
    a29()
def a17():
    pass
def a19():
    try:
        for i in a28:
            if i.endswith(a27.selection_get()):
                b=Tk()
                b.title('txt viewer')
                b.geometry('250x200+600+300')
                b=Text(b)
                b.pack()
                with open(i,'rb')as s:
                    try:
                        while True:
                            b.insert('end',chr(s.read(1)[0]))
                            a.update()
                    except:
                        pass
                break
    except:
        pass
def a21():
    try:
        for i in a28:
            if i.endswith(a27.selection_get()):
                if '/'in i.rsplit('.',1)[-1]:
                    copy(i,i+' (copy)')
                    a28.insert(a28.index(i)+1,i+' (copy)')
                else:
                    copy(i,' (copy).'.join(i.rsplit('.',1)))
                    a28.insert(a28.index(i)+1,' (copy).'.join(i.rsplit('.',1)))
                break
    except:
        a04,t=a28.copy(),1
        for i in a04:
            if '/'in i.rsplit('.',1)[-1]:
                copy(i,i+' (copy)')
                a28.insert(a28.index(i)+1,i+' (copy)')
            else:
                copy(i,' (copy).'.join(i.rsplit('.',1)))
                a28.insert(a28.index(i)+1,' (copy).'.join(i.rsplit('.',1)))
            t+=1
    a29()
def a23():
    if a01.get():
        a02(None)
    else:
        a01.place(x=390*u,y=310*u)
def a25():
    try:
        for j,i in enumerate(a28):
            if i.endswith(a27.selection_get()):
                remove(i)
                a27.delete(j)
                a28.remove(i)
                break
    except:
        for i in a28:
            remove(i)
        a27.delete(0,'end')
        a28.clear()
def a0():
    try:
        for j,i in enumerate(a28):
            if i.endswith(a27.selection_get()):
                send2trash(i)
                a27.delete(j)
                a28.remove(i)
                break
    except:
        for i in a28:
            send2trash(i)
        a27.delete(0,'end')
        a28.clear()
def a02(s):
    try:
        for i in a28:
            if i.endswith(a27.selection_get()):
                if not a01.get():
                    rename(i,i.rsplit('/',1)[0]+'/ ')
                    a28.append(i.rsplit('/',1)[0]+'/ ')
                else:
                    rename(i,i.rsplit('/',1)[0]+'/'+a01.get())
                    a28.append(i.rsplit('/',1)[0]+'/'+a01.get())
                a28.remove(i)
                a29()
                break
        a01.delete(0,'end')
        a01.forget()
    except FileExistsError:
        a03.place(x=400*u,y=280*u)
    except:
        pass
def a31(s):
    op('https://youtube.com/frostdream')
def a32(s):
    op('https://instagram.com/_frost_dream_')
def a33(s):
    op('https://discord.gg/hX5ZUsyK')
def a34(s):
    op('https://twitch.tv/frost___dream')
def b53(s):
    op('https://www.reddit.com/r/FrostDream/')
def d13(s):
    op('https://stackoverflow.com/users/19773037/frost-dream')
def a05():
    b36()
    a06.place(x=120*u,y=40*u)
    a07.place(x=165*u,y=130*u)
    a08.place(x=163*u,y=190*u)
    a09.place(x=170*u,y=250*u)
    a30.place(x=280*u,y=130*u)
    b54.place(x=282*u,y=190*u)
    d12.place(x=263*u,y=250*u)
def a36():
    a55.place_forget()
    a42.deselect();a46.deselect();a45.deselect();a44.deselect();a43.deselect()
def a37():
    a55.place_forget()
    a47.deselect();a42.deselect();a45.deselect();a44.deselect();a43.deselect()
def a38():
    a55.place_forget()
    a47.deselect();a46.deselect();a42.deselect();a44.deselect();a43.deselect()
def a39():
    a55.place_forget()
    a47.deselect();a46.deselect();a45.deselect();a42.deselect();a43.deselect()
def a40():
    a55.place_forget()
    a47.deselect();a46.deselect();a45.deselect();a44.deselect();a42.deselect()
def a41():
    a55.place_forget()
    a47.deselect();a46.deselect();a45.deselect();a44.deselect();a43.deselect()
def b51():
    for i in range(randint(0,11)):
        s=[a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72]
        s[randint(0,10)].set(fabs(s[randint(0,10)].get()-1))
    a85()
def a56():
    a58=b''
    for i in a28:
        a58+=i.rsplit('/')[1].encode()+b'?'+str(getsize(i)).encode()+b'?'
        with open(i,'rb')as s:
            try:
                while True:
                    a58+=s.read(1000)
            except:
                pass
    s=[a49.get(),a50.get(),a51.get(),a52.get(),a53.get(),1].index(1)
    if s is 5:
        a55.place(x=230,y=300)
        return 7
    elif s is 0:
        a59=format(int.from_bytes(a58),'b')
        a59=(8-len(a59))*'0'+a59
        for i in range(len(a59)//4):
            a59=a59[i*4+1:]+{'1':'0','0':'1'}[a59[i*4]]+a59[:i*4]
        a58=b'\x14'+int(+a59,2).to_bytes(len(a58))
    elif s is 1:
        a59=[21]
        for i in range(randint(1,256)):
            a59.append(randint(0,254))
        a59.append(255)
        a58=bytes(a59)+a58
    elif s is 2:
        a59=''
        s={'0000':'000','1111':'001','0001':'0100','0010':'0101','0100':'0110','1000':'0111','1110':'1000','1101':'1001','1011':'1010','0111':'1011','0011':'1100','0101':'11010','0110':'11011','1100':'1111','1010':'11101','1001':'11100'}
        for i in a58:
            i=format(i,'08b')
            a59+=s[i[:4]]+s[i[4:]]
        a59=(8-len(a59)%8)*'0'+a59
        a58=b'\x16'+int(a59,2).to_bytes(len(a58))
    elif s is 3:
        for i in a58:
            a59+=format(i,'08b')[4:]+format(i,'08b')[:4]
        a58=b'\x17'+int(a59,2).to_bytes(len(a58))
    else:
        b36()
        a61.place(x=40*u,y=40*u)
        a74.place(x=40*u,y=80*u)
        a75.place(x=40*u,y=120*u)
        a76.place(x=40*u,y=160*u)
        a77.place(x=40*u,y=200*u)
        a78.place(x=40*u,y=240*u)
        a79.place(x=150*u,y=160*u)
        a80.place(x=150*u,y=40*u)
        a81.place(x=150*u,y=80*u)
        a82.place(x=150*u,y=120*u)
        a83.place(x=240*u,y=300*u)
        a84.place(x=277*u,y=300*u)
        a86.place(x=40*u,y=295*u)
        return 0
    a92()
def a92(s):
    b36()
    a93.place(x=100*u,y=400*u,width=70*u,height=20*u)
    a94.place(x=180*u,y=400*u,width=40*u)
    a95.place(x=230*u,y=400*u,width=40*u)
def a96():
    a93.delete('1.0','end')
    a93.insert('end',asksaveasfile(initialdir=b65,title='save in'))
def a97():
    try:
        with open(a93.get(),'wb')as s:
            s.write(a58)
    except:
        showerror('Error','invalid file address')
def a85(s):
    if a62.get():
        a87=int.from_bytes(a58)
        a87=format(int(format(10**(int(log10(a87))+1)-a87,'b'),2),'b')
        a58=b'`'+int(a87).to_bytes(ceil(len(a87)/8))
    if a63.get():
        a58=b'a'+a58[::-1]
    if a64.get():
        a59,s='',{'0000':'000','1111':'001','0001':'0100','0010':'0101','0100':'0110','1000':'0111','1110':'1000','1101':'1001','1011':'1010','0111':'1011','0011':'1100','0101':'11010','0110':'11011','1100':'1111','1010':'11101','1001':'11100'}
        for i in a58:
            i=format(i,'08b')
            a59+=s[i[:4]]+s[i[4:]]
        a58=b'\x18'+int(a59,2).to_bytes(ceil(len(a59)/8))
    if a65.get():
        a87=int.from_bytes(a58[::-1])
        a59=randint(0,1208925819614629174706174)
        a58=b'\x17'+a59.to_bytes(10)+(a87-a59).to_bytes(len(a58))
    if a66.get():
        a58=b'\x16'+choice([b'a',b'b',b'c',b'd',b'A',b'B',b'C'])+a58
    if a67.get():
        a59=int.from_bytes(a58)-factorial(len(a58))
        if a59<0:
            a87='0'
        else:
            a87='1'
        a59='1'+a87+format(fabs(a59),'b')
        a58=str(hex(len(a58))).encode()+b'?'+int(a59,2).to_bytes(ceil(len(a59)/8))
    if a68.get():
        s=b''
        for i in range(100):
            s+=bytes([255-a58[i]])
        a58=b'\x1a'+s+a58[100:]
    if a69.get():
        a58=format(int.from_bytes(a58),'b')
        a58,a59,a87,s,t,r=(8-len(a58)%8)*'0'+a58,[],0,0,0,''
        for i in range(randint(1,8)):
            a59.append(randint(2,9))
        try:
            while True:
                if s==a87:
                    s+=a59[t]
                    if t+1==len(a59):
                        t=0
                    else:
                        t+=1
                    if a58[a87]=='1':
                        r+='1'
                    else:
                        r+='0'
                else:
                    if a58[a87]=='0':
                        r+='1'
                    else:
                        r+='0'
                a87+=1
        except:
            a58='1'+format(len(a59)-1,'03b')+''.join([format(i-2,'03b')for i in a59])+r
            a58=b'\x19'+int(a58,2).to_bytes(ceil(len(a58)/8))
    if a70.get():
        s=choice(a90).encode()
        for i in s:
            t=a58.find(i)
            a58=a[:t]+bytes([a[t]])+a[t:]
        a58=b'\x1a'+s+b'?'+a58
    if a71.get():
        s=len(a58//2)
        a58=b'\x1c'+str(s).encode()+b'?'+a58[s:]+a58[:s]
    if a72.get():
        while i==a58[0]:
            i=randint(0,255)
        a58=b'\x1b'+bytes(randint(100,1000)*[i])+a58
    a58+=bytes([[a62.get(),a63.get(),a64.get(),a65.get(),a66.get(),a67.get(),a68.get(),a69.get(),a70.get(),a71.get()].count(1)])
def b35():
    b36()
    b39.place(x=10*u,y=7*u)
    b43.place(x=80*u,y=150*u)
    b44.place(x=110*u,y=150*u,width=25*u)
    b45.place(x=140*u,y=150*u,width=25*u)
    b46.place(x=170*u,y=150*u,width=25*u)
    b38.place(x=120*u,y=30*u,height=60*u,width=60*u)
    b41.place(x=250*u,y=30*u,height=60*u,width=60*u)
def c71():
    global u
    if c70.get():
        from pyautogui import position
        del position
        a.geometry('780x445+535+260')
        c.add_cascade(label='cache',menu=b)
        c.delete('cache')
        u=4/3
    else:
        u=1
        if askyesno('Restart?','action need restart, continue?'):
            op(argv[0])
            c77()
def b47():
    b35()
    t=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
    sleep(.1)
    while b46.winfo_ismapped():
        sleep(.01)
        try:
            if b43.cget('text')=='#':
                while len(b44.get())>2:
                    b44.delete(len(b44.get())-1)
                while len(b45.get())>2:
                    b45.delete(len(b45.get())-1)
                while len(b46.get())>2:
                    b46.delete(len(b46.get())-1)
                for j,i in enumerate(b44.get()):
                    if i not in t:
                        b44.delete(j)
                for j,i in enumerate(b45.get()):
                    if i not in t:
                        b45.delete(j)
                for j,i in enumerate(b46.get()):
                    if i not in t:
                        b46.delete(j)
                b38.config(bg='#'+(format(int(b44.get(),16),'02x')if b44.get()!='' else '00')+(format(int(b45.get(),16),'02x')if b45.get()!='' else '00')+(format(int(b46.get(),16),'02x')if b46.get()!='' else '00'))
            else:
                for j,i in enumerate(b44.get()):
                    try:
                        int(i)
                    except:
                        b44.delete(j)
                for j,i in enumerate(b45.get()):
                    try:
                        int(i)
                    except:
                        b45.delete(j)
                for j,i in enumerate(b46.get()):
                    try:
                        int(i)
                    except:
                        b46.delete(j)
                b38.config(bg='#'+(format(int(b44.get()),'02x')if b44.get()!='' else '00')+(format(int(b45.get()),'02x')if b45.get()!='' else '00')+(format(int(b46.get()),'02x')if b46.get()!='' else '00'))
                while int(b44.get())>255:
                    b44.delete(len(b44.get())-1)
                while int(b45.get())>255:
                    b45.delete(len(b45.get())-1)
                while int(b46.get())>255:
                    b46.delete(len(b46.get())-1)
        except:
            pass
def b42(s):
    b43.config(text='#'if b43.cget('text')=='-'else '-')
def b48(s):
    try:
        s=askcolor()[1][1:]
        b44.delete(0,'end')
        b45.delete(0,'end')
        b46.delete(0,'end')
        if b43.cget('text')=='#':
            b44.insert(0,s[:2])
            b45.insert(0,s[2:4])
            b46.insert(0,s[4:])
        else:
            b44.insert(0,int(s[:2],16))
            b45.insert(0,int(s[2:4],16))
            b46.insert(0,int(s[4:],16))
    except:
        pass
def b49(s):
    b41.config(bg=askcolor()[1])
def b50():
    s=Thread(target=b47)
    s.start()
def b96():
    if not a28:
        showerror('Error','No file')
        return False
    b36()
    c02.place(x=270*u,y=250*u)
    c04.place(x=240*u,y=220*u,width=40*u)
    c06.place(x=290*u,y=170*u)
    c05.place(x=320*u,y=220*u,width=40*u)
    c00.place(x=230*u,y=150*u)
def b95():
    j()
    a16.config(text='merge',state=NORMAL,command=b96)
def b52():
    global b77
    init()
    b77=display.set_mode((1920,1080),FULLSCREEN)
    while c14:
        sleep(.00001)
        b77.fill((0,0,0))
        draw.rect(b77,(255,0,0),(randint(0,1920),randint(0,1080),randint(0,30),randint(0,30)))
        draw.rect(b77,(0,0,255),(randint(0,1920),randint(0,1080),randint(0,30),randint(0,30)))
        draw.rect(b77,(0,255,0),(randint(0,1920),randint(0,1080),randint(0,30),randint(0,30)))
        display.update()
def b80():
    def b94(key7):
        if not b87:
            return False
        global b79,c14
        b79=time()
        c14=False
        b81.withdraw()
        quit()
        bye()
    s=li(on_press=b94)
    s.start()
def b82():
    def b83(key1,key2,key3,key4):
        if not b87:
            return False
        global b79,c14
        b79=time()
        c14=False
        b81.withdraw()
        quit()
        bye()
    def b84(key5,key6):
        if not b87:
            return False
        global b79,c14
        b79=time()
        c14=False
        b81.withdraw()
        quit()
        bye()
    s=lis(on_click=b83,on_move=b84)
    s.start()
def c26():
    b36()
    c27.place(x=0*u,y=0*u)
    c28.place(x=0*u,y=0*u)
def b90():
    global b79,c14
    while b87:
        sleep(.00001)
        try:
            if time()-b79>int(b92.get()):
                b81.wm_deiconify()
                b81.config(bg='black')
                b81.lift()
        except:
            b92.delete(0,'end')
        try:
            if b92.get()=='':
                r=True
            else:
                r=time()-b79<int(b92.get())
            if time()-b79>int(b91.get())and r:
                if c17.get():
                    s=Thread(target=b52())
                    s.start()
                elif c18.get():
                    s=Thread(target=c15)
                    s.start()
                elif c20.get():
                    pass
        except:
            b91.delete(0,'end')
def c03():
    global a58
    a58=b''
    for i in a28:
        b97=format(getsize(i),'b');b97=format(ceil(len(b97)/8)-1,'03b')+b97
        with open(i,'rb')as s:
            a58+=int('1'+b97,2).to_bytes(ceil((len(b97)+1)/8))+i.encode()+b'?'+s.read()
    with open(c04+'.'+c05 if c05 else c04,'wb')as s:
        s.write(a58)
def b85():
    b36()
    b88.place(x=210*u,y=20*u)
    b93.place(x=170*u,y=60*u)
    b91.place(x=250*u,y=55*u,width=30*u,height=30*u)
    b92.place(x=380*u,y=55*u,width=30*u,height=30*u)
    c21.place(x=250*u,y=100*u)
    c16.place(x=50*u,y=100*u)
    c19.place(x=150*u,y=100*u)
def b89():
    global b87,b79
    b79=time()
    b87=b86.get()
    if b86.get():
        s=Thread(target=b90)
        s.start()
        b80()
        b82()
        b91.config(state=NORMAL)
        b92.config(state=NORMAL)
        b93.config(state=NORMAL)
        c21.config(state=NORMAL)
        c16.config(state=NORMAL)
        c19.config(state=NORMAL)
    else:
        b91.config(state=DISABLED)
        b92.config(state=DISABLED)
        b93.config(state=DISABLED)
        c21.config(state=DISABLED)
        c16.config(state=DISABLED)
        c19.config(state=DISABLED)
def b64():
    try:
        s=VideoCapture(b56).get(CAP_PROP_FPS)
        ffmpeg_extract_subclip(b56,int(b57.get())*3600+int(b58.get())*60+int(b67.get())+int(b68.get())/s,int(b69.get())*3600+int(b70.get())*60+int(b71.get())+int(b72.get())/s,targetname=b56.rsplit('/',1)[0]+'/'+'-final.'.join(b66.cget('text').split('.')))
    except:
        pass
def b63():
    global b56
    b56=askopenfilename(initialdir=b65,title='choose file')
    b66.place(x=280-5*(len(b56.rsplit('/',1)[1])//2),y=200)
    b66.config(text=b56.rsplit('/',1)[1])
def b55():
    b59.place(x=120*u,y=50*u)
    b57.place(x=70*u,y=100*u,width=30*u)
    b58.place(x=115*u,y=100*u,width=30*u)
    b67.place(x=165*u,y=100*u,width=30*u)
    b68.place(x=213*u,y=100*u,width=30*u)
    b69.place(x=325*u,y=100*u,width=30*u)
    b70.place(x=370*u,y=100*u,width=30*u)
    b71.place(x=415*u,y=100*u,width=30*u)
    b72.place(x=465*u,y=100*u,width=30*u)
    b61.place(x=130*u,y=250*u,width=50*u)
    b62.place(x=400*u,y=250*u)
    b60.place(x=70*u,y=130*u)
    while b74:
        sleep(.0001)
        for i in [b57,b58,b67,b68,b69,b70,b71,b72]:
            try:
                int(i.get())
            except:
                i.delete(0,'end')
            if i.get()=='':
                i.insert(0,'0')
def b73():
    b36()
    global b74
    b74=True
    s=Thread(target=b55)
    s.start()
def c07():
    b36()
    c08.place(x=280*u,y=15*u)
    c09.place(x=293*u,y=275*u)
    c2.place(x=300*u,y=30*u)
def c15():
    speed(0)
    colormode(255)
    setup(width=1.0,height=1.0)
    getcanvas().winfo_toplevel().overrideredirect(1)
    hideturtle()
    bgcolor('black')
    c12=time()
    while c14:
        if time()-c12>20:
            clear()
            b=time()
        pensize(randint(0,30))
        color(randint(0,255),randint(0,255),randint(0,255))
        begin_fill()
        c13=choice(['s','t','c'])
        if c13=='c':
            circle(randint(0,30))
        elif c13=='t':
            fd(30)
            right(120)
            fd(30)
            right(120)
            fd(30)
        else:
            fd(40)
            right(90)
            fd(40)
            right(90)
            fd(40)
            right(90)
            fd(40)
        if randint(0,1):
            end_fill()
        penup()
        goto(randint(-960,960),randint(-540,540))
        pendown()
def c11():
    global c9
    c9='none'
def c10():
    c9=c8.get()
    try:
        while True:
            try:
                a28.append(argv[1].replace('\\','/'))
                argv.pop(1)
                a29()
            except:
                pass
            factorial(1000)
            sleep(fabs((c09.winfo_rooty()-310)/260))
            if c9!=c8.get():
                    c9=c8.get()
                    init()
                    stop()
                    if c8.get!='none':
                        if c8.get()=='wind':
                            Sound(b'').play()
                            Timer(180,c11).start()
            if c68.get()=='save':
                pass
    except:
        pass
def c76():
    if c83.get():
        c4=askyesnocancel('Exit?','are you sure you want to exit?\n\napplication can run into the background')
        if c4:
            c77()
        elif c4==False:
            c79()
    elif c87.get():
        c77()
    else:
        c79()
def c81():
    global c80
    c80.stop()
    a.wm_iconify()
    a.lift()
    sleep(.01)
    del c80
def c82():
    c80.stop()
    c77()
def c79():
    global c80
    a.withdraw()
    c80=Icon('clauth app',c78,'clauth',(MenuItem('open',c81),MenuItem('exit',c82)))
    s=Thread(target=c80.run)
    s.start()
def c77():
    a.destroy()
    if not d10.get():
        exit(1)
def c5():
    showinfo('Fact',['when you got nothing you got nothing to lose','A dream you dream alone is only a dream. A dream you dream together is reality.','Nobody promised you tomorrow','We humans are more concerned with having than with being','Laughter is the language of the soul','The only way you can know where the line is is if you cross it','You only live once, but if you do it right, once is enough','Luck is a word used to describe the success of people you don’t like','Make each day your masterpiece','All the darkness in the world cannot extinguish the light of a single candle','You don’t have a soul. You are a soul. You have a body','Faithless is he that says farewell when the road darkens','When you fail, you also learn how not to fail','In order to be irreplaceable, one must always be different','You cannot be lonely if you like the person you’re alone with','Life has more imagination than we carry in our dreams','Good things come in good time','Tomorrow hopes we have learned something from yesterday','What we do is more important than what we say or what we say we believe','If you are not having fun you are doing something wrong','All humor is rooted in pain','Don’t cry because it’s over. Smile because it happened','You pray for rain, you gotta deal with the mud too. That’s a part of it','Governments change… the lies stay the same','My fear was not of death itself, but a death without meaning','Where the willingness is great, the difficulties cannot be great','You don’t have to eat less. You just have to eat right','clauth extract subclip works in no time','A woman’s heart is a deep ocean of secrets','You must work in the dark for your light to shine','You don’t get respect if you don’t deserve it','We can be heroes just for one day','It doesn’t hurt to get more education','Fight with a happy heart and a strong spirit','We’ve added years to life, not life to years','The goal is timeless. Chase the moment, and you lose','The choices we make dictate the lives we lead','I don’t want to end up simply having visited this world','My fake plants died because I did not pretend to water them','Don’t be afraid to give up the good to go for the great','An intelligent woman doesn’t get sad, she gets pretty','Yesterday don’t matter if it’s gone','Time is a wonderful storyteller','Behind every successful person lies a pack of haters','If there is no struggle, there is no progress','Luck is not a business model','Sometimes it takes years for a person to become an overnight success','The harder I work, the luckier I become','The best revenge is massive success','Nothing left to do but smile','I found out that there weren’t too many limitations, if I did it my way','The beginning is the most important part of the work','Your river is strong. Let it flow','Faith is a knowledge within the heart, beyond the reach of proof','Nothing is stopping me from doing what I love to do','Well, it’s hard to be yourself, it’s the hardest job there is','It takes a lot of courage to show your dreams to someone else','I paint flowers so they will not die','There can only be one king','Don’t wait for them to tell you. Tell them','In life you always see the darkest days before the sunshine','Keep your friends close, your enemies even closer','Haters keep on hating cause somebody’s gotta do it','The good life is one inspired by love and guided by knowledge','There is no normal life, there’s just life. Get on with it','It’s okay to start over, let someone else love you the right way','Even a blind man knows when the sun is shining','Life is what you make it, just don’t fake it','Wear your crown and go chase your dreams','It’s never too late to get good at something','In every walk with nature one receives far more than he seeks','Our weary eyes still stray to the horizon','I will not let anyone scare me out of my full potential','To lose your path is the way to find that path','I’m not afraid of dying, I’m afraid of not trying','There is no way to happiness – happiness is the way','What a dog I got. His favorite bone is in my arm','Only thing free in life is options','Look at the sky tonight. All the stars have a reason','I am my inspiration','Be kind to one another, even when it’s not requested','Don’t be scared to live your life without judgment','you either die a hero or you live long enough to see yourself become the villain','when you break with your love it means he/she is in love with another person','they say money can’t by happiness','i love walking in the rain because nobody can see my tears','they don’t know your kindness until you turn to a villain','you need to lye if you want others think of you','ppl is like when they understand you have fun with them they break with you','let something inside youself because if you done everything they end up with you','looking for the best? look for the one who tries to be best for you','ppl never hate you ’cause of your limits they hate you for your powers. so try to be powerful and don’t care to what they say','you better to be alone except having someone who makes you feel alone','Happiness is not by chance, but by choice','Keep your face to the sunshine and you cannot see a shadow','Impossible is for the unwilling','Believe you can and you’re halfway there','It is never too late to be what you might have been','When you have a dream, you’ve got to grab it and never let go','Whatever you are, be a good one','You must do the things you think you cannot do','Be faithful to that which exists within yourself','Dream big and dare to fail','My mission in life is not merely to survive, but to thrive','You are enough just as you are','To be the best, you must be able to handle the worst','Life is like riding a bicycle. To keep your balance, you must keep moving','Every moment is a fresh beginning','Your mind must be stronger than your feelings','I know that now, and now is all that matters','Sometimes you have to take two steps back to take ten forward'][int(time()//86400%111)])
def c0():
    if Controller().position[1]>310 and Controller().position[1]<570:
        c09.place(x=293,y=Controller().position[1]-280)
def c3(s):
    c0()
def c6():
    b36()
    c7.place(x=30*u,y=30*u)
    c67.place(y=120*u,x=30*u)
    c69.place(x=150*u,y=30*u)
    c84.place(x=300*u,y=30*u)
    c86.place(x=300*u,y=60*u)
    c88.place(x=30*u,y=5*u)
    c90.place(x=150*u,y=100*u)
    c94.place(x=450*u,y=30*u)
    d11.place(x=300*u,y=100*u)
def c92():
    a.attributes('-topmost',c93.get())
def c30():
    if not a28:
        showerror('Error','No file')
        return False
    b36()
    c65.pack(side=RIGHT,fill=Y)
    c31.place(x=30*u,y=20*u)
    c32.place(x=110*u,y=22*u,width=30*u)
    c33.place(x=230*u,y=15*u)
    c37.place(x=350*u,y=20*u)
    c36.pack(side=LEFT)
    c65.config(command=c36.yview)
    c42.place(x=440*u,y=20*u)
    c44.place(x=490*u,y=60*u,width=70*u)
    c45.place(x=490*u,y=100*u,width=70*u)
    c49.place(x=490*u,y=150*u,width=70*u)
    c51.place(x=490*u,y=200*u,width=70*u)
    global c40
    c40=True
    while c40:
        for i in a28:
            c36.insert('end',' '+i.rsplit('/',1)[1]+' : ')
            with open(i,'rb')as s:
                s=s.read()
            if c35.get():
                c42.config(state=NORMAL)
                if c43.get():
                    t=0
                else:
                    t=1
                if c34.get()=='0b':
                    c36.insert('end',c32.get().join([str(k+t)+'-'+i for k,i in enumerate(list(map(bin,s)))]))
                elif c34.get()=='decimal':
                    c36.insert('end',c32.get().join([str(k+t)+'-'+i for k,i in enumerate(list(map(str,s)))]))
                elif c34.get()=='bits':
                    c36.insert('end',c32.get().join([str(k+t)+'-'+i for k,i in enumerate([format(i,'b')for i in s])]))
                elif c34.get()=='bitful':
                    c36.insert('end',c32.get().join([str(k+t)+'-'+i for k,i in enumerate([format(i,'08b')for i in s])]))
                else:
                    c36.insert('end',c32.get().join([str(k+t)+'-'+i for k,i in enumerate([hex(i)for i in s])]))
            else:
                c42.config(state=DISABLED)
                if c34.get()=='0b':
                    c36.insert('end',c32.get().join(list(map(bin,s))))
                elif c34.get()=='decimal':
                    c36.insert('end',c32.get().join(list(map(str,s))))
                elif c34.get()=='bits':
                    c36.insert('end',c32.get().join([format(i,'b')for i in s]))
                elif c34.get()=='bitful':
                    c36.insert('end',c32.get().join([format(i,'08b')for i in s]))
                else:
                    c36.insert('end',c32.get().join([hex(i)for i in s]))
        c60,c61,c62,c63,c64=c35.get(),c43.get(),c34.get(),c32.get(),a28.copy()
        while not any([c60!=c35.get(),c61!=c43.get(),c62!=c34.get(),c63!=c32.get(),c64!=a28]):
            sleep(.0000001)
            a.update()
        c36.delete('1.0','end')
def c52():
    b36()
    d00.place(x=260*u,y=100*u,width=100*u)
    d02.place(x=100*u,y=220*u)
    d04.place(x=292*u,y=260*u,width=30*u)
    d05.place(x=470*u,y=260*u,width=40*u)
def d07():
    while d00.cget('text')=='stop':
        d06.write(cvtColor(array(grab()),COLOR_RGB2BGR))
def d01():
    if d00.cget('text')=='start':
        try:
            d00.config(text='stop',fg='white',bg='black')
            global d06
            d06=VideoWriter(str(int(time()))+".avi",VideoWriter_fourcc(*"XVID"),int(d04.get()),(1920,1080))
            s=Thread(target=d07)
            s.start()
        except:
            showerror('Error','invalid data')
            d00.config(text='start',fg='black',bg='darkorange')
    else:
        d00.config(text='start',fg='black',bg='darkorange')
        d06.release()
def c53():
    b36()
    c54.place(x=20*u,y=10*u)
    c55.place(x=25*u,y=50*u,width=550*u,height=230*u)
    c56.place(x=300*u,y=290*u)
    c57.place(x=30*u,y=290*u)
def c58():
    pass
def c59():
    pass
def c46():
    global c48
    c36.config(font=(None,c48+1))
    c48+=1
def d16():
    b36()
    d14.place(x=250*u,y=150*u)
def d15(s):
    try:
        showinfo('congratulations',{'CLAUTH':'you won 50 coins','frost dream':'you won 500 coins'}[d14.get()])
    except:
        showinfo('Not found','there is nothing')
def c85():
    if c83.get():
        c86.config(state=DISABLED)
        return False
    c86.config(state=NORMAL)
def c47():
    global c48
    c36.config(font=(None,c48-1))
    c48-=1
def d04():
    b36()
    d03.place(x=220*u,y=120*u)
def c50():
    global c40
    if c49.cget('text')=='freeze':
        c49.config(text='unfreeze')
        c40=False
    else:
        c49.config(text='freeze')
        c30()
    a29()
def c29():
    j()
    a16.config(text='binary',state=NORMAL,command=c30)
def c22():
    c18.set(0);c17.set(0)
def c23():
    c20.set(0);c17.set(0)
def c24():
    c18.set(0);c20.set(0)
def c91(s):
    try:
        if c89.get()and a.state()[0]=='i':
            c80
    except:
        c79()
def d09():
    for i in a28:
        VideoFileClip(i).write_videofile('file.mkv',threads=8,logger=None,codec='libx264')
def d08():
    j()
    a16.config(text='c media',state=NORMAL,command=d09)
    a01.place(x=390*u,y=310*u)
    a01.delete(0,'end')
    a01.insert(0,'format: (e.g. mp4)')
def b36():
    global b74,b40
    b74,b40=False,False
    d12.place_forget();d11.place_forget();d05.place_forget();d04.place_forget();d03.place_forget();d02.place_forget();d00.place_forget();c94.place_forget();c90.place_forget();c88.place_forget();c86.place_forget();c84.place_forget();c75.place_forget();c72.place_forget();c73.place_forget();c69.place_forget();c67.place_forget();c65.place_forget();c57.place_forget();c56.place_forget();c55.place_forget();c54.place_forget();c51.place_forget();c49.place_forget();c45.place_forget();c44.place_forget();c42.place_forget();b57.place_forget();b58.place_forget();b67.place_forget();b68.place_forget();b69.place_forget();b70.place_forget();b71.place_forget();b72.place_forget();c36.place_forget();c37.place_forget();c33.place_forget();c32.place_forget();c31.place_forget();c28.place_forget();c27.place_forget();c21.place_forget();c16.place_forget();c19.place_forget();c7.place_forget();b93.place_forget();c2.place_forget();c09.place_forget();c08.place_forget();c06.place_forget();c04.place_forget();c05.place_forget();c02.place_forget();c00.place_forget();b91.place_forget();b92.place_forget();b88.place_forget();b75.place_forget();b62.place_forget();b61.place_forget();b60.place_forget();b59.place_forget();b57.place_forget();b58.place_forget();b60.place_forget();b59.place_forget();b54.place_forget();b46.place_forget();b45.place_forget();b44.place_forget();b43.place_forget();b41.place_forget();b39.place_forget();b38.place_forget();a84.place_forget();a93.place_forget();a94.place_forget();a95.place_forget();a89.place_forget();a86.place_forget();a83.place_forget();a82.place_forget();a81.place_forget();a80.place_forget();a79.place_forget();a78.place_forget();a77.place_forget();a76.place_forget();a75.place_forget();a74.place_forget();a61.place_forget();a57.place_forget();a55.place_forget();a54.place_forget();a47.place_forget();a46.place_forget();a45.place_forget();a44.place_forget();a43.place_forget();a42.place_forget();a30.place_forget();a09.place_forget();a08.place_forget();a07.place_forget();a06.place_forget();a03.place_forget();a01.place_forget();a00.place_forget();a27.place_forget();a22.place_forget();a24.place_forget();a26.place_forget();a20.place_forget();a18.place_forget();a16.place_forget();a14.place_forget();a11.place_forget();a9.place_forget();a2.place_forget();a3.place_forget();a4.place_forget();a6.place_forget()
a48=IntVar();a49=IntVar();a50=IntVar();a51=IntVar();a52=IntVar();a53=IntVar()
a62=IntVar();a63=IntVar();a64=IntVar();a65=IntVar();a66=IntVar();a67=IntVar();a68=IntVar();a69=IntVar();a70=IntVar();a71=IntVar();a72=IntVar()
b40=IntVar()
b86=IntVar()
c01=IntVar()
c70=IntVar()
c83=IntVar()
c87=IntVar()
c89=IntVar()
c93=IntVar()
d10=IntVar()
d10.set(1)
c83.set(1)
c8=StringVar()
c68=StringVar()
c68.set('save')
c8.set('none')
c34=StringVar()
c34.set('0b')
c17=IntVar();c18=IntVar();c20=IntVar()
c35=IntVar()
c43=IntVar()
c66=Frame(a)
c66.place(x=30,y=50,width=400,height=250)
c65=Scrollbar(c66)
d14,d12,d11,d03,d02,d00,c94,c90,c88,c86,c84,c75,c72,c73,c69,c67,c57,c56,c55,c54,c51,c49,c48,c44,c45,c42,c36,c37,c31,c28,c27,c14,c21,c19,c16,c7,c08,c06,c04,c05,c02,c00,b93,b91,b92,b87,b88,b75,b67,b68,b69,b70,b71,b72,b60,b66,b61,b62,b59,b57,b58,b54,b46,b45,b44,b43,b41,b39,b38,a93,a94,a95,a89,a86,a83,a82,a81,a80,a79,a78,a77,a76,a75,a74,a61,a57,a55,a54,a47,a46,a45,a44,a43,a42,a30,a09,a08,a07,a06,a03,a01,a00,a28,a27,a22,a24,a26,a20,a18,a16,a14,a11,a9,a2,a3,a4,a6=Entry(a),Label(a,text='stackoverflow',fg='blue'),Checkbutton(a,text='stay in background',variable=d10),Label(a,text='this page is empty',fg='darkred',font=(None,15)),Label(a,text='real fps                            fps                        audio bitrate\n\n22                                                                          ',font=(None,13)),Button(a,text='start',command=d01,bg='darkorange',font=(None,20)),Checkbutton(a,text='stay on top',variable=c93,command=c92),Checkbutton(a,text='minimize to tray',variable=c89),Label(a,text='music\n\n\n\n\n\nsave settings'),Checkbutton(a,text='exit on close',variable=c87,state=DISABLED),Checkbutton(a,variable=c83,text='ask before exit',command=c85),Button(a,text='own',bg='#a8a8ff'),Button(a,text='convert',command=e),Text(a),Checkbutton(a,text='high resolution',variable=c70,command=c71),OptionMenu(a,c68,'save','reset on every restart','only settings','only app choices'),Button(a,text='common questions',command=c59),Button(a,text='submit',command=c58,bg='#ffee79'),Text(a,font=('Montserrat',13)),Label(a,font=(None,13),fg='dark blue',text='having any question? advice? opinion? bug? or anything you wish to tell us?'),Button(a,text='add file',command=a12),Button(a,text='freeze',command=c50),10,Button(a,text='zoom',command=c46),Button(a,text='zoom out',command=c47),Checkbutton(a,state=DISABLED,text='start with 0',variable=c43),Text(c66,yscrollcommand=c65.set),Checkbutton(a,text='bytes num',variable=c35),Label(a,text='bytes spliter                         show as'),Button(a,text='travel to stw'),Button(a,text='travel to lobby'),False,Checkbutton(a,state=DISABLED,command=c22,text='blank blinking',variable=c20),Checkbutton(a,state=DISABLED,command=c23,text='mate math',variable=c18),Checkbutton(a,state=DISABLED,command=c24,text='glitch',variable=c17),OptionMenu(a,c8,'none','wind','brahms','rain','alone wolf','one mans dream','canon','snow','time','white hats','hooked on you'),Label(a,text='Hot\n\n\n\n\n\n\n\n\nNormal\n\n\n\n\n\n\n\n\n\nCold'),Label(a,text='.',font=(None,50)),Entry(a),Entry(a),Button(a,text='continue',command=c03),Checkbutton(a,text='remmember files path',variable=c01),Label(a,text='turn on after                   turn off after',state=DISABLED),Entry(a,state=DISABLED),Entry(a,state=DISABLED),False,Checkbutton(a,text='enable screen saver',variable=b86,command=b89),Button(a,text='add dir',bg='#a8a8ff',command=b76),Entry(a),Entry(a),Entry(a),Entry(a),Entry(a),Entry(a),Label(a,text='hour     minute    second    frame                           hour     minute    second    frame'),Label(a),Button(a,text='open',command=b63),Button(a,text='extract',command=b64),Label(a,text='start                           end',font=(None,20)),Entry(a),Entry(a),Label(a,text='Reddit',fg='blue'),Entry(a),Entry(a),Entry(a),Label(a,text='#'),Label(a,bg='black'),Checkbutton(a,text='link',variable=b40),Label(a,bg='black'),Entry(a),Button(a,text='browse',command=a96),Button(a,text='start',command=a85),Checkbutton(a,text='round',variable=a72),Button(a,text='choose random and continue',command=b51),Label(a,text='click                to continue'),Checkbutton(a,text='split',variable=a71),Checkbutton(a,text='phrase',variable=a70),Checkbutton(a,text='pattern',variable=a69),Checkbutton(a,text='bits',variable=a68),Checkbutton(a,text='factorial',variable=a67),Checkbutton(a,text='letter',variable=a66),Checkbutton(a,text='reduce',variable=a65),Checkbutton(a,text='count',variable=a64),Checkbutton(a,text='bytes',variable=a63),Checkbutton(a,text='number',variable=a62),Label(a,text='all methods can be modified by passwords',fg='gray'),Label(a,text='please choose a method',fg='red'),Button(a,text='finish',command=a56),Checkbutton(a,text='quick                            \nno time no extra data',command=a36,variable=a48),Checkbutton(a,text='low                                                                                          \nunable to read by other applications suitable for sharing',command=a37,variable=a49),Checkbutton(a,text='high                                                           \nhigh level encryption with more file size',command=a38,variable=a50),Checkbutton(a,text='ultra                                                                                             \nreadable only by clauth app recommended for file storage',command=a39,variable=a51),Checkbutton(a,text='recommended                                                     \na balance for security fast dataless and secure',command=a40,variable=a52),Checkbutton(a,text='custom',command=a41,variable=a53),Label(a,text='Twitch',fg='blue'),Label(a,text='Discord',fg='blue'),Label(a,text='Instagram',fg='blue'),Label(a,text='YouTube',fg='blue'),Label(a,text='made by frost dream',fg='gray',font=(None,30)),Label(a,text='file name already exist',fg='red',font=10),Entry(a),Button(a,text='trash',bg='#a8a8ff',command=a0),[],Listbox(a),Button(a,text='copy',bg='#a8a8ff',command=a21),Button(a,text='rename',bg='#a8a8ff',command=a23),Button(a,text='delete',bg='#a8a8ff',command=a25),Button(a,text='  .txt',bg='#ff9393',command=a19),Button(a,text='view',bg='#ff9393',command=a17),Button(a,text='next',bg='#f8fea9',state=DISABLED),Button(a,text='remove',bg='#a8a8ff',command=a13),Button(a,text='add',bg='#a8a8ff',command=a12),Button(a,text='translate',command=a8),Text(a),Label(a,text='Enter input in binary or decimal or hexadecimal with "," or "  " or "/" or "\\".'),Button(a,text='compile',command=a5),Label(a,text='invalid syntax',fg='red')
d05,d04=Entry(a),Entry(a)
d14.bind('<Return>',d15)
d04.insert(0,'22')
d05.insert(0,'44000')
c33,c32=OptionMenu(a,c34,'0b','hexadecimal','decimal','bits','bitful'),Entry(a)
c2=Label(a,text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|')
c09=Button(a,text='    ',command=c0,bg='gray')
a84=Label(a,text='here',fg='blue')
c2.bind('<1>',c3)
b38.bind('<Button-1>',b48)
b41.bind('<Button-1>',b49)
b54.bind('<Button-1>',b53)
a07.bind('<Button-1>',a31)
a08.bind('<Button-1>',a32)
a09.bind('<Button-1>',a33)
a30.bind('<Button-1>',a34)
d12.bind('<1>',d13)
b43.bind('<Double-Button-1>',b42)
a.bind('<Unmap>',c91)
a01.bind('<Return>',a02)
a84.bind('<Button-1>',a92)
c.add_cascade(label='File',menu=b)
b.add_command(label='Home',command=j)
b.add_separator()
b.add_command(label='New file')
b.add_command(label='Open',command=a12)
b.add_command(label='Open copy')
b.add_command(label='Open copy beta')
b.add_command(label='Open folder',command=b76)
b.add_separator()
b.add_command(label='Save')
b.add_command(label='Save new')
b.add_separator()
b.add_command(label='Background',command=c79)
b.add_command(label='Exit',command=c77)
b=Menu(c,tearoff=False)
c.add_cascade(label='Editor',menu=b)
b.add_command(label='Undo')
b.add_command(label='Redo')
b=Menu(c,tearoff=False)
c.add_cascade(label='Settings',menu=b)
b.add_command(label='General')
b.add_command(label='System')
b.add_command(label='Users')
b.add_command(label='Main',command=c6)
b=Menu(c,tearoff=False)
c.add_cascade(label='Tools',menu=b)
b.add_command(label='File to number',command=d)
b.add_command(label='Number to file',command=c74)
b.add_command(label='Calculator',command=a91)
b.add_command(label='Binary viewer',command=f)
b.add_command(label='Write binary',command=a1)
b.add_command(label='Advance Binary viewer',command=c29)
b.add_command(label='Extract subclip',command=b73)
b.add_command(label='Colors',command=b50)
b.add_command(label='C controller')
b.add_command(label='Screen recorder',command=c52)
b.add_command(label='Clock')
b.add_command(label='Check sectors')
b.add_command(label='VPN')
b.add_command(label='Video from images')
b.add_command(label='YouTube downloader')
b.add_command(label='Video editor')
b=Menu(c,tearoff=False)
c.add_cascade(label='Security',menu=b)
b.add_command(label='File encryption',command=a10)
b.add_command(label='Merge files',command=b95)
b.add_command(label='System security')
b=Menu(c,tearoff=False)
c.add_cascade(label='Convert',menu=b)
b.add_command(label='Media',command=d08)
b.add_command(label='Programming')
b.add_command(label='Text')
b.add_command(label='Apk and exe')
b.add_command(label='Games')
b=Menu(c,tearoff=False)
c.add_cascade(label='App',menu=b)
b.add_command(label='Credit',command=a05)
b.add_command(label='Check for update',command=g)
b.add_command(label='News',command=d04)
b.add_command(label='Help',command=c53)
b=Menu(c,tearoff=False)
c.add_cascade(label='More',menu=b)
b.add_command(label='Screen saver',command=b85)
b.add_command(label='Pc temperature',command=c07)
b.add_command(label='Fact of the day',command=c5)
b.add_command(label='Chatroom')
b.add_command(label='Fortnite',command=c26)
b.add_command(label='Search')
b.add_command(label='Enter code',command=d16)
a.config(menu=c)
a.protocol('WM_DELETE_WINDOW',c76)
Thread(target=c10).start()
j()
a.mainloop()