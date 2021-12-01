#coding:utf-8

import os
print os.getcwd(a)
note_path=os.getcwd()+'/My Clippings.txt'
f=open(note_path,'r+')
digest_path=os.getcwd()+'/digest/'
os.mkdir(digest_path)
while True:
    onenote=[]
    for i in range(0,5):
        line=f.readline()
        if not line:
            exit()
        onenote.append(line+'==========')
        print onenote[0]
    book_note=open('%s%s.txt' %(digest_path,onenote[0].replace('=','')),'a+')
    book_note.write(onenote[3]+'\n')
    book_note.close()
