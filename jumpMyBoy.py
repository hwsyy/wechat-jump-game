# -*-coding:utf8-*-  

from PIL import Image, ImageTk
import os
import sys
import Tkinter
import time


pointOne = None
pointTwo = None
pointName = None

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


def pullFunc():
    global png
    global photo
    global imglabel
    global pointOne
    global pointTwo
    global pointName
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
    # set point one
    pointOne = None
    pointTwo = None
    pointName = 'one'
    log('click point one ...')

pullBtn = Tkinter.Button(window,command = pullFunc, text = 'pull', width = 5)
pullBtn.place(x = 100, y = 580)

def pushFunc():
    log('***************push****************')
    global pointOne
    global pointTwo
    global pointName
    if pointName == None or pointOne == None or pointTwo == None:
        log('please set the points ...')
        return
        pass
    log('playing the game ...')
    x1 = int(pointOne.x)
    y1 = int(pointOne.y)
    x2 = int(pointTwo.x)
    y2 = int(pointTwo.y)
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    timeToJump = int(distance * 4.4)       
    log('distance:' + str(distance))
    log('timeToJump:' + str(timeToJump))
    os.system('adb shell input touchscreen swipe 200 200 200 200 ' + str(timeToJump))
    pointOne = None
    pointTwo = None
    pointName = None
    log('===========end===============\n')
    time.sleep(1)
    pullFunc()
    pass

def pressThree(e):
    log('***************point****************')
    global pointOne
    global pointTwo
    global pointName
    if pointName == 'one':
        pointOne = e
    elif pointName == 'two':
        pointTwo = e
    else:
        log('please pull the image ...')
        return
    log("setPoint:" + pointName)
    log("value:" + str(e.x) + "," + str(e.y))
    if pointTwo == None:
        pointName = 'two'
        log('click point two ...')
    else:
        pushFunc()
        return
window.bind('<Button-3>',pressThree)
 
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