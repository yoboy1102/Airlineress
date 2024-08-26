#Departure

import customtkinter as ctk
import PIL
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from ExploreMenu import continents_explore
from TopMenu import TopMenu
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\user data\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def DepartuePage(window):
    canvas_2 = Canvas(
        window,
        bg = "#282829",
        height = 1000,
        width = 1880,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas_2.place(x = 0, y = 0)
    image_image_Departure = PhotoImage(
        file=relative_to_assets("Departure_bg_2.png"))
    bg_image_pg_2 = ctk.CTkLabel(
        window, 
        image=image_image_Departure,
        text=''
    )
    bg_image_pg_2.place(x=0, y=93)

    main_frame_ticket = ctk.CTkScrollableFrame(
        window,
        height = 425,
        width = 1232,
    )
    main_frame_ticket.place(x=325, y=522)

    for k in range(6):

        image_image_3 = ctk.CTkImage(
            light_image=Image.open(relative_to_assets("tkct_bg.png")),
            dark_image=Image.open(relative_to_assets("tkct_bg.png")),
            size=(485, 64))
        tkct_label = ctk.CTkLabel(
            main_frame_ticket,
            image=image_image_3,
            text=''
        )

        #tkct_label.place(x=342, y=443)

        tkct_label.grid(row=k, column=0, padx=5, pady=5)

        for i in range(2):
            buttonsss_font = ctk.CTkFont('Georgia', 20, weight='bold', underline=True)
            buttonsss = ctk.CTkButton(
                main_frame_ticket,
                fg_color='black',
                #bg_color='black',
                width=356,
                height=64,
                text='From  500',
                font=buttonsss_font,
                text_color='#CCD09F',
                corner_radius=10
                )
            buttonsss.grid(row=k, column=i+1, padx=5, pady=5)

    TopMenu(window, canvas_2)
    web.mainloop

web = ctk.CTk()
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
web.geometry("1880x1000")
web.configure(bg = "#FCFFDD")
DepartuePage(web)

web.mainloop()
