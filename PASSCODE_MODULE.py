###########Imports:

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Button, Entry, StringVar, ttk
from tkinter import messagebox
import time
import os
import json

#------------------
#########SCREEN-CONFIGURATION##########
window1 = tk.Tk()
window1.title('Unix-Passcode:')
window1.geometry("300x200")
window_1 = tk.Label(window1, text="UNIX-WSL PASSCODE:")
window_1.pack(pady=10)
#------------------------------
dir_name = os.path.dirname(__file__)
dir_name_unix = dir_name.replace("\\", "/")
#------------------
#getting user passcode window

password = []
entry_module = Entry(window1, width=10)
entry_module.pack(pady=10)
def getpasswd():
    password1 = entry_module.get()
    password.append(password1)
    pswd= fr'{dir_name}\pswd.txt'
    with open(pswd, 'w') as arquivo:
        arquivo.write(json.dumps(password))
    print(password)




button_get = Button(window1, text="Allow", command=getpasswd)
button_get.pack(pady=10)
#------------------------------
window1.mainloop()
