# -*- coding: UTF-8 -*-
import webbrowser
import tkinter as tk  # 使用Tkinter前需要先导入


# 第1步，实例化object，建立窗口window
window = tk.Tk()

window.title("定边采油厂党建平台")
# 设置小图标
window.iconbitmap("./icon/db.ico")

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('600x60')  # 这里的乘是小x
window.iconname("定边采油厂")

def open(url):
    webbrowser.open(url)

btn1 = tk.Button(window, text='主网址',  width=10, height=1, font=('微软雅黑', 14), command=open("http://116.196.78.130/") )
btn1.place(x=5, y=5, anchor='nw')

btn2 = tk.Button(window, text='主网址1',  width=10, height=1, font=('微软雅黑', 14), command=open("http://dbcycdjpt.com/") )
btn2.place(x=145, y=5, anchor='nw')

btn3 = tk.Button(window, text='备用网址1',  width=10, height=1, font=('微软雅黑', 14), command=open("http://dj.micuer.com/") )
btn3.place(x=290, y=5, anchor='nw')

btn4 = tk.Button(window, text='备用网址2',  width=10, height=1, font=('微软雅黑', 14), command=open("http://dingbian.hvtong.cn/") )
btn4.place(x=435, y=5, anchor='nw')

window.mainloop()