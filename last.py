from os.path import expanduser,getsize
from PIL.ImageTk import PhotoImage
from PIL.Image import open as ope
from ctypes import windll
from time import sleep
from io import BytesIO
from sys import argv,executable
from threading import Thread
from random import randint
from colorir import HSL
from tkinter import Tk,Menu,Button,Label,Text,Checkbutton,Listbox,Entry,DISABLED,NORMAL,IntVar,StringVar,OptionMenu,RIGHT,LEFT,Scrollbar,Y,Frame,X
a36,a37,a38,a39,a40,a41=[0,0,0,0,0,0]
b65=expanduser("~")+'\\desktop'
a,b81=Tk(),Tk()
a.withdraw()
b81.attributes('-fullscreen',True)
b81.withdraw()
a.geometry('600x350+430+220')
a.resizable(False,False)
a.title('clauth app')
c78=ope(BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x1e\x00\x00\x00\x1f\x08\x06\x00\x00\x00\xf0l}\x07\x00\x00\x00\tpHYs\x00\x00\x12t\x00\x00\x12t\x01\xdef\x1fx\x00\x00\t1IDATH\x89u\x97k\x8c]\xd5u\xc7\x7fk\xef\xf3\xb8\x8f\x99{\xef<\xec\xb1\xc7\x8fa\xf0\xd8\x80\x8d\xed\x00\xe6\x15\x9c\x86\x86$MIQH\x82\x15!\x92H(\x12\x8aH\xd2\x8aD\x8a\xd2~)TU\xd5\x0f\xad\xda*i\xf3T[\xc5\xa4\xa5\r)%\x15"\xd8I\x808\x0f\x0c\x81\x10\x88\xb1y\xd8\x8c_\xe3\xb1=\x8f;\xf7}\x1e{\xaf~\xb8c\xf3\x889\x1f\x8e\x8e\xce^\xda\xbf\xbd\xd6\xfa\xef\xbd\xd6\x16.\xf0D"(\xe0T\xf1\xcb\xff\x0c\xb2jK\x18]9\x19F\x97o\x8c\xe2\x8bo\xd8\xb9sUy\xd5\x98\xe8\xf0\xd0\xd9\xf6@\xf9\xf0\x0bss/\xfc\xcf\x9e=\xbfy\xf1\xd0\xc1\x99\x01\x11\xc20\xc4\x88\xa1\x9e\xf4\xd8~\xd9\xa5|\xfd;\xffJ\xa1X\xc0\xfb\xfe\x8c\xc1\x85\xc0\x00\x0e\xf0\xc0\xa8\xb1\xd7\xdf1P\xbd{W\xb9\xf2\xa1\xadQ<Z\xb1\x01\x88\x90\xb7\xba\x046\x86\xab\xae&_\xb3\x8a?\xf6\x9e\x8f\xdct\xd3\xc2C\x0f?\xbc\xe7?\xff\xf7\xa1\x7fy}aa\xdf`\x18\xbd\xd3\xf4\xc8;\r\x84\xc8\xc4\xdd\x83\xb5\xbf\xba\xa76\xf2\xc9\x89 2^\x95\x04\x05\x11\xbc\xf7\xe4\xc5"\xd3"l\x1e\xaa\xe1.\xdf\x8c\x94\x8a\xc4k\xd6\xc0\xe5[\x98m\xb7\xf4\x9b?|\xf8\xbf\xbf\xf6\xe0\x83\x7f1\xd7i\x1f\xb9\xf2\x02\x1e_\x10<i\x83\x0f\x7fct\xf5\xb7>8P\x1d\xcf]NO\xf5m\xe1P\xe6\xe3\x84_\xdcp\x86\x9b\x7f\xb8\x928R4.\xa0\xe5\x12fr\x82\xe8\x9a\xab\xb1\x9b6\xf2\xd4\xf1cg\xef\xfc\xea?~\xc6\xc7\xd1\xff\xdd\xbf\xfb{\xc4o\x02\xdb\xb7C\xb7E\xf1\xa7\x1e]?\xf5\xc0\x8ej\xad\x9a#\xa4\xce\xa1\xbc\x01\xf6\xaa\xd0\x83\xe3\x9b:\xac\xb8\xb7\xce\xec\xf7\xcbT]@\xa0\x8e0M\xa1\xbeD\xf7\xf5i\x92g\x9ee\xca\x86\xe5[\xb7l\xdd5\xed\xf2\xd3[\xdf\x7f\xd3\xb3\xb5J\x05c-a\x18\xbe\x15<\x15\x84\x1f{lj\xcb\xf7&\xc6\xc6\xac\x07|/\xc1\xbb\xfc<V\x01\xe7=i\x0f\x16nos\xc9\xae\x90C\xfb`\xf1e\xe1\x8cu\x0c\x1bK\xac\x8a&\t\x9dN\x9b\xd6\xa9S\x8c\x89\x98\x9d\xeb\xd6\xdf\xf2t\xb7\xfd\xea\xe1\x13\'^<}\xec\x18\'\xa7\x8f\xbe!\xae"2u\xffE\x1b\xbf\xbdn|\xdcj\x1cA\xb7\x8bs9^\xdfHH\xee=\xc6C\xbd\x9aS\xb8!\xc2t\xaa\x94\xde\xbb\xc8\xec\x8f<\x1d\xaf$Y\xca\xa5\x1a\x10#\x18 \x11a\xee\xe81\xc6\x8aE\xb6N\x1f\xff\xea\x9f\xee}l\xbf\x81\xc3F\xe4\xbc\xc7\xe6\xde5\x13\x0f\xdc\xbe\xf3\x0f\xb6h\xad\n\xcd&\xdah\xe2\xd3\xb4\x1f\xdaeO\xbd*6\x85\xd9\x1dP\xbd\xa3HA3\xa8.\xf1\xca\x0f\x02\x8a\xdeb\x0cX\x04\x8bP\x10C,B\xb6\x9c\xd3\x89\xb8X\\\xf7\x9ewo\xeb\xae]}\xff\x86\xa9)5\xcb!\xfe\xf0=W\xecx?S\x17\xc3\xf00\xdal\xa2i\xfa\x16\xf5\xe9\xf2+\xb5\xd0{\xb7\xa5\\\x00\x9fu\x98\xb8,\xc1mIH\x93\xbeM\x8a\xd2V\xa5\x8d\'OS\xc2n\x0f\xd7l\xd2;v\x8c\xeb\xbb\xc9\x8d\x1bV\xae\xbamxx\x04\x03\xc8g\xc7\xc6\xbfX\x1a\x1d\x05\x11\xa4\xd5\xc6tS\xac\x07\xeb\r\xd6\x81u\x82\xcd\x95(\x83VU\x89\xaf\x04\xdf\xcb\xf0>\xa3\x18\x07\\ts\xc6Pj\x19\xf4\x06\xeb\x84\xdc)\x9d\\1\x18\x8c\xf3\xd8$\xa3\xdbhR\x9a=\xcd%q\xe1\xcf^<t\xd0\xd8\xaa\xc8U\xdf\xd8\xb8\xf9\xaf\x07\'\xd6KR,\xb2p\xe4\x15\x92\xfa"\xadPiE)\x8d8\xa7\x15;\xea\x03Jc@\x99\xde\xae\x8c\xfcI\x80q=\nQ\x82\xc1\x10\r{N\xed\r(:\xa1\x17xRQz(m\xafx/x<\x9d\xd8\x12\xa4\x8ej\xb9\xbcv\xf0\xaa+\xf7\x067\x96+\x1f\x1a_\xb1\xc2P\xab\xd1j\xf4\xf8Q\xfc,\xdb\xfe\xd93T\xa8\xd1l+XA\x0c\xa81x\x845\x05KQ\x1cB\x8e\xb5\x9e<\x81Uk-\xd7<\xb2\x80\xcf\x1d\xeaA\x9d\xe0S\xf09\x10\xc3K/\x0b\xcd\xbf_\xc7\x07\x92aF\x0e\x1c\x94Vk\xe9\xa3\xc1\x8ejm;+W\xa0c+\x189p\x88]\x87\xd6\xf1\xdaC\x8b\xf09\xcf\x9a\x8b"|7\x052\xd0\x0cU!\xcf\x85\xa4\x97\x11\x85\x19\xde\x83\x88`\x15\xd6\x8e[\x88\xf27\x14\x11\x00\x06~\xb7/`\xe5\xbfO\xf2\xbe\xee\x08i\xa1G\x18V9\xbb\xf7\xa7\xef2\x93C\xc3\x93\xacX\xd97o,Q\x8c,\x97\xef\x19"\xfd\xb2\xe5\xe5}\x1d\x12k\xc8S\x8b\xcb2\x0c-"[\xa7\\j\x13\x859^\rynP\x15\x9c\xf3\x90\x00\xbd>\xb0\x99\xc1\xde\xfb\x8a\x98\x8f\xaca\xfb\x891\xecX\x8d\xc0\x06\x10\x04l\x1e\x18\\g\xc6\xcb\xe51\n1\xa4\x19\x84!*\x8aj\xca\xd4\xef\x02\xd6\xfe\xad\xe1\xe8\xee.\xf5\x1c\xbc\x1d$I\x0b8o1\xc6\x9f\x97\xbb\x08\x18\xa3\xc8\xb9c\xa6\x02\xaf\xbd*<\xf1\xf1\x1aC\x7f\xb3\x82\xd5\xa1\xc1\xd9\x04\xcd\x1dA\xad\n.gE\xa18hb\xaf1($I\x7f\xf3,\x97\xc44\xcd\x18=e\xd8\xfc\xed\x88\xfa_\xa6\x9c=\xea\xb0A\x01\xefC\x8cQ\xac\xf5X\xeb\tC\x8f1\xfd\x15\xe4\x16~\xfe`\xc0\xe3\x7f4B\xf5\xc7\x83h\xd5\xd1\x11\x8f\xa4)4[\xe0\x1d\xe49\xd6{k\xbaY\xd6\xc39\xc82P\x05k\x11@Qr\x94 \x81\xed\x8f\x15\xe8}\'\xa7g\xfb#F\x14k\x94 P\x82\xc0!&\xc7\x04\x9e\xd3g\xe0\xd9\xcf\xd7\xb8x\xa1@>\xe8hxE\x00\xd7\xeb\xf5\x1d[j@\x92\xe0\xbcs\xe6T\xaby\x86,\xefC\x0b1\x04\x967\xd7"\x05\x92@\xd1M\x1eQpN9g (\xc68\xac\xc9\xc1{V\xae\x86\xf0\x8a\x84\xa2\xc2\x98\x18\x82sE\xc5\xf7\xcb)^!\xcf9\x9d\xf4\x1af\xba\xd98B\xa7\x03Q\x04Q\x08\xaah\xbe\xbc\x10\xc0*\xd4k\x9e\xf0\xba\x90\xd0+Q\x98c\x8cb,\xc4%\xfa!7}\xfb0\x86M7\'\xfdm\xa4JY\xa0h\x0cA\xb1\x00\xc1rY0\x96\xd7\xd2\xe4\x84y\xba\xb1\xf4<G\x8f#\xad\x16$}\x11\xe0\xfdy\x8f%\x17\x167z*\x93\x01\x96\x948\xce\x88\xcbJ\xd7)/=\xa7\xf8B\x0e\xd1rh2\xd8\xb03#\xad8b5\x8c\x88\xa1(\x061\x16\x8c F \xcfx\xb2\xbe\xf8k\xf3d\xaf\xfd\xe8\x89\x99\x93\x8e\xa5&d\xae/.\xefA\xfbNg\xb9\'\xbbZ\x19(C\x1c\xa6\x94F\x13^?\xac<sO\x89\xa3\xb7Wy\xf4\x0beN\xce\xf7\xd5L\n#\x1b\x94dC\x8a\xcd\x84\xa2\x18"c\xc0\xe5\xfd]`\x0cg\x16\x16\xf4\xf1F\xfda\xd3P}\xfe?fO>\xc9\xe2"\x94K\xfd\xbc\xaa\xf6\x05\xaeJ]\x1c\xf1V\xc7`\xa9\x87\xaf4\xf9\xe5\xb7\x0c\x0bw\x0c3\xfe\xf3\x02\x15\x85\x81\x7f\xab\xf1\xb3\x9bF\xd9\xff\x88\xc5\x97\xa1R\x81\xe0\xbd]Z\x89\x90\x03*\x02q\x0c\xc6\x82\xf3\xfc`i\xf1\xe99\xef\xf6\x1b\x80o\xce\x9f\xf9\xbb\xf6\xcc\x0c\xd2h\x82\x11P\xf0\xdecsaa\xdcQ\xbd>\xe1\xc4\xf4i\x9e\xfbT\xcc\xea?_\xcd\xc4|H\x9a{\xf2\\05e\xfd\x89"\xb3\x9fX\xc9#_(s\xa6\x0e\x93\xbbz\xb4\n\x8e\xa2\x18L`\xd1\xb8\x80\x00i\xb7\xc7\xd7\xeb\xf3\xff\x00x\x0b\xb0\xe8\xdd\xe1(\xcb\xaf\xbd\xd1\xc6S\x9a\xa6h\x96\xe1\xf2\x9c\xbc\xa3\x1c\xfa\xc3\x05\xda\xf4H\xef\x1a\xe2\xd2\x03\x15\xa2AeI=-\xaf4UI\xe8\xeb\xa6b\r\xf1/K\x1c\xdf\x13\xd1\xbd\xae\x0b\x07b\xd6\x9f\x8d\t\xcb1R,"\xaa\xfc\xd3\xcc\xb1}\xbb\x9b\x8b_\x01\xfc\xf9f/\x12\xb9\xe8\xa7\x97l}\xe6\x86\xf2\xe0h\xd6l\xe2\xf2\x9cf/e\x7f\xa5\xc9\xb6\xc52CX\xba\x81\xc3\xa9\xd2q\x9e\xa6:\xea^\x99S\x8f\x05\xca"\x94\xc5P\xebY\x9aeGV\xf4\\\xdd+\x11\x0fU\x90b\x89\xe7\xe7\xcf6\xdfs\xf4\x95k[\xaa\x07\xe1M\xcd\x9e\x83\xfa\x13\x8d\xfa\xc1[\xa2\xc2m\xa3b\xac\xa3\x1f\xf5\xc9NDh\x05g\xfb[Q\x15\xfa\xad\x8bP\x10(-\x7f\x87"\x141\x94#\x98 d\x9d\x0b\xd1( \xb2\x013\x8d%\xbdu\xe6\xf5;O:\xf7\xf89\xde[\x9a\xbdE\xe7^\xd9\xdbj\xbe\xfa\x81B\xf9\x961c\x82L\x15o\xc0-\x9f\x18\x82 \xcb]\x895\x82A\x08\x80\xa2\x18\nb(\x8bP5\x06k\xc0\tTl\xc0t\xd2u\xb7\xce\x1e\xbb\xeb\x85,\xfd\xee\x9bY\xbf\xd7\xde\xceyw\xe0\xa1v\xe3\xa9K\x83\xe8\xc6-Q\\\xb5"\xb8e\xa5\x8b\x08Fdy\x11\xfd\xab\xce\xb9\xc6-\x14\xa1l\x0c\x05c\x88\x8d!Bx"\xe9\x9c\xbamn\xe6\x93\x07\xf3\xf4\x81\xb7s~\x0f\x0c\xd0T\x7f\xe4\xbf\xda\x8d\xef\x9f\xcc\xf3\xc1\xcb\xc2h\xdbx\x18\xd9\xd8\x08"r\x1e\x1e\x18C \xfd\x10\x17\xaca\xc0ZjA@)\x089\x9ag\xfe\xbe\xe6\xfc\xee/\xd5\xe7>=\xef\xdd\xfe\x0b1.x\x93\xb0\xfd\x9c\x030l\xcc\x8e;\x06\xaa\x9f\xfbx\xa9\xf2\xc1\xcb\xc2h|\xd8Z\x0cBN\xff\xcc6\x00(\xf3\xceq\xd8e\xb3\x0fv\x9a?\xd9\xdd\\\xfa\xda\x9cwO\x9d\x03\xe8\x05\x18\xef\x08\xf6\xf4\'\xd5\xe5\xef\x92\x98\xd5\x9b\xc2h\xfb\x1a\x1b\\sm\\\x98\xd8\x11\x15\x02\x83\xf0\\\xdau\xbfJz\xc7g\\\xbe\xffH\x9e\xfdv\xd1\xbb\x93\xf4\xed\xe9\xa9G\xdf\x01\xfc\xff\xebKj\xac\xe04\xa1\xb7\x00\x00\x00\x00IEND\xaeB`\x82'))
a.wm_iconphoto(False,PhotoImage(c78))
u=1
c=Menu(a)
b=Menu(c,tearoff=False)
d47,d50=[[]],0
def a91():
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
    aa=[b1,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32]
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
        Button(b02,text=b03[b18],bg=b07[b18],font=(None,b08[b18]),command=aa[b18]).place(x=b04[b18*2],y=b04[b18*2+1],width=b05[b18],height=b06[b18])
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
    if a16.cget('text')=='load':
        a28.clear()
        a29()
    b36()
    a27.place(x=40*u,y=40*u,width=270*u,height=250*u)
    a11.place(x=350*u,y=50*u,width=50*u,height=25*u)
    a14.place(x=350*u,y=100*u,width=50*u,height=25*u)
    a16.place(x=350*u,y=150*u,width=50*u,height=25*u)
    a16.config(text='next',state=DISABLED,command=d45)
    a18.place(x=350*u,y=200*u,width=50*u,height=25*u)
    a20.place(x=350*u,y=250*u,width=50*u,height=25*u)
    a22.place(x=420*u,y=50*u,width=50*u,height=25*u)
    a24.place(x=420*u,y=100*u,width=50*u,height=25*u)
    a26.place(x=420*u,y=150*u,width=50*u,height=25*u)
    a00.place(x=420*u,y=200*u,width=50*u,height=25*u)
    b75.place(x=420*u,y=250*u,width=50*u,height=25*u)
    c75.place(x=490*u,y=50*u,width=50*u,height=25*u)
    d27.place(x=490*u,y=100*u,width=50*u,height=25*u)
def d45():
    pass
def b76():
    try:
        b77,b78=[askdirectory()],0
        while len(b77)!=b78:
            for i in scandir(b77[b78]):
                if isfile(i.path):
                    a28.append(i.path)
                else:
                    b77.append(i.path)
            b78+=1
        a29()
    except:
        pass
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
        if a16.cget('text')=='load':
            a27.insert('end',i)
        else:
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
    if a16.cget('text')=='load':
        a28.append(simpledialog.askstring('input link','enter youtube link',parent=a).split('//',1)[-1])
    else:
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
def d17():
    try:
        for i in a28:
            if i.endswith(a27.selection_get()):
                s=0
                while True:
                    try:
                        mkdir(str(s))
                        break
                    except:
                        s+=1
                copy(i,str(s))
                make_archive(i if '/'in i.rsplit('.',1)[1]else i.rsplit('.',1)[0],'zip' if d23.get()=='archive format'else d23.get(),str(s))
                rmtree(str(s))
                return False
    except:
        if d21.get():
            s=0
            while True:
                try:
                    mkdir(str(s))
                    break
                except:
                    s+=1
            for i in a28:
                copy(i,str(s))
            make_archive(str(s),'zip'if d23.get()=='archive format'else d23.get(),str(s))
            rmtree(str(s))
        else:
            for i in a28:
                s=0
                while True:
                    try:
                        mkdir(str(s))
                        break
                    except:
                        s+=1
                copy(i,str(s))
                make_archive(i if '/'in i.rsplit('.',1)[1]else i.rsplit('.',1)[0],'zip' if d23.get()=='archive format'else d23.get(),str(s))
                rmtree(str(s))
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
    op('https://twitter.com/_Frost_Dream_')
def a05():
    b36()
    a06.place(x=120*u,y=40*u)
    a07.place(x=120*u,y=130*u)
    a08.place(x=118*u,y=190*u)
    a09.place(x=125*u,y=250*u)
    a30.place(x=235*u,y=130*u)
    b54.place(x=237*u,y=190*u)
    d12.place(x=237*u,y=250*u)
    d34.place(x=350*u,y=130*u)
    d36.place(x=348*u,y=190*u)
def d35(s):
    op('https://www.quora.com/profile/Frost-Dream')
def d37(s):
    op('https://github.com/frost-dream')
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
        s[randint(0,10)].set(abs(s[randint(0,10)].get()-1))
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
        a59='1'+a87+format(abs(a59),'b')
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
        a.geometry('780x445+550+260')
        c.add_cascade(label='cache',menu=b)
        c.delete('cache')
        u=4/3
        if not bb:
            c6()
            a.geometry('780x445+535+260')
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
    b77=display.set_mode((a.winfo_screenwidth()*windll.shcore.GetScaleFactorForDevice(0)//100,a.winfo_screenheight()*windll.shcore.GetScaleFactorForDevice(0)//100),FULLSCREEN)
    while c14:
        sleep(.00001)
        b77.fill((0,0,0))
        draw.rect(b77,(255,0,0),(randint(0,a.winfo_screenwidth()*windll.shcore.GetScaleFactorForDevice(0)//100),randint(0,a.winfo_screenheight()*windll.shcore.GetScaleFactorForDevice(0)//100),randint(0,30),randint(0,30)))
        draw.rect(b77,(0,0,255),(randint(0,a.winfo_screenwidth()*windll.shcore.GetScaleFactorForDevice(0)//100),randint(0,a.winfo_screenheight()*windll.shcore.GetScaleFactorForDevice(0)//100),randint(0,30),randint(0,30)))
        draw.rect(b77,(0,255,0),(randint(0,a.winfo_screenwidth()*windll.shcore.GetScaleFactorForDevice(0)//100),randint(0,a.winfo_screenheight()*windll.shcore.GetScaleFactorForDevice(0)//100),randint(0,30),randint(0,30)))
        display.update()
def d33():
    if not b87:
        return False
    global b79,c14
    b79=time()
    c14=False
    b81.withdraw()
    display.quit
    quit()
    bye()
    return True
def b80():
    def b94(key7):
        return d33()
    s=li(on_press=b94)
    s.start()
def b82():
    def b83(key1,key2,key3,key4):
        return d33()
    def b84(key5,key6):
        return d33()
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
            if time()-b79<int(b92.get())and time()-b79<int(b91.get()):
                b81.withdraw()
                display.quit
                quit()
                bye()
        except:
            pass
        try:
            if b92.get()=='':
                r=True
            else:
                r=time()-b79<int(b92.get())
            if time()-b79>int(b91.get())and r:
                if c17.get():
                    c14=True
                    s=Thread(target=b52())
                    s.start()
                elif c18.get():
                    s=Thread(target=c15)
                    s.start()
                elif c20.get():
                    pass
        except:
            b91.delete(len(b91.get())-1,'end')
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
    if b87:
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
        while b87:
            a.update()
            try:
                if time()-b79>int(b92.get()):
                    b81.config(bg='black')
                    b81.lift()
            except:
                b92.delete(len(b92.get())-1,'end')
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
def bk(s):
    if u==1:
        s=Controller().position[0]-639
        cast(AudioUtilities.GetSpeakers().Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL,None),POINTER(IAudioEndpointVolume)).SetMasterVolumeLevelScalar(s/329,None)
        bj.place(width=cast(AudioUtilities.GetSpeakers().Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None), POINTER(IAudioEndpointVolume)).GetMasterVolumeLevelScalar()*329)
    else:
        s=Controller().position[0]-825
        cast(AudioUtilities.GetSpeakers().Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL,None),POINTER(IAudioEndpointVolume)).SetMasterVolumeLevelScalar(s/440,None)
def bn(s):
    if u==1:
        s=Controller().position[0]-639
        custom(s/3.29)
        bm.place(width=get_brightness()[0]*3.29)
    else:
        s=Controller().position[0]-825
        custom(s/4.40)
def c10():
    global get_brightness,custom,bl,bm,CLSCTX_ALL,AudioUtilities,IAudioEndpointVolume,POINTER,cast,bj,bi,bh,bf,simpledialog,YouTube,concatenate_videoclips,ffmpeg_extract_audio,ffmpeg_movie_from_frames,ffmpeg_resize,time,bgcolor,clear,begin_fill,circle,getcanvas,pensize,hideturtle,speed,colormode,setup,fd,right,color,end_fill,goto,penup,pendown,recycle_bin,_exit,d55,d49,isfile,quit,Timer,factorial,init,copy,make_archive,rmtree,extract_archive,li,lis,Controller,draw,display,FULLSCREEN,VideoFileClip,remove,rename,scandir,rmdir,mkdir,sqrt,sin,cos,tan,log,radians,ceil,log10,urlopen,askopenfilenames,askopenfilename,asksaveasfile,askdirectory,Icon,MenuItem,choice,op,grab,VideoCapture,CAP_PROP_FPS,VideoWriter,VideoWriter_fourcc,cvtColor,COLOR_RGB2BGR,array,bye,MessageBeep,Beep,send2trash,askcolor,Image,ImageTk,ffmpeg_extract_subclip,ffmpeg_merge_video_audio,showerror,showinfo,askyesno,askyesnocancel,notification
    from shutil import copy,make_archive,rmtree
    from os.path import isfile
    from threading import Timer
    from patoolib import extract_archive
    from winshell import recycle_bin
    from pynput.keyboard import Listener as li
    from pynput.mouse import Listener as lis,Controller
    from ctypes import POINTER,cast
    from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
    from comtypes import CLSCTX_ALL
    from pygame import draw,init,display,FULLSCREEN,quit
    from pytube import YouTube
    from pybrightness import custom
    from screen_brightness_control import get_brightness
    from pygame.mixer import Sound,stop
    from os import remove,rename,scandir,rmdir,mkdir,_exit
    from math import ceil,log10,factorial,sqrt,sin,cos,tan,log,radians
    from moviepy.editor import concatenate_videoclips,VideoFileClip
    from urllib.request import urlopen
    from tkinter.filedialog import askopenfilenames,askopenfilename,asksaveasfile,askdirectory
    from time import time
    from tkinter import simpledialog
    from pystray import Icon,MenuItem
    from random import choice
    from webbrowser import open as op
    from PIL.ImageGrab import grab
    from cv2 import VideoCapture,CAP_PROP_FPS,VideoWriter,VideoWriter_fourcc,cvtColor,COLOR_RGB2BGR
    from numpy import array
    from turtle import bye,pendown,goto,penup,end_fill,fd,right,color,speed,colormode,setup,getcanvas,pensize,hideturtle,bgcolor,clear,begin_fill,circle
    from winsound import MessageBeep,Beep
    from send2trash import send2trash
    from tkinter.colorchooser import askcolor
    from PIL import Image,ImageTk
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip,ffmpeg_merge_video_audio,ffmpeg_extract_audio,ffmpeg_movie_from_frames,ffmpeg_resize
    from tkinter.messagebox import showerror,showinfo,askyesno,askyesnocancel
    from plyer import notification
    c9,d55=c8.get(),False
    be,bg=PhotoImage(ope(BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02X\x00\x00\x01^\x08\x02\x00\x00\x00\xd6\xb5\xf6\x0b\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x18\xd9IDATx\x9c\xed\xddi\x9c\x1du\x9d\xa8\xf1\xa7\xf7\xd3k:\x0b\xa4\x93@\x12\x12\x91E\xb6\x89\x82\xc3rEVEP@\xe7\xe3\x86\xa0\xa0" \x08sq\x06e\x94q\xc5\xf1\xaa\xe3\xa8\xa8#2\\q\xc4\x01\xc6\x11F\x88(\x02\xb2j\x10\x10\x10C\x08$$d!\x0b\xe9t\xd2\xdd\xe9\xd3\xdb9}_\x14u\xa8\xee\x93db.t7\xfc\x9e\xef\x0b>\xffS\xa7\xba\xaa\xda\x17y\xac\xaa\x7fUW\xc0\x10\x0c\x01\x15\x99\xff\x8e\xf8\xf8\xf2,\xc4\xfd\xba_\xf7\xeb~\xdd\xaf\xfb\x1d\xf3\xfdV"IR`\x86P\x92\x14\x9a!\x94$\x85f\x08%I\xa1\x19BIRh\x86P\x92\x14\x9a!\x94$\x85f\x08%I\xa1\x19BIRh\x86P\x92\x14\x9a!\x94$\x85f\x08%I\xa1\x19BIRh\x86P\x92\x14\x9a!\x94$\x85f\x08%I\xa1\x19BIRh\x86P\x92\x14\x9a!\x94$\x85f\x08%I\xa1\x19BIRh\x86P\x92\x14\x9a!\x94$\x85f\x08%I\xa1\x19BIRh\x86P\x92\x14\x9a!\x94$\x85f\x08%I\xa1\x19BIRh\x86P\x92\x14\x9a!\x94$\x85f\x08%I\xa1\x19BIRh\x86P\x92\x14\xda\x18\x84p\x88\x9e\xcd\x1c\xbc\x99\x0f\x8f\xfe\xae\xb7/\xcf\xe2\xa7\xd8\xfb)\xf6\x1e\xa4}\xac\x8fE\x924J\xc6 \x84\x03<>\xc4\xd2"7\x0e\xb0\xf0%\xdcl\x17\xb7\xacb\xe6\x16\xee\xde\xe9-\xb4s]2\xa8\xa4\xe1%:(I\xd2x7\x06!,\xb0\xe6e\xd8\xe6\x86\xcd\x9c\x07l\xe4\x8c"=;\xb1\x85"\xf9<?\x05j9\xa1\x92\xfa\x1d\xfc\xa9\xe5|y!\'\r\xb0q\'\xf6(I\x1a\x0f\xc6$\x84O$\x83j\xf6x\xa9\xb6\xd9\xcb\x9f\x93A\x05{\xec\xdc\xf9\\\x9eE\xc9\xa0\x99\xc3v\xf0G\x8a\xe4\xbb\xb8\xa1\xc8\xcaN\x1e\xda\x89=J\x92\xc6\x83\xea\xd1\xdfe\x81\x1b\x81JN\xadx\xe9\xae@\xe6\xd8\xaf\x82=*i\x9b\xcc?\xee\xdc\x16zY\x9anj\xee\x0e\xfeHa\xa7N=%I\xe3\xcah\x87p\x90\xe5C,\x05\xaay\xf3K\xb8\xd9*\xa6\xcc\xe0n\xa0\x82\xa1\x9d\xdbB7\xf7\'\x83z\xf6\xd9\xc1\x1f)\x92O\x06\xb5\xec\xbas;\x95$\x8d\xb9\xd1\xbe4:\xc0\xa3\xc9\xa0\x9a\xd7\x8e\xf2\xae\xb7\xa3H\xbe\x9f[\xf9\x0bo\x10nI\'\xfb4\xb2\xd7\xcbud\x92\xa4\x97\xd9h\x9f\x11\x16X\x08T0\xb7\x96\xfdGy\xd7\xdbQ\xbaA\xd8\xca\xf1;\xfeS}\xac\x05r\x1c_I=\xff\xd3\x99h/\xab\x16rJ-\xf3^\xc77\xab\xa8\xdf\xccc\xeb\xf9\xf5&\xfe\x0b\x98\xc6\x053y\xff\xce\x1e\xfb\x8b\xbaX\xba\x86\xbbWs-\xd0\xca\x9b\xf6\xe1#\rL\x1b\xb1N\'\xcf\xac\xe6\x9e\x95\\\x07L\xe2\x88\xd7qfc\xd9:\x92\x14\xcah\x9f\x11\x16\xb9\x11\xa8\xda\xb1\x1b\x84\x9b\xf9\xfez\xdaz\xf8-\xd0\xcf\x13\x1b\xb8t-\xd3\xd7rD\xb2\xa4d\x0bw\xadb\xe6Z>\xbe\xed\xed\xcc\x7f\x96\xa3\x971w\x19sW\xf2\x89~V\x8cX\xa1\x8f%\xc9\xa0\x9e\xfdv\xfcw\xd9\xc2\x9f\x81\t\x1c\x9a|\xec\xe2\xd1vn{\x8c\xbfz\x94y\xe5\xf3H\xd7\xf2\x0b\xa0\xc0\xfa\x016.\xe1\xabOqvRA`\r\xdfy\x8e\xff\xde\xf1\xfdn\xd52\xae\x7f\x88\xb3\x93\n\x02\x9b\xb8\xe7I\xae\x1a\xb1\xceR\xfes\x01\xe7\xadL\x9f\x12\xd9\xc8}\x0b\xf9\xbf\xff\x9f\xfb\x95\xa4W\xbaQ=#\xec\xe7\x81\xe4\x06a\x15\xfb\x02\x83,\xef\xe3\xde~.J\xbem\xe0\xfaz\x8e\xce\xae?\xc0\xed\xc0\x10]\xdd\xdc\xbc\x85\xb3\x93\x85C,\xdb\xcc\x07\x8a\xfck3\'%K\xba\xb9\x01(\xa4\x13G\x87\xefq\xc5z.)\xb0 \xb3\xcd\xf9\xeb\x18\xda\x9dogW\xeb\xe6w@%\xb3\xea\xd8}\x07\x7f\x97"\xf9^~\r\xf4\xb0\xe8i\xfe\xae\x97\xdb\xb2\xdf\xf6\xb2\xa2\x86I\xa5\x8f\x05\xf2\xed\\\r4\xf1\xd7\x8b\xb8\xa0\xc0\xaa\x11[\xeb\xe0\xc1\xe9\x9c\\\xbe\x97\x02\xf9v~\xb7\x8c+\x0b\xac\x06\xda8}\x16\xef\xaae\xe2\xf0\xdf\xb1\xe3Q>\x97\xe7O\xdb9\xda>:\xfe\xc8\x97\xb6\xf0\xf8\x0e\xfev\x92\x14\xc7\xa8\x86p\x90\xa7\x92A\r\x07u\xf3\xdd\x01>\x9b\xfd\xb6\x87\xf7TqW\x1d\xfb\x96\x96\x14\xb9\x1f\xc8sM1\x9d\xc9R\xd2\xcdW\x93\x10\x16\xe9\x19\xe4f\xa0\x9e\xd3F\xac\xd3\xcf\x8a\xb5|p\x88\xe5\xc0D\xbe\xd3\xca\xdb\x9e\xe5\x98"\xcb\x8b\xc3_\x1cS$\xdf\xcf/\x81\x06\xdeVZ\x98g\xf1\x16\xfe\xd4\xcee@5\x07\xcf\xe5\xfbU\xe4\x80\x01\xda\x9f\xe6\xc8\xec\x8fwq\xc3\x88\xfd\xee\xcaE\xcd\x1c\x94]\xd2\xc1}\xc9`3?K\x06\xd3\xf8\xc44\xdeYE\xfd\x1fyW\x81U[}\x12\xb1\x9d\x05\x8b\xf9dv\xc9Z\xfe}\x13\x7f:xx\xc5\x9f\xe0\xdbI\x05\xeb9`\x16\'O\xe3\xcdE\xf2K\xf8iK\xe6\xe9\x94?\xf3\xdd\xa4\x82\x8d\xec?\x9b\x93fpd\x91\xfcS\\7\xe1\xa5{\x82E\x92^\xa1F5\x84\x05\xeeJ\x06=|1\xb9F:B?\x8f\x94B8\x94>\x9c\x90T\xb0\x8a\x93[\xb8\xa0\x8e}\xdb\xf9\xf4\x00\xd7\x0c\xb1,\xf9\xb6/}*\xb1\x9ey\xd9M\r\xb2!\xa9`\x05\xb3\xa7\xf2\xbd\x1c{\x97n\xe3\xe5x}v\xcd\xd2\r\xc2z\xf6\x02\x06i_\xcb\x15=\xfcGfS\x0fv\xf1p+\x87\x03=\xe9\xca\xe5\xda\xb8\xac\x9a\xc6\xc9\x1c_>su\x03w\x94\xc6\xb5\xcc\x9b\xcb\xc5M\xbc\xa6\xb4\xd3nV\xb5p\xe0\x88\x1fY\xcf\x1dK\xb9\xac|/\xbd<\xd6OG\x1d\xad\xc9\xc7\xb5\xfcv3w\x01s\xb9xf\x1a\xf2*r{qV\xe90\x9e\xe3\xee\x0e\xee\x01^\xcbE\xb3yki\x9d}\xf8\xd0NO\xb2\x95\xa4W\x8d\xd1\x0b\xe1\x10=E~\x9e\x8c\x93\nVsq-\xc7\xe48d\x88\x9e\x0ef\x02Ct\x96\xd6\x1f`y\xe6(?4\x99\xaf$\xffjO\xe0c\xed\xdcS\xc7\xe9\xc9W\xfd<\x9d\x0c\xb2\xa7\x92\xc0z>\x97T\xb0\x8dk\x92\x0b\x9e=<\\d9P\xc3n\xd95K7\x08\x1b\xd8/\xcf\xe2\xd5|\xa2\xc8\xb3#\x0e>\xc7\xacd0\x81#z\xb9\xb8\x9do\xa4\xcb\x8f\x9f\xc4qM\xec\x9bc\x06\xdbxx\xa3\x97U=\xdc\x9e\xfe\xf8\xdf\xcc\xe1\x82\xaatrM\x81|7w\x00\xa5.\xa6\x07\xffB\x05\xab\x98\xb1\x07gO\xe5h\xe0I\xbe\xd1\xceM@\xd5\xd6\xe6\xb5\xb6\xb2w\xf9\xc2\x11&:\xbbU\x92\xca\x8c^\x08\xfb\xf9}i\\\xc9\xa9\r\xfc\xef\x9a\x17\xd25T`}\xb2\xbc\x8a\x19\xa5u\x06\xd2>Uq\xf2d\xbeRZ^\xc3\xac\xb6\x17\xae4\x0e\x01\xbd\xdc\x0bT\xf3\xf6\xec\x0be:\x99?\xc8-@\x1b\xd7\xd423Ys#\xd7\xa4[h\xcb\x1eX\xe9\x06a\x81\x9eU\x9c\x0cTs\xc8T.lb\xdeb\xf6\x01\xeaxk\x1d\xbb\x97N(\xdb\xf8P\x13\x07>\xcb\x19@\x1b\xa7\xa5WA\xb7yj\xb5)}\xef\xcc\x0c\xfe\xa1\x8dS\xb2\xb1\xdc\x9c>L\xd2\x9c\xc9X\x9e\xd5I\x05\'q\xca\x9e|\xbcH~\x1dwv\xf0HR\xc1i\x9c^E\xae\xb4\xbbFf&\x83\x87\xf9\xe8\x0cN\x9b\xc6\x91\xcde/\x04hJo|>\xc0\xb9\xbb\xf3\xde\x19\xbc\xa9\x859\xdb:ZI\x8af\xf4B8\x98\xceX\xa9\xe3\xeazN\xa9\x80\xd2\xbf\xe6\xfd<\x96~\xf5\xe2\xeb\xcd\x06\xd2k\x9e\xad|y[\xdb,\xdd \xccqDv\xe1f\xbe\x06L\xe4\x8a\xda\xb4\x13\x9b\x99?\xc0\xfct/\xb33+\xbfp\x83\xb0\x92\xa9\xabx\x07\xd0\xcc9\xd3\xb9\x10\xe8ce\xb2\xceD\x8e\x1b\xb1\xdf<\xcf$\x83\x1dy\x82p\x03\xb7\x02\x8d\x1c\xdb\xc6)#\xbej\xe7^\xa0\x89c\xea\xd3\xff\x07\xd0\xcd\x92E|:\x19o\xe4\xa6\x07\xb8)\xbb~\x0bG\xed\xc1\x07\xb2K\x9a\x99\xbb\x17\x97-\xe6\x0b\xc0j\xae]\xcd\xb5\xbb\xf2\xf69\xbc;\xfb\xe0D\x0bs\xf6\xe5\x1f\x9e\xe0\xcb\xc0J\xae[\xc9um\x9c\xf8\x1a\xde\xe5\x83\x13\x92\xc4h>>\x91\\\x17\xad\xe2\x93\xf5\xc3{P\xe0\xf9>.\x07\xaa8\xab\x8a]2\xcb\xff\x00Tqr\x15S\xb6\xb5\xcd-\xdc\x99\x0c\xea\xd8\xb3\xb4\xb0\x9b;\x93\x8b\xa2-\x9c\x98,\xe9gE\x07\x17\x94V\xa8\xcel\xb0t\x83p\x90?\x00\xad\xfc\xfd\xb4t\x16kWZ\xee\t\xc3g\xc7\x00\x9d\xfc\x1e\xc8\xf1\x96\xf2\xa7\xef\x9f\xe2\x92u\x99\xdb\x9f\xbd\xac\xea\xe7a`2\xc7\x8cX\xb3\x9f\x8d\xc9\x13\x14S8\xaa\xb4p9?J&\x88\x8eP\xc5\x8c=\xf9\xdc\x01|>\x99\xb3\x93\xd5\xc6Q\xaf\xe7\x87\xd3\xd3\xb9B\xeb\xb9y\x01\xa7\xf7\xd1\x91]g:G\xbe\x91\xef\xef\xce{\x93\x8fk\x99\x7f\x1fg\xf5\xb1\xa9|G\x92\x14\xcd(\x9d\x11\x16\xd27\xab\xd5rlv\xf9\x10=]\\\x9a|\xd5\x9c\x99!9DO2G&\x97\xc6l\xab\xfa\xd3\x8ceo\x10\xf6\xf1$\xd0\xcc9\xc9\xc7^\x16\xad\xe7\xbc\xd2\xb75\x9c\x98\xbd\x88Z\xbaA\x084q\xee\xae\x9cU\xfa\xd8\xc1\xbf\x01\r\xbc\xaf\xbcv\xc9~\x1b\xcb\x1e:|\x8e\x1f\xe7\xb9m*\xef(-\xe9N\x8fpR\xe6\x9c5\x91\x9c\x0e\x02\xad\xc3\xa7\xf9dM\xe5\x8cf\xe662\xb3\x89\xd7lgbK3s\x9b\x99;\x9bS\x97p\xcdzn\x06:y:\xc7\xc1\xd9uZ\x98\xd3\xc2\x9c9\x9c\xb2\x98\x7f_\xcb|`\x13K\xda\x86\xcf\x1b\x92\xa4\x80F\xe9\x8c0y\xb3Z\x05sk2/\x94\x19`a\'\xefK&\xce\xd4sU\xf6t\xb0/}(\xb0\xb6l:eV?\xbf\xa0\xec\x06a\x1f\xb7\x94\xc6\x1d\\\xbf\x8e\xb7\re\xe6\xdd\xd4f\xae\x8b\x92\xde \x04\xaa9\xa4t.\x08\xe4Y\x9cL\x99i\x1e\x9e\x93D\x91\x15@5M\xd9\x85+\xb9\xe2y\xbeY\xc3\xeb[3\x17x\xdb\xb9\x03h\xe0\xd8\x113\\\n\xe4\xd7\xf0c`"\xef\xac\xcd<q8-}8\xf2 n8\x8c\xfb\xe6r\xf6T\x8e.M\xa5Y\xc7\x9d\xf7r\xe4\xda\xe1\xef\x13(\xa9c\xe2\x1e\xbc;\x1dO\xde\xc6:\xads\xf9\x9bd\x9c\xcb\xecW\x92\xc2\x1a\xb53\xc2\x85@%GU\xd0\x00C\x03,\xec\xe3\xbf\x07\xf9z\xf2m\r_h\x18\xfe8y\x81\xb5@\x05sj\xd2\xe9\x9a\xe5\x06x6y\x88"\xc7\xff*\xff\xb6\x93Ou\xf2\xa9\xd2\xc7:>\xd0\xc7O\x80\\fZJ\x91\x9e\xe4\x06!0\x83\xcb\x87\xff\xf8\xef\xd2c\xdb\xe6\x0b\xb5\xdb\x99?\x85\x13*\xa9\xef\xe2\xd1\xd5|g\x80\x87\x80\xe9\x9c\x99\xf9-\xf2=\xfc\x06h\xe5\xafG\xfcl7O%\x8f\xd5O\x1e~\xf0\x05\xb6$\x83.\x9el`z\xba\xf2\x92\xcd,Z\xce\xffI>\xe6\xb6v\xadx\rw\x15\xe8^\xc2?\x03\r\x1c\xd0\xc2\xdc\xf2\xf9;\xcfq\xf7 [\x16\xf3-\xa0\x91\xfd&0\xe7\x7f|3\x9c$\xbd\xea\x8dR\x08K\x0fN\xe4\xb9i\x80/\r\xa5\x7f\xf3\x08\xc8\xf1o\r\x9c<\xe2_\xe4d\xa6LU\xd9\xcd\xb9\xac\xde\xf4=)\xb5\x99\x1b\x84@\x0b\x9f\xdc\x9cy\xddZ\x05\xb3w\xe1k},\xe9\x03\x86\xbfD\xadt\x83p\x02\x97\xd4\x0e\x7f\xa7L\'\xd7\'\x83\x9a\xccyjI\x13\xef\xe9\xe6\xfaA\x1eZ8\xbcp\x13\xf9H+\x87\x97~\x97\xde\xf4\r2\re\xcf\xadoL\xe7\xd0N\x18\xfe\xe8}\xc9R.\xdb\xeas\x84S8\xb9\x95\xfda\xa8@\xef\x02\xce*\xf0\\\xf9:\xfb\xa6\xbf~\x81\xde\xfb8{pk\x7f\ty\x7f\xce\xdd\xea~%)\x9aQ\naR\xbe\x02W\x152/\xc0\xac\xe4\xd4\x06\xfe\xb6v\xf8\xf3\x7f\x89t\xa6\xcc\xcc\xedls\x90\xd5@\x05{\xd4\xf3\x86lG[8\xa9\x8a\xa6\x8d|\x10h\xe1\x9f&\xf0\xf6*\xea;\xf8\x11P\xc9\xec\xd2\xd3\x14@_\xda\xe3\x89\xc3\xe7\xef\x0c\xd2^z\x94\xb0fk\xa7_m|hIZ\xca\x92\x89|d\xe6\xf0\xf7\x9d\xf6\xf3|2\xa8-\xbbP\xd9\xc9c\xc0\x14\xce\x1cq\xc9t2\x87\xad\xe6\xaf\xfaxd\xab\xbf\xf2\xde|m\x17\x0e\xd9\xeaW\x89\x19\x9c6\x8bSs\xe9\xe3\xf6[\xb5;\xef\x9d\xc3)9&lg\x1dI\x8ac\x94BX\xc5\xdf\x15\xf8Z%\xef\x1c\xe2\xb1!\x96Vrj\x1d\xef\xcf\xbd\xf0f\xd1\xad\\\x9d\xab\xe1\xb8>\xee\xaf\xce<VX\xae\x89\xb7\xf6\xf2\x93\xfa\xe1\x8f\x13\xa4_\x1d\xd9\xc4\xf2\x8a\x17\x1f\xcfx6yv\xa2%}ai\xba\x976`\x12_\xaafr\xf60\xaa\x99\\\xc7\t}\xdc:\x85/l\xf5/K\xd4\xb1\xdb\x1c~\xf6\x1c?L^7Z\xc3\x1bv\xe3\xfcf\x0e\x1a\xb1f=3\x81\x06\x8e\xcd\r\x7f\x84\x1f\xa8ab?\xecZ6\x95\xb4\x8a\xfa\x03\xf8\xfaF\xee_\xce\x0fJ\xd3G\xdb8\xa3\x89\xb9m/L.\x1dJ\xd7\xcc\x1d\xc0\x17\x9f\xe4\xdby\x1e\xabf\xfa\\>\xd2\xca\x9e\xe9\xd5\xd4\x17\xd7\x99\xc7\xe7\xfe\xcc\x15=<^\xcd\xb4\xbd8\xb3\x95=\xd3\xa7&\xbc(*I\x00\x150\x94\xfc\x9bX\x91\xf9\xef\x88\x8f/\xcfBFm\xbf\xed\xfc\xb0\x9b\xcb\x81i\xcc\xafO\xdf\xb5\xf6*\xfe}\xdd\xaf\xfbu\xbf\xee\xd7\xfd\xee\xf8\xc2\xd1\xfe3L\xa3\xaf\x9f\x15I\x05\xeb\xf8@n\x07\xdeC&I\n\xe5U\x1e\xc2A6\xac\xe7\x92d<\x89\xf7\x8d\xed\xc1H\x92\xc6\xa1\xd1\xfe\x0b\xf5\xa3\xa6\x93\xf9\x15\x0cm\xe2\xeb\xc9C\x84M\\\xea\xe9\xa0$\xa9\xdc\xab0\x84\x83lX3\xfc\x85)5\x9c8\x89\xf7\x8f\xd5\xf1H\x92\xc6\xb3Wa\x08\xbb\xd3\xbfy\x94\xa8\xe7\xfc]8\xa7\x92\x06\xe7IJ\x92\xca\xbd\nCX\x99\xbe\xf9\xac\x89K\x1b9"\xc7>\x15&P\x92\xb4\r\xaf\xc2\x10\xb6p\xd2\x04N$3MV\x92\xa4my\x95\xcf\x1a\x95$i\xfb\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10\x8e\x99\xe7\xb9\xfdA\xde\xb8\x8c\x7f\x1d\xeb\x03\x91\xa4\xd0\x0c\xe1\x98y\x9e;\x81\x8d\xdc>\xd6\x07"I\xa1\x19\xc2\xb1Q \xbf\x85;\x80I\x1c;\xd6\xc7"I\xa1\x19\xc2\xb1\xd1\xcdS\xc9\xa0\x91\xd7\x8c\xed\x91HRp\x86pll\xe4\xf7\xc9\xa0\x99}\xc6\xf6H$)8C86:\xf8\rP\xc5n\xf5\xcc\x18\xebc\x91\xa4\xd0\x0c\xe1\x18\xe8eu\x81U\xc0D\x8e\x1b\xebc\x91\xa4\xe8\x0c\xe1\x18\xe8bQ2\xc81ml\x8fD\x92\xf4J\na77\xaf\xe3\x885\xccX\xc3\x8cnn\xde\xce\x9a=<\xf4<\xdfx\x96=\x9ee\x8fN\xe6\xffE{\xc9\xb3x1\xfb,\xe5\x83E\xf2#\xbe\xeac\xe5\x13\xec\xb7\x98\xb3\x92\xaf\xbaxd9_~\x9c\x03\x1f\xe7\xc0\xe7\xf8\xf1\x8e\xefb\x03w&\x83\x06f\xffE\xc7&Iz\xc9U\x8f\xf5\x01\xec\x90~\x9e\xd8\xcceE\xee/-\xe9\xe2\x9cjn\xac\xe7\xe0\x11k\x0e\xb0b\x03_\x1d\xe4\x96\xd2\x92\x0e\xce/\xf2\x95\x89\xbc\'\xbbZ\x91\x9e\x95|\xb4\xc0\x03S\xf8V+\'d\xbf\xea\xe1O\xc0 \x7f\xe8cE\x03\xaf\xcd~\xb5\x81\x1b\x81"\xeb\x06h_\xc9\x8f\xba\xb9>\xf3\xd5?W\xd34\x95S\xb7z\xfc[xz\x13\x0b\xd6\xf1-\xa0\x96y\xfd\xfc1Y\xde4|\xfb\x92\xa4\xd1\xf7\n\x08\xe1\x16~\xb1\x85\xb3wl\xcd\xbb:8\xa3|\xf9f>\xdd\xcc15L.-\xe9eQ\x81\x07\x80"]#V\xee\xe2w\xc9\xa0\x92\x86\xec\xf2"\xf9\xcd\\\t4p\xe83|\xac\xc8\x8a\xb2\xbd,(\x0fa\x81\xfcj\xaen\xe7\xea\xd2\x92R\x05\x1b9\xa6\x8az\x18\xda\x91_M\x92\xf42\x19\xef\x97F{y\xb0T\xc1\x1c\x97M\xe4\xf6i\xac\x9e\xc8MU\xbc\xa3\x8e\xd7e\xd7\xec\xe2\x96l\x05+\x98=\x91+\x9a\xb84\xfd\xf6\x8e\xe1\x9b]\x9a\x0c\xea\x86?\xc6W$\xdf\xcf\xad\xc9\xb8\x86)\xd9\xaf6qO2\xe8\xe6\xfa\xa4\x82\x93\xb9\xf8u,\xd8\x9f\xc7*\xd9\x1d\x18dc\xd9\xc1\xafZ\xc4\x85\xd9\nfM\xe4\x8d\xdb\xfd\xd5%I\xa3a\xbc\x9f\x11vq!P\xc9\xe1\xad|\xa3\x96\x99\x00\x0c\xe588\xc7\xc1\x15\x99s\xa9<\x0fm\xe6\xbcd<\x81\xefN\xe0D\xa0\x82\xa1A6ts90\xc0\xea\xecf\xb7p_2\xa8\x1f\xfe\x18_>\x9d\xc6R\xc7\t\x95\xc3O\xd7:\xb8\xad4\xae\xe6\xe0\x99\\\xd2\xc0k\x93c\xa8e\x9f^V6qPvS\xbd\xacz\x9a\xf3\x0b\xacL>\xce\xe03\xad\xbc!\xc7\x8cu\xdc\xb8\x8a\xcb\xf1\x06\xa1$\x8d\x0f\xe3=\x84C<\x03T\xb2g\r\xb3\xb6u\x15\xb1\xc0\x86\x8d\\\x9c\x8cw\xe5Wu\xecSZ\xb3\x9a)\x15\xcc\x1eby\x81M\xa5\xf5\x8b\xf4\x0c\xf0K\xa0\x91\xf3*\xa9\xcfn\xaat\xa6\xd8\xc4\xa1\xd9\xe5}\xac\xec\xe3\xd7\xe9W\xef\xd9\x9d\x8b\xab\xc8\xa5[\xcb\xf7r\x1b\x90\xbd\xa1X \xbf\x94\xcf\'\x15\x9c\xccY\xbbqfu\x9a\xd5^\xd6\xa4\xdb\xf1\x06\xa1$\x8d\xbd\xf1~i\xb4\x9a3\x81A~\xb4\x9e\xc3\xb75S\xb4\x93\x9f\x0f\xb1\x0c\x98\xcc\xcf\xeb\x86\x9f\xe1\x15\xe9\x19b9\x90\xcb\\G\xedMO\xfb\x1ay\xfd\x88MupU2\xc817\xbb\xbc\x8b\x07\x92\xc1.|~\x16\x9f\xc9\xe6\xb3\xf3\xc5{~\xfb\x96\x16n\xe0W\x03<\x0cL\xe73\xb38\xaf*\xb3~\xf2(}z\x83P\x924\xc6\xc6{\x08\'pq%\x87\x03C<\xd3\xcd\xc7\xd62}D\x0e\x0bl\xe8\xe1\x8b@\x03\x9f\xa9\xe7\r#~\xbc\x9b\xdf&\x83\xec\xbd\xc0.\xeeN\x06\x8d\xc3\xd7\xef\xe4\xde"\xcf&\xe3\x1av\xc9~\xd5\xc1-@\x1do\xd9\x85w\x8d\xd8\xc5&\xee\x02\xea9>\xc7n\xe9!\xe5\xd7\xf0E`\x12\x1f\x1e1}\xa6\xf4(}\xfd\x0b\x97y%Icl\xbc\x87\xb0\x8a)S\xf8\xafF\xae\xac`N\xb2\xa4\x8bs:\xf8Ai\x85\x1e\x16$\x83\t\xbc\xb3\xfc\xc7;\xf9\tP\xc1\xec\\\xe6L1\xcf/\x81\x1c\xa7e\xe7\x85\x16\xc9\xb7se\xe9c\x1d\xbb\x97\xc6}\xac\x1c\xe4A`"\xc7\x8f\xd8\xfe\x00\x1b\xbb\xb8\x81\xe1\x7fD\xa2\x83{\x93\xc1t\xde;b\xfd.\x9eH\x0654o\xfb\x97\x96$\x8d\x9e\xf1\x1e\xc2D\x13o\xdf\x95\xfb[\xb86\xf9\xd8\x9f\xf9\x1b~},\x02\xaa8\xb4j\xf8$O\xa0\x83\xeb\x0b,\x00Z\xb9\xb8\xd4\xbcA\xda\x8b,\x07\x1a9$\xbb\xf2:~0\xc8\x1f\x92q\xf5\xf0\xafzX\x98\x0cZyS\xd9.\xeeJ\x06-\x99\x93\xcb\xf6\x17\xfe\xbe\xd2\x87k\x98\x94]\xb9\x97\xd5\xab\xf9^2\xaec\xea\xf6\x7feI\xd2\xe8xe\x840\xd1\xc0Q\xb5\\\x04T\xb1gia\x91M@\x91\xb5#V\xeed~\'\x9f\x02\xaa9)\x99D\x9a\x18\xe4\xf9\xf2-o\xe2\xd6n\xbe\xbf\xad\xfd&w\xf5\xeax\xcb\x88\x995E\xf2\xcfs5\xd0\xcc\xbb\xb3\xcd\xeb\xe3\xc9\xf2\x8dt\xf2\xd8\x93\x9c\x9f\\\x17\x95$\x8d\x1f\xaf\x8c\x10\xf6\xf3D77?\xcf9\xfd\xfc\x0b\xd0P\xf6\xae\xea!\x96m\xe2?\x92q\x1f\x8b\xd6\xf2\xd9M|\x1c\xa8`\xf6T\xfe1\xbbf\xe9\xd4p\x13?-\xd23H\xfbZ\xbe\xb9\x81\x0b\x81]\xf8\x97ZN\x00J\xa7\x86@\x91|\x1f\xbf\x02Z8l\xc4N\xb7\xf0d\x91\x95@+o\xce.O\x16n\xe2\xb6^V\x01[xz)\xff\xf44\x1f\xceV\xb0\x8a\xc6\x9d\xf9\x1fB\x92\xf4R\x1b\xbf\x8fOl\xe1\x17=|\xb4|y\r\x1fl\xe0\xa8\xd2\xc7z\x0e\x1d\xe0\xc7@7\x97tsIv\xcd\nf\xb7qM5S\xb2\xcf]\xd42\xb3\x8a7\x16x\xa0\xc0\x03\xcb8\xb0\xb4\xbc\x89s[9\xa1;\x9d\x1dZ\xd2\x97\xbeA\xa6>\xbdIY\xb29}\x18\xb1\x85y\xd9\xe5\xf5\x1c\x97\xe77EV.\xe2\xe4\xec\xf2Z\xe6\xd53g3?\xdb\xde\xaf-I\x1a]\xaf\x8c3\xc2D\x05sZ\xb8v\n\x97g\x176rt\xe5\xf0g\xfe\x12\xd5\x9c4\x9d\xff\xac\xdd\xda\xe4\xcc\xa9|v\xc4\x92&\xce\x9d\xc6E[\xdd\xe9\x00\xeb\x93AM\xd9=\xc8n\x1e\x01Z\xf9\xe8\x88K\xa6S\x87\xf7/]x\xe1\xfe\xfc`B\x9a\xcc\x06g\x8dJ\xd2\xf80~C\xd8\xc8;\xea\xd2\xab\x9a\xb5\\\xd4\xc8\x95S\xb9/{.\x98\xa8\xa4aW\xbe\xd7\xc0gJK\xaa9\xa9\x95\xefN\xe7\x8a\xea\xb2t%r\xec=\x9d[r\x9c\x06T2k*W\xb5\xf1\xb7\xc9W\xcd\x1c\x02\xb4\xf2\xf7\xa5\x95\xeb\x98\r\xd4\xf1\xd6\xec<\xd2tG\x93\x81\xc9eSI[9l6WT\xa6\xeb\xcf\xe4+\xfbr\xd3n\x9cN\xfa6\x99Z\xe6\xe5\xfc{\xbc\x924>T\xc0Pr\xe5\xb0"\xf3\xdf\x11\x1f_\x9e\x85\xb8_\xf7\xeb~\xdd\xaf\xfbu\xbfc\xbe\xdf\xf1{F(I\xd2(0\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\x0c\xa1$)4C(I\n\xcd\x10J\x92B3\x84\x92\xa4\xd0\xfe\x1fo\x7f\x82\xbe\xfb\x91\xb8\x99\x00\x00\x00\x00IEND\xaeB`\x82'))),PhotoImage(ope(BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x03\x0c\x00\x00\x01\xbd\x08\x02\x00\x00\x007\x14f\xd5\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00"\x8fIDATx\x9c\xed\xddy\x9c]ea\xff\xf1of&\xb3e\x85$\x90\x84\x84\x10\x16\x15T*\x8aKE+\x05\xabl\xad\xb8\xa0\xb6\xb5\xadEK\xa9\xadV\xa5.\xb5(*\nU\xebn\xa9R\x97\xba\xb4jm\xeb\xcf\x16\x95\xbaP\xb4\xa2\x82\x02\x8a"\x01d\x0b\x04\xc8\xbe\xccd&3\x93\x99\xfc\xfe8\xde\xcb\x99{\x9f\t\x08\xc1\x84\xe6\xfd\xfe\xeb\x99s\xcf\xb9\xf7D\xff\xe0\xf3:\xe79\xcf\x99\x96\xecHv$I2m\x8f\x1b\xc4\xb997\xe7\xe6\xdc\x9c\x9bssn\xcem\xb7\x0c:\x02\x00@\x1b\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(xhD\xd2H.\xdf\x90\xf9\x9br\xeax\xd6\xee\xeesy@&2|K^\xbd"G\xdc\x90\x13\xc6\xb2~w\x9f\x0e\x000\xa5\x87F$\x8d\xe5\x87I&\xf2\x9dm\xf9\xef\xdd}.\x0f\xc8\xe6|k$\x17\'\x99\xc8\xca\x89\x0c\xed\xee\xd3\x01\x00\xa6\xf4\xd0\x88\xa4\x89\xdcV\r\xb6\xe7\x9a_\xc9\xcf\r\xad\xcd\xbbW\xe6\xa0\xa1\\\xb9k\xbfys\xbeV\r:r`O\x96\xee\xda/\x07\x00v\xa1\x87J$]Z\r\xa6e\x9f_\xc1\xcf\xad\xc9\xf9\xc3\xf9`\x92\xb5y\xde.\xec\xa4\x89\x0c\x8f\xe4\xab\xd5xfN\xdcU_\x0b\x00<\x18\x1e\x02\x91\xb4#C;rS5\xee|\xf0\xaf\xbeLdh4\x9fn\xfe\xb9=w\xef\xaao\x1e\xcau\xcdq_\x1e~\xff\xbed<\xc3?\xcbK\x7f\x9c\xa3\x06\xf2\xa3]sZ\x00@\xc9C \x92F\xf3\x93\xe6\xb8+\x0f{\xb0\x7fn<\xeb\x9a\xe3i9\xa8?O\xdcU\xdf\xbc\xad\x91zI\xfa\xf3\xc8\xfb\xf7%\x9b\xf2\xbfc\xb92\xc9-9g\xd7\x9c\x16\x00P\xf2\x10\x88\xa4\xed\xb9\xa19\xee\xce\xa3\x1e\xec\x9f\x9b\x9e\x03\xfb\xf2\xf2$\xdd\xf9\x83\x85\xf9dW\xe6\xef\xaao\x1e\xcc\xf7\xaa\xc1.\x99\x904\x91\xdb\x1f\xf0\x19\x01\x00S\xea\xda\xdd\'p\xef\xb6\xe7[\xd5\xa03\xa7OK\x7f\xb2\xe3\xc1\xfe\xc5\x059+9+\xc9\xb4]\xf7[\xbb|B\xd2\xf4<\xee\x81\x7f\t\x000\x95=\xfdJ\xd2\x8e\x0cM\xe4\x8b\xd5xz\x8e\xd9\xbd\'\xf3@\xd4\'$\xcd\xccc\xef\xf7\xf7l\xcd\x8d\xd5`~Nz\xa0\xe7\x04\x00LmO\x8f\xa4\x91\xc6-\xaa$\xdd\xf9\xb5\xddx&\x0fP}B\xd2\xcc\x1c}\xbf\xbfgsc\xa5\xa8\xfe,\x7f\xa0\xe7\x04\x00LmO\xbf\xdd6\x96\xcb\xabAG\x9e\xd2\x95\x83v\xeb\xb9< \xcd\tI=9\xa1#}\xf7\xefK\x86rCs*R\xff/\xff|\xdcx\x86\xaf\xcf\xb9[\xf3\xcd\x999\xfe\xe19\xbb+\xbdI\x06\xf3\xf3\x81\\\xbb2\x7f[\xeds@\xfe\xfc\x80<\xbb\xfa\xe8\xc1pg.\xbd5\xff9\xd4\x98\x8c\x7fp^\xba$\xbf\xd5\x9b9;9\xe4\x8e|\xfb\x96|y0?\xad\xfe<,\x7f\xbc,\xc7\xf5d\xee\x83t\x86\x00P\xd9\xd3#i<\xff\xaf\x1aL\xcf\xf3~\xd9c7\xe6\x1d\xa3y_G\x9e\xbc_\xfe\xad\xda2\x98\xff\x1a\xcc;v\xe4\x96$3\xf3\xce\xfe\x1c3=\x07\xd6\x0f\xd9\x9aom\xc8\x1f&\xd97\x9f\x9c\x99\xa7\xed\xfc\xfb\xb7g\xfd\xd6\\\xbe1\xef\x99\xc8\xad\xd5\x969y\xdd\xbc\xfc^{\x03m\xcf\xfa\xe6\x84\xa4Yy\xf2/\xfb\x0fij\x86B_\x9e\xd1\xd9\xf8\x95\xad\xb9q8\xb7n\xcd\x8d\x1b\xf2\xb1$\x8bs\xf6\xa2\x9cZ<|C.\xdb\x9ao&\x19\xcc7\xc7s\xd6D\x86n\xcd\xc76\xe6?\xea\xfb\xac\xca\xdf\xaf\xcbe\x8f\xcb\x87\xee\xf7INeC~\xfa\x93\xbcs{\xee\xaao\xbc9\x1f\x1d\xcb\xe0\xe1yq\xf1\x90\xf5\xb9\xf6\xea\xbc\xbbe\x15\x86\x1b\xf3\x89\xb1\x0c>2\x7f\xb8\xcb\xcf\x10\x00\xea\xf6\xe8H\xda\x9e[\x9b+$5\x1f\xfe\x1f\xcf\xda\x91|w[\xce\xdb\x91\x9b\x93t\xe4\x98\x19y}o\x9e\xd0r\xecD\x86F\xf3\xbe$\x13\xf9\xeeD\x86\x92\xad\xeb\xf3\xc6\xf1\xfcgs\x87\xc1\xbcv0\x99\x9f\xaf\xf5\xe6\x11\xcd\x8d\x1b\x1b\xcf\xd5\x8f\xe4\x86\x9dG\xd2\x86|~S\xde\xd0\xb2qs\xde1\x98K\x97\xd7\x96Yj\xfc\xd6\x15\xcdqo\x0e\xde\xf9\xbfz\'6\xe7\xfb\xcd\xf1\xea|\xf1\xae\x9c\xdb\xbe\xcfH\xee\x9c\xea\xf0\xb5\xb9\xa4\x1a\xec\x93\xe7\x0c\xe6\xfa\x9f\xe7U\xc5\xddF\xf2\xa3M\xb9fn\x8e\xdc\xc9\x99\x8cf\xe3\xc6\\}S\xfeq\xbc\xf1s\x0f\xcf\x9b\xf6\xcb\x93:K\x97\xa0\xc6\xb3\xed\xba|xM.\x9a\xe2\xab\x06\xdb7n\xcf\xb6k\xf3\xd1\xbb\xf2\x95\xfb~\x08\x00\xecZ{t$\x8d\xd6\xd6K\xec\xce\xa3vdh \xef\xdf\x9ew\xd7\xf7\x99\xc8e\x03\xf9\xed\xf1\xfc\xe3\x8c\xfcN}\xfb\xf6\xc6\xd5\x9d$\xa3\xb9vs^Y]@j\xb1!\xe7,\xce\xe7\xab\xf1XV6\xf7\xe9\xcbQS\x9d\xd5D\x86\xee\xce;F\xf2\x99\xe2\xa7\xe3\xb9|8+Z\xee\x85\r\xe7\xfa\xe6\xb8?\x87\xd7?\x1a\xc9\xedC\xb9vM\xde?\x91\x95If\xe6\x05KsV=5n\xcck\xb65^fR\xfb\xc2\xaf\r\xb7mL2\'\xcf[\x9c\x17\x16Olkn\xac.#%\x19\xca-\xcd\x0bH\x0b\xf2\xe2\xc59\xb9/\x07l\xce5\xd7\xe5\xcc\xc6Y\xad+~I\xe5\xd6|\xee\xf6\xfcC\xcb\xc6\xeb\xf3\xd6\x959\xf2\xe8\xfcmK\'\x8dd\xe3\xd59w\xa8\xf1>\x99\xae,zXN_\x9c\xa7%Y\x99\xaf\xdc\x90\xf7-\xcc\x93Z\xbej$\x9b~\x90\xb7om\\6\xeb\xca\xc2\xc3\xf3GK\xf3\xd4$\xb7\xe6\xe2\x9f\xe5C\x8bv\xdd\xe2U\x000\x95=:\x92\xb6\xe7\xb2j\xd0\x91go\xcf-\x839}Gm\xfas\xddp\xceo\x89\xa4\xbaMyV5\xe8\xcd\x9b\xe6\xe6E\x1d\xe9_\x9b\xbf\x19\xcb\'\x93L\xd4&\x86\x0f\xd7^\x0c\xd7\x9b#\x8a_5\x91\xa1;\xf3\xfa\xb1|\xb9\xb9en\xce\x9b\x97\xd3\xd6\xe6c[\x1a\xd3z\xa6gA\xcbQ[\x1b\xf7\xda\xfa\xf3\xbb\xcd\x9bq#\xb9}u\xfeik>W\xdfs0\x9f\xdf\x94\xc7\xcf\xcb3\x1a\xfb\xdc\xd1^H-\x16\xe7\xec\xce\xcc\xec\xcbA3s\xe8Nv\xdbX\xbb\x9a5\x92\xab\x93\xf4\xe4\xa8C\xf3\xea\x999\xb4Z\xe9\xa0/Kv\xfeCIF\xb3\xf1\x9a\xbci[~\\\xfct8\xd7l\xc9\xcf\xf7\xa9\xade5\x9em\xf5BZ\x9e3\x0e\xc9i\xcdE\x1c\x96\xe5\xc4e\xbfX\raG\xfd\x90z!\x1d\x9a\xd3\x0f\xcbs\x9b\xfb\x1c\x94\x13\x96\xe7\x99\xf7z\x9e\x00\xf0\xc0\xed\xb9\x91\xb4#C\xe3\xf9X\xe3\xaf\xb5\x03\x8d\x9b_\x9d9\xb5;\xa7\xf4\xe7Y\xd3\xb2c0\x9f\xd9\x96W\'\xd9\x91\x9b\xc7\xb3\xae+\xf3\x9a\x87o\xcf\xea\xfa\xb7M\xcb\xf2}raO\x8e\xa8\x82`\xdf\xbcjCv\x8c\xe5S\xb3kWD\x86\x1b\x93\xc4\xbbrJG\xfa\xdbOi"Cw\xd5\n\xa93O\\\x94\xf3\xbbs`\xb2cz\x16U\x1b;\xb2\xac+\xf3\xea\xff\xd5\x1f\xc9\xed\xcd\x17\xf4\xcel\xdc\x16\xdc\x98\x8bW\xe7\xd5\xf7\xfa?BO\x96,\xcd\x05w\xe7\xe3c\xf9as\xe3\xac\x9c6\'G\';\xe6\xe7\x19\x99\xb4\x98\xd3\x94\xab:\x8dgx\xcd\xe4\xb9G\xfb\xe49\x87\xe4/:k\xd3\xa7\xc63\\\xfb\xdd\xc2\x12\x9a\xa3\xd9xM\xcei\x16\xd2\x819siN\xedL\xef\xfa\\~m^Wm\xdc6\xf9\x12\xd4\x9a|\xbfYH\x8f\xcey\xfb\xe5\xf1\xf7\xf6/\xce\xdd\xb9\xa2YHG\xe5\xad\x0b-\x07\x05\xc0n\xb2\xe7F\xd2X\xedm$\x13\xf9N\x92i9\xa4/\xe7\xf7\xe57\x9b\xdb;\xb3x\xaa\xc3\xeb\x13\x84\xa7\xe5\xe0y\xf9\xcc\xf4,\xab\x1d8\x7f\xbf\xbc=y{\x92\xaa-&24\x9aOU\x9f\xf6\xe7)\xc5\xef\\\x97\x0f7\x0bizN> \xe77[jk\xe3:MW\xdb\xfbF\x86\x1b\xff\xc9O\xd2\x9fGNd\xf8\x8e\xfc\xddP>\x9bdF^\xb8\x7f^\xdc\x9b%+rRu\xbb-\xc9\x8c\xc9\xdf07\xc7\xcc\xcd1\x83\xb9\xfa\x96\xc6\xec\xe6\x85y^\x7f\x1e\xf6K-t\xb99?\x1a\xcf\x1d\xcd?\x97\xe6\xaf\x17\xe5Y-\xdf0\x90\x15\xcd\xf1\xac\x1c\xd6\xf2\r\xe3\xd9vM\xce\xd9\x96\x1f%\xe9\xcc\xe2G\xe7m\xb3K\x93\xabz\'\xd7\xd5\xfaFQ\xed\x97S\xeeK!%Y\xd7\x88\xaaE9i\xff\x1c\xfd+X;\x14\x00\x8a\xf6\xdcH\xaa\xbf\x8d$IgN\x9f\x9d7\xb7\xac\xb8\xdd\x9c5<-\x07wf~\xfd\xa3\xd1|\xbb9\x9e\x93\xf7\xd6\x0b\xa9h$?k\x8e\xbbK\xf7\xad6\xe7\xcbC\x8dg\xbez\xf2\xa2\x03\xf2\x96\xe6\xcfm\xcb\x8am\xf9\xe7j<\xb3\xed\xe1\xb5\xe6\x84\xa4\x8e,\x9b\x9e\xf9\xb7\xe5\r#\xb98\xc9\xc2\xbc{\x9f\x9c\x90d"C\xcdB\xea\xca\xe3{\xb2\xa4\xbd\x0c\x86ss\xe3K\x96\xf6\xff\xf2/\xb0[\x9d\xffj\x8e\x0f\xcd{\xf7\xcd\xaf\xb7\xef\xb31WU\x83Y9\xae\xb3\xed\x01\xbd\x1br\xc1\xb6\xc6\x14\xb1\xa3\xf2\xee\xbe,\xaeNrc~r}\xde\xdf8\xf9\xc5\xb3\'\xffO7;\x87\xaeI\x92\xac\xc9E+s\xd8\x019\xee^\x17\x17\x98\x9bC\xaa\x87\xd9\xee\xcaW\xe6\xe4\xd0\xa5y\xda\x83\xb7\x1e\x01\x00\xec\xc4\x9e\x1cI\x976\xc7\xddy\xdf\xcc\xbc\xa8}\x9f\xb1F\tu5f\x1dU&24\x9e/U\xe3\xfe\xfc]o\x1e\x7f\xaf\x17$F\x1a+Y\xa74!i"C\x9b\x1a\x13\xc6\xa7\xe7\xe4\x85\x8d\xbbK\x955\xb5{v\x1d\x99\xd5rlsBRo\x9e\xbc2\x7fS\x15\xd2\xb2|\xb1\xd9:\x9bj=\xb7 /(\x9e^\xf3\xb9\xb6\x19m\xd3\x9c\xef\xd5\xb6\xac\xda\x9aoT\xe3#\xf2\x99\xe2\xd4\xa5\xd1l\xd8\xd8X\xd9|\xbf\x1c\xdb\xf2\xe9\xea\\\xb2\xbe\xb1\x16\xc3ays_\x16\xdf\x9d\xff\x99\x96\x1d\xf5\xa7\xdb\x92\xfcZ\xde\xd22k{n\xed\xc9\xc1\x1b\xf3\xde\x1b\xf3\xde\xe59cQ\x8e\xe9o\xdc\x9dl7\xb76\xe7}E>\xb0"\x1f84\xa7/\xce\x93gf\xe1\xbd\xffS\x01`\xd7\xd9C#i{nm\xbe\x8d\xa4/\xff\xda\x9b\xe3\xdb+g4?k\xae\xa2\xd43y\t\x80\xf1\xacm\x8e\xfb\xee\xdb\xcbL\xb6\xe5;\xd5\xa07/o\x9f\x90\xb49\xff\xb5\xa3\xf1\xb8\xdc\xc2\x9cS\xdfas\xbe2V{R\xbd\x7f\xf2+x\xeb\x13\x92\xaa[lI\x96\xe5\x8b}yx\xf3_T\x7f\xf6mVi1\xee\x89\x0c7\x9fe\x9bQ\xcb\x8e\x16+\xf2\xfa\xe9\x99{H^\xdf\xb2}S~P\r\xba\xf3\xd8\x199\xac\xd8\x8b\x9brus<w\xf2[SV\xe7\x92\x9f7VFHrc\xde|c\xde\xdcr\xf8\x9c\x1c\xfb\xb0\xfc\xc9\x8c\xb6\xf4\x99\x9dC\x1e\x9d\xf3~R[+\xe1\x96\\xK.\xdc?\xa7,\xcb)sJ\x8b\x86\xcf\xc9\xc1\x8f\xc9\xb9?\xca\x1b\x9b[~\x9e\x8f\xff<\x1f_\x9c\x13\x97\xe7\xa4\xe2!\x00\xf0`\xd8C_K2\xd6\xb8\xb3\xd3\x91\xa7\xf4\xe6\xf8\xe2>C\x8d)D\x1d9\xa6/\xc7\xd5?\x1ai\xcck\x99\x96\x83\xef\xf5F[\x92\xb1\xac\xdc\xde\xb8!\xd5S\xaa\x90-\xf9H5\xd87\x1f\xacO\x0f\x1f\xcd\xca\xf5yE}\xcf\xae\xc9\x93r\xea\x13\x92*K\xf2\x99\xbe\xda\xc5\x92\x89\x0co\xce\x85\xd5xN\xce\x98^\xfb\xf2\xda\xe9\xado\x8e\xfb\xa7Xfi]\xbe>\x94otev\xfbGkrq5X\xfc\x8b\xc7\xc4\nn\xcb\x87\xab\xc1\xbeyvw\xf6in\xdf\x94\x9f\xd4\x0b\xa9\xdd\xa2\xbc\xe8\xc8|\xe019\xa7\x7f\x8a\xf9a\x0b\xf2\x84\'\xe5\xd3\xcbsF}\xe3\xea\\tE\xce\\\xd3\xa8\xb7\x16\xfb\xe7\xe8\xa7\xe6c\x87\xe4%\xf5\x8dw\xe6\xab\x97\xe5\xe5\xabk\x13\xd8\x01\xe0A\xb5\x87^I\x1ao\xcc\x10\xea\x9ab\xa1\xed\xe1\\\xb2=\x1f\xaf\xc6\xfd\xf9\x8b\x96O\xc7\x1a\x87O\x9fz]\x80\xbam\xb5\x87\xff\xfb\xda\x16Q\xdc\x96\xeb\x9a\x97\x91f\xd5nEm\xcb\x8a\xbb\'\xfftwNjYn\xbb~\x95(\xc9\xbc\xbc\xb5\xe5\xed\xb6\x03\xb9\xb29\x9e5\xc5\xe2L\xa3\xb5G\xc6\xa6\x97\x9e;\xdb\x96;n\xcf\xeb\x93\xcc\xcec\xda>Z5z\xcfd\xa3\xc3S\xb2>\xdf\x1f\xcf\xaaj<\x7f\xf2\xa4\xf5\x91\xda5\xb9\xa6\xe5yMWfLO\xdf\xfc<1\x93\x1e\xaf+\xeb\xcf\xa2\x83s\xda\xb2\xfc\xf6\xea|\xff\xba_L\x96O\x92\x95\xf9\xef\xa9fs\xcf\xc8\xa2\xc3\xf2\xdc\xe59yu.\xffI\xde\xd1\xdc~k\xbe\xeey7\x00~5\xf6\xd8H\xfa\xc5\xbd\xb6\xae\xd2$\xe5\xd1\\;\xd4\x98\xbb3=\xafn\xb9\x8c\x94d\xac\xb1\xb2v\x7f\xedQ\xb8\x9d\x18i<\xd85-\xcb\xa7\xe7\xc0\x96\x1bR\xa3\x8dI\xd3=yQ\xf3F\xdb@\xbe\xbd6\x7f\xdc\xf2=\xddmW\xad\x9a\x13\x92\x92\xf4\xe4\xc4\xf9\xb5U\x82*\x83\x8d\x82I2k\x8a\xff\xfc\x8fgks\xdc~\xa9i<\xc3?\xcf[\x93t\xe7q\xfb\xb4M\x1b\x1f\xc8u\xd5`F\x8e\xef\xcd\x01\xc5\xef_\x97\xff\xad\x06\x9d9`\xee\xe4\xb7\x08\xef\x9f\xe3\xd6\xe4\xd2-\xf9\x9f$\x0b\xf3\x07\x87\xe6O\x9aI\xf4K=^\x97\xa43\xbd\x8bs\xec\xc2<\xe9Gy\xd7\xc6|;\xc9h6\xed\xfc\x90\xae\xf4.\xc9o,\xcc\x13\xae\xca{\xd7\xe7;IF\xee\xed\x10\x00\xd8U\xf6\xc4\xdbm\xcd\xb7\x91L\xcb!=mk+\x8f\xe4\x8a\x81\xc6\xe5\x9c\x8e\x1c3{\xf2\xdd\xae$\xe3Y\xb7\xa3\x915\xddm\x0f\xe4\x17\x8d4\xee\xb5\xf5\xe7\xf7v\xb2\xdbD6&\xd9\x96\x15w\xe6\x9cf!u\xd4^\xbb\xdb;\xf9V\xdd\xd6\\\xd5\x9c\x90\x94dQ\xdbk@&2\xdc\xbc\x91\xd7\x93g\xde\xbf\x17\xdf\xde\x9a\xf7\x8f\xe5\xca$\x07\xe4\x8f\xda?\xdd\xdc\xb8R\xb5\xcf\x14\xabT\xd7\xa7l/\xcc\xa9\xed\xcf\xb5U\x85\x94dV\x0e\xd9\xc9i\xac\xcb\x15\x97\xe7\x95\xdf)\xcd\xaf\xaf\xebL\xef\x82\xc6\xb5\xb4\xfd\xef\xdb\xc2\xd9]\xe9\xdd\xafq\x8d\xcdZ\xdb\x00\xfc\xca\xec\x89W\x92j\x13\x92\x8em\xf9h \x17\x8c\xe5M\x8dO\x8f\x99\x93\x0b[\x16\x05H2\xd6x\xb5Hg\x9eU\\\x13\xb2\xed\xe7\xeao#yl\xfb\x0e\xdd\x8di@c\xf9\xf2-\xb5\xb5\xb6\x93\xcc\xcdy\x9d\x99\xd9\x9c\x96\xd42k{[m}\xf0yykO\x96\xb6|\xf3Pmi\xa2\xde\xa9\xe7Nu\xd7\x96\xf0\x1e\xcb\xfa\xce\xda\xd2\xd87\xe7\xfc-\xf9B\x92\xe9\xa5\xcbH\xe3\x19\xde\x94\x7fo\x9c\xdbA\xc5/\xafO\xd9^\xb0\xd3\xd7\xd5\rgMq\xfb@n\xba)\x9f\xd9\x9cK\x93tM\xbdrU\xa5z\x15I\xe3\xe7\xee\xd3\x8d\xb3[s\xf1u\xf9`5\xdeo\xea\xd7\xc5\x00\xc0\xae\xb5\'FRsBRgmz\xd0P\xbe4\x92\xf3\x9a\xaf%\xe9\xcc\xa9s\xf3\xbei\xa5\x06\x1ak,\xb0\xd4\xd56A\xa7\xa8>!\xa9\xa7\xf46\x92\xde\x1c>3o\x18\xccy\xf5\x8d\x9dy\xd2\xfe9\xbb7\x8fX\x9d\xf7T[:\xb2\xac{r\x06\r\xde\xf3Z\x95e\xfb\xe6\x94\xd2O\xdfSQ\xddS\xdc\x0bK\xd2\x9b\xa5\x1dY:\x91\xdb\x93\xdc\x99O\x1d\x9c7$\x19\xc8\x8f\xee\xccg\x87\xf3\xf5j\x9f\xe5yM\xfb\x81[kkM\x15\x17\xd1N\xb2\xb6q\xa1\xa8\'G\xf5\x95\xce\xa13\x07T3\x96\xee\xc8\x05\xd33cQ\x9e^=\xe7?\x9emk\xf3\xbd\xd5\xf9\xd6\xe6\xdab\r\x87\xe4\xa5\xc5_\xb93\x97n\xcf\xd0\x8dyos\xcb\x92\xfcnq9\xca\xa6U\xf9\xf6X\x86V\xe4\x03\xcd-\xcb\xf2\xfc9YnyI\x00~5\xf6\xccH\xfa\xc5\xdd\x9fi\x995\x94/M\xe4\x8e\xe6\xd5\xa3J_>\xda\xdf\xb6`t\xd3\xe8=\x8b\'M\x99\x1du\xc3\x8d%\x88\xa6z\x1bI\x92\xf9yio\x0e[\x9f\xb7\xec\xc8\xad\xd3s\xf2\xac\x9c07\'U\xff\xb5\x1en<\xff\xdf\x97\x93\xeb\x87Ldx\xb41!iv^P\xbc\x956\xd4\x980\x94\xa433\xa7:\xc3\x8e\xf4-\xca\xcbW\xe5\xb5I\x06\xf2\x85\x1f\xe7\x0b-;\x1c\x94\x0f\x16\x9f\xed\x1fi\\\xfb\xe9\xcc\x92\xe2\x84\xa4\xf1\x0c\x0f6\xdez{@\x9eS\xfc\xf5\xe59\xa3\xf9\x80\xdb-y\xd7-yWq\xb7\xae,~d^\xdf|q\xdb\r\xf9\xf8\xaa\xc6\x02\x9b\xed\x8e\xc8\xdf,\xce\xd3ZN\xf8\xba\xfc\xd3\xed\x93\xdfdWwd^\xb7$O\x9d\xeaS\x00\xd8\xe5\xf6\xb8H\x9a\xc8\xda\xe6\xe5\xa2\x91\x9c\xde\xf2igN\x9f\x99\x97u\xed\xf4\xa9\xfe\x1d;}\x83}\xbb\x8e\xcc\xad\x06};\xfdo\xf0\xcc<mf.i)\xb3\xa1\\9\xd1x\xf0\xad\xb7\xf6`\x7f\x92\x89\x0c5\xc7\xb3\xee\xc3ZM\xbdS\xdc\x0e\xab\xcc\xcb3\xb6\xe4\x87\x03\xf9\xd7\x96\xed\x1dYzh\xde5\xa3\xed-"-fM1\x95g\xb8\xf1P[\x92YS\xac\xc0\xb4\x7f\x8e\xdb\x98\xab\x9b\x8bI\x16\x1d\x92\xb3\x16\xe5\xe9]\xe9in\x19\xcb\x96\xe2\x9e\xcbs\xc6\x92\x1c\xdfS[e\xa0v\xc8@\xf1\x90Cs\xfa\x819\xbe7svr\x02\x00\xb0\xcb\xedq\x914-3\x9a\xe3\xae\xfc\xd5D\xbe_\xbd\xb8mz\xde\xda\x9b\xa7M\xcf#\xef\xf5\xa1\xaa\xbe\xfc\xd1\xd6\\\xd6\x91cz\xda\x1e\xe6/\x9a\x93\xe7\x8f\xe5\x07\xe3\xf9\xde\xcc<\xfd\x97=\xdb\xfa\xfd\xb2\xd9\x93gPue^wN\x1c\xcdW\xe7\xe5\xdc\xfa\xd2\x91u\x0b\xf2\xfc\xad\xf9\\\x92\x05yK\xff\x14\xfb4-\xcf\x1b\xd6\xe7\xe85\xf9|5M\xbb#K\x17\xe7\xcf\xf7\xc9Sw\xf2\xd6\x8eY9\xa23K\xc6s\xc7\xa2)\xae\x12ug\xdfjpp\xce\xed\xcb\x01S\x9d\xc0#r\xd6\xe6\xfc\xd6\xa6\\{G.\xa8o\x7fX\xceI\xb2\xe8\x9e\x7f\xf8=\x87?2\xaf\xdc7\x8fY\x91s\x1b\'\x7fFo\x16,\xce\xb1\xd3&\xefVwd^>?G\xfe4\xe7W\x7f\x1e\x92\x97\xf4gA\xed\xea\x91\xbbl\x00\xfcJMKv\xa4\xed\xa1\xee\xdd;\xd8\x96/\x8e\xe4\xf4\x8e<{v>8\xadq\x97j\x0f9\xb7\xda \x13\xd9\xba2\xbfS]I\x9a\x91\x97-\xcc\xabv\xf7)\xddsn{\xda\xff\xa7\xce\xcd\xb997\xe7\xe6\xdc\x9c\xdbC\xee\xdc\xf6\xb8+II\xfarj_N\xcd\xe4\xff\xe1\xf6@\x03\xb9\xb4y\xafmnN\xdc\xad\xe7\x02\x00\xecb{\xe2:I\x0f\t\xdb\xb3~c\xe3\xb9\xb6\xde\xfc~\xef\xd4\xafT\x03\x00\x1e\x8aD\xd2\xfdtW\xde\xd2\xbc\x8c\xb4`\xf2[\xc6\x00\x80\xff\x03D\xd2\xfdqg\xce\x19k\xac*9/\x1f\xe8n[%\x12\x00x\xa8\xdb\x13\xe7$\xed\x99\xb6g\xdd\xd6\\\xbe=w\x0e4\x1e\xbfJ2#/\x9b\xd3X0\t\x00\xf8\xbfD$\xdd\'\x1b\xf3\xf9\xcd\xf9\xeb\x96\x8d3\xf2\xb2\xfd\xf3\xea\xddr>\x00\xc0\x83M$\xdd\xbb\x89\x0c\xb5\x14RG\x0e\x9a\x97sfY\x00\x1a\x00\xfe\xef\x12I\xf7Ig\x9e4\x9e\xef\'\xe9\xcf\x9f\xf7\xe6\x11sr\xd2\x1e\xbe<\x01\x00\xf0\x00\x89\xa4{\xd7\x91\xfe\xa5\xf9\x97j<M\x18\x01\xc0\xde\xc1\xd3m\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92(X\x9dK\xbe\x9b\xa7\\\x9e\x17\x0c\xe7\xce\xdd}.\x00\xb0{\x88$Z\x8dg\xf8\xa6\xbc)\xc9xV\xad\xc9\xb7v\xf7\xe9\x00\xc0\xee!\x92h5\x9a\r\xcdqo\xf6\xdf\x8dg\x02\x00\xbb\x91H\xa2\xd5@V4\xc7\xb3\xf3\x88\xddx&\x00\xb0\x1b\x89$Z\r\xe6\xa6j\xd0\x99\x03\xfa\xb2x\xf7\x9e\x0c\x00\xec."\x89V\xeb\xf2\x8dj0?\xc7\xef\xde3\x01\x80\xddH$1\xc9pV\x8dgU5\x9e\x99Cw\xef\xc9\x00\xc0n$\x92\x98\xc4\x84$\x00\xa8\x88$&1!\t\x00*"\x89ILH\x02\x80\x8aH\xe2\x1e\x9bs\x8d\tI\x00P\x11I\xdccknm\x8eMH\x02`/\'\x922\x90\x8b\xee\xca\x0b\xee\xc8\x81\xb7g\xd9\xedY\xb6!\x17n\xcf\xba\xfb|\xec\xb7o\xce\xa17\xe5\xb0\x9br\xd8\xa6|\xe5\x81\x9c\xc6D\x86\xaf\xcf\xe9\xd7\xe6\xd1\xb7\xe5m\x13\x19\x9ej\x9f\x1b\xf2\xba\x1f\xe7\xa8\x1b\xf2\xba\xf1\xc6>[s\xe3\xea|\xf1\xea<\xee\xaa\x1c}U\x8e^\x95O\x8fOq\xf8\xbd\xda\x90\x1fT\x03\x13\x92\x00\xa0kw\x9f\xc0\xee4\x9c\x1fn\xcc\xabw\xe4\x96\xfa\xc6\xady\xfbD\xb6,\xc8Y;9p[V\xac\xcb\x05c\xf9r}\xe3\xfa\xfc\xe5P.? o.\x1e\xb21\x17\xaf\xc9\xab\x92\xec\x9f\xf7\xec\x93\x13\xdaw\x18\xca\x8a\xed\xf9A\x92\xc1|~kN\x9a\x95\xa3J_\xf2\xbf\xc3\xf9Z\x92\xe1|m"\xaf\x9d\xc8\xf0\xed\xf9\xc8\x96|\xa1\xbe\xcf\xea\xbc\x7fc\xbe\xf3\xe8|x\'\xe7_\x19\xce\xaa\x81\xac\xb8%gW\x7f\xee\x93g\x0f\xe4\x92jlB\x12\x00\xec\xa5\x914\x91\xa1\xf5y\xdbX>U\xfct<\x9bvr\xec\xba|t \xe7\x17?\x1a\xce\xbfl\xca\x13\xe7\xe6\xc4\xd2Q\xef\xab\x06\xeb\xf3\xd9b$\r\xe7\xe6\xfa\xe9\x15\xbf\x7fCcV\xf5\xac\x9c\xb65+n\xcd_\x14w\x1b\xcd\x95[\xf2\xe3\xd9\xf9\xb5\xa9\xfe\t\xc3YuG\xfeyc\xfe\xa3\xbeqc\xbe\xd8\x1c\x9b\x90\x04\x00{\xe3\xed\xb6\xf1\xac[\x93\x177\x0biZ\x96\xcf\xc9\x05K\xb2rin\x9b\x95w$\x99\x99\xa7\x17\x0f\xdc\x9euw\xe4\x15\xed\x854/\xef\xef\xc8\xb2j\xbc!\xefi\xbfY6\x92\xdb\'r[5\xee\xcfc\x8b_\xbe%\xdfm\x8e;\xd2\xdf\xbe\xc3Pn\xa8.#%\xd9\x96\x9b\x9b\x85\xb4o^rx\xbetT\xae<4\x1f\xab\xfd\xe2\x9a\xe2\xaf$Y\x93o\xfc$\xcfm)\xa4\x16&$\x01\xc0^w%i"Ck\xf3\xb2\x89F\x91\xf4\xe7\x8d\xfb\xe6O\x9a\x9f\xce\xcd\x0b\xe7\xe6\x85\xd3\xb2\xa3\xfd\xc0\xedYwW^1\x9e\xefW\x7fN\xcf\xc9\xb3\xf3\xcc\xbe<\xaa;\x07V\xfb\xaf\xcf_&\x99\xc8m[ri\xcb\xb5\xa2\xe1\xfc\xb49\x9eY\x8a\xa4\x89\x0c\x8f\xe4\xbf\x9b\x7f\xce(5\xca\xa6\xc6O\'\x19\xcb\x95I\xa6\xe7q\x07\xe553sX\xb5\xb1/Kw\xfaOO\x92[\xf2\xe1u\xf9D\xedd\x8e_\x90\xdf\xdc?\xc7%\xb99\x1fY\x93O\xc6\x84$\x00H\xb2\x17F\xd2\xd6\\\xd2,\xa4\xb9\xf9\xf4\x8c\x1c\x9bR\x12\xb5\x98\xc8P\xbd\x90\xf6\xcd\x07\xe7\xe6\xa4\xfa\x81\xb3s\xec\xc6,\xab.\x17Md\xa0\xe5\xf0M\x8d+@If\xe6\xe8\xf6\xef\x1f\xaa\xads\xdd\x9bgv\xa4\xaf\xed\x04\x867L\x9e{4;\xa7-\xcb+;\xd3\xd7<\x8d\xf1\xdaM\xba\x9e\xec\xd7\xfe+7\xe6\x9d\x9b\xf2\xef\x8d\x1d\x8eZ\x9e3\xe7\xe4\xc8$\xd57\x8ceK\xf5\xd1\xfc).\xa4\x01\xc0^e\xaf\x8b\xa4m\xf9^5\x98\x9e?\x9c\x91c\xef\xe3Q\xeb\xf2\xe1f!\xcd\xcf\'f\xe57Zv\xe8H\xff\xb4,LnK2>9\x92&2<\x9a\xafV\xe3Y9\xb3=\x80\x92\x0c\xe6\xc7\xcd\xf1\xec\xfcz\xfb\x0e[r\xd5Dno\xfe\xb90o\\\x98g\xb7}\xc9u\xcd\xf1\x8c<\xac\xe5\xd3[\xf2\xe1f!-\xc8\x8b\x97\xe7\xcc\x96\x0bf[rE5\x98\x99C\xdaO\x00\x00\xf66{\xdd\x9c\xa4\xee<\xaa\x1a\x8c\xe5S\x9b\xf3\xd9\xa9\xa6H\xd7m\xc9\x97\x87\xf2\xa1j\xbco>\xd8^HI&24\x9e\xcb\xabqgf\xd5?\x1a\xae\xb5\xcbT\xf7\xda6\xe5_\x9b\x7f\xf6\xe5\xe0\xf6}\xd6\xe6K\xcd\xf1\xb2|h\xff<\xa7}\x9f\xcd\xb9\xb2\x1a\xcc\xc8\xd3;\'\xa7\xd8\x86|\xafy\x97mQ^\xbe<g\xb6\x1c;\x9e\xe1\xe62\x92\x9d\x99\xd1\xfe\xe5\x00\xb0\xb7\xd9\xeb"\xa97\x8fi\x8e\x07\xf3\xda\xbb\xf2\xf0\r\xb9p,+\xa7\xda\x7f"C\x9b\xf2w\xd5\xb8\'/\x9a\x93\x93\x8a\xbb\xd5K\xa8cr$mk\xbc\r-S\xdck\x1b\xc8\x95\x13\xb5\x13\xe8o\x9b\x904\x92;\x9aS\xb6\x0f\xcb\xe7\xe7\xe6\x98\xf6/\x19\xcb\x86\xcd\xf9\xb7j<o\xf2\x03\xfc\xe3\x19\xbe-\xef\xaa\xc63r\xfc\xd2\xfc~\xfb\xe1\x83\xb9\xb19\xee\xc9\xfc\xf6\x1d\x00`o\xb3\xd7ERO\x0e\x9f\x93\xcf\xd4\xb7\x0c\xe5m\xab\xf3\x9459{\xa4\x16:M\x83\xf9\x9f\x1d\x8du\xa8\x17\xe4\x15S}\xed\xc8\xa4\x12zB\xfd\xa3\x8d\xf9h5\x98\xea^\xdb\xea\xdaSi]y|\xfb>\x9b\x1b7\xc2\xa6\xe7\xe8\xfe\xb6\xfbh\x8d}\xael\x8e\xe7\xe6q\xf5\x8f6\xe4\xb2\xf1\xdc\x91\xa43K\x0e\xcd_\x15\x0f\xaf\xaf\xb5\xdd\x9dy\xc5}\x00`\xaf\xb2\xd7ER\x92\x199vA.\xeb\xcf\x1b\xeb\x1bG\xf3\xa959ak\xbe\xd5\xb2\xf3@.\xae\x063\xf3\x86\xae).\xb1Ldhs.\xac\xc6}\xf9\xbd\xaeZd\xd4\x1f\xfe\x9f\x9d\xa7\xb6\x1f\xbb1\x17oo\xacs\x9ddFi\r\xc9\r\x8dU+\xf7\xcb\xf3\xa7\xfaG\xdd\x99\xbf\xaf\x06s\xf2\xbc\xe9\xd9\xb7\xfe\xd1]\x8d+LK\xf3g\xdd\x93?\xaa\xfd\xc4\x15\xcdqw\xf6\x99\xeaW\x00`\xef\xb17FR\x92\xe9Y\xb6O\xceX\x94\xebg\xe7\x1f\xea\xdb\xb7\xd4\xe6\x06%\x19\xcd\xca\xed\xb9\xa8\x1a\xf7\x97\xf2\xa5q\xd4\xa5\xcd\x12\xda7/\xac\x7fT\x7f\xf8\xbf?\x87\xb7\x1c8\x92\xdb\xef\x9e\xbc\xb4wO\xdb\xb3\xf7#\xb9c,?\xac\xc63rD\xf1\x046\xe6\xbb\xe3\x8di\xdd\xfbN\x9e2\xb5-\xabFsU5\x9e\xd5v\x02\x95\xcd\xb9f\xb0\xb1\xd6vg\x0e(\xee\x03\x00{\x9b\xbd4\x92*\x1d\xe9\x9f\x95S\x16gEW~\xbb\xda\xb2#\xeb\xeb;l\xcf\xda\xe6\xb8\xbb\xb1\\d\x8b\xd1\xac\xacVHJ23\x7f\xd67yF\xd1h\xee\xaa\x06]yB\xcb}\xb4\xb1\xac\xbf5g\xb4|[gf\xb6l\x19\xcc\xcf\xaaA_\x9e\xd1\x9b%\xc5s\xd8\x90o7\x0e_2{r\xcc\r4\xee!vfIo)\x80F\xb3\xe1\xe6|\xa4\xf9gW\x16\x14\x7f\x02\x00\xf66{u$U:\xd2\xdf\x9b\xa7T\xe3\xde\x1cW\xffh"\x83;?v{\xd6\xdf\x95\xbf\xae\xc6\x9dy\xe2~mO\x8d\xd5\xf6\xbc\xa2\xbe\x12\xf7p\xae\xbf9/\xaa\xe6kw\xe5\xf1\xcd\xed\xe3m\xbf8\xd0\xb8\x197\'O*~\xf3X64_\xdf6?\xcfmy\xaem$w7N\xaf\xb0r\xd2pV\xfd,g\x8f\xe4\xea\xa9N\x1b\x00\xf6Z")\x9b\xf2\xd9\xc1\xbc\xae\x1a\xcf(M\x1b\xaal\xcb\xb5-[F\xb3rU^Q=\xf9\xdf\x91e\x8bs~\xfb\x9c\xeb\xfar\x00k\xf3\xb9$\x13\x19^\x97\x7f\xbb-\xcfn\x16\xd2\x92\xbc\xbe\xb9O\xfb\x1aK\x03\x8d;\x80\xc5\xa5\x012y\xca\xf6\xbc\xfc\xe6T\xe7?\x9a\xab\xc6\'\xbf/eC\xbewM\x9e\xd7RH3\xb2|\xaao\x00\x80\xbd\xca^\xb7\x98d\xd3@.\x9a\xc8\xc0`^\xdb\xdc\xd2\x9b\x97\xf7L\x9e\xb5\xd3]+\x86\xf5yKG\xde5#\x8fM\xb2=\xeb\x07\xf2\x8dMyC\xf5QG\x96\x1d\x90Otgi\xfb\xe2\xdd\xfd9\xb2y\x03oS\xde\xb9)\xefl\xd9\xe1\xc0\x9c\xbb\x93\xa7\xc9\xb6\xe6\xfa\xe6x\xfa\x14\xd3\xc6\xd7\xe7\x9b\x8d\xb3}\\\xfb\xfd\xb8\x9e,l\x8eW\xe6\x93\xd5\nI\x1b\xf2\xbd\xbbs\xd1`\xe3\xc0\x9e\x1c\xd5L\xa5\xe9\x99=\xd5\xc9\x00\xc0^e/\x8a\xa4\ry\xe7H\xde?\xd5\xa7sr\xc1\xec\x9c\xdc\xb2\xb1;\x07\xf6\xe4\x0fF\xf2\xe9$;r\xeb\x9a\x9c\xd6~`g\x9e\xb88\xe7wO\xf1\xde\xb4\xbe<\xbc;\'6W\xdcnqP\xfe\xa3\'K\x8b\xaf\x8a\xab\x8c6\xdeS\xdb\x91\xa5\xc5\tI\xe3\x19\x1e\xca\xd7\xab\xf1\xc2<\xaf}\x87\xb9y\xecm\x8d\xf1\xba|\xa2\xfe\xe2\xb6\xca\xf2\xbcm\xff\x1c\xf7\x83\x9cV-&i\xb9m\x00\xa8\xecE\xb7\xdb&\xb2\xa9\xb8\xbd?g/\xcaU\xb3rJ\xf1\xd3\xf9yE\xe7\x14\x93\x81\x92\xcc\xc8\xcb\x96\xe6\x1f\xa7*\xa4\xca\x92\x9c\xdd5y\xe5\xa4$]y\xfc\xc1\xb9\xb8/\x0f\xaf\xfe\xec\xc8\x81\xd5\xa0e\xb5\xee\xda\x0f\x15\xdeU\x92d[\xed]%3K\x0f\xafM\xcf\xbe\xcbr^\xf1\xd8\x05y\xf1Q\xf9\xf2~9>\xc9\xbc<=IO\x1e3\xb7\xb4&8\x00\xec\x85\xf6\xa2+I\xf3s\xde`~}\xa01\xb7\xba?o\xec\xca\xe2Y9e\'\x17r\x92te\xfe\x92|vK.\x1a\xcc\xc5c\x8d\xf5\x8a:r\xd0>9\xab/\x8f\xec\xfeE\xdc\xec\xfc\x1b\xe6\x1d\x9cOm\xcaW7\xe4\xb3\xdbsEG\x0e\\\x90W\xee\x93\x13\xea\xbf;//Y\x9bs:r\xe0\xdc\xc9\xaf\x93\x9b\x99#:\xb2t"\xb7\xef_\xbaJ\x94\xa4\xbbq\x0fni\xfev\xaag\xdf\x16\xe4\xe9=Y\xb0*\x9f\xdb\x9ao&\xe9\xcc\x92\xa59sn\x1e\xdbS[\x0f\xe9\xe0\xfc\xe9\xc1\xf9\xd3\x9d\xffO\x01\x00{\x95i\xc9\x8e\xe6\x7f\xe3\xa7\xedq\x8387\xe7\xe6\xdc\x9c\x9bssn\xce\xcd\xb9\xed\x96\xc1^t\xbb\r\x00\xe0\xbe\x13I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0@$\x01\x00\x14\x88$\x00\x80\x02\x91\x04\x00P \x92\x00\x00\nD\x12\x00@\x81H\x02\x00(\x10I\x00\x00\x05"\t\x00\xa0\xe0\xff\x03\xfcHp\xeaP=\xfb\x1e\x00\x00\x00\x00IEND\xaeB`\x82')))
    bf,bh=Label(a,image=be),Label(a,image=bg)
    bi=Frame(a,bg='black')
    bj=Label(bi,bg='yellow')
    bl=Frame(a,bg='black')
    bm=Label(bl,bg='yellow')
    bl.bind('<1>',bn)
    bm.bind('<1>',bn)
    bi.bind('<1>',bk)
    bj.bind('<1>',bk)
    while True:
        if d49!=a28:
            d47.append(a28.copy())
            d49=a28.copy()
        try:
            if int(d39.get())<len(d47):
                d47.pop(0)
        except:
            pass
        try:
            a28.append(argv[1].replace('\\','/'))
            argv.pop(1)
            a29()
        except:
            pass
        if c9!=c8.get():
                c9=c8.get()
                init()
                stop()
                if c8.get!='none':
                    if c8.get()=='wind':
                        Sound(b'').play()
                        Timer(180,c11).start()
        with open(argv[0],'r+b')as s:
            s.seek(getsize(argv[0])-11)
            if not ar.get():
                s.write(b'\x00\x00\x00\x00\x00\x00\x00\x10\x08@\x00')
            else :
                s.write(int(str(av.get())+str(ar.get())+format(['undo values','10','20','30','50','100','ultimate'].index(d39.get()),'03b')+format(['archive format','zip','tar'].index(d23.get()),'02b')+format(['settings saving','save','reset on every restart','only settings','only app choices'].index(c68.get()),'04b')+format(['Music','none','wind','brahms','rain','alone wolf','one mans dream','canon','snow','time','white hats','hooked on you'].index(c8.get()),'04b')+str(d57.get())+str(d28.get())+str(d31.get())+str(d25.get())+str(d21.get())+str(d20.get())+str(d10.get())+str(c93.get())+str(c89.get())+str(c87.get())+str(c83.get())+str(c70.get())+str(c01.get())+str(b86.get())+str(a99.get())+format([a48.get(),a49.get(),a50.get(),a51.get(),a52.get(),a53.get()].index(1),'03b')+str(a72.get())+str(a71.get())+str(a70.get())+str(a69.get())+str(a68.get())+str(a67.get())+str(a66.get())+str(a65.get())+str(a64.get())+str(a63.get())+str(a62.get())+'0',2).to_bytes(11,'big'))
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
    a.deiconify()
    a.lift()
    sleep(.01)
    del c80
def c82():
    global c80
    c80.visible=False
    c80.stop()
    del c80
    c77()
def c79():
    global c80
    a.withdraw()
    c80=Icon('clauth app',c78,'clauth',(MenuItem('open',c81),MenuItem('exit',c82)))
    s=Thread(target=c80.run)
    s.start()
def c77():
    if not d10.get():
        _exit(1)
    else:
        a.withdraw()
def c5():
    showinfo('Fact',['clauth app and video editor are two different parts','all life is a game of luck','when you got nothing you got nothing to lose','A dream you dream alone is only a dream. A dream you dream together is reality.','Nobody promised you tomorrow','We humans are more concerned with having than with being','Laughter is the language of the soul','The only way you can know where the line is is if you cross it','You only live once, but if you do it right, once is enough','Luck is a word used to describe the success of people you don’t like','Make each day your masterpiece','All the darkness in the world cannot extinguish the light of a single candle','You don’t have a soul. You are a soul. You have a body','Faithless is he that says farewell when the road darkens','When you fail, you also learn how not to fail','In order to be irreplaceable, one must always be different','You cannot be lonely if you like the person you’re alone with','Life has more imagination than we carry in our dreams','Good things come in good time','Tomorrow hopes we have learned something from yesterday','What we do is more important than what we say or what we say we believe','If you are not having fun you are doing something wrong','All humor is rooted in pain','Don’t cry because it’s over. Smile because it happened','You pray for rain, you gotta deal with the mud too. That’s a part of it','Governments change… the lies stay the same','My fear was not of death itself, but a death without meaning','Where the willingness is great, the difficulties cannot be great','You don’t have to eat less. You just have to eat right','clauth extract subclip works in no time','A woman’s heart is a deep ocean of secrets','You must work in the dark for your light to shine','You don’t get respect if you don’t deserve it','We can be heroes just for one day','It doesn’t hurt to get more education','Fight with a happy heart and a strong spirit','We’ve added years to life, not life to years','The goal is timeless. Chase the moment, and you lose','The choices we make dictate the lives we lead','I don’t want to end up simply having visited this world','My fake plants died because I did not pretend to water them','Don’t be afraid to give up the good to go for the great','An intelligent woman doesn’t get sad, she gets pretty','Yesterday don’t matter if it’s gone','Time is a wonderful storyteller','Behind every successful person lies a pack of haters','If there is no struggle, there is no progress','Luck is not a business model','Sometimes it takes years for a person to become an overnight success','The harder I work, the luckier I become','The best revenge is massive success','Nothing left to do but smile','I found out that there weren’t too many limitations, if I did it my way','The beginning is the most important part of the work','Your river is strong. Let it flow','Faith is a knowledge within the heart, beyond the reach of proof','Nothing is stopping me from doing what I love to do','Well, it’s hard to be yourself, it’s the hardest job there is','It takes a lot of courage to show your dreams to someone else','I paint flowers so they will not die','There can only be one king','Don’t wait for them to tell you. Tell them','In life you always see the darkest days before the sunshine','Keep your friends close, your enemies even closer','Haters keep on hating cause somebody’s gotta do it','The good life is one inspired by love and guided by knowledge','There is no normal life, there’s just life. Get on with it','It’s okay to start over, let someone else love you the right way','Even a blind man knows when the sun is shining','Life is what you make it, just don’t fake it','Wear your crown and go chase your dreams','It’s never too late to get good at something','In every walk with nature one receives far more than he seeks','Our weary eyes still stray to the horizon','I will not let anyone scare me out of my full potential','To lose your path is the way to find that path','I’m not afraid of dying, I’m afraid of not trying','There is no way to happiness – happiness is the way','What a dog I got. His favorite bone is in my arm','Only thing free in life is options','Look at the sky tonight. All the stars have a reason','I am my inspiration','Be kind to one another, even when it’s not requested','Don’t be scared to live your life without judgment','you either die a hero or you live long enough to see yourself become the villain','when you break with your love it means he/she is in love with another person','they say money can’t by happiness','i love walking in the rain because nobody can see my tears','they don’t know your kindness until you turn to a villain','you need to lye if you want others think of you','ppl is like when they understand you have fun with them they break with you','let something inside youself because if you done everything they end up with you','looking for the best? look for the one who tries to be best for you','ppl never hate you ’cause of your limits they hate you for your powers. so try to be powerful and don’t care to what they say','you better to be alone except having someone who makes you feel alone','Happiness is not by chance, but by choice','Keep your face to the sunshine and you cannot see a shadow','Impossible is for the unwilling','Believe you can and you’re halfway there','It is never too late to be what you might have been','When you have a dream, you’ve got to grab it and never let go','Whatever you are, be a good one','You must do the things you think you cannot do','Be faithful to that which exists within yourself','Dream big and dare to fail','My mission in life is not merely to survive, but to thrive','You are enough just as you are','To be the best, you must be able to handle the worst','Life is like riding a bicycle. To keep your balance, you must keep moving','Every moment is a fresh beginning','Your mind must be stronger than your feelings','I know that now, and now is all that matters','Sometimes you have to take two steps back to take ten forward'][int(time()//86400%113)])
def c0():
    if Controller().position[1]>310 and Controller().position[1]<570:
        c09.place(x=293,y=Controller().position[1]-280)
def c3(s):
    c0()
def c6():
    b36()
    c7.place(x=30*u,y=30*u)
    au.place(y=240*u,x=300*u)
    c69.place(x=150*u,y=30*u)
    c84.place(x=300*u,y=30*u)
    c86.place(x=300*u,y=60*u)
    c90.place(x=150*u,y=100*u)
    c94.place(x=450*u,y=30*u)
    d11.place(x=300*u,y=100*u)
    d19.place(x=450*u,y=100*u)
    d18.place(x=20*u,y=280*u,width=90*u)
    d22.place(x=150*u,y=170*u)
    d24.place(x=30*u,y=65*u)
    d26.place(x=300*u,y=170*u)
    d29.place(x=450*u,y=170)
    d30.place(x=450*u,y=200*u)
    d38.place(x=30*u,y=135*u)
    d40.place(x=30*u,y=100*u)
    d58.place(x=150*u,y=240*u)
    d72.place(x=65*u,y=250*u)
    at.place(x=450*u,y=240*u)
    aw.place(x=20*u,y=250*u,width=40*u)
def c92():
    a.attributes('-topmost',c93.get())
def d32():
    if d28.get():
        d30.config(state=NORMAL)
    else:
        d30.config(state=DISABLED)
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
def ao():
    if not a28:
        showerror('Error','No link')
        return False
    for i in a28:
        YouTube(i).streams.get_highest_resolution().download()
def ap():
    j()
    a16.config(command=ao,text='load',state=NORMAL)
    a28.clear()
    a29()
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
            d06=VideoWriter(str(int(time()))+".avi",VideoWriter_fourcc(*"XVID"),int(float(d04.get())),(a.winfo_screenwidth()*windll.shcore.GetScaleFactorForDevice(0)//100,a.winfo_screenheight()*windll.shcore.GetScaleFactorForDevice(0)//100))
            s=Thread(target=d07)
            s.start()
        except:
            showerror('Error','    invalid data       ')
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
def d74():
    a.config(bg='SystemButtonFace')
    bi.config(bg='black');bj.config(bg='yellow')
    au.config(fg='black',bg='SystemButtonFace');az.config(fg='black',bg='SystemButtonFace');at.config(fg='black',bg='SystemButtonFace');aw.config(fg='black',bg='SystemButtonFace')
    c66.config(bg='SystemButtonFace');d72.config(fg='black',bg='SystemButtonFace');d59.config(fg='black',bg='SystemButtonFace');d58.config(fg='black',bg='SystemButtonFace');d40.config(fg='black',bg='SystemButtonFace');d38.config(fg='black',bg='SystemButtonFace');d36.config(fg='black',bg='SystemButtonFace');d34.config(fg='black',bg='SystemButtonFace');d30.config(fg='black',bg='SystemButtonFace');d29.config(fg='black',bg='SystemButtonFace');d27.config(fg='black',bg='#42da16');d26.config(fg='black',bg='SystemButtonFace');d24.config(fg='black',bg='SystemButtonFace');d19.config(fg='black',bg='SystemButtonFace');d22.config(fg='black',bg='SystemButtonFace');d18.config(fg='black',bg='SystemButtonFace');d14.config(fg='black',bg='SystemButtonFace');d12.config(fg='black',bg='SystemButtonFace');d11.config(fg='black',bg='SystemButtonFace');d05.config(fg='black',bg='SystemButtonFace');d04.config(fg='black',bg='SystemButtonFace');d03.config(fg='black',bg='SystemButtonFace');d02.config(fg='black',bg='SystemButtonFace');d00.config(fg='black',bg='SystemButtonFace');c94.config(fg='black',bg='SystemButtonFace');c90.config(fg='black',bg='SystemButtonFace');c88.config(fg='black',bg='SystemButtonFace');c86.config(fg='black',bg='SystemButtonFace');c84.config(fg='black',bg='SystemButtonFace');c75.config(fg='black',bg='#a8a8ff');c72.config(fg='black',bg='SystemButtonFace');c73.config(fg='black',bg='SystemButtonFace');c69.config(fg='black',bg='SystemButtonFace');c67.config(fg='black',bg='SystemButtonFace');c65.config(bg='SystemButtonFace');c57.config(fg='black',bg='SystemButtonFace');c56.config(fg='black',bg='SystemButtonFace');c55.config(fg='black',bg='SystemButtonFace');c54.config(fg='black',bg='SystemButtonFace');c51.config(fg='black',bg='SystemButtonFace');c49.config(fg='black',bg='SystemButtonFace');c45.config(fg='black',bg='SystemButtonFace');c44.config(fg='black',bg='SystemButtonFace');c42.config(fg='black',bg='SystemButtonFace');b57.config(fg='black',bg='SystemButtonFace');b58.config(fg='black',bg='SystemButtonFace');b67.config(fg='black',bg='SystemButtonFace');b68.config(fg='black',bg='SystemButtonFace');b69.config(fg='black',bg='SystemButtonFace');b70.config(fg='black',bg='SystemButtonFace');b71.config(fg='black',bg='SystemButtonFace');b72.config(fg='black',bg='SystemButtonFace');c36.config(fg='black',bg='SystemButtonFace');c37.config(fg='black',bg='SystemButtonFace');c33.config(fg='black',bg='SystemButtonFace');c32.config(fg='black',bg='SystemButtonFace');c31.config(fg='black',bg='SystemButtonFace');c28.config(fg='black',bg='SystemButtonFace');c27.config(fg='black',bg='SystemButtonFace');c21.config(fg='black',bg='SystemButtonFace');c16.config(fg='black',bg='SystemButtonFace');c19.config(fg='black',bg='SystemButtonFace');c7.config(fg='black',bg='SystemButtonFace');b93.config(fg='black',bg='SystemButtonFace');c2.config(fg='black',bg='SystemButtonFace');c09.config(fg='black',bg='SystemButtonFace');c08.config(fg='black',bg='SystemButtonFace');c06.config(fg='black',bg='SystemButtonFace');c04.config(fg='black',bg='SystemButtonFace');c05.config(fg='black',bg='SystemButtonFace');c02.config(fg='black',bg='SystemButtonFace');c00.config(fg='black',bg='SystemButtonFace');b91.config(fg='black',bg='SystemButtonFace');b92.config(fg='black',bg='SystemButtonFace');b88.config(fg='black',bg='SystemButtonFace');b75.config(fg='black',bg='#a8a8ff');b62.config(fg='black',bg='SystemButtonFace');b61.config(fg='black',bg='SystemButtonFace');b60.config(fg='black',bg='SystemButtonFace');b59.config(fg='black',bg='SystemButtonFace');b57.config(fg='black',bg='SystemButtonFace');b58.config(fg='black',bg='SystemButtonFace');b60.config(fg='black',bg='SystemButtonFace');b59.config(fg='black',bg='SystemButtonFace');b54.config(fg='black',bg='SystemButtonFace');b46.config(fg='black',bg='SystemButtonFace');b45.config(fg='black',bg='SystemButtonFace');b44.config(fg='black',bg='SystemButtonFace');b43.config(fg='black',bg='SystemButtonFace');b41.config(fg='black',bg='SystemButtonFace');b39.config(fg='black',bg='SystemButtonFace');b38.config(fg='black',bg='SystemButtonFace');a84.config(fg='black',bg='SystemButtonFace');a93.config(fg='black',bg='SystemButtonFace');a94.config(fg='black',bg='SystemButtonFace');a95.config(fg='black',bg='SystemButtonFace');a89.config(fg='black',bg='SystemButtonFace');a86.config(fg='black',bg='SystemButtonFace');a83.config(fg='black',bg='SystemButtonFace');a82.config(fg='black',bg='SystemButtonFace');a81.config(fg='black',bg='SystemButtonFace');a80.config(fg='black',bg='SystemButtonFace');a79.config(fg='black',bg='SystemButtonFace');a78.config(fg='black',bg='SystemButtonFace');a77.config(fg='black',bg='SystemButtonFace');a76.config(fg='black',bg='SystemButtonFace');a75.config(fg='black',bg='SystemButtonFace');a74.config(fg='black',bg='SystemButtonFace');a61.config(fg='black',bg='SystemButtonFace');a57.config(fg='black',bg='SystemButtonFace');a55.config(fg='black',bg='SystemButtonFace');a54.config(fg='black',bg='SystemButtonFace');a47.config(fg='black',bg='SystemButtonFace');a46.config(fg='black',bg='SystemButtonFace');a45.config(fg='black',bg='SystemButtonFace');a44.config(fg='black',bg='SystemButtonFace');a43.config(fg='black',bg='SystemButtonFace');a42.config(fg='black',bg='SystemButtonFace');a30.config(fg='black',bg='SystemButtonFace');a09.config(fg='black',bg='SystemButtonFace');a08.config(fg='black',bg='SystemButtonFace');a07.config(fg='black',bg='SystemButtonFace');a06.config(fg='black',bg='SystemButtonFace');a03.config(fg='black',bg='SystemButtonFace');a01.config(fg='black',bg='SystemButtonFace');a00.config(fg='black',bg='#a8a8ff');a27.config(fg='black',bg='SystemButtonFace');a22.config(fg='black',bg='#a8a8ff');a24.config(fg='black',bg='#a8a8ff');a26.config(fg='black',bg='#a8a8ff');a20.config(fg='black',bg='#ff9393');a18.config(fg='black',bg='#ff9393');a16.config(fg='black',bg='#f8fea9');a14.config(fg='black',bg='#a8a8ff');a11.config(fg='black',bg='#a8a8ff');a9.config(fg='black',bg='SystemButtonFace');a2.config(fg='black',bg='SystemButtonFace');a3.config(fg='black',bg='SystemButtonFace');a4.config(fg='black',bg='SystemButtonFace');a6.config(fg='black',bg='SystemButtonFace')
    a48.set(0);a49.set(0);a50.set(0);a51.set(0);a52.set(1);a53.set(0)
    a62.set(0);a63.set(0);a64.set(0);a65.set(0);a66.set(0);a67.set(0);a68.set(0)
    a69.set(0);a70.set(0)
    a71.set(0);a72.set(1)
    b86.set(0);c01.set(0);c70.set(0)
    d28.set(1)
    c83.set(1)
    c17.set(0);c18.set(0);c20.set(0);c35.set(0);c43.set(0)
    d41.set('Language')
    d39.set('undo values')
    c34.set('0b')
    d23.set('archive format')
    c68.set('settings saving')
    c8.set('Music')
    c87.set(0);c89.set(0);c93.set(0);d10.set(0);d20.set(0);d21.set(0);d25.set(0);d31.set(0)
    d57.set(0)
    ar.set(1)
    av.set(0)
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
def d51():
    global a28,d50
    try:
        d50-=2
        a28=d47[d50]
    except:
        d50=-len(d47)
        a28=d47[d50]
    a29()
def d52():
    global a28,d50
    try:
        a28=d47[d50]
    except:
        pass
    a29()
def d42():
    try:
        with open(askopenfilename(initialdir=b65,title='choose file'),'rb')as s:
            global d43
            d43=s.read()
    except:
        pass
def d44():
    global d43
    try:
        with open(asksaveasfile(initialdir=b65,title='choose file').name,'wb')as s:
            s.write(d43)
        del d43
    except:
        pass
def c50():
    global c40
    if c49.cget('text')=='freeze':
        c49.config(text='unfreeze')
        c40=False
    else:
        c49.config(text='freeze')
        c30()
    a29()
def d48():
    s=askopenfilename(initialdir=b65,title='choose file')
    copy(s,s+'-copy'if'\\'in s.rsplit('.',1)[1]else s.rsplit('.',1)[0]+'-copy.'+s.rsplit('.',1)[1])
    a28.append(s+'-copy'if'\\'in s.rsplit('.',1)[1]else s.rsplit('.',1)[0]+'-copy.'+s.rsplit('.',1)[1])
    a29()
def d60():
    b36()
    d59.pack()
def c29():
    j()
    a16.config(text='binary',state=NORMAL,command=c30)
def d75():
    with open(argv[0],'r+b')as s:
        s.seek(getsize(argv[0])-1)
        t=s.read()
        s.seek(getsize(argv[0])-1)
        s.write((t[0]+1).to_bytes(1,'big'))
    op(argv[0])
    _exit(1)
def d80():
    while d84:
        sleep(1)
    d77.destroy()
    d78.destroy()
    d79.destroy()
    d81.destroy()
    d82.destroy()
    d91.destroy()
    d85.destroy()
    d88.destroy()
    d93.destroy()
    d98.destroy()
def d86(s):
    s=askopenfilename(initialdir=b65,title='choose video')
    t=asksaveasfile(initialdir=b65,title='choose file')
    ffmpeg_extract_subclip(s,float(t.split('-')[0]),float(t.split('-')[1]),s+t)
def d87(s):
    ffmpeg_merge_video_audio(askopenfilename(initialdir=b65,title='choose video'),askopenfilename(initialdir=b65,title='choose audio'),asksaveasfile(initialdir=b65,title='save'))
def d89(s):
    ffmpeg_extract_audio(askopenfilename(initialdir=b65,title='choose video'),asksaveasfile(initialdir=b65,title='save'))
def d90(s):
    s=askopenfilename(initialdir=b65,title='choose video')
    t=asksaveasfile(initialdir=b65,title='save')
    ffmpeg_resize(s,t,(t.split('-')[0],t.split('-')[1]))
def d99():
    if d97:
        s=1
        while isfile('output-'+str(s)+'.mp4'):
            s+=1
        concatenate_videoclips(d97).write_videofile('output-'+str(s)+'.mp4')
def bc():
    bi.place(x=200*u,y=60*u,width=330*u,height=20*u)
    bl.place(x=200*u,y=30*u,width=330*u,height=20*u)
    bj.place(height=20*u)
    bm.place(height=20*u)
    bf.pack()
    '''
    global b74
    b74=True
    s=Thread(target=bo)
    s.start()
    '''
def bo():
    if u==1:
        bf.pack()
        while b74:
            sleep(.001)
            bj.place(width=cast(AudioUtilities.GetSpeakers().Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None), POINTER(IAudioEndpointVolume)).GetMasterVolumeLevelScalar()*329)
            bm.place(width=get_brightness()[0]*3.29)
    else:
        bh.pack()
        while b74:
            sleep(.001)
            bm.place(width=get_brightness()[0]*4.40)
            bj.place(width=cast(AudioUtilities.GetSpeakers().Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None), POINTER(IAudioEndpointVolume)).GetMasterVolumeLevelScalar()*440)
def d96():
    global ab
    s=askopenfilename(initialdir=b65,title='choose video')
    d97.append(VideoFileClip(s))
    Button(d88,text=s.rsplit('/',1)[1],bg='#'+format(randint(0,255),'02x')+format(randint(0,255),'02x')+format(randint(0,255),'02x'),fg='#'+format(randint(0,255),'02x')+format(randint(0,255),'02x')+format(randint(0,255),'02x')).place(x=ab+30,y=30,width=d97[-1].duration*10)
    ab+=d97[-1].duration*10
def d83():
    if d82.cget('bg')=='#ffffff':
        d82.config(bg='#000000',fg='#ffffff')
        d85.bind('<1>',d86)
        d85.bind('<3>',d87)
        d88.bind('<1>',d89)
        d88.bind('<3>',d90)
    else:
        d82.config(bg='#ffffff',fg='#000000')
        d85.unbind('<1>')
        d85.unbind('<3>')
        d88.unbind('<1>')
        d88.unbind('<3>')
def d92():
    d93.deiconify()
    a.bind('<1>',d95)
def d95(s):
    d93.lift()
    print('\a')
def d94():
    a.unbind('<1>')
    d93.withdraw()
def d73():
    s=askcolor()[1]
    a.config(bg=s)
    bi.config(bg=s);bj.config(bg=s)
    az.config(bg=s)
    au.config(bg=s);at.config(bg=s);aw.config(bg=s)
    c66.config(bg=s);d72.config(bg=s);d59.config(bg=s);d58.config(bg=s)
    d40.config(bg=s)
    d38.config(bg=s);d36.config(bg=s)
    d34.config(bg=s);d30.config(bg=s);d29.config(bg=s);d27.config(bg=s);d26.config(bg=s);d24.config(bg=s);d19.config(bg=s);d22.config(bg=s);d18.config(bg=s);d14.config(bg=s);d12.config(bg=s);d11.config(bg=s);d05.config(bg=s);d04.config(bg=s);d03.config(bg=s);d02.config(bg=s);d00.config(bg=s);c94.config(bg=s);c90.config(bg=s);c88.config(bg=s);c86.config(bg=s);c84.config(bg=s);c75.config(bg=s);c72.config(bg=s);c73.config(bg=s);c69.config(bg=s);c67.config(bg=s);c65.config(bg=s);c57.config(bg=s);c56.config(bg=s);c55.config(bg=s);c54.config(bg=s);c51.config(bg=s);c49.config(bg=s);c45.config(bg=s);c44.config(bg=s);c42.config(bg=s);b57.config(bg=s);b58.config(bg=s);b67.config(bg=s);b68.config(bg=s);b69.config(bg=s);b70.config(bg=s);b71.config(bg=s);b72.config(bg=s);c36.config(bg=s);c37.config(bg=s);c33.config(bg=s);c32.config(bg=s);c31.config(bg=s);c28.config(bg=s);c27.config(bg=s);c21.config(bg=s);c16.config(bg=s);c19.config(bg=s);c7.config(bg=s);b93.config(bg=s);c2.config(bg=s);c09.config(bg=s);c08.config(bg=s);c06.config(bg=s);c04.config(bg=s)
    c05.config(bg=s);c02.config(bg=s);c00.config(bg=s);b91.config(bg=s);b92.config(bg=s);b88.config(bg=s);b75.config(bg=s);b62.config(bg=s);b61.config(bg=s);b60.config(bg=s);b59.config(bg=s);b57.config(bg=s);b58.config(bg=s);b60.config(bg=s);b59.config(bg=s);b54.config(bg=s);b46.config(bg=s);b45.config(bg=s);b44.config(bg=s);b43.config(bg=s);b41.config(bg=s);b39.config(bg=s);b38.config(bg=s);a84.config(bg=s);a93.config(bg=s);a94.config(bg=s);a95.config(bg=s);a89.config(bg=s);a86.config(bg=s);a83.config(bg=s);a82.config(bg=s);a81.config(bg=s);a80.config(bg=s);a79.config(bg=s);a78.config(bg=s);a77.config(bg=s);a76.config(bg=s);a75.config(bg=s);a74.config(bg=s);a61.config(bg=s);a57.config(bg=s);a55.config(bg=s);a54.config(bg=s);a47.config(bg=s);a46.config(bg=s);a45.config(bg=s);a44.config(bg=s);a43.config(bg=s);a42.config(bg=s);a30.config(bg=s);a09.config(bg=s);a08.config(bg=s);a07.config(bg=s);a06.config(bg=s);a03.config(bg=s);a01.config(bg=s);a00.config(bg=s);a27.config(bg=s);a22.config(bg=s);a24.config(bg=s);a26.config(bg=s);a20.config(bg=s);a18.config(bg=s);a16.config(bg=s);a14.config(bg=s);a11.config(bg=s);a9.config(bg=s);a2.config(bg=s);a3.config(bg=s);a4.config(bg=s);a6.config(bg=s)
def c22():
    c18.set(0);c17.set(0)
def c23():
    c20.set(0);c17.set(0)
def c24():
    c18.set(0);c20.set(0)
def d56():
    try:
        if d57.get():
            recycle_bin().empty()
        else:
            recycle_bin().empty(confirm=False)
    except:
        pass
def c91(s):
    try:
        if c89.get()and a.state()[0]=='i':
            c80
    except:
        c79()
def d09():
    if a01.get()[0]=='.':
        a01.delete(0,1)
    for i in a28:
        VideoFileClip(i).write_videofile(i.rsplit('/',1)[1].split('.')[0]+'.'+a01.get(),threads=8,codec='libx264')
def bp():
    s=Thread(target=d09)
    s.start()
def d08():
    j()
    a16.config(text='c media',state=NORMAL,command=bp)
    a01.place(x=390*u,y=310*u)
    a01.delete(0,'end')
    a01.insert(0,'format: (e.g. mp4)')
def d54():
    d56=randint(0,239)
    d53.place(x=250*u,y=13*u)
    while d55:
        d53.config(fg='#'+''.join([format(int(i),'02x')for i in HSL(d56%240,1,.5).rgb()]))
        a.update()
        sleep(.01)
        d56+=1
    d53.destroy()
def aq(s):
    ad.place(width=600,height=500)
    ae.place(x=250,y=50)
    af.place(x=240,y=100)
    ag.place(x=255,y=150)
    ah.place(x=270,y=200)
    am.place(x=50,y=50)
def an(s):
    ad.place_forget()
    ae.place_forget()
    af.place_forget()
    ag.place_forget()
    ah.place_forget()
    am.place_forget()
def ax():
    s=askcolor()[1]
    az.config(fg=s)
    bj.config(fg=s)
    au.config(fg=s)
    at.config(fg=s)
    aw.config(fg=s)
    d72.config(fg=s)
    d59.config(fg=s);d58.config(fg=s);d40.config(fg=s);d38.config(fg=s);d36.config(fg=s);d34.config(fg=s);d30.config(fg=s);d29.config(fg=s);d27.config(fg=s);d26.config(fg=s);d24.config(fg=s);d19.config(fg=s);d22.config(fg=s);d18.config(fg=s);d14.config(fg=s);d12.config(fg=s);d11.config(fg=s);d05.config(fg=s);d04.config(fg=s);d03.config(fg=s);d02.config(fg=s);d00.config(fg=s);c94.config(fg=s);c90.config(fg=s);c88.config(fg=s);c86.config(fg=s);c84.config(fg=s);c75.config(fg=s);c72.config(fg=s);c73.config(fg=s);c69.config(fg=s)
    c67.config(fg=s);c57.config(fg=s);c56.config(fg=s);c55.config(fg=s);c54.config(fg=s);c51.config(fg=s);c49.config(fg=s);c45.config(fg=s);c44.config(fg=s);c42.config(fg=s);b57.config(fg=s);b58.config(fg=s);b67.config(fg=s);b68.config(fg=s);b69.config(fg=s);b70.config(fg=s);b71.config(fg=s);b72.config(fg=s);c36.config(fg=s);c37.config(fg=s);c33.config(fg=s);c32.config(fg=s);c31.config(fg=s);c28.config(fg=s);c27.config(fg=s);c21.config(fg=s);c16.config(fg=s);c19.config(fg=s);c7.config(fg=s);b93.config(fg=s);c2.config(fg=s);c09.config(fg=s);c08.config(fg=s);c06.config(fg=s);c04.config(fg=s);c05.config(fg=s);c02.config(fg=s);c00.config(fg=s);b91.config(fg=s);b92.config(fg=s);b88.config(fg=s);b75.config(fg=s);b62.config(fg=s);b61.config(fg=s);b60.config(fg=s);b59.config(fg=s);b57.config(fg=s);b58.config(fg=s);b60.config(fg=s);b59.config(fg=s);b54.config(fg=s);b46.config(fg=s);b45.config(fg=s);b44.config(fg=s);b43.config(fg=s);b41.config(fg=s);b39.config(fg=s);b38.config(fg=s);a84.config(fg=s);a93.config(fg=s);a94.config(fg=s);a95.config(fg=s);a89.config(fg=s);a86.config(fg=s);a83.config(fg=s);a82.config(fg=s);a81.config(fg=s);a80.config(fg=s);a79.config(fg=s);a78.config(fg=s);a77.config(fg=s);a76.config(fg=s);a75.config(fg=s);a74.config(fg=s);a61.config(fg=s)
    a57.config(fg=s);a55.config(fg=s);a54.config(fg=s);a47.config(fg=s);a46.config(fg=s);a45.config(fg=s);a44.config(fg=s);a43.config(fg=s);a42.config(fg=s)
    a30.config(fg=s);a09.config(fg=s);a08.config(fg=s);a07.config(fg=s);a06.config(fg=s);a03.config(fg=s);a01.config(fg=s);a00.config(fg=s);a27.config(fg=s);a22.config(fg=s);a24.config(fg=s);a26.config(fg=s);a20.config(fg=s);a18.config(fg=s);a16.config(fg=s);a14.config(fg=s);a11.config(fg=s);a9.config(fg=s);a2.config(fg=s);a3.config(fg=s);a4.config(fg=s);a6.config(fg=s)
def ai(s):
    pass
def aj(s):
    pass
def ak(s):
    pass
def al(s):
    pass
def d61(s):
    j()
def d62(s):
    a12()
def d63(s):
    d48()
def d64(s):
    try:
        d43
        d44()
    except:
        d42()
def ay():
    b36()
    az.place(width=600*u,height=350*u)
def bs(s):
    global br,bs
    br=True
    bs+=1
def ba(s):
    s=Thread(target=bt)
    s.start()
def bt():
    s=time()
    global b74,bq,br,bs
    try:
        bq.config(text='',bg='black')
    except:
        bq=Label(a,bg='black')
        bq.bind('<1>',bs)
        br=False
        bs=0
    az.place_forget()
    b74=True
    t=3
    while b74:
        bq.place(x=randint(0,600*u),y=randint(0,350*u),width=abs(time()-s-50),height=abs(time()-s-50))
        r=time()+abs(time()-s-t)
        while r>time():
            if br:
                br=False
                t/=2
                break
        if r>time():
            continue
        az.place(width=600*u,height=350*u)
        bq.config(text=f'time {time()-s}   count {bs}',bg='white')
        bq.place(x=250,y=200)
        break
def d65(s):
    b76()
def d66(s):
    d51()
def d67(s):
    d52()
def d68(s):
    c77()
def d69(s):
    c6()
def d70(s):
    c79()
def d71(s):
    d56()
def b36():
    global b74,b40,d84,bb
    b74,b40,d84,bb=[False]*4
    bl.place_forget();bm.place_forget();bj.place_forget();bi.place_forget();bh.pack_forget();bf.pack_forget();az.place_forget();au.place_forget();at.place_forget();aw.place_forget();c66.place_forget();d72.place_forget();d59.pack_forget();d58.place_forget();d40.place_forget();d38.place_forget();d36.place_forget();d34.place_forget();d30.place_forget();d29.place_forget();d27.place_forget();d26.place_forget();d24.place_forget();d19.place_forget();d22.place_forget();d18.place_forget();d14.place_forget();d12.place_forget();d11.place_forget();d05.place_forget();d04.place_forget();d03.place_forget();d02.place_forget();d00.place_forget();c94.place_forget();c90.place_forget();c88.place_forget();c86.place_forget();c84.place_forget();c75.place_forget();c72.place_forget();c73.place_forget();c69.place_forget();c67.place_forget();c65.place_forget();c57.place_forget();c56.place_forget();c55.place_forget();c54.place_forget();c51.place_forget();c49.place_forget();c45.place_forget();c44.place_forget();c42.place_forget();b57.place_forget();b58.place_forget();b67.place_forget();b68.place_forget();b69.place_forget();b70.place_forget();b71.place_forget();b72.place_forget();c36.place_forget();c37.place_forget();c33.place_forget();c32.place_forget();c31.place_forget();c28.place_forget();c27.place_forget();c21.place_forget();c16.place_forget();c19.place_forget();c7.place_forget();b93.place_forget();c2.place_forget();c09.place_forget();c08.place_forget();c06.place_forget();c04.place_forget();c05.place_forget();c02.place_forget();c00.place_forget();b91.place_forget();b92.place_forget();b88.place_forget();b75.place_forget();b62.place_forget();b61.place_forget();b60.place_forget();b59.place_forget();b57.place_forget();b58.place_forget();b60.place_forget();b59.place_forget();b54.place_forget();b46.place_forget();b45.place_forget();b44.place_forget();b43.place_forget();b41.place_forget();b39.place_forget();b38.place_forget();a84.place_forget();a93.place_forget();a94.place_forget();a95.place_forget();a89.place_forget();a86.place_forget();a83.place_forget();a82.place_forget();a81.place_forget();a80.place_forget();a79.place_forget();a78.place_forget();a77.place_forget();a76.place_forget();a75.place_forget();a74.place_forget();a61.place_forget();a57.place_forget();a55.place_forget();a54.place_forget();a47.place_forget();a46.place_forget();a45.place_forget();a44.place_forget();a43.place_forget();a42.place_forget();a30.place_forget();a09.place_forget();a08.place_forget();a07.place_forget();a06.place_forget();a03.place_forget();a01.place_forget();a00.place_forget();a27.place_forget();a22.place_forget();a24.place_forget();a26.place_forget();a20.place_forget();a18.place_forget();a16.place_forget();a14.place_forget();a11.place_forget();a9.place_forget();a2.place_forget();a3.place_forget();a4.place_forget();a6.place_forget()
with open(argv[0],'rb')as s:
    s.seek(getsize(argv[0])-11)
    s=format(int.from_bytes(s.read(),'big'),'088b')
a48=IntVar();a49=IntVar();a50=IntVar();a51=IntVar();a52=IntVar();a53=IntVar()
[a48,a49,a50,a51,a52,a53][int(s[-15:-12],2)-5].set(1)
a62=IntVar();a63=IntVar();a64=IntVar();a65=IntVar();a66=IntVar();a67=IntVar();a68=IntVar();a69=IntVar();a70=IntVar();a71=IntVar();a72=IntVar()
a62.set(int(s[-2]));a63.set(int(s[-3]));a64.set(int(s[-4]));a65.set(int(s[-5]));a66.set(int(s[-6]));a67.set(int(s[-7]));a68.set(int(s[-8]));a69.set(int(s[-9]));a70.set(int(s[-10]));a71.set(int(s[-11]));a72.set(int(s[-12]))
a99=IntVar()
a99.set(int(s[-16]))
b86=IntVar()
b86.set(int(s[-17]))
c01=IntVar()
c01.set(int(s[-18]))
c70=IntVar()
c70.set(int(s[-19]))
c83=IntVar()
c83.set(int(s[-20]))
c87=IntVar()
c87.set(int(s[-21]))
c89=IntVar()
c89.set(int(s[-22]))
c93=IntVar()
c93.set(int(s[-23]))
d10=IntVar()
d10.set(int(s[-24]))
d20=IntVar()
d20.set(int(s[-25]))
d21=IntVar()
d21.set(int(s[-26]))
d25=IntVar()
d25.set(int(s[-27]))
d31=IntVar()
d31.set(int(s[-28]))
d28=IntVar()
d28.set(int(s[-29]))
d57=IntVar()
d57.set(int(s[-30]))
ar=IntVar()
ar.set(int(s[-44]))
av=IntVar()
if s[-45]=='1':
    av.set(1)
    if not windll.shell32.IsUserAnAdmin():
        windll.shell32.ShellExecuteW(None,"runas",executable,argv[0],None,True)
        from os import _exit
        _exit(1)
c8=StringVar()
c68=StringVar()
d23=StringVar()
d23.set(['archive format','zip','tar'][int(s[-40:-38])])
c68.set(['settings saving','save','reset on every restart','only settings','only app choices'][int(s[-38:-34])])
c8.set(['Music','none','wind','brahms','rain','alone wolf','one mans dream','canon','snow','time','white hats','hooked on you'][int(s[-34:-30])])
c34=StringVar()
d39=StringVar()
d41=StringVar()
d41.set('Language')
d39.set(['undo values','10','20','30','50','100','ultimate'][int(s[-43:-40])])
c34.set('0b')
c17=IntVar();c18=IntVar();c20=IntVar()
c35=IntVar()
c43=IntVar()
c66=Frame(a)
c66.place(x=30,y=50,width=400,height=250)
c65=Scrollbar(c66)
bb,az,aw,at,au,d72,d59,d58,d53,d40,d38,d36,d34,d30,d29,d27,d26,d24,d22,d19,d18,d14,d12,d11,d03,d02,d00,c94,c90,c88,c86,c84,c75,c72,c73,c69,c67,c57,c56,c55,c54,c51,c49,c48,c44,c45,c42,c36,c37,c31,c28,c27,c14,c21,c19,c16,c7,c08,c06,c04,c05,c02,c00,b93,b91,b92,b87,b88,b75,b67,b68,b69,b70,b71,b72,b60,b66,b61,b62,b59,b57,b58,b54,b46,b45,b44,b43,b41,b39,b38,a93,a94,a95,a89,a86,a83,a82,a81,a80,a79,a78,a77,a76,a75,a74,a61,a57,a55,a54,a47,a46,a45,a44,a43,a42,a30,a09,a08,a07,a06,a03,a01,a00,a28,a27,a22,a24,a26,a20,a18,a16,a14,a11,a9,a2,a3,a4,a6=True,Label(a,text='start\n\n',font=(None,30)),Button(a,text='text',command=ax),Checkbutton(a,text='administrator',variable=av),Checkbutton(a,text='save settings',variable=ar),Button(a,text='Theme',command=d73),Label(a,text='\n\nnew file      ctrl+N                              open     ctrl+O                           home       ctrl+H\n\nopen copy      ctrl+shift+O                    beta       ctrl+alt+O                  open folder       shift+alt+O\n\nsave       ctrl+S                      save new        ctrl+shift+S                         empty recycle bin         shift+alt+E\n\nbackground       ctrl+shift+E                           exit         ctrl+E\n\nsettings      ctrl+T                        undo       ctrl+Z                           redo        ctrl+shift+Z\n\n'),Checkbutton(a,text='ask empty dialog',variable=d57),Label(a,text='clauth is loading...'),OptionMenu(a,d41,'English'),OptionMenu(a,d39,'10','20','30','50','100','ultimate'),Label(a,text='GitHub',fg='blue'),Label(a,text='Quora',fg='blue'),Checkbutton(a,text='show dialog',variable=d31),Checkbutton(a,text='allow run twice',variable=d28,command=d32),Button(a,text='zip',bg='#42da16',command=d17),Checkbutton(a,text='launch on startup',variable=d25),OptionMenu(a,d23,'zip','tar'),Checkbutton(a,text='archive single file',variable=d21),Checkbutton(a,text='delete file after zip',variable=d20),Button(a,text='restore defaults',command=d74),Entry(a),Label(a,text='twitter',fg='blue'),Checkbutton(a,text='stay in background',variable=d10),Label(a,text='this page is empty',fg='darkred',font=(None,15)),Label(a,text='real fps                            fps                        audio bitrate\n\n22                                                                          ',font=(None,13)),Button(a,text='start',command=d01,bg='darkorange',font=(None,20)),Checkbutton(a,text='stay on top',variable=c93,command=c92),Checkbutton(a,text='minimize to tray',variable=c89),Label(a,text='music\n\n\n\n\nsave settings\n\n\n\n\narchive format'),Checkbutton(a,text='exit on close',variable=c87,state=DISABLED),Checkbutton(a,variable=c83,text='ask before exit',command=c85),Button(a,text='own',bg='#a8a8ff'),Button(a,text='convert',command=e),Text(a),Checkbutton(a,text='high resolution',variable=c70,command=c71),OptionMenu(a,c68,'save','reset on every restart','only settings','only app choices'),Button(a,text='common questions',command=c59),Button(a,text='submit',command=c58,bg='#ffee79'),Text(a,font=('Montserrat',13)),Label(a,font=(None,13),fg='dark blue',text='having any question? advice? opinion? bug? or anything you wish to tell us?'),Button(a,text='add file',command=a12),Button(a,text='freeze',command=c50),10,Button(a,text='zoom',command=c46),Button(a,text='zoom out',command=c47),Checkbutton(a,state=DISABLED,text='start with 0',variable=c43),Text(c66,yscrollcommand=c65.set),Checkbutton(a,text='bytes num',variable=c35),Label(a,text='bytes spliter                         show as'),Button(a,text='travel to stw'),Button(a,text='travel to lobby'),False,Checkbutton(a,state=DISABLED,command=c22,text='blank blinking',variable=c20),Checkbutton(a,state=DISABLED,command=c23,text='mate math',variable=c18),Checkbutton(a,state=DISABLED,command=c24,text='glitch',variable=c17),OptionMenu(a,c8,'none','wind','brahms','rain','alone wolf','one mans dream','canon','snow','time','white hats','hooked on you'),Label(a,text='Hot\n\n\n\n\n\n\n\n\nNormal\n\n\n\n\n\n\n\n\n\nCold'),Label(a,text='.',font=(None,50)),Entry(a),Entry(a),Button(a,text='continue',command=c03),Checkbutton(a,text='remmember files path',variable=c01),Label(a,text='turn on after                   turn off after',state=DISABLED),Entry(a,state=DISABLED),Entry(a,state=DISABLED),0,Checkbutton(a,text='enable screen saver',variable=b86,command=b89),Button(a,text='add dir',bg='#a8a8ff',command=b76),Entry(a),Entry(a),Entry(a),Entry(a),Entry(a),Entry(a),Label(a,text='hour     minute    second    frame                           hour     minute    second    frame'),Label(a),Button(a,text='open',command=b63),Button(a,text='extract',command=b64),Label(a,text='start                           end',font=(None,20)),Entry(a),Entry(a),Label(a,text='Reddit',fg='blue'),Entry(a),Entry(a),Entry(a),Label(a,text='#'),Label(a,bg='black'),Checkbutton(a,text='link',variable=a99),Label(a,bg='black'),Entry(a),Button(a,text='browse',command=a96),Button(a,text='start',command=a85),Checkbutton(a,text='round',variable=a72),Button(a,text='choose random and continue',command=b51),Label(a,text='click                to continue'),Checkbutton(a,text='split',variable=a71),Checkbutton(a,text='phrase',variable=a70),Checkbutton(a,text='pattern',variable=a69),Checkbutton(a,text='bits',variable=a68),Checkbutton(a,text='factorial',variable=a67),Checkbutton(a,text='letter',variable=a66),Checkbutton(a,text='reduce',variable=a65),Checkbutton(a,text='count',variable=a64),Checkbutton(a,text='bytes',variable=a63),Checkbutton(a,text='number',variable=a62),Label(a,text='all methods can be modified by passwords',fg='gray'),Label(a,text='please choose a method',fg='red'),Button(a,text='finish',command=a56),Checkbutton(a,text='quick                            \nno time no extra data',command=a36,variable=a48),Checkbutton(a,text='low                                                                                          \nunable to read by other applications suitable for sharing',command=a37,variable=a49),Checkbutton(a,text='high                                                           \nhigh level encryption with more file size',command=a38,variable=a50),Checkbutton(a,text='ultra                                                                                             \nreadable only by clauth app recommended for file storage',command=a39,variable=a51),Checkbutton(a,text='recommended                                                     \na balance for security fast dataless and secure',command=a40,variable=a52),Checkbutton(a,text='custom',command=a41,variable=a53),Label(a,text='Twitch',fg='blue'),Label(a,text='Discord',fg='blue'),Label(a,text='Instagram',fg='blue'),Label(a,text='YouTube',fg='blue'),Label(a,text='made by frost dream',fg='gray',font=(None,30)),Label(a,text='file name already exist',fg='red',font=10),Entry(a),Button(a,text='trash',bg='#a8a8ff',command=a0),[],Listbox(a),Button(a,text='copy',bg='#a8a8ff',command=a21),Button(a,text='rename',bg='#a8a8ff',command=a23),Button(a,text='delete',bg='#a8a8ff',command=a25),Button(a,text='.txt',bg='#ff9393',command=a19),Button(a,text='view',bg='#ff9393',command=a17),Button(a,text='next',bg='#f8fea9',state=DISABLED,command=d45),Button(a,text='remove',bg='#a8a8ff',command=a13),Button(a,text='add',bg='#a8a8ff',command=a12),Button(a,text='translate',command=a8),Text(a),Label(a,text='Enter input in binary or decimal or hexadecimal with "," or "  " or "/" or "\\".'),Button(a,text='compile',command=a5),Label(a,text='invalid syntax',fg='red')
d93=Tk()
d93.geometry('400x300+500+250')
d93.withdraw()
d93.protocol('WM_DELETE_WINDOW',d94)
d84=True
d05,d04=Entry(a),Entry(a)
d55=True
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
az.bind('<1>',ba)
d34.bind('<1>',d35)
d36.bind('<1>',d37)
a09.bind('<Button-1>',a33)
a30.bind('<Button-1>',a34)
d12.bind('<1>',d13)
b43.bind('<Double-Button-1>',b42)
a.bind('<Unmap>',c91)
a01.bind('<Return>',a02)
a84.bind('<Button-1>',a92)
a.bind('<Control-h>',d61)
a.bind('<Control-o>',d62)
a.bind('<Control-O>',d63)
a.bind('<Control-Alt-o>',d64)
a.bind('<Alt-O>',d65)
a.bind('<Control-z>',d66)
a.bind('<Control-Z>',d67)
a.bind('<Control-e>',d68)
a.bind('<Control-t>',d69)
a.bind('<Control-E>',d70)
a.bind('<Alt-E>',d71)
c.add_cascade(label='File',menu=b)
b.add_command(label='Home',command=j)
b.add_separator()
b.add_command(label='New file')
b.add_command(label='Open',command=a12)
b.add_command(label='Open copy',command=d48)
b.add_command(label='Open beta',command=d42)
b.add_command(label='load beta',command=d44)
b.add_command(label='Open folder',command=b76)
b.add_separator()
b.add_command(label='Save')
b.add_command(label='Save new')
b.add_separator()
b.add_command(label='Empty recycle bin',command=d56)
b.add_separator()
b.add_command(label='Background',command=c79)
b.add_command(label='Exit',command=c77)
b=Menu(c,tearoff=False)
c.add_cascade(label='Editor',menu=b)
b.add_command(label='Undo',command=d51)
b.add_command(label='Redo',command=d52)
b.add_separator()
b.add_command(label='Settings',command=c6)
b.add_command(label='Shortcuts',command=d60)
b.add_separator()
b.add_command(label='Video editor',command=d75)
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
b.add_command(label='YouTube downloader',command=ap)
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
b.add_command(label='Image to text')
b.add_command(label='Visualizer')
b=Menu(c,tearoff=False)
c.add_cascade(label='App',menu=b)
b.add_command(label='Credit',command=a05)
b.add_command(label='Check for update',command=g)
b.add_command(label='News',command=d04)
b.add_command(label='Coming',command=d04)
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
b.add_command(label='Overclock')
b.add_command(label='Adjust pc',command=bc)
b.add_command(label='Aim booster',command=ay)
b.add_command(label='Tight type')
a.config(menu=c)
a.protocol('WM_DELETE_WINDOW',c76)
Thread(target=c10).start()
d49=a28.copy()
if c70.get():
    c71()
if int(s[-1]):
    with open(argv[0],'r+b')as s:
        s.seek(getsize(argv[0])-1)
        t=s.read()
        s.seek(getsize(argv[0])-1)
        s.write((t[0]-1).to_bytes(1,'big'))
    d76=PhotoImage(ope(BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02X\x00\x00\x01^\x08\x06\x00\x00\x00Y\xd7a\\\x00\x00\x00\tpHYs\x00\x00\x12t\x00\x00\x12t\x01\xdef\x1fx\x00\x00\x06\x99IDATx\x9c\xed\xd9\xb1\x8d\xc30\x14\x05A\xf1 \xc0\xb1\xfa/R\xb1"^\xea\x02\x16"`\xce4\xf0_\xb8 \xc7\x9c\xf3\x00\x80_6\xc6\xb8\xe7\x9c\xd7\xea\x1d\xec\xe3o\xf5\x00\x00\x80_#\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\xe7\xea\x01\x00\xf0\x82g\x8cq\xaf\x1e\xc1>\x04\x16\x00;\xf8\xcc9\xaf\xd5#\xd8\x87/B\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\x98\xc0\x02\x00\x88\t,\x00\x80\xd8\xb9z\x00\x00\xbc\xe0\x19c\xdc\xabG\xb0\x0f\x81\x05\xc0\x0e>s\xcek\xf5\x08\xf6\xe1\x8b\x10\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 &\xb0\x00\x00b\x02\x0b\x00 v\x8e1\xee\x97n=\xc7q|^\xba\x05\x00\xdf\x9e\xd5\x03\xd8\xcb9\xe7\xbc\xde84\xc6\xb8\xdf\xba\x05\x00\xdf^|L\x80\xe38|\x11\x02\x00\xe4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\x04\x16\x00@L`\x01\x00\xc4\xfe\x01\xb3\xc2\x1e\xb0\x17\xf4%\xeb\x00\x00\x00\x00IEND\xaeB`\x82')))
    d77=Label(a,image=d76)
    d78,d79=Label(a,text='Tools',fg='darkblue'),Label(a,text='nothing yet')
    d78.bind('<1>',aq)
    d81,d82,d91,d98=Button(a,text='i',command=d96,bg='#ffffff'),Button(a,text='z',command=d83,bg='#ffffff'),Button(a,text='s',bg='#ffffff',command=d92),Button(a,text='e',bg='#ffffff',command=d99)
    d85=Frame(a)
    d85.place(x=0,y=0,width=440,height=215)
    d88=Frame(a)
    d88.place(x=27,y=223,height=110,width=416)
    ad=Frame(a)
    ae,af,ag,ah=Label(a,text='extract subclip',fg='blue'),Label(a,text='merge video audio',fg='blue'),Label(a,text='extract audio',fg='blue'),Label(a,text='resize',fg='blue')
    ae.bind('<1>',ai)
    af.bind('<1>',aj)
    ag.bind('<1>',ak)
    ah.bind('<1>',al)
    am=Label(a,text='back')
    am.bind('<1>',an)
    d77.pack()
    d78.place(x=500,y=0)
    d79.place(x=485,y=75)
    d81.place(x=4,y=225,width=20,height=20)
    d82.place(x=4,y=245,width=20,height=20)
    d91.place(x=4,y=265,width=20,height=20)
    d98.place(x=4,y=305,width=20,height=20)
    d97,ab=[],0
    Thread(target=d80).start()
else:
    a27.place(x=40*u,y=40*u,width=270*u,height=250*u)
    a11.place(x=350*u,y=50*u,width=50*u,height=25*u)
    a14.place(x=350*u,y=100*u,width=50*u,height=25*u)
    a16.place(x=350*u,y=150*u,width=50*u,height=25*u)
    a16.config(text='next',state=DISABLED,command=d45)
    a18.place(x=350*u,y=200*u,width=50*u,height=25*u)
    a20.place(x=350*u,y=250*u,width=50*u,height=25*u)
    a22.place(x=420*u,y=50*u,width=50*u,height=25*u)
    a24.place(x=420*u,y=100*u,width=50*u,height=25*u)
    a26.place(x=420*u,y=150*u,width=50*u,height=25*u)
    a00.place(x=420*u,y=200*u,width=50*u,height=25*u)
    b75.place(x=420*u,y=250*u,width=50*u,height=25*u)
    c75.place(x=490*u,y=50*u,width=50*u,height=25*u)
    d27.place(x=490*u,y=100*u,width=50*u,height=25*u)
Thread(target=d54).start()
a.lift()
a.deiconify()
a.mainloop()
      8 