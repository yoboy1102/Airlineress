#SeatReservation

import customtkinter as ctk
import PIL
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from TopMenu import TopMenu
from SeatResFunc import SeatResFunc

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def SeatRes(window):
    def CBcheck_val(p, q, er):
        print(len(er))
        print(p+1, let_list[q])
        for h in er:
            for i in h:
                if i == er[p][q]:
                    print(i, i.get())
                    print('a')
                    pass
                elif i!= er[p][q]:
                    if i.get() == 1:
                        print(i, i.get())
                        i.deselect()    
        er[p][q].configure(fg_color='#ED5E7A')
        for i in er:
            break
            print(i)
    canvas_2 = Canvas(
        window,
        bg = "#1E1E1E",
        height = 1000,
        width = 1880,
        bd = 0,
        highlightthickness = 0
    )
    canvas_2.place(x = 0, y = 0)

    seat_frame = ctk.CTkScrollableFrame(window,
                                    fg_color = '#394E7A',
                                    bg_color = '#1E1E1E',
                                    corner_radius = 58,
                                    width=1000,
                                    height=1000-92,
                                    border_color = '#CCD09F',
                                    border_width = 0 
                                    )
    seat_frame.place(x=-50, y=94)
    air_w, air_h = 2445, 2715
    seat_i_frame = ctk.CTkFrame(seat_frame,height=air_h, width=air_w, fg_color='transparent')
    seat_i_frame.pack()
    air_image = ctk.CTkImage(light_image=Image.open(relative_to_assets('Air_Image.png')),
                             dark_image=Image.open(relative_to_assets('Air_Image.png')),
                             size=(air_w, air_h))
    air_label = ctk.CTkLabel(seat_i_frame,
                             image=air_image,
                             #fg_color='white'
                             )
    air_label.place(x=-1880/2.6, y=50)

    all_frm = ctk.CTkFrame(seat_i_frame,
                           width=185, height=1400,
                           corner_radius=15,
                           fg_color='#EAEBFF',
                           bg_color='#EAEBFF',
                           )
    all_frm.place(x=417-34, y=505)
    eco_buss, w_h = [], [312, 420, 470]
    for i in range(3):
        v = ctk.CTkFrame(all_frm,
                           width=185-8, height=w_h[i],
                           corner_radius=25,
                           fg_color='white',
                           bg_color='transparent',
                           )
        v.grid(row=i, column=0, padx=4, pady=20)
        eco_buss.append(v)
    eco_rad,bus_rad = [],[]

    let_list = [' A', 'B ', ' C ', 'D ', ' E', ' F ']

    n, m=4, 6    

    var = ctk.IntVar()

    SeatResFunc(6, 4, eco_buss[0], CBcheck_val, 1.4, 33, bus_rad)
    SeatResFunc(8, 6, eco_buss[1], CBcheck_val, 1.3, 26, eco_rad)
    TopMenu(window, canvas_2, -50)
    
web=ctk.CTk()
web.geometry('1880x1000')
SeatRes(web)
web.mainloop()
