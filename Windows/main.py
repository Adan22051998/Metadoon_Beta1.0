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
from tkinter import messagebox
import os
dir_name = os.path.dirname(__file__)
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
metainfo.iconbitmap(default=fr'{dir_name}/Metadoon.ico')
#Defining Functions
#class container:
class container:
    dir_name = os.path.dirname(__file__)
    _LIST_db = ["Use your own database..."]


#class to functions that shall modify the window
class _functions_:
    class window_functions:
        def create_file():
            os.system(f'')
        def openf():
            try:
                file_dir = filedialog.askopenfilename()
                return file_dir
            except:
                messagebox.showinfo("METADDOON","This is not a valid directory!")
        def executar_comando():
            try:
                name_usr = getpass.getuser()
                n_sistem = platform.system()
                comand_ = entry_comand.get()
                output = "Prompt " + name_usr + n_sistem + comand_
                return texto_output.insert(END, output + "\n")
            except:
                None
#classes of aplications
class FastQC:
    outputqc =''
    inputqc = ''
    def do_fatqc():
        try:
            os.system(fr'wsl fastqc -o {outputqc} {inputqc}')
        except:
            print('Something went wrong!')
            messagebox.showinfo("METADDOON","Something Went Wrong")
class Trimmomatic:
    threads = ''
    trimput_1 = ''
    trimput_2 = ''
    trimpout_1 = ''
    trimpout_2 = ''
    trimming_options = ''
    def trim():
        try:
            os.system(fr'trimmomatic PE [-threads <n>] <input_1.fq> <input_2.fq> <output_1.fq> <output_2.fq> <options>')
        except:
            print('Something went wrong!')
            messagebox.showinfo("METADDOON","Something Went Wrong")
class usearch:
    def merge():
        try:
            n1 = en_miss.get()
            n2 = en_pctid.get()
            os.system(fr'./_Usearch -fastq_mergepairs ./Sample/*_R1*.fastq -fastq_maxdiffs {n1} -fastq_pctid {n2} -fastqout ./Metarquivos/Mesclados/_merged.fq -relabel @')
            messagebox.showinfo("METADDOON:", "Fastq/Fasta files merged sucessfuly...")
            return print("Samples Mergeds Sucessfully.")
        
        except:
            messagebox.showinfo("METADDOON:", "Something went wrong!")
            return print("ERROR")
    def quali():
        try:
            n1 = en_MEE.get()
            os.system(fr'./_Usearch -fastq_filter ./Metarquivos/Mesclados/_merged.fq -fastq_maxee {n1} -fastaout ./Metarquivos/Filtro_de_qualidade/_filtered.fa')
            messagebox.showinfo("METADDOON:", "Files filtrated.")
            return print("Quality Filter Applyed.")
        except:
            messagebox.showinfo("METADDOON:", "Something went wrong!")
            return print("ERROR")
    def uniq():
        try:
            os.system(fr'./_Usearch -fastx_uniques ./Metarquivos/Filtro_de_qualidade/_filtered.fa -fastaout ./Metarquivos/Leituras_unicas/_uniques.fa -relabel uniq -sizeout')
            messagebox.showinfo("METADDOON:", "Unique sequences successfully stored.")
        except:
            messagebox.showinfo("METADDOON:", "Something went wrong!")
            return print("ERROR")

    def otus():
        try:
            os.system(fr'./_Usearch -cluster_otus ./Metarquivos/Leituras_unicas/_uniques.fa -minsize 2 -otus ./Metarquivos/Geracao_de_otus/_otus.fa -relabel otu')
            messagebox.showinfo("METADDOON:", "OTUS verification done successfully.")
            return print("The OTU's Have Been Clustered Sucessfully")
        except:
            messagebox.showinfo("METADDOON:", "Something went wrong!")
            return print("ERROR")
    def otutable():
        try:
            os.system(fr'./_Usearch -usearch_global ./Metarquivos/Mesclados/_merged.fq  -db ./Metarquivos/Geracao_de_otus/_otus.fa -strand plus -id 0.97 -otutabout ./Metarquivos/Tabela_de_OTU/_otutable.txt')
            os.system("cd ./Metarquivos/Tabela_de_OTU/ | cp ./Metarquivos/Tabela_de_OTU/_otutable.txt ./Metarquivos/Tabela_de_OTU/_otutable.tsv")
            os.system(fr"Rscript {container.dir_name}/CHAO1.R")
            os.system(fr"Rscript {container.dir_name}/SHANNON.R")
            os.system(fr"Rscript {container.dir_name}/Ace.R")
            os.system(fr"Rscript {container.dir_name}/SIMPSON.R")
            os.system(fr"Rscript {container.dir_name}/RIQUEZA.R")
            os.system(fr"Rscript {container.dir_name}/INV_SIMPSON.R")
            messagebox.showinfo("METADDOON:", "The Otutable is Ready now...")
            return print("")
        except:
            messagebox.showinfo("METADDOON:", "Something went wrong!")
            return print("ERROR")
    def otu16s():
        try:
            xvis_db = CB_DB.get()
            if xvis_db == container._LIST_db[0]:
                db_file_path = filedialog.askopenfilename()
                os.system(fr'./_Usearch -nbc_tax ./Metarquivos/Geracao_de_otus/_otus.fa -db {db_file_path} -strand plus -tabbedout ./Metarquivos/XVI_S_DB/_taxonomy.tsv')
                os.system(fr"Rscript {container.dir_name}/taxax.R")
            messagebox.showinfo("METADDOON:", "Base de dados verificada...")
            return print("DB verification Done.")
        except:
            messagebox.showinfo("METADDOON:", "Something went wrong!")
            return print("ERROR")
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