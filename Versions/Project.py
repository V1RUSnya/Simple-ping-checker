from ping3 import ping, verbose_ping
import time
from tkinter import *

def pingg():
    q = ping('8.8.8.8')
    q1 = int(q * 1000)
    q1 = str(q1)
    lbl.configure(text='Google = ' +q1)
    w = ping('77.88.8.8')
    w1 = int(w * 1000)
    w1 = str(w1)
    lbla.configure(text='Yandex = ' +w1)
    e = ping('1.1.1.1')
    e1 = int(e * 1000)
    e1 = str(e1)
    lblb.configure(text='CloudFlare = ' +e1)
    print('G ' + q1 + ' Y ' + w1 + ' CF ' + e1)

root = Tk()

#root['bg'] = 'white'
root.title('Ping')
root.wm_attributes('-alpha', 0.7)
root.geometry('300x150') 

root.resizable(width=False, height=False)

lbl = Label(root, text='Google = ', font=('Arial Blod', 30))
lbl.grid(column=0, row=0)

lbla = Label(root, text='Yandex = ', font=('Arial Blod', 30))
lbla.grid(column=0, row=1)

lblb = Label(root, text='CloudFlare = ', font=('Arial Blod', 30))
lblb.grid(column=0, row=2)


#btn = Button(root, text='Ping', command=pingg)
#btn.grid(column=1, row=0)
#root.mainloop()

a=0
while True:
    a = a+1
    pingg()
    root.update()
    time.sleep(3)

