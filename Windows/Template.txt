#encoding-utf-8
#Importing UTILS
import os
from typing import Any
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4
from datetime import datetime
import getpass
import platform
#IMPORTING tkinter WIDGETS:
from tkinter import *
from tkinter import filedialog, Frame
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

#class container:
class container:
    dir_name = os.path.dirname(__file__)
    _LIST_db = ["Use your own database..."]




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

messagebox.showinfo("WELCOME TO METADDOON","This is a pipeline called Metadoon, aimed at processing 16S data. \nMetadoon has a graphical interface.\nEnjoy!")


metainfo = Tk()
monitor_height = metainfo.winfo_screenheight()
monitor_width = metainfo.winfo_screenwidth()
pipeH = round(monitor_height * 75/100)
pipeW = round(monitor_width * 40/100)
metainfo.title("Metadoon")
metainfo.geometry(f"{pipeW}x{pipeH}")
metainfo.configure(background="gray")
# icon app
#metainfo.iconphoto(TRUE, PhotoImage(file=fr'{container.dir_name}/metainfo_TOOLS/_icon.png'))
#Creating menu
menubar = Menu(metainfo)
metainfo.config(menu=menubar)
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

#creating layouts 
Ulabel = Label(metainfo, text="Usearch")
Ulabel.pack(expand=True)
uframe = Frame(metainfo, borderwidth=5, relief="solid")
uframe.pack(fill="both", expand=True)

trimlabel = Label(metainfo, text="Trimmomatic")
trimlabel.pack(expand=True)
trimframe = Frame(metainfo, borderwidth=5, relief="solid")
trimframe.pack(fill="both", expand=True)
#_console = Frame(metainfo, borderwidth=5, relief="raised")
#_console.pack(expand=True)
# 1
en_miss = Entry(uframe, bd=2, font=("Calibri", 9), justify=CENTER)
en_miss.grid(row=1,column=2)
# 2
en_pctid = Entry(uframe, bd=2, font=("Calibri", 9), justify=CENTER)
en_pctid.grid(row=1,column=3)
# 3
en_MEE = Entry(uframe, bd=2, font=("Calibri", 9), justify=CENTER)
en_MEE.grid(row=1,column=4)
# 4
en_name_project = Entry(uframe, bd=2, font=("Calibri", 9), justify=CENTER)
en_name_project.grid(row=0,column=3)
#inner label usearch
lab_name_of_project = Label(uframe, text="Give a name to your data:")
lab_name_of_project.grid(row=0,column=2)

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
#layout
# Campo de entrada para inserção de comandos
#entry_comand = Entry(_console)
#entry_comand.pack(expand=True)

# Botão para executar o comando
#botao_executar = Button(_console, text="Executar Comando", command=_functions_.window_functions.executar_comando())
#botao_executar.pack(expand=True)

# Área de texto para mostrar a saída dos comandos
#texto_output = scrolledtext.ScrolledText(_console)
#texto_output.pack(fill="both", expand=True)
#comands for menuboxes:
#file menu
file_menu.add_command(label='New', command= _functions_.window_functions.create_file())
file_menu.add_command(label='Open...',command= _functions_.window_functions.openf())
file_menu.add_command(label='Close',command='')
file_menu.add_separator()
file_menu.add_command(
label='Exit',
command=metainfo.destroy
)
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