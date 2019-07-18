#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from tkinter import  *
import tkinter as tk
import  os,pygame,time
window = Tk()    # 创建窗口对象的背景色
root = Tk()
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
# listb  = Listbox(root)          #  创建两个列表组件
# listb2 = Listbox(root)
# for item in  li :
#     listb.insert(0,item)
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
def t():
    print(1)
def key(event):
    print( "pressed", repr(event.char))

def callback():
    print(11111)
def bofang():
    file = r'./paishou.mp3'
    pygame.mixer.init()
    print("播放音乐1")
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()
    # os.system("paplay 1.wav")

window.title('米醋儿直播音效')
window.geometry('500x200')
btn1 = tk.Button(window,text='one',width=10)
btn1.grid(row=0,column=0)




btn2 = tk.Button(window,text='two',width=10)
btn2.grid(row=0,column=1)
root.geometry('800x300')
Button(root,text="F1金宝音乐",command=bofang).pack()

# btn3 = tk.Button(window,text='three',width=3,height=3,bg='blue')
# btn3.grid(row=1,column=0)
#
# btn4 = tk.Button(window,text='four',width=15,height=10,bg='yellow')
# btn4.grid(row=1,column=1)



# 需要用pygame去播放 mp3
window.mainloop()                 # 进入消息循环


