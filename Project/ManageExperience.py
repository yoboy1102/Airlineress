import customtkinter as ctk
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\Project\Text Files")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def read_file(path):
    with open(path, 'r') as ff:
        ff.readline()
        fff = ff.read()
        return fff

def Manage_Exp(frames, page, font1, f_head):
    
    def btn_creator(root, text, font, i, j, f_head):
        btn = ctk.CTkButton(root, text=text, font=font, text_color='#D8EADF', fg_color='transparent', border_width=0, hover_color='#CCD09F', hover=FALSE)
        btn.grid(row=i, column=0, pady=9, padx=0, sticky='w')
        btn.columnconfigure(0, weight=1)
        #btn.pack(anchor='w', pady=8, padx=0)
        if f_head==True:
            if i>1:
                btn_hover(btn, font)
        else:
            btn_hover(btn, font)
    def btn_hover(btn, font):
        def hover_in(e):
            font.configure(slant='roman', underline=True)
            btn.configure(font=font)
        def hover_out(e):
            font.configure(slant='roman', underline=False)
            btn.configure(font=font)
        btn.bind("<Leave>", hover_out)
        btn.bind("<Enter>", hover_in)

        


#FRAME=================================================================================================================================
    sze_frm_h, frms = [100, 200], []
    frame = ctk.CTkFrame(frames, width=1880, height=sum(sze_frm_h), fg_color='black')
    frame.pack_propagate(False)
    #frame.pack()
    
    for i in range(2):
        frm = ctk.CTkFrame(frames, bg_color='transparent', fg_color='transparent', corner_radius=0, height=sze_frm_h[i], width=1580, border_width=0)
        frm.pack(pady=1)
        frm.pack_propagate(False)
        frm.grid_propagate(False)
        frms.append(frm)

#FIRST FRAME=================================================================================================================================
    fff = read_file(relative_to_assets(f'{page}\Header.txt'))
    fff = fff.split('\n')
    root1=frms[0]
    #font1=('Imprint MT Shadow', 24, 'italic', 'bold')
    for i in range(2):
        header_lbl = ctk.CTkLabel(root1, text=fff[i], font=font1, text_color='#CCD09F')#D8EADF
        header_lbl.pack(anchor='w', pady=10, padx=5)

#SECOND FRAME=================================================================================================================================
    plc_frame = ctk.CTkFrame(frms[1], width=1580, height=100, bg_color='transparent', fg_color='transparent', corner_radius=0, border_width=0)
    plc_frame.place(x=55, y=10)
    
    jj, ii, in_list = 0, 0, []
    fff = read_file(relative_to_assets(f'{page}\Footer.txt'))
    fff = fff.split('\n')
    print(fff)

    for i in range(2):
        in_frm = ctk.CTkFrame(plc_frame, width=320, height=200, bg_color='transparent', fg_color='transparent', corner_radius=0, border_width=0)
        in_frm.grid(row=0, column=i, pady=5, padx=55)
        in_frm.pack_propagate(False)
        in_list.append(in_frm)
    
    for i, v in enumerate(fff):
        if i%2==0:
            ii+=1
            jj=0
        else:
            jj+=1
        font2=ctk.CTkFont('Georgia', 16, 'bold', 'roman')
        btn_creator(in_list[jj], v, font2, i, jj, f_head)

def managemenu(frames):
    Manage_Exp(frames,'Manage')

def ExperienceMenu(frames):
    Manage_Exp(frames,'Experience')
'''''''''
web = ctk.CTk()
web.geometry('1880x500')
font1= ctk.CTkFont('Imprint MT Shadow', 24, 'bold', 'roman')
Manage_Exp(web,'Experience', font1, True)
Manage_Exp(web,'Manage', font1, False)
web.mainloop()
'''''''''