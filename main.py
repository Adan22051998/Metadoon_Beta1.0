#encoding-utf-8
#Importing UTILS
import os
from typing import Any
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4
from datetime import datetime
import getpass
import platform
import pip 

#IMPORTING tkinter WIDGETS:
from tkinter.tix import *
from tkinter import *
from tkinter import filedialog, Frame
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.tix import *

metainfo = Tk()
monitor_height = metainfo.winfo_screenheight()
monitor_width = metainfo.winfo_screenwidth()
pipeH = round(monitor_height * 75/100)
pipeW = round(monitor_width * 60/100)
metainfo.title("Metadoon")
metainfo.geometry(f"{pipeW}x{pipeH}")
metainfo.configure(background="gray")
#icon app
metainfo.iconbitmap(default='./Metadoon.ico')
#Defining Functions

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
#Creating-Layouts
f1 = Canvas(metainfo,background='#04322b')
f1.pack(fill=BOTH, expand=True)
#scrollbar
# Create a scrollbar
scrollbar = Scrollbar(f1, orient="vertical", command=f1.yview)
scrollbar.pack(side="right", fill="y")
# Configure the canvas to use the scrollbar
f1.configure(yscrollcommand=scrollbar.set)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
#Creating menu
menubar = Menu(metainfo)
metainfo.config(menu=menubar,background='#04322b')
#menu boxes
file_menu = Menu(
menubar,
tearoff=0
)
top_menu = Menu(
menubar,
tearoff=0
)
help_menu = Menu(
menubar,
tearoff=0
)
#file menu
file_menu.add_command(label='New', command= '')
file_menu.add_command(label='Open...',command= '')
file_menu.add_command(label='Close',command='')
file_menu.add_separator()
file_menu.add_command(label='Exit',command=metainfo.destroy)
#tools menu
top_menu.add_command(label='Console[...]')
top_menu.add_command(label='Conect to Server [SSH...]')
#help menu
help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')
#placing menu
menubar.add_cascade(
label="File",
menu=file_menu
)
menubar.add_cascade(
label="Tools",
menu=top_menu
)
menubar.add_cascade(
label="Help",
menu=help_menu
)
metainfo.mainloop()