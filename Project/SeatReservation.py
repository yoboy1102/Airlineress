#SeatReservation

import customtkinter as ctk
import PIL
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from TopMenu import TopMenu

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def radd(x , m, n):
    pass




def SeatRes(window):
    def CBcheck_val(p, q):
        print(p, q)
        print(eco_rad[p])
        for i in eco_rad:
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
    all_frm.place(x=417-20, y=505)
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
    let_list = [' A', 'B ', ' C ', 'D ', ' E', ' F ']

    n, m=4, 6    

    var = ctk.IntVar()
    eco_rad = []
    k,l=0, 0
    for i in range(m):
        ff=0
        v = []
        let_new = let_list[0:n]
        let_new.insert(int(n/2), '    ')
        for j in range(n):
            
            var = ctk.IntVar(eco_buss[0])  
            ff+=1.4
            
            #print(ff, int(ff), int(ff-1))
            radd = ctk.CTkCheckBox(eco_buss[0],
                                  corner_radius=8, fg_color='#3DCCB2', text=None,
                                  variable=var, 
                                  onvalue=None,
                                  border_color='#3DCCB2', checkbox_height=43, checkbox_width=33,
                                  height=20, width=0, command=lambda: CBcheck_val(k, l))
            #vED5E7A
            radd.grid(row=i+1, column=int(ff-1), padx=3, pady=10)
            v.append(radd)
            v.append(l)
            l+=1  
            if i==0:
                le_lbll =  ctk.CTkLabel(eco_buss[0],
                                    text=let_new[int(ff-1)], font=('georgia', 14, 'bold'),
                                    #text_color=''
                                    )
                le_lbll.grid(row=i, column=int(ff-1), sticky='s')  
        n0_lbll = ctk.CTkLabel(eco_buss[0], text=str(i+1)+'  ',font=('georgia', 14, 'bold'))
        n0_lbll.grid(row=i+1, column=2)

        emp_label = ctk.CTkLabel(eco_buss[0], text=let_new[int(n/2)])
        emp_label.grid(row=0, column=(int(n/2)))

        eco_rad.append(v)
        eco_rad.append(k)
        k+=1
    TopMenu(window, canvas_2, -50)
    
web=ctk.CTk()
web.geometry('1880x1000')
SeatRes(web)
web.mainloop()
