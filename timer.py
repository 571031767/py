import threading
def fun_timer():
    print("hello word")
    global  timer
    timer = threading.Timer(1,fun_timer)
    timer.start()

timer = threading.Timer(1,fun_timer)
timer.start()