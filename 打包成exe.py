# 安装 pip3 install pyinstaller
# pyinstaller -F -w -i favicon love.py
#
# pyinstaller -F -w (-i icofile) filename
#
# filename表示你的Python程序文件名
#
# -w 表示隐藏程序运行时的命令行窗口（不加-w会有黑色窗口）
#
# 括号内的为可选参数，-i icofile表示给程序加上图标，图标必须为.ico格式
#
# icofile表示图标的位置，建议直接放在程序文件夹里面，这样子打包的时候直接写文件名就好
#
# 输入完成，按回车，就会开始自动打包了，第一次打包过程可能比较缓慢
#
# 输入示例：
#
# pyinstaller -F -w -i favicon love.py  # -w  运行时不出现黑框
# pyinstaller -F -w -i icon/db.ico dbcyc.py  打包注意事项：如引用了相对路径的文件，需要将文件拷贝到相应文件夹下

