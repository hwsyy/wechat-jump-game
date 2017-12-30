# -*-coding:utf8-*-  

from PIL import Image, ImageTk
import os
import sys
import Tkinter

pointOne = None
pointTwo = None
window = Tkinter.Tk()
window.title("Jump My Boy")
window.resizable(width=True,height=True)
# window.geometry('600x500+10+20')
# window['bg'] = 'black'

logText = Tkinter.Text(window, width = 50, height = 40, padx = 0)
logText.pack(side = Tkinter.LEFT)

def log(msg):
    print msg
    logText.insert(Tkinter.END,msg + '\n')#END表示在末尾处插入 
    pass

def getImage():
    png = Image.open('E:/test/jump.png')
    w, h = png.size
    png = png.resize((w / 2, h / 2), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(png)
    return photo

photo=getImage()
imglabel = Tkinter.Label(window, image=photo, width = 350, heigh = 620)
imglabel.pack(side = Tkinter.RIGHT)

val = Tkinter.StringVar()
def radcall():
    global val
    log('***************select****************')
    log("selected point name:" + val.get())
r1 = Tkinter.Radiobutton(window, text = "one", variable = val, value = "one", command = radcall)
r1.place(x = 100, y = 10)
r2 = Tkinter.Radiobutton(window, text = "two", variable = val, value = "two", command = radcall)
r2.place(x = 200, y = 10)

def pressThree(e):
    log('***************point****************')
    global pointOne
    global pointTwo
    global val
    if val.get() == 'one':
        pointOne = e
        pass
    elif val.get() == 'two':
        pointTwo = e
        pass
    else:
        log('please select point name ...')
        return
    log("setPoint:" + val.get())
    log("value:" + str(e.x) + "," + str(e.y))
    pass
window.bind('<Button-3>',pressThree)

def pullFunc():
    global png
    global photo
    global imglabel
    global pointOne
    global pointTwo
    global val
    log('\n===============start================')
    log('***************pull****************')
    log('taking the picture ...')
    os.system(' adb shell screencap -p /sdcard/jump.png')
    log('pulling the picture ...')
    os.system('adb pull /sdcard/jump.png E:/test/')
    # set image 
    log('setting the picture ...')
    photo=getImage()
    imglabel['image'] = photo
    imglabel.pack(side = Tkinter.RIGHT)
    # clear
    pointOne == None
    pointTwo == None
pullBtn = Tkinter.Button(window,command = pullFunc, text = 'pull', width = 5)
pullBtn.place(x = 100, y = 580)

def pushFunc():
    log('***************push****************')
    global pointOne
    global pointTwo
    global val
    if val == '' or pointOne == None or pointTwo == None:
        log('please set the points ...')
        return
        pass
    log('playing the game ...')
    x1 = int(pointOne.x)
    y1 = int(pointOne.y)
    x2 = int(pointTwo.x)
    y2 = int(pointTwo.y)
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    time = int(distance * 4.4)       
    log('distance:' + str(distance))
    log('time:' + str(time))
    os.system('adb shell input touchscreen swipe 200 200 200 200 ' + str(time))
    pointOne == None
    pointTwo == None
    log('===========end===============\n')
    pass
pushBtn = Tkinter.Button(window,command = pushFunc, text = 'push', width = 5)
pushBtn.place(x = 200, y = 580)


 
log('\nWelcome To Py Jump Game !\n')#END表示在末尾处插入 
log('1. connect android with usb')
log('2. adb connect')
log('3. open jump game and start')
log('4. pull image')
log('5. select point name')
log('6. set point')
log('7. push result')
log('*************************\n\n')#END表示在末尾处插入 

# 进入消息循环
window.mainloop()