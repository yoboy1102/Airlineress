import tkinter as tk
from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import customtkinter as ctk
import time
app = ctk.CTk()
app.geometry('1900x800')
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\user data\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def hover_enter(e, k):
                
        for i, v in enumerate(eur_place):
                        if eur_places[i] == eur_places[k] :
                                
                                eur_font[i].configure(underline=True, slant='roman')
                                eur_place[i].configure(font=eur_font[i])
                                if eur_vars[i] == True: 
                                        #eur_vars[i]=False
                                        eur_image_label.configure(image=eur_image[i])
                                        
                                elif eur_vars[i] == False:
                                        #eur_vars[i]=True
                                        eur_image_label.configure(image=eur_image_2[i])
                                
                                #print(i)
                                #yx=v
                                #hover_enters.append(yx)
#print(hover_enters)
#print()

def hover_leave(e, k):

        for i, x in enumerate(eur_place):
                if eur_places[i] == eur_places[k] :

                        eur_font[i].configure(underline=False,  slant='roman')
                        eur_place[i].configure(font=eur_font[i])
                       
                        #eur_image_label.configure(image=eur_image[0])
                        #print(i)
                        #yx= x
                        #hover_enters.append(yx)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
continents = [
        'eur',
        'asia',
        'AMRCS',
        'M_E'
]
eur_variables = [
        'eur_frame',
        'eur_image_paths',
        'eur_image_paths_2',
        'eur_places',
        'eur_image',
        'eur_image_2',
        '',

]

frame_names = ['frame_1',
          #'frame_2',
          #'frame_3',
          #'frame_4'
          ] 
frames = []
colors_frame = ['#0B041B',
          'blue',
          'green',
          'brown']

for i, v in enumerate(frame_names):
        v = ctk.CTkFrame(
                app,
                width=1880,
                height=800,
                fg_color=colors_frame[i]
                )
        v.pack()
        frames.append(v)

for inte, places in enumerate(continents):
        pass

eur_frame = ctk.CTkFrame(
                frames[0],
                #width=1880,
                #height=800,
                fg_color='#0B041B',
                )
eur_frame.place(x=1880/2+300, y =35)


eur_places = [
        'Madrid',
        'Athens',
        'Bali',
        'Berlin',
        'Paris',
        'Rome',
        'London',
        'Vienna',
          ]
eur_image_paths = []
eur_image_paths_2 = []
for places1 in eur_places:
        pi1 = places1+' 1.jpeg'
        pi2 = places1+' 2.jpeg'
        eur_image_paths.append(pi1)
        eur_image_paths_2.append(pi2)

eur_image = []
eur_image_2 =[]

title_font = ctk.CTkFont('Times', 20, 'bold', underline=True)
eur_title = ctk.CTkLabel(
        eur_frame,
        text='TITLE',
        font=title_font
)

eur_title.pack(pady=10)#(x=1880/2+335, y=30)

eur_place = []

placey=60
eur_fonts = [
        'eur_Font1',
        'eur_Font2',
        'eur_Font3',
        'eur_Font4',
        'eur_Font5',
        'eur_Font6',
        'eur_Font7',
        'eur_Font8',
        ]
eur_font = []

for i, v in enumerate(eur_fonts):
        v = ctk.CTkFont('Times', 18, 'bold')
        eur_font.append(v)


colors_test = ['white', 'green','white', 'green','white', 'green','white', 'green','white', 'green','white', 'green']
for k, v in enumerate(eur_places):
        v = ctk.CTkButton(
                eur_frame,
                width=len(eur_places[k])*6,
                height=20+18,
               # placeholder_text='eur_places[k]',
                #placeholder_text_color='black',
                text=eur_places[k],
                text_color_disabled='white',
                state='disabled',
                font=eur_font[k],
                #textvariable=
                bg_color='#0B041B',#colors_test[k],
                fg_color='#0B041B',#colors_test[k]
)                          
                
        v.pack(pady=0)#(x=1880/2+300, y=placey)
        eur_place.append(v)
        placey+=30

for i, img in enumerate(eur_places):
        img = ctk.CTkImage(light_image=Image.open(relative_to_assets(eur_image_paths[i])),
                           dark_image=Image.open(relative_to_assets(eur_image_paths[i])),
                           size=(300, 300))
        eur_image.append(img)
for i, img in enumerate(eur_places):
        img = ctk.CTkImage(light_image=Image.open(relative_to_assets(eur_image_paths_2[i])),
                           dark_image=Image.open(relative_to_assets(eur_image_paths_2[i])),
                           size=(300, 300))
        eur_image_2.append(img)

eur_image_label = ctk.CTkLabel(
        frames[0],
        width=300,
        height=300,
        image=None,
        corner_radius=25,
)            

eur_image_label.place(x=1880/2-100, y=85)

eur_vars = [True,True,True,True,True,True,True,True]
#for v in eur_vars:
 #       v=True


eur_place[0].bind('<Enter>', lambda f: hover_enter(e=E, k=0)) 
eur_place[0].bind('<Leave>', lambda f: hover_leave(e=E, k=0))

eur_place[1].bind('<Enter>', lambda f: hover_enter(e=E, k=1)) 
eur_place[1].bind('<Leave>', lambda f: hover_leave(e=E, k=1))  
    
eur_place[2].bind('<Enter>', lambda f: hover_enter(e=E, k=2)) 
eur_place[2].bind('<Leave>', lambda f: hover_leave(e=E, k=2)) 

eur_place[3].bind('<Enter>', lambda f: hover_enter(e=E, k=3)) 
eur_place[3].bind('<Leave>', lambda f: hover_leave(e=E, k=3)) 

eur_place[4].bind('<Enter>', lambda f: hover_enter(e=E, k=4)) 
eur_place[4].bind('<Leave>', lambda f: hover_leave(e=E, k=4))
     
eur_place[5].bind('<Enter>', lambda f: hover_enter(e=E, k=5)) 
eur_place[5].bind('<Leave>', lambda f: hover_leave(e=E, k=5)) 

eur_place[6].bind('<Enter>', lambda f: hover_enter(e=E, k=6)) 
eur_place[6].bind('<Leave>', lambda f: hover_leave(e=E, k=6)) 

eur_place[7].bind('<Enter>', lambda f: hover_enter(e=E, k=7)) 
eur_place[7].bind('<Leave>', lambda f: hover_leave(e=E, k=7))       
                
app.mainloop()

eur_variables = [
        'eur_frame',
        'eur_frame_1',
        'eur_frame_2',
        'eur_image_paths',
        'eur_image_paths_2',
        'eur_place'
        'eur_places',
        'eur_image',
        'eur_image_2',
        'eur_title',
        'eur_fonts',
        'eur_font',
        'eur_image_label',
        'eur_vars'
]
'''def hover_enter_eur(e, k):
        conts = continent[0]                
        for i, v in enumerate(conts[5]):
                        if conts[6][i] == conts[6][k] :
                                conts[11][i].configure(underline=True, slant='roman')
                                conts[5][i].configure(font=conts[11][i])
                                conts[12].configure(image=conts[7][i])       
                                
def hover_leave_eur(e, k):
        conts = continent[0]
        for i, x in enumerate(conts[5]):
                if conts[6][i] == conts[6][k] :
                        conts[11][i].configure(underline=False,  slant='roman')
                        conts[5][i].configure(font=conts[11][i])


def hover_enter_asia(e, k):
        conts = continent[1]                
        for i, v in enumerate(conts[5]):
                        if conts[6][i] == conts[6][k] :
                                conts[11][i].configure(underline=True, slant='roman')
                                conts[5][i].configure(font=conts[11][i])
                                conts[12].configure(image=conts[7][i])       
                                
def hover_leave_asia(e, k):
        conts = continent[1]
        for i, x in enumerate(conts[5]):
                if conts[6][i] == conts[6][k] :
                        conts[11][i].configure(underline=False,  slant='roman')
                        conts[5][i].configure(font=conts[11][i])


def hover_enter_AMRCS(e, k):
        conts = continent[2]                
        for i, v in enumerate(conts[5]):
                        if conts[6][i] == conts[6][k] :
                                conts[11][i].configure(underline=True, slant='roman')
                                conts[5][i].configure(font=conts[11][i])
                                conts[12].configure(image=conts[7][i])       
                    
def hover_leave_AMRCS(e, k):
        conts = continent[2]
        for i, x in enumerate(conts[5]):
                if conts[6][i] == conts[6][k] :
                        conts[11][i].configure(underline=False,  slant='roman')
                        conts[5][i].configure(font=conts[11][i])


def hover_enter_M_E(e, k):
        conts = continent[3]                
        for i, v in enumerate(conts[5]):
                        if conts[6][i] == conts[6][k] :
                                conts[11][i].configure(underline=True, slant='roman')
                                conts[5][i].configure(font=conts[11][i])
                                conts[12].configure(image=conts[7][i])       
                                print('hello world')              

def hover_leave_M_E(e, k):
        conts = continent[3]
        for i, x in enumerate(conts[5]):
                if conts[6][i] == conts[6][k] :
                        conts[11][i].configure(underline=False,  slant='roman')
                        conts[5][i].configure(font=conts[11][i])
                        print('bye - world')
                       

hover_enter = [hover_enter_eur, hover_enter_asia, hover_enter_AMRCS,hover_enter_M_E]
hover_leave = [hover_leave_eur, hover_enter_asia, hover_enter_AMRCS,hover_enter_M_E]'''