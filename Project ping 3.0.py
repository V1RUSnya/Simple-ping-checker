from ping3 import ping, verbose_ping
from time import sleep
import datetime
from tkinter import *

def google():
    try: 
        q = ping('8.8.8.8')
        q1 = int(q * 1000)
        q1 = str(q1)
        lbl.configure(text='Google = ' +q1)
    except:
        print('Сервера Google не доступны!')
        lbl.configure(text='Google = X')
    return q1

def yandex():
    try:
        w = ping('77.88.8.8')
        w1 = int(w * 1000)
        w1 = str(w1)
        lbla.configure(text='Yandex = ' +w1)
    except:
        print('Сервера Yandex не доступны!')
        lbla.configure(text='Yandex = X')
    return w1

def cloud():
    try:
        e = ping('1.1.1.1')
        e1 = int(e * 1000)
        e1 = str(e1)
        lblb.configure(text='CloudFlare = ' +e1)
    except:
        print('Сервера CloudFlare не доступны!')
        lblb.configure(text='CloudFlare = X')
    return e1

root = Tk()
root['bg'] = 'white'
root.title('Ping')
root.geometry('300x150')
root.lift()
root.attributes("-topmost", True)
root.resizable(width=False, height=False)

lbl = Label(root, text='Google = ', font=('Arial Blod', 30), bg="white")
lbl.grid(column=0, row=0)
lbla = Label(root, text='Yandex = ', font=('Arial Blod', 30), bg="white", fg='Orange')
lbla.grid(column=0, row=1)
lblb = Label(root, text='CloudFlare = ', font=('Arial Blod', 30), bg="white", fg='Blue')
lblb.grid(column=0, row=2)

while True:
    try:
        g,y,c = google(),yandex(),cloud()
        print('Google: {0} Yandex: {1} CloudFlare: {2}'.format(g,y,c))
        root.update()
        sleep(1)
    except:
        TimeError = str(datetime.datetime.now().time())
        print('Произошла ошибка! Время {0}'.format(TimeError[0:5]))
        sleep(3)
