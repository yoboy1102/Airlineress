#TopMenu

import customtkinter as ctk
import PIL
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from ExploreMenu import continents_explore


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\user data\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def TopMenu(window, canva):
    canva.create_rectangle(
        0.0,
        1.0,
        1880.0,
        92.0,
        fill="#0B031A",
        outline="")


#Sign IN
    button_image_1 = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_1.png")),
                                dark_image=Image.open(relative_to_assets("button_1.png")),
                                size=(167, 39))
    button_1 = ctk.CTkButton(window,
        image=button_image_1,
        border_width=0,
        text='',
        fg_color='#0B041B',
        bg_color='#0B041B',
        hover_color='#0B041B',
        border_color='#0B041B',
        #highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        #relief="flat",
        width=167.0,
        height=34.0
    )
    button_1.place(
        x=1650.0,
        y=27.0,
    )

#logo down
    button_image_2 = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_2.png")),
                                  dark_image=Image.open(relative_to_assets("button_2.png")),
                                  size=(100, 74))
    button_2 = ctk.CTkButton(window,
        image=button_image_2,
        border_width=0,
        text='',
        fg_color='transparent',
        bg_color='#0A071E',
        hover_color='#0A071E',
        border_color='#0A071E',
        #highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        #relief="flat"
        width=100.0,
        height=74.0
    )
    button_2.place(
     x=95.0,
      y=88,   
    )
#logo
    button_image_3 = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_3.png")),
                                dark_image=Image.open(relative_to_assets("button_3.png")),
                                size=(100, 80))
    button_3  = ctk.CTkButton(window,
        image=button_image_3,
        border_width=0,
        text='',
        fg_color='transparent',
        bg_color='#0B041B',
        hover_color='#0B041B',
        border_color='#0B041B',
        #highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        #relief="flat"
        width=100.0,
        height=91.0
    )
    button_3.place(
        x=95.0,
        y=1.0
    )
#Explore
    button_image_4 = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_4.png")),
                                dark_image=Image.open(relative_to_assets("button_4.png")),
                                size=(84, 57))
    button_4 = ctk.CTkButton(window,
        image=button_image_4,
        border_width=0,
        text='',
        fg_color='transparent',
        bg_color='#0B041B',
        hover_color='#0B041B',
        border_color='#0B041B',
        #highlightthickness=0,
        #relief="flat"
        width=84,
        height=57,
        command = lambda :btn(frames[0])
    )
    button_4.place(
        x=316.0,
        y=16.0,
    )
#Manage
    button_image_5 = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_5.png")),
                                dark_image=Image.open(relative_to_assets("button_5.png")),
                                size=(85, 57))
    button_5 = ctk.CTkButton(window,
        image=button_image_5,
        border_width=0,
        text='',
        fg_color='transparent',
        bg_color='#0B041B',
        hover_color='#0B041B',
        border_color='#0B041B',
        #highlightthickness=0,
        #relief="flat"
        width=85,
        height=57,
        command = lambda :btn(frames[1])
    )
    button_5.place(
        x=442.0,
        y=17.0
    )
#Experience
    button_image_6 = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_6.png")),
                                dark_image=Image.open(relative_to_assets("button_6.png")),
                                size=(127, 57))
    button_6 = ctk.CTkButton(window,
        image=button_image_6,
        border_width=0,
        text='',
        fg_color='transparent',
        bg_color='#0B041B',
        hover_color='#0B041B',
        border_color='#0B041B',
        #highlightthickness=0,
        #relief="flat"
        width=127,
        height=57,
        command = lambda :btn(frames[2])
    )
    button_6.place(
        x=569.0,
        y=16.0
    )
#Destinations
    button_image_7 = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_7.png")),
                                dark_image=Image.open(relative_to_assets("button_7.png")),
                                size=(140, 57))
    button_7 = ctk.CTkButton(window,
        image=button_image_7,
        border_width=0,
        text='',
        fg_color='transparent',
        bg_color='#0B041B',
        hover_color='#0B041B',
        border_color='#0B041B',
        #highlightthickness=0,
        #relief="flat"
        width=140,
        height=57,
        command = lambda :btn(frames[3])
    )
    button_7.place(
        x=735.0,
        y=16.0
    )


#Experience
    button_image_hover_6 = ctk.CTkImage(
        light_image=Image.open(relative_to_assets("button_hover_1.png")),
        size=(127, 57))
    def button_6_hover(e):
        button_6.configure(
            image=button_image_hover_6
        )
    def button_6_leave(e):
        button_6.configure(
            image=button_image_6
        )

    button_6.bind('<Enter>', button_6_hover)
    button_6.bind('<Leave>', button_6_leave)
#Explore
    button_image_hover_4 = ctk.CTkImage(
        light_image=Image.open(relative_to_assets("button_hover_2.png")),
        dark_image=Image.open(relative_to_assets("button_hover_2.png")),
        size=(84, 57))
    def button_4_hover(e):
        button_4.configure(
            image=button_image_hover_4
        )
    def button_4_leave(e):
        button_4.configure(
            image=button_image_4
        )

    button_4.bind('<Enter>', button_4_hover)
    button_4.bind('<Leave>', button_4_leave)
#Manage
    button_image_hover_5 = PhotoImage(
        file=relative_to_assets("button_hover_3.png"))
    def button_5_hover(e):
        button_5.configure(
            image=button_image_hover_5
        )
    def button_5_leave(e):
        button_5.configure(
            image=button_image_5
        )

    button_5.bind('<Enter>', button_5_hover)
    button_5.bind('<Leave>', button_5_leave)
#Destinations
    button_image_hover_7 = PhotoImage(
        file=relative_to_assets("button_hover_4.png"))
    def button_7_hover(e):
        button_7.configure(
            image=button_image_hover_7
        )
    def button_7_leave(e):
        button_7.configure(
            image=button_image_7
        )

    button_7.bind('<Enter>', button_7_hover)
    button_7.bind('<Leave>', button_7_leave)    
    
    button_image_hover_1 = PhotoImage(
    file=relative_to_assets("button_hover_5.png"))

    def button_1_hover(e):
        button_1.configure(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        button_1.configure(
            image=button_image_1
        )

    button_1.bind('<Enter>', button_1_hover)
    button_1.bind('<Leave>', button_1_leave)
    framev = ['frame_1','frame_2','frame_3','frame_4'] 
    frames = []
    colors = ['#0B041B','#26294F','#CCD09F','green','brown']
    
    
    for i, v in enumerate(framev):
        v = ctk.CTkFrame(
                window,
                width=1880,
                height=420,
                fg_color=colors[i],
                border_width=1,
                border_color='#CCD09F',#colors[i],
                corner_radius=0
                )
        v.place(x=0,y=1004,)   
        frames.append(v)
    frame_inner_explore = ctk.CTkFrame(
                frames[0],
                width=1600,
                height=200,
                fg_color=colors[0]
                )
    frame_inner_explore.place(x=135, y=18)
    


    #---------------------------=================================-----------------------------================================----------------#
    continents_explore(frames=frame_inner_explore)

    window.resizable(False, False)




global my_y
my_y = 1004
def up(frm):
        frm.place(x=0, y=my_y)
        #button_frame_1.configure(text=my_y)
def down(frm):
        frm.place(x=0, y=my_y)
        #button_frame_1.configure(text=my_y)
def btn(frm):
    global my_y
    if my_y > 93:        
        my_y=93
        frm.place(x=0, y=my_y)
    elif my_y < 1004:      
        my_y=1004
        frm.place(x=0, y=my_y)