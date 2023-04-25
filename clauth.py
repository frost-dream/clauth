#1.12.3
from os.path import expanduser,getsize
from PIL.ImageTk import PhotoImage
from PIL.Image import open as ope
from time import sleep
from io import BytesIO
from sys import argv
from threading import Thread
from random import randint
from colorir import HSL
from tkinter import Tk,Menu,Button,Label,Text,Checkbutton,Listbox,Entry,DISABLED,NORMAL,IntVar,StringVar,OptionMenu,RIGHT,LEFT,Scrollbar,Y,Frame,X
a36,a37,a38,a39,a40,a41=[0,0,0,0,0,0]
b65=expanduser("~")+'\\desktop'
a,b81=Tk(),Tk()
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
        a28.append(simpledialog.askstring('input link','enter youtube link',parent=a))
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
        a.geometry('780x445+535+260')
        c.add_cascade(label='cache',menu=b)
        c.delete('cache')
        u=4/3
        c6()
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
def c10():
    global simpledialog,YouTube,get_brightness,set_brightness,concatenate_videoclips,ffmpeg_extract_audio,ffmpeg_movie_from_frames,ffmpeg_resize,windll,time,bgcolor,clear,begin_fill,circle,getcanvas,pensize,hideturtle,speed,colormode,setup,fd,right,color,end_fill,goto,penup,pendown,recycle_bin,_exit,d55,d49,isfile,quit,Timer,factorial,init,copy,make_archive,rmtree,extract_archive,li,lis,Controller,draw,display,FULLSCREEN,VideoFileClip,remove,rename,scandir,rmdir,mkdir,sqrt,sin,cos,tan,log,radians,ceil,log10,urlopen,askopenfilenames,askopenfilename,asksaveasfile,askdirectory,Icon,MenuItem,choice,op,grab,VideoCapture,CAP_PROP_FPS,VideoWriter,VideoWriter_fourcc,cvtColor,COLOR_RGB2BGR,array,bye,MessageBeep,Beep,send2trash,askcolor,Image,ImageTk,ffmpeg_extract_subclip,ffmpeg_merge_video_audio,showerror,showinfo,askyesno,askyesnocancel,notification
    from ctypes import windll
    from shutil import copy,make_archive,rmtree
    from os.path import isfile
    from threading import Timer
    from patoolib import extract_archive
    from winshell import recycle_bin
    from pynput.keyboard import Listener as li
    from pynput.mouse import Listener as lis,Controller
    from pygame import draw,init,display,FULLSCREEN,quit
    from pytube import YouTube
    from screen_brightness_control import get_brightness,set_brightness
    from pygame.mixer import Sound,stop
    from moviepy.video.io.VideoFileClip import VideoFileClip
    from os import remove,rename,scandir,rmdir,mkdir,_exit
    from math import ceil,log10,factorial,sqrt,sin,cos,tan,log,radians
    from moviepy.editor import concatenate_videoclips
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
        factorial(1000)
        sleep(abs((c09.winfo_rooty()-310)/260))
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
            if c68.get()=='reset on every restart':
                s.write()
            elif c68.get()=='only settings':
                s.write(int(format(['undo values','10','20','30','50','100','ultimate'].index(d39.get()),'03b')+format(['archive format','zip','tar'].index(d23.get()),'02b')+format(['settings saving','save','reset on every restart','only settings','only app choices'].index(c68.get()),'04b')+format(['Music','none','wind','brahms','rain','alone wolf','one mans dream','canon','snow','time','white hats','hooked on you'].index(c8.get()),'04b')+str(d57.get())+str(d28.get())+str(d31.get())+str(d25.get())+str(d21.get())+str(d20.get())+str(d10.get())+str(c93.get())+str(c89.get())+str(c87.get())+str(c83.get())+str(c70.get())+str(c01.get())+str(b86.get())+str(a99.get())+'100000000000000',2).to_bytes(11,'big'))
            elif c68.get()=='only app choices':
                s.write()
            else :
                s.write(int(format(['undo values','10','20','30','50','100','ultimate'].index(d39.get()),'03b')+format(['archive format','zip','tar'].index(d23.get()),'02b')+format(['settings saving','save','reset on every restart','only settings','only app choices'].index(c68.get()),'04b')+format(['Music','none','wind','brahms','rain','alone wolf','one mans dream','canon','snow','time','white hats','hooked on you'].index(c8.get()),'04b')+str(d57.get())+str(d28.get())+str(d31.get())+str(d25.get())+str(d21.get())+str(d20.get())+str(d10.get())+str(c93.get())+str(c89.get())+str(c87.get())+str(c83.get())+str(c70.get())+str(c01.get())+str(b86.get())+str(a99.get())+format([a48.get(),a49.get(),a50.get(),a51.get(),a52.get(),a53.get()].index(1),'03b')+str(a72.get())+str(a71.get())+str(a70.get())+str(a69.get())+str(a68.get())+str(a67.get())+str(a66.get())+str(a65.get())+str(a64.get())+str(a63.get())+str(a62.get())+'0',2).to_bytes(11,'big'))
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
    c80.stop()
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
    c67.place(y=100*u,x=30*u)
    c69.place(x=150*u,y=30*u)
    c84.place(x=300*u,y=30*u)
    c86.place(x=300*u,y=60*u)
    c90.place(x=150*u,y=100*u)
    c94.place(x=450*u,y=30*u)
    d11.place(x=300*u,y=100*u)
    d19.place(x=450*u,y=100*u)
    d18.place(x=20*u,y=280*u)
    d22.place(x=150*u,y=170*u)
    d24.place(x=30*u,y=65*u)
    d26.place(x=300*u,y=170*u)
    d29.place(x=450*u,y=170)
    d30.place(x=450*u,y=200*u)
    d38.place(x=30*u,y=135*u)
    d40.place(x=30*u,y=170*u)
    d58.place(x=150*u,y=240*u)
    d72.place(x=30*u,y=250*u)
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
            d06=VideoWriter(str(int(time()))+".avi",VideoWriter_fourcc(*"XVID"),int(d04.get()),(a.winfo_screenwidth()*windll.shcore.GetScaleFactorForDevice(0)//100,a.winfo_screenheight()*windll.shcore.GetScaleFactorForDevice(0)//100))
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
def d74():
    a.config(bg='SystemButtonFace')
    c66.config(bg='SystemButtonFace');d72.config(bg='SystemButtonFace');d59.config(bg='SystemButtonFace');d58.config(bg='SystemButtonFace');d40.config(bg='SystemButtonFace');d38.config(bg='SystemButtonFace');d36.config(bg='SystemButtonFace');d34.config(bg='SystemButtonFace');d30.config(bg='SystemButtonFace');d29.config(bg='SystemButtonFace');d27.config(bg='#42da16');d26.config(bg='SystemButtonFace');d24.config(bg='SystemButtonFace');d19.config(bg='SystemButtonFace');d22.config(bg='SystemButtonFace');d18.config(bg='SystemButtonFace');d14.config(bg='SystemButtonFace');d12.config(bg='SystemButtonFace');d11.config(bg='SystemButtonFace');d05.config(bg='SystemButtonFace');d04.config(bg='SystemButtonFace');d03.config(bg='SystemButtonFace');d02.config(bg='SystemButtonFace');d00.config(bg='SystemButtonFace');c94.config(bg='SystemButtonFace');c90.config(bg='SystemButtonFace');c88.config(bg='SystemButtonFace');c86.config(bg='SystemButtonFace');c84.config(bg='SystemButtonFace');c75.config(bg='#a8a8ff');c72.config(bg='SystemButtonFace');c73.config(bg='SystemButtonFace');c69.config(bg='SystemButtonFace');c67.config(bg='SystemButtonFace');c65.config(bg='SystemButtonFace');c57.config(bg='SystemButtonFace');c56.config(bg='SystemButtonFace');c55.config(bg='SystemButtonFace');c54.config(bg='SystemButtonFace');c51.config(bg='SystemButtonFace');c49.config(bg='SystemButtonFace');c45.config(bg='SystemButtonFace');c44.config(bg='SystemButtonFace');c42.config(bg='SystemButtonFace');b57.config(bg='SystemButtonFace');b58.config(bg='SystemButtonFace');b67.config(bg='SystemButtonFace');b68.config(bg='SystemButtonFace');b69.config(bg='SystemButtonFace');b70.config(bg='SystemButtonFace');b71.config(bg='SystemButtonFace');b72.config(bg='SystemButtonFace');c36.config(bg='SystemButtonFace');c37.config(bg='SystemButtonFace');c33.config(bg='SystemButtonFace');c32.config(bg='SystemButtonFace');c31.config(bg='SystemButtonFace');c28.config(bg='SystemButtonFace');c27.config(bg='SystemButtonFace');c21.config(bg='SystemButtonFace');c16.config(bg='SystemButtonFace');c19.config(bg='SystemButtonFace');c7.config(bg='SystemButtonFace');b93.config(bg='SystemButtonFace');c2.config(bg='SystemButtonFace');c09.config(bg='SystemButtonFace');c08.config(bg='SystemButtonFace');c06.config(bg='SystemButtonFace');c04.config(bg='SystemButtonFace');c05.config(bg='SystemButtonFace');c02.config(bg='SystemButtonFace');c00.config(bg='SystemButtonFace');b91.config(bg='SystemButtonFace');b92.config(bg='SystemButtonFace');b88.config(bg='SystemButtonFace');b75.config(bg='#a8a8ff');b62.config(bg='SystemButtonFace');b61.config(bg='SystemButtonFace');b60.config(bg='SystemButtonFace');b59.config(bg='SystemButtonFace');b57.config(bg='SystemButtonFace');b58.config(bg='SystemButtonFace');b60.config(bg='SystemButtonFace');b59.config(bg='SystemButtonFace');b54.config(bg='SystemButtonFace');b46.config(bg='SystemButtonFace');b45.config(bg='SystemButtonFace');b44.config(bg='SystemButtonFace');b43.config(bg='SystemButtonFace');b41.config(bg='SystemButtonFace');b39.config(bg='SystemButtonFace');b38.config(bg='SystemButtonFace');a84.config(bg='SystemButtonFace');a93.config(bg='SystemButtonFace');a94.config(bg='SystemButtonFace');a95.config(bg='SystemButtonFace');a89.config(bg='SystemButtonFace');a86.config(bg='SystemButtonFace');a83.config(bg='SystemButtonFace');a82.config(bg='SystemButtonFace');a81.config(bg='SystemButtonFace');a80.config(bg='SystemButtonFace');a79.config(bg='SystemButtonFace');a78.config(bg='SystemButtonFace');a77.config(bg='SystemButtonFace');a76.config(bg='SystemButtonFace');a75.config(bg='SystemButtonFace');a74.config(bg='SystemButtonFace');a61.config(bg='SystemButtonFace');a57.config(bg='SystemButtonFace');a55.config(bg='SystemButtonFace');a54.config(bg='SystemButtonFace');a47.config(bg='SystemButtonFace');a46.config(bg='SystemButtonFace');a45.config(bg='SystemButtonFace');a44.config(bg='SystemButtonFace');a43.config(bg='SystemButtonFace');a42.config(bg='SystemButtonFace');a30.config(bg='SystemButtonFace');a09.config(bg='SystemButtonFace');a08.config(bg='SystemButtonFace');a07.config(bg='SystemButtonFace');a06.config(bg='SystemButtonFace');a03.config(bg='SystemButtonFace');a01.config(bg='SystemButtonFace');a00.config(bg='#a8a8ff');a27.config(bg='SystemButtonFace');a22.config(bg='#a8a8ff');a24.config(bg='#a8a8ff');a26.config(bg='#a8a8ff');a20.config(bg='#ff9393');a18.config(bg='#ff9393');a16.config(bg='#f8fea9');a14.config(bg='#a8a8ff');a11.config(bg='#a8a8ff');a9.config(bg='SystemButtonFace');a2.config(bg='SystemButtonFace');a3.config(bg='SystemButtonFace');a4.config(bg='SystemButtonFace');a6.config(bg='SystemButtonFace')
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
    for i in a28:
        VideoFileClip(i).write_videofile('file.mkv',threads=8,logger=None,codec='libx264')
def d08():
    j()
    a16.config(text='c media',state=NORMAL,command=d09)
    a01.place(x=390*u,y=310*u)
    a01.delete(0,'end')
    a01.insert(0,'format: (e.g. mp4)')
def d54():
    d56=randint(0,239)
    d53.place(x=250,y=13)
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
    global b74,b40,d84
    b74,b40,d84=[False]*3
    d88.place_forget();d85.place_forget();c66.place_forget();d72.place_forget();d59.pack_forget();d58.place_forget();d40.place_forget();d38.place_forget();d36.place_forget();d34.place_forget();d30.place_forget();d29.place_forget();d27.place_forget();d26.place_forget();d24.place_forget();d19.place_forget();d22.place_forget();d18.place_forget();d14.place_forget();d12.place_forget();d11.place_forget();d05.place_forget();d04.place_forget();d03.place_forget();d02.place_forget();d00.place_forget();c94.place_forget();c90.place_forget();c88.place_forget();c86.place_forget();c84.place_forget();c75.place_forget();c72.place_forget();c73.place_forget();c69.place_forget();c67.place_forget();c65.place_forget();c57.place_forget();c56.place_forget();c55.place_forget();c54.place_forget();c51.place_forget();c49.place_forget();c45.place_forget();c44.place_forget();c42.place_forget();b57.place_forget();b58.place_forget();b67.place_forget();b68.place_forget();b69.place_forget();b70.place_forget();b71.place_forget();b72.place_forget();c36.place_forget();c37.place_forget();c33.place_forget();c32.place_forget();c31.place_forget();c28.place_forget();c27.place_forget();c21.place_forget();c16.place_forget();c19.place_forget();c7.place_forget();b93.place_forget();c2.place_forget();c09.place_forget();c08.place_forget();c06.place_forget();c04.place_forget();c05.place_forget();c02.place_forget();c00.place_forget();b91.place_forget();b92.place_forget();b88.place_forget();b75.place_forget();b62.place_forget();b61.place_forget();b60.place_forget();b59.place_forget();b57.place_forget();b58.place_forget();b60.place_forget();b59.place_forget();b54.place_forget();b46.place_forget();b45.place_forget();b44.place_forget();b43.place_forget();b41.place_forget();b39.place_forget();b38.place_forget();a84.place_forget();a93.place_forget();a94.place_forget();a95.place_forget();a89.place_forget();a86.place_forget();a83.place_forget();a82.place_forget();a81.place_forget();a80.place_forget();a79.place_forget();a78.place_forget();a77.place_forget();a76.place_forget();a75.place_forget();a74.place_forget();a61.place_forget();a57.place_forget();a55.place_forget();a54.place_forget();a47.place_forget();a46.place_forget();a45.place_forget();a44.place_forget();a43.place_forget();a42.place_forget();a30.place_forget();a09.place_forget();a08.place_forget();a07.place_forget();a06.place_forget();a03.place_forget();a01.place_forget();a00.place_forget();a27.place_forget();a22.place_forget();a24.place_forget();a26.place_forget();a20.place_forget();a18.place_forget();a16.place_forget();a14.place_forget();a11.place_forget();a9.place_forget();a2.place_forget();a3.place_forget();a4.place_forget();a6.place_forget()
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
d72,d59,d58,d53,d40,d38,d36,d34,d30,d29,d27,d26,d24,d22,d19,d18,d14,d12,d11,d03,d02,d00,c94,c90,c88,c86,c84,c75,c72,c73,c69,c67,c57,c56,c55,c54,c51,c49,c48,c44,c45,c42,c36,c37,c31,c28,c27,c14,c21,c19,c16,c7,c08,c06,c04,c05,c02,c00,b93,b91,b92,b87,b88,b75,b67,b68,b69,b70,b71,b72,b60,b66,b61,b62,b59,b57,b58,b54,b46,b45,b44,b43,b41,b39,b38,a93,a94,a95,a89,a86,a83,a82,a81,a80,a79,a78,a77,a76,a75,a74,a61,a57,a55,a54,a47,a46,a45,a44,a43,a42,a30,a09,a08,a07,a06,a03,a01,a00,a28,a27,a22,a24,a26,a20,a18,a16,a14,a11,a9,a2,a3,a4,a6=Button(a,text='Theme',command=d73),Label(a,text='\n\nnew file      ctrl+N                              open     ctrl+O                           home       ctrl+H\n\nopen copy      ctrl+shift+O                    beta       ctrl+alt+O                  open folder       shift+alt+O\n\nsave       ctrl+S                      save new        ctrl+shift+S                         empty recycle bin         shift+alt+E\n\nbackground       ctrl+shift+E                           exit         ctrl+E\n\nsettings      ctrl+T                        undo       ctrl+Z                           redo        ctrl+shift+Z\n\n'),Checkbutton(a,text='ask empty dialog',variable=d57),Label(a,text='clauth is loading...'),OptionMenu(a,d41,'English'),OptionMenu(a,d39,'10','20','30','50','100','ultimate'),Label(a,text='GitHub',fg='blue'),Label(a,text='Quora',fg='blue'),Checkbutton(a,text='show dialog',variable=d31),Checkbutton(a,text='allow run twice',variable=d28,command=d32),Button(a,text='zip',bg='#42da16',command=d17),Checkbutton(a,text='launch on startup',variable=d25),OptionMenu(a,d23,'zip','tar'),Checkbutton(a,text='archive single file',variable=d21),Checkbutton(a,text='delete file after zip',variable=d20),Button(a,text='restore defaults',command=d74),Entry(a),Label(a,text='twitter',fg='blue'),Checkbutton(a,text='stay in background',variable=d10),Label(a,text='this page is empty',fg='darkred',font=(None,15)),Label(a,text='real fps                            fps                        audio bitrate\n\n22                                                                          ',font=(None,13)),Button(a,text='start',command=d01,bg='darkorange',font=(None,20)),Checkbutton(a,text='stay on top',variable=c93,command=c92),Checkbutton(a,text='minimize to tray',variable=c89),Label(a,text='music\n\n\n\n\nsave settings\n\n\n\n\narchive format'),Checkbutton(a,text='exit on close',variable=c87,state=DISABLED),Checkbutton(a,variable=c83,text='ask before exit',command=c85),Button(a,text='own',bg='#a8a8ff'),Button(a,text='convert',command=e),Text(a),Checkbutton(a,text='high resolution',variable=c70,command=c71),OptionMenu(a,c68,'save','reset on every restart','only settings','only app choices'),Button(a,text='common questions',command=c59),Button(a,text='submit',command=c58,bg='#ffee79'),Text(a,font=('Montserrat',13)),Label(a,font=(None,13),fg='dark blue',text='having any question? advice? opinion? bug? or anything you wish to tell us?'),Button(a,text='add file',command=a12),Button(a,text='freeze',command=c50),10,Button(a,text='zoom',command=c46),Button(a,text='zoom out',command=c47),Checkbutton(a,state=DISABLED,text='start with 0',variable=c43),Text(c66,yscrollcommand=c65.set),Checkbutton(a,text='bytes num',variable=c35),Label(a,text='bytes spliter                         show as'),Button(a,text='travel to stw'),Button(a,text='travel to lobby'),False,Checkbutton(a,state=DISABLED,command=c22,text='blank blinking',variable=c20),Checkbutton(a,state=DISABLED,command=c23,text='mate math',variable=c18),Checkbutton(a,state=DISABLED,command=c24,text='glitch',variable=c17),OptionMenu(a,c8,'none','wind','brahms','rain','alone wolf','one mans dream','canon','snow','time','white hats','hooked on you'),Label(a,text='Hot\n\n\n\n\n\n\n\n\nNormal\n\n\n\n\n\n\n\n\n\nCold'),Label(a,text='.',font=(None,50)),Entry(a),Entry(a),Button(a,text='continue',command=c03),Checkbutton(a,text='remmember files path',variable=c01),Label(a,text='turn on after                   turn off after',state=DISABLED),Entry(a,state=DISABLED),Entry(a,state=DISABLED),0,Checkbutton(a,text='enable screen saver',variable=b86,command=b89),Button(a,text='add dir',bg='#a8a8ff',command=b76),Entry(a),Entry(a),Entry(a),Entry(a),Entry(a),Entry(a),Label(a,text='hour     minute    second    frame                           hour     minute    second    frame'),Label(a),Button(a,text='open',command=b63),Button(a,text='extract',command=b64),Label(a,text='start                           end',font=(None,20)),Entry(a),Entry(a),Label(a,text='Reddit',fg='blue'),Entry(a),Entry(a),Entry(a),Label(a,text='#'),Label(a,bg='black'),Checkbutton(a,text='link',variable=a99),Label(a,bg='black'),Entry(a),Button(a,text='browse',command=a96),Button(a,text='start',command=a85),Checkbutton(a,text='round',variable=a72),Button(a,text='choose random and continue',command=b51),Label(a,text='click                to continue'),Checkbutton(a,text='split',variable=a71),Checkbutton(a,text='phrase',variable=a70),Checkbutton(a,text='pattern',variable=a69),Checkbutton(a,text='bits',variable=a68),Checkbutton(a,text='factorial',variable=a67),Checkbutton(a,text='letter',variable=a66),Checkbutton(a,text='reduce',variable=a65),Checkbutton(a,text='count',variable=a64),Checkbutton(a,text='bytes',variable=a63),Checkbutton(a,text='number',variable=a62),Label(a,text='all methods can be modified by passwords',fg='gray'),Label(a,text='please choose a method',fg='red'),Button(a,text='finish',command=a56),Checkbutton(a,text='quick                            \nno time no extra data',command=a36,variable=a48),Checkbutton(a,text='low                                                                                          \nunable to read by other applications suitable for sharing',command=a37,variable=a49),Checkbutton(a,text='high                                                           \nhigh level encryption with more file size',command=a38,variable=a50),Checkbutton(a,text='ultra                                                                                             \nreadable only by clauth app recommended for file storage',command=a39,variable=a51),Checkbutton(a,text='recommended                                                     \na balance for security fast dataless and secure',command=a40,variable=a52),Checkbutton(a,text='custom',command=a41,variable=a53),Label(a,text='Twitch',fg='blue'),Label(a,text='Discord',fg='blue'),Label(a,text='Instagram',fg='blue'),Label(a,text='YouTube',fg='blue'),Label(a,text='made by frost dream',fg='gray',font=(None,30)),Label(a,text='file name already exist',fg='red',font=10),Entry(a),Button(a,text='trash',bg='#a8a8ff',command=a0),[],Listbox(a),Button(a,text='copy',bg='#a8a8ff',command=a21),Button(a,text='rename',bg='#a8a8ff',command=a23),Button(a,text='delete',bg='#a8a8ff',command=a25),Button(a,text='.txt',bg='#ff9393',command=a19),Button(a,text='view',bg='#ff9393',command=a17),Button(a,text='next',bg='#f8fea9',state=DISABLED,command=d45),Button(a,text='remove',bg='#a8a8ff',command=a13),Button(a,text='add',bg='#a8a8ff',command=a12),Button(a,text='translate',command=a8),Text(a),Label(a,text='Enter input in binary or decimal or hexadecimal with "," or "  " or "/" or "\\".'),Button(a,text='compile',command=a5),Label(a,text='invalid syntax',fg='red')
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
b.add_command(label='Aim booster')
a.config(menu=c)
a.protocol('WM_DELETE_WINDOW',c76)
Thread(target=c10).start()
d49=a28.copy()
if int(s[-1]):
    with open(argv[0],'r+b')as s:
        s.seek(getsize(argv[0])-1)
        t=s.read()
        s.seek(getsize(argv[0])-1)
        s.write((t[0]-1).to_bytes(1,'big'))
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
    j()
Thread(target=d54).start()
a.lift()
a.mainloop()
       8 