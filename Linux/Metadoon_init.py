#encoding-utf-8
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import time
import os
dir_name = os.path.dirname(__file__)
#download_
class application_fetch:
    #FASTQC
    Fastqc_universal = "sudo install fastqc"
    Fastqc_permission = "chmod 755 fastqc"
    #TRIMMOMATIC
    Trimmomatic = "sudo apt install trimmomatic"
    #USEARCH
    Usearch = "https://drive5.com/downloads/usearch11.0.667_i86linux32.gz"
    #R-CRAN
    R_script = "sudo apt-get install r-base"
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
image = Image.open(fr".\OP.png")
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
        os.system('sudo apt update')
        os.system('sudo apt install python3-pip')
        os.system('pip3 --version')
        os.system('pip install tk')
        
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
        os.system(fr'wget {application_fetch.Usearch}')
        
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
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if '1' in line:
                os.startfile(fr'{dir_name}\main.py')
                return print('Opening Metadoon...')

        else:
            install_dependencies()
    except FileNotFoundError:
        print('Verification file not found, plesase download metadoon again!')

check_one('verification_mode.txt')
# Start the main loop.
window.mainloop()