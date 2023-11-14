#encoding-utf-8
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import time
import os
from tkinter import Button, Entry, StringVar, ttk
from tkinter import messagebox


import json
dir_name = os.path.dirname(__file__)
dir_name = dir_name.replace("\\", "/")
###############################################################################################
#janela secundaria
#------------------
#########SCREEN-CONFIGURATION##########
def secondary_window():

    window1 = tk.Toplevel(window)
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



###############################################################################################

#download_
class application_fetch:
    #FASTQC
    Fastqc_universal = "wsl sudo install fastqc"
    Fastqc_permission = "wsl chmod 755 fastqc"
    #TRIMMOMATIC
    Trimmomatic = "wsl sudo apt install trimmomatic"
    #USEARCH
    Usearch = "https://drive5.com/downloads/usearch11.0.667_i86linux32.gz"
    #R-CRAN
    R_script = "wsl sudo apt-get install r-base"
# Create the main window.
window = tk.Tk()
window.title("Metadoon")
# Obtém as dimensões da tela
class functional():
    def get_screen_size(window):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        return screen_width, screen_height

largura_janela = 400
altura_janela = 560

# Obtém o tamanho da tela
largura_tela, altura_tela = functional.get_screen_size(window)

# Calcula as coordenadas para o centro da tela
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
# Define o tamanho e a posição da janela
window.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
window.overrideredirect(True)
# Load the GIF image.
image = Image.open(fr"{dir_name}\OP.png")
image_tk = ImageTk.PhotoImage(image)
# Create a label to display the GIF image.
label1= tk.Label(window, bg='#04322b', fg='white', text='Metadoon is Loading...')
label1.pack(fill='x')
label = tk.Label(window, image=image_tk)
label.pack()
label2= tk.Label(window, bg='black', fg='white', text='Installing Resources...')
label2.pack(fill='x')
#progressbar
progresso = ttk.Progressbar(window, length=10,  mode='indeterminate')
progresso.pack(fill='x')




#installing ressources
def install_dependencies():
    try:
        #os.system(fr'pip install -r requirements.txt')
        os.system('wsl sudo apt update')
        os.system('wsl sudo apt install python3')
        os.system('wsl python3 --version')     
        os.system('wsl sudo apt install python3-pip')
        os.system('wsl pip3 --version')
        os.system('wsl pip install tk')
        
        progresso.update()
        time.sleep(2)
        os.system(fr'MKDIR ./app_to_run')
        
        progresso.update()
        time.sleep(2)
        os.system(fr'{application_fetch.Fastqc_universal}')
        
        progresso.update()
        os.system(fr'{application_fetch.Fastqc_permission}')
        
        progresso.update()
        time.sleep(2)        
        os.system(fr'{application_fetch.Trimmomatic}')
        
        progresso.update()
        time.sleep(2)
        os.system(fr'wsl wget {application_fetch.Usearch}')
        
        progresso.update()
        time.sleep(2)
        os.system(fr'{application_fetch.R_script}')
        
        progresso.update()
        progresso.step()
        time.sleep(2)
        #os.system(fr'wget {application_fetch.Bowtie2}')
        #progresso.step()
        
        return
    except:
        messagebox.showinfo("METADDOON ERROR","SOMETHING WENT WRONG!\n-TRY REINSTAL OR UPGRADE YOUR SYSTEM\n-CHECK YOUR CONNECTION\n-TRY TO CONTACT DEVELOPERS")
        time.sleep(10)
        window.destroy
def check_one(filename):
    global install_dependencies
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if '1' in line:
                os.system(fr'python3 {dir_name}\main.py')
                return print('Opening Metadoon...')

        else:
            with open(fr'{dir_name}/pswd.txt', 'r') as pass_word:
                pass_word = str(pass_word)
                os.system(fr'wsl sudo su')
                time.sleep(2)
                os.system(fr'{pass_word}')
            install_dependencies()
            with open(fr'{dir_name}/verification_mode.txt', 'a') as arquivo:
                arquivo.write('1\n')

    except FileNotFoundError:
        print('Verification file not found, plesase download metadoon again!')

check_one(fr'{dir_name}/verification_mode.txt')
# Start the main loop.
window.mainloop()