from os import scandir
from os.path import isdir
a,b=[r'C:\Users\lenovo\AppData\Local\Programs\Python\Python37-32\Lib'],0
while len(a)!=b:
    for i in scandir(a[b]):
        if isdir(i.path):
            a.append(i.path)
    b+=1
for i in a:
    for j in scandir(i):
        if not isdir(j.path):
            try:
                with open(j.path,'r')as b:
                    with open(j.path,'w')as c:
                        input(''.join([k for k in b.readlines()if k[0]!='#']))
                        #c.write(''.join([k for k in b.readlines()if k[0]!='#']))
                    '''
                    c=''.join([k for k in b.readlines()if k[0]!='#']).split('\'\'\'')
                    c=''.join([c[k]for k in range(0,len(c),2)]).split('\"\"\"')
                with open(j.path,'w')as b:
                    b.write(''.join([c[k]for k in range(0,len(c),2)]))
                    '''
            except:
                pass