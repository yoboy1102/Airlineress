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
def continents_explore(frames):

        def hover_enter(e, k, j):
                conts = continent[j]                
                for i, v in enumerate(conts[5]):
                                if conts[6][i] == conts[6][k] :
                                        conts[11][i].configure(underline=True, slant='roman')
                                        conts[5][i].configure(font=conts[11][i])
                                        conts[12].configure(image=conts[7][i])       
                                        
        def hover_leave(e, k, j):
                conts = continent[j]
                for i, x in enumerate(conts[5]):
                        if conts[6][i] == conts[6][k] :
                                conts[11][i].configure(underline=False,  slant='roman')
                                conts[5][i].configure(font=conts[11][i])




        #---------------------------------------------------------------------------------------------------------------------------------------------------------------#
        continents = [
                'eur',
                'asia',
                'AMRCS',
                'M_E'
        ]
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
                'eur_vars',
                ''
        ]
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

        asia_variables = [
                'asia_frame',
                'asia_frame_1',
                'asia_frame_2',
                'asia_image_paths',
                'asia_image_paths_2',
                'asia_place'
                'asia_places',
                'asia_image',
                'asia_image_2',
                'asia_title',
                'asia_fonts',
                'asia_font',
                'asia_image_label',
                'asia_vars'
        ]
        asia_places = [
                'Madrid',
                'Athens',
                'Bali',
                'Berlin',
                'Paris',
                'Rome',
                'London',
                'Vienna',
                ]

        AMRCS_variables = [
                'AMRCS_frame',
                'AMRCS_frame_1',
                'AMRCS_frame_2',
                'AMRCS_image_paths',
                'AMRCS_image_paths_2',
                'AMRCS_place'
                'AMRCS_places',
                'AMRCS_image',
                'AMRCS_image_2',
                'AMRCS_title',
                'AMRCS_fonts',
                'AMRCS_font',
                'AMRCS_image_label',
                'AMRCS_vars'
        ]
        AMRCS_places = [
                'Madrid',
                'Athens',
                'Bali',
                'Berlin',
                'Paris',
                'Rome',
                'London',
                'Vienna',
                ]

        M_E_variables = [
                'M_E_frame',
                'M_E_frame_1',
                'M_E_frame_2',
                'M_E_image_paths',
                'M_E_image_paths_2',
                'M_E_place'
                'M_E_places',
                'M_E_image',
                'M_E_image_2',
                'M_E_title',
                'M_E_fonts',
                'M_E_font',
                'M_E_image_label',
                'M_E_vars'
        ]
        M_E_places = [
                'Madrid',
                'Athens',
                'Bali',
                'Berlin',
                'Paris',
                'Rome',
                'London',
                'Vienna',
                ]

        continent = []
        continent.append(eur_variables)
        continent.append(asia_variables)
        continent.append(AMRCS_variables)
        continent.append(M_E_variables)

        all_places = []
        all_places.append(eur_places)
        all_places.append(asia_places)
        all_places.append(AMRCS_places)
        all_places.append(M_E_places)

#_-------------------------------------------------------------------------------------------------------------------------------------------#
        colors_test = ['white', 'green','white', 'green','white', 'green','white', 'green','white', 'green','white', 'green']
#_-------------------------------------------------------------------------------------------------------------------------------------------#

        for cvar, places in enumerate(continents):
                cont = continent[cvar]
                cont[0]= ctk.CTkFrame(
                                frames[0],
                                #width=1880,
                                #height=800,
                                fg_color='transparent',
                                )
                cont[0].grid(row=0, column=cvar, padx = 20, pady=10)
                cont[1] = ctk.CTkFrame(
                                cont[0],
                                #width=1880,
                                #height=800,
                                fg_color='transparent',
                                )
                cont[1].grid(row=0, column=0, padx = 20, pady=10)
                cont[2] = ctk.CTkFrame(
                                cont[0],
                                #width=1880,
                                #height=800,
                                fg_color='transparent',
                                )
                cont[2].grid(row=0, column=1, padx = 20, pady=10)

                
                cont[3] = []
                cont[4] = []


                cont[5] = []
                cont[6] = all_places[cvar]
                for places in cont[6]:
                        pi1 = places+' 1.jpeg'
                        pi2 = places+' 2.jpeg'
                        cont[3].append(pi1)
                        cont[4].append(pi2)
                

                cont[7] = []
                cont[8] =[]

                title_font = ctk.CTkFont('Times', 22, 'bold', underline=True)
                cont[9] = ctk.CTkLabel(
                        cont[2],
                        text='TITLE',
                        font=title_font
                )

                cont[9].pack(pady=0)#(x=1880/2+335, y=30)


                cont[10] = [
                        'eur_Font1',
                        'eur_Font2',
                        'eur_Font3',
                        'eur_Font4',
                        'eur_Font5',
                        'eur_Font6',
                        'eur_Font7',
                        'eur_Font8',
                        ]
                cont[11] = []

                for i, v in enumerate(cont[10]):
                        v = ctk.CTkFont('Times', 18, 'bold')
                        cont[11].append(v)



                for k, v in enumerate(cont[6]):
                        v = ctk.CTkButton(
                                cont[2],
                                width=len(cont[6] [k])*6,
                                height=20+18,
                        # placeholder_text='eur_places[k]',
                                #placeholder_text_color='black',
                                text=cont[6] [k],
                                text_color_disabled='white',
                                state='disabled',
                                font=cont[11][k],
                                #textvariable=
                                bg_color='#0B041B',#colors_test[k],
                                fg_color='#0B041B',#colors_test[k]
                )                          
                                
                        #v.place(x=10, y=placey)
                        v.pack(padx = 10, pady=0)
                        cont[5].append(v)
                szew = 200
                szeh = 300
                for i, img in enumerate(cont[6]):
                        img = ctk.CTkImage(light_image=Image.open(relative_to_assets(cont[3][i])),
                                        dark_image=Image.open(relative_to_assets(cont[3][i])),
                                        size=(szew, szeh))
                        cont[7].append(img)
                for i, img in enumerate(cont[6]):
                        img = ctk.CTkImage(light_image=Image.open(relative_to_assets(cont[4][i])),
                                        dark_image=Image.open(relative_to_assets(cont[4][i])),
                                        size=(szew, szeh))
                        cont[8].append(img)

                cont[12]  = ctk.CTkLabel(
                        cont[1],
                        width=200,
                        height=300,
                        #image=cont[8][3],
                        #corner_radius=25,
                )            

                cont[12].pack(pady=20)#(x=0, y=0)

                #cont[13] = [True,True,True,True,True,True,True,True]
                #for v in eur_vars:
                #       v=True
        #eur
        continent[0][5][0].bind('<Enter>', lambda f: hover_enter(e=E, k=0, j=0)) 
        continent[0][5][0].bind('<Leave>', lambda f: hover_leave(e=E, k=0, j=0))

        continent[0][5][1].bind('<Enter>', lambda f: hover_enter(e=E, k=1, j=0)) 
        continent[0][5][1].bind('<Leave>', lambda f: hover_leave(e=E, k=1, j=0))  
                
        continent[0][5][2].bind('<Enter>', lambda f: hover_enter(e=E, k=2, j=0)) 
        continent[0][5][2].bind('<Leave>', lambda f: hover_leave(e=E, k=2, j=0)) 

        continent[0][5][3].bind('<Enter>', lambda f: hover_enter(e=E, k=3, j=0)) 
        continent[0][5][3].bind('<Leave>', lambda f: hover_leave(e=E, k=3, j=0)) 

        continent[0][5][4].bind('<Enter>', lambda f: hover_enter(e=E, k=4, j=0)) 
        continent[0][5][4].bind('<Leave>', lambda f: hover_leave(e=E, k=4, j=0))
                
        continent[0][5][5].bind('<Enter>', lambda f: hover_enter(e=E, k=5, j=0)) 
        continent[0][5][5].bind('<Leave>', lambda f: hover_leave(e=E, k=5, j=0)) 

        continent[0][5][6].bind('<Enter>', lambda f: hover_enter(e=E, k=6, j=0)) 
        continent[0][5][6].bind('<Leave>', lambda f: hover_leave(e=E, k=6, j=0)) 

        continent[0][5][7].bind('<Enter>', lambda f: hover_enter(e=E, k=7, j=0)) 
        continent[0][5][7].bind('<Leave>', lambda f: hover_leave(e=E, k=7, j=0))

        #asia
        continent[1][5][0].bind('<Enter>', lambda f: hover_enter(e=E, k=0, j=1)) 
        continent[1][5][0].bind('<Leave>', lambda f: hover_leave(e=E, k=0, j=1))

        continent[1][5][1].bind('<Enter>', lambda f: hover_enter(e=E, k=1, j=1)) 
        continent[1][5][1].bind('<Leave>', lambda f: hover_leave(e=E, k=1, j=1))  
                
        continent[1][5][2].bind('<Enter>', lambda f: hover_enter(e=E, k=2, j=1)) 
        continent[1][5][2].bind('<Leave>', lambda f: hover_leave(e=E, k=2, j=1)) 

        continent[1][5][3].bind('<Enter>', lambda f: hover_enter(e=E, k=3, j=1)) 
        continent[1][5][3].bind('<Leave>', lambda f: hover_leave(e=E, k=3, j=1)) 

        continent[1][5][4].bind('<Enter>', lambda f: hover_enter(e=E, k=4, j=1)) 
        continent[1][5][4].bind('<Leave>', lambda f: hover_leave(e=E, k=4, j=1))
                
        continent[1][5][5].bind('<Enter>', lambda f: hover_enter(e=E, k=5, j=1)) 
        continent[1][5][5].bind('<Leave>', lambda f: hover_leave(e=E, k=5, j=1)) 

        continent[1][5][6].bind('<Enter>', lambda f: hover_enter(e=E, k=6, j=1)) 
        continent[1][5][6].bind('<Leave>', lambda f: hover_leave(e=E, k=6, j=1)) 

        continent[1][5][7].bind('<Enter>', lambda f: hover_enter(e=E, k=7, j=1)) 
        continent[1][5][7].bind('<Leave>', lambda f: hover_leave(e=E, k=7, j=1))

        #AMRCS
        continent[2][5][0].bind('<Enter>', lambda f: hover_enter(e=E, k=0, j=2)) 
        continent[2][5][0].bind('<Leave>', lambda f: hover_leave(e=E, k=0, j=2))

        continent[2][5][1].bind('<Enter>', lambda f: hover_enter(e=E, k=1, j=2)) 
        continent[2][5][1].bind('<Leave>', lambda f: hover_leave(e=E, k=1, j=2))  
                
        continent[2][5][2].bind('<Enter>', lambda f: hover_enter(e=E, k=2, j=2)) 
        continent[2][5][2].bind('<Leave>', lambda f: hover_leave(e=E, k=2, j=2)) 

        continent[2][5][3].bind('<Enter>', lambda f: hover_enter(e=E, k=3, j=2)) 
        continent[2][5][3].bind('<Leave>', lambda f: hover_leave(e=E, k=3, j=2)) 

        continent[2][5][4].bind('<Enter>', lambda f: hover_enter(e=E, k=4, j=2)) 
        continent[2][5][4].bind('<Leave>', lambda f: hover_leave(e=E, k=4, j=2))
                
        continent[2][5][5].bind('<Enter>', lambda f: hover_enter(e=E, k=5, j=2)) 
        continent[2][5][5].bind('<Leave>', lambda f: hover_leave(e=E, k=5, j=2)) 

        continent[2][5][6].bind('<Enter>', lambda f: hover_enter(e=E, k=6, j=2)) 
        continent[2][5][6].bind('<Leave>', lambda f: hover_leave(e=E, k=6, j=2)) 

        continent[2][5][7].bind('<Enter>', lambda f: hover_enter(e=E, k=7, j=2)) 
        continent[2][5][7].bind('<Leave>', lambda f: hover_leave(e=E, k=7, j=2))

        #M_E
        continent[3][5][0].bind('<Enter>', lambda f: hover_enter(e=E, k=0, j=3)) 
        continent[3][5][0].bind('<Leave>', lambda f: hover_leave(e=E, k=0, j=3))

        continent[3][5][1].bind('<Enter>', lambda f: hover_enter(e=E, k=1, j=3)) 
        continent[3][5][1].bind('<Leave>', lambda f: hover_leave(e=E, k=1, j=3))  
                
        continent[3][5][2].bind('<Enter>', lambda f: hover_enter(e=E, k=2, j=3)) 
        continent[3][5][2].bind('<Leave>', lambda f: hover_leave(e=E, k=2, j=3)) 

        continent[3][5][3].bind('<Enter>', lambda f: hover_enter(e=E, k=3, j=3)) 
        continent[3][5][3].bind('<Leave>', lambda f: hover_leave(e=E, k=3, j=3)) 

        continent[3][5][4].bind('<Enter>', lambda f: hover_enter(e=E, k=4, j=3)) 
        continent[3][5][4].bind('<Leave>', lambda f: hover_leave(e=E, k=4, j=3))
                
        continent[3][5][5].bind('<Enter>', lambda f: hover_enter(e=E, k=5, j=3)) 
        continent[3][5][5].bind('<Leave>', lambda f: hover_leave(e=E, k=5, j=3)) 

'''        continent[3][5][6].bind('<Enter>', lambda f: hover_enter(e=E, k=6, j=3)) 
        continent[3][5][6].bind('<Leave>', lambda f: hover_leave(e=E, k=6, j=3)) 

        continent[3][5][7].bind('<Enter>', lambda f: hover_enter(e=E, k=7, j=3)) 
        continent[3][5][7].bind('<Leave>', lambda f: hover_leave(e=E, k=7, j=3))'''     

                
app.mainloop()