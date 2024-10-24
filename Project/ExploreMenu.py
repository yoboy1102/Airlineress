#Explore Menu
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
import customtkinter as ctk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
def continents_explore(frames):

        def hover_enter(e, k, j, l):
                conts = continent[j]                
                for i, v in enumerate(conts[5]):
                                if conts[6][i] == conts[6][k] :
                                        conts[11][i].configure(underline=True, slant='roman')
                                        conts[5][i].configure(font=conts[11][i])
                                        conts[12].configure(image=conts[l][i])
        def hover_leave(e, k, j, l):
                conts = continent[j]
                for i, x in enumerate(conts[5]):
                        if conts[6][i] == conts[6][k] :
                                conts[11][i].configure(underline=False, slant='roman')
                                conts[5][i].configure(font=conts[11][i])
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------#
        continents = ['eur', 'asia', 'AMRCS', 'M_E']
    
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
                'eur_frame_3',
                ''
        ]
        eur_places = [
                'Madrid',
                'Athens',
                'Bali',
                'Berlin',
                'Paris',
                'Rome',
                #'London',
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
                'asia_frame_3'
        ]
        asia_places = [
                'Madrid',
                'Athens',
                'Bali',
                'Berlin',
                'Paris',
                'Rome',
                #'London',
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
                'AMRCS_frame_3'
        ]
        AMRCS_places = [
                'Madrid',
                'Athens',
                'Bali',
                'Berlin',
                'Paris',
                'Rome',
                #'London',
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
                'M_E_frame_3',
                ''
        ]
        M_E_places = [
                'Madrid',
                'Athens',
                'Bali',
                'Berlin',
                'Paris',
                'Rome',
                #'London',
                'Vienna',
                ]

        continent = [eur_variables, asia_variables, AMRCS_variables, M_E_variables]
        all_places = [eur_places, asia_places, AMRCS_places, M_E_places]
        cont_name_title = ['    EUROPE    ','    ASIA    ', '    AMERICAS    ','    MIDDLE-EAST    ']
        
        for cvar, places in enumerate(continents):
                cont = continent[cvar]
                cont[0]= ctk.CTkFrame(
                                frames,
                                #width=1880,
                                #height=800,
                                fg_color='transparent',
                                #border_color='#CCD09F',
                                #border_width=1,
                                corner_radius=10
                                )
                cont[0].grid(row=0, column=cvar, padx = 45, pady=0)
                '''cont[13] = ctk.CTkFrame(
                                cont[0],
                                #width=1880,
                                #height=800,
                                fg_color='transparent',
                                )
                cont[13].grid(row=0, column=0, padx = 10, pady=10)'''
                cont[1] = ctk.CTkFrame(
                                cont[0],
                                #width=1880,
                                #height=800,
                                fg_color='transparent',
                                )
                cont[1].grid(row=1, column=0, padx = 6, pady=10)
                cont[2] = ctk.CTkFrame(
                                cont[0],
                                #width=1880,
                                #height=800,
                                fg_color='transparent',
                                )
                cont[2].grid(row=1, column=1, padx = 6, pady=10)

                
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

                title_font  = ctk.CTkFont('Georgia', 18, 'bold', underline=False)
                
                emp  = ctk.CTkLabel(
                        cont[2],
                        text='',
                        text_color='#A6ACAC',
                        font=title_font
                )  
                emp.pack(pady=3)#(x=1880/2+335, y=30)


                cont[10] = [
                        'Font1',
                        'Font2',
                        'Font3',
                        'Font4',
                        'Font5',
                        'Font6',
                        'Font7',
                        'Font8',
                        ]
                cont[11] = []

                for i, v in enumerate(cont[10]):
                       #v = ctk.CTkFont('Times', 18, 'bold')
                        v = ctk.CTkFont('Georgia', 16, 'bold')
                        cont[11].append(v)

                for k, v in enumerate(cont[6]):
                        v = ctk.CTkButton(
                                cont[2],
                                width=len(cont[6] [k])*6,
                                height=20+18,
                        # placeholder_text='eur_places[k]',
                                #placeholder_text_color='black',
                                text=cont[6][k],
                                text_color_disabled='#CCD09F',#'#CCD09F',
                                state='disabled',
                                font=cont[11][k],
                                #textvariable=
                                bg_color='#0B041B', #'#26294F',#colors_test[k],
                                fg_color='#0B041B',#'#26294F',#colors_test[k]
                )                          
                                
                        #v.place(x=10, y=placey)
                        v.pack(padx = 10, pady=0)
                        cont[5].append(v)
                szew = 200
                szeh = 245
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
                
                cont[9] = ctk.CTkLabel(
                        cont[1],
                        text=cont_name_title[cvar],
                        text_color='#CCD09F',
                        font=title_font
                )

                cont[9].grid(row=0, column=0, padx = 0, pady = 1)
                frameys = ctk.CTkFrame(cont[1],
                                       border_color='#CCD09F',
                                       border_width=2,
                                       fg_color='white',
                                       #corner_radius=10
                                       )
                frameys.grid(row=1, column=0, padx = 0, pady = 15)
                cont[12]  = ctk.CTkLabel(
                        frameys,
                        #cont[1],
                        width=szew,
                        height=szeh,
                        image=cont[8][3],
                        text='',
                        #corner_radius=3,
                )            

                #cont[12].grid(row=1, column=0, padx = 0, pady = 18)
                cont[12].pack(padx=2, pady=2)

                #cont[13] = [True,True,True,True,True,True,True,True]
                #for v in eur_vars:
                #       v=True

        lvaleur =   [7, 7, 7, 7, 7, 7, 7, 7]
        lvalasia =  [7, 7, 7, 7, 7, 7, 7, 7]
        lvalAMRCS = [8, 8, 8, 8, 8, 8, 8, 8]
        lvalM_E =   [8, 8, 8, 8, 8, 8, 8, 8]
        lval = [lvaleur, lvalasia, lvalAMRCS, lvalM_E]
        ccc=5
        for i in range(4):
                for j in range(7):
                        continent[i][ccc][j].bind('<Enter>', lambda E=E, j=j, i=i: hover_enter(e=E, k=j, j=i, l=lval[i][j])) 
                        continent[i][ccc][j].bind('<Leave>', lambda E=E, j=j, i=i: hover_leave(e=E, k=j, j=i, l=lval[i][j]))
