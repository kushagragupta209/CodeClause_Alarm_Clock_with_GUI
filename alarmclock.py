from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime
import time
import winsound
from pygame import mixer

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            sound_alarm()

            break


def stop_time():
    mixer.music.stop()
mixer.init()


def sound_alarm():
        mixer.music.load('mixkit-classic-alarm-995.wav')
        mixer.music.play()
mixer.init()



def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()

clock.title("Alarm Clock")
clock.geometry("400x200")

time_format=Label(clock, text= "Enter time in 24 hour format!", fg="black",font="Arial").place(x=70,y=120)


hour = StringVar()
min = StringVar()
sec = StringVar()

hour_text=Label(clock,text='Hour',font=10,fg='purple').place(x=120,y=40)
hourTime= ttk.Combobox(clock,textvariable = hour,width = 5).place(x=110,y=70)
min_text=Label(clock,text='Min',font=10,fg='purple').place(x=170,y=40)
minTime= ttk.Combobox(clock,textvariable = min,width = 5).place(x=160,y=70)
sec_text=Label(clock,text='Sec',font=10,fg='purple').place(x=220,y=40)
secTime = ttk.Combobox(clock,textvariable = sec,width = 5 ).place(x=210,y=70)
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =200,y=170)
stop_alarm = Button(clock,text = "stop_alarm",fg="red",width = 10,command = stop_time).place(x =110,y=170)

clock.mainloop()
