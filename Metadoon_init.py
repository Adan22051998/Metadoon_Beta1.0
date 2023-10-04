#encoding-utf-8
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import time
import os
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
        os.system(fr'wsl pip install -r requirements.txt')
        time.sleep(2)
        os.system(fr'wsl wget {fastqc}')
        time.sleep(2)
        os.system(fr'wsl MKDIR ./app_to_run')
        time.sleep(2)
        os.system(fr'wsl wget {usearch}')
        time.sleep(2)
        os.system(fr'wsl wget {trimmomatic}')
        time.sleep(2)
        os.system(fr'wsl')
        time.sleep(2)
        return
    except:
        messagebox.showinfo("METADDOON ERRPR","SOMETHING WENT WRONG!\n-TRY REINSTAL OR UPGRADE WSL TO NEWST VERSION\n-CHECK YOUR CONNECTION\n-TRY TO CONTACT DEVELOPERS")
        time.sleep(10)
        window.destroy

# Start the main loop.
window.mainloop()