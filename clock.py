import time
import tkinter as tk
from tkinter import *
background_color = input("Enter a color (ALL CAPS) for background: ")
color = input("Enter text color: ")
def tick(time1 =''):
 time2 = time.strftime('%I:%M:%S')
 if time2 != time1:
     time1 = time2
     clock_frame.config(text=time2)
     clock_frame.after(200, tick)
     
def fajar_namaz():
 fajar.config(text="05:40       فجر")

def Duhr_namaz():
 duhr.config(text="04:30        ظهر")
def Asar_namaz():
 asar.config(text="05:20        عصر")

def Maghrib_namaz():
 maghrib.config(text="06:10     مغرب")
def Esha_namaz():
 esha.config(text="08:40        عشاء")
def Jummah_namaz():
 esha.config(text="02:40        جمعہ")
root = tk.Tk()
clock_frame = tk.Label(root, font=('arial 100 bold'),bg = background_color, fg=color)
clock_frame.pack(fill='both', expand=1)
fajar = tk.Label(root, font=('arial 50 bold'),bg = background_color,anchor=N, fg=color)
fajar.pack(fill=X)
duhr = tk.Label(root, font=('arial 50 bold'),bg = background_color,anchor=N, fg=color)
duhr.pack(fill=X)
asar = tk.Label(root, font=('arial 50 bold'),bg = background_color,anchor=N, fg=color)
asar.pack(fill=X)
maghrib = tk.Label(root, font=('arial 50 bold'),bg = background_color,anchor=N, fg=color)
maghrib.pack(fill=X)
esha = tk.Label(root, font=('arial 50 bold'),bg = background_color,anchor=N, fg=color)
esha.pack(fill=X)
Jummah = tk.Label(root, font=('arial 50 bold'),bg = background_color,anchor=N, fg=color)
Jummah.pack(fill=X)
root.attributes('-fullscreen', True)
root.configure(background="lightgreen")
tick()
fajar_namaz()
Duhr_namaz()
Asar_namaz()
Maghrib_namaz()
Esha_namaz()
Jummah_namaz()
root.mainloop()
