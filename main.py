#encoding-utf-8
#Importing UTILS
import os
from typing import Any
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4
from datetime import datetime

#IMPORTING tkinter WIDGETS:
from tkinter.tix import *
from tkinter import *
from tkinter import filedialog, Frame
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.tix import *

metainfo = Tk()
metainfo.title("Metadoon")
# Obtém o tamanho da tela
monitor_height = metainfo.winfo_screenheight()
monitor_width = metainfo.winfo_screenwidth()
pipeH = round(monitor_height * 75/100)
pipeW = round(monitor_width * 60/100)
largura_janela =  pipeW
altura_janela = pipeH
class functional():
    def get_screen_size(metainfo):
        screen_width = metainfo.winfo_screenwidth()
        screen_height = metainfo.winfo_screenheight()
        return screen_width, screen_height
largura_tela, altura_tela = functional.get_screen_size(metainfo)

# Calcula as coordenadas para o centro da tela
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
# Define o tamanho e a posição da janela
metainfo.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
#metainfo.eval('tk::PlaceWindow . center')
metainfo.configure(background="blue",)
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
#Creating frames
frame_1 = Frame(f1, borderwidth=5, relief="solid",background='#04322b')
frame_1.pack(fill=BOTH, expand=True)
frame_2 = Frame(f1,borderwidth=5 ,relief="solid" ,background='#04322b')
frame_2.pack(fill=BOTH, expand=True)
frame_3 = Frame(f1,borderwidth=5 ,relief="solid" ,background='#04322b')
frame_3.pack(fill=BOTH, expand=True)
#secondary frames
f1_ = Frame(frame_1,borderwidth=5, relief="solid",background='white')
f1_.grid(column=0, row=1)
f2_ =Frame(frame_1,borderwidth=5, relief="solid",background='white')
f2_.grid(column=1, row=1)
f3_ =Frame(frame_1,borderwidth=5, relief="solid",background='white')
f3_.grid(column=2, row=1)
#identifiers frame_1
seq_id_box = Label(frame_1, text='Imput a sequence:',background='#04322b', foreground='White')
seq_id_box.grid(column=0, row=0)
detail_ = Label(frame_1, text='Detail:',background='#04322b', foreground='White')
detail_.grid(column=1, row=0)
bt_ = Label(frame_1, text='What to do ?',background='#04322b', foreground='White')
bt_.grid(column=2, row=0)
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