#SeatReservation
import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from TopMenu import TopMenu
from SeatResFunc import SeatResFunc
from SeatResFunc import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path) 

def SeatRes(window, list_no_pass, count_pass):

    def CBcheck_val(bools, p, q, er, alph, n__0, clrr):
        print(len(er))
        print(n__0+p,alph[q][0], q+1)
        er[n_0+p-1][q].configure(fg_color='#ED5B80', hover_color='#ED5B80')
        for h in er:   
            for i in h:
                    
                    if i == er[p][q]:
                        #F6C0CF'
                        print(i, i.get())
                        print('a')
                        pass
                    elif i!= er[p][q] and i.cget("state")=='normal':
                        if i.get() == 1:
                            print(i, i.get())
                            i.deselect()
                            i.configure(fg_color=clrr[0], hover_color=clrr[1]) 
           
        er[n_0+p-1][q].configure(fg_color='#ED5B80', hover_color='#ED5B80')

    canvas_2 = Canvas(
        window,
        bg = "#1E1E1E", bd = 0,  height = 1000, width = 1880,
        highlightthickness = 0)
    canvas_2.place(x = 0, y = 0)
    
    s_frm_w= 1200
    seat_frame = ctk.CTkScrollableFrame(window,
                                    fg_color = '#0A2355', bg_color = '#1E1E1E',
                                    corner_radius = 58,width=s_frm_w, height=1000-92,
                                    border_color = '#CCD09F', border_width = 0, )
    seat_frame.place(x=-50, y=94)
    air_w, air_h = s_frm_w+1700, 3285
    seat_i_frame = ctk.CTkFrame(seat_frame,height=air_h, width=air_w, fg_color='transparent')
    seat_i_frame.pack()

    air_image = ctk.CTkImage(light_image=Image.open(relative_to_assets('Air_Image.png')),
                             dark_image=Image.open(relative_to_assets('Air_Image.png')),
                             size=(air_w, air_h))
    air_label = ctk.CTkLabel(seat_i_frame,image=air_image,)
    air_label.place(x=-(air_w/2)/(s_frm_w/720.25), y=40)

    all_frm = ctk.CTkFrame(seat_i_frame,
                           width=185, height=1400,corner_radius=15,
                           fg_color='#EAEBFF', bg_color='#EAEBFF',)
    all_frm.place(x=s_frm_w/2.748, y=559)
    eco_buss, w_h = [], [312, 420, 470]

    exit_row_img = ctk.CTkImage(light_image=Image.open(relative_to_assets(r'Exit row.png')),
                            dark_image=Image.open(relative_to_assets(r'Exit row.png')),
                            size=(200, 20)) 

    for i in range(3*2):
        if i%2==0:
            v = ctk.CTkFrame(all_frm,
                            width=185-8, height=w_h[i//2],
                            corner_radius=25, fg_color='white',
                            bg_color='transparent',
                            )
            v.grid(row=i, column=0, padx=4, pady=3)
            eco_buss.append(v)
        else:
            v = ctk.CTkLabel(all_frm,
                            image=exit_row_img, text='')
            v.grid(row=i, column=0, padx=4, pady=0, sticky='w')


    bus_rad, eco_rad, ecoradd = [], [], []
    bus_clr, eco_clr = ['#3DCCB2', '#84FFE9'],  ['#5E7FDE', '#9FC9FF'], #['#ED5B80', '#F6C0CF'],
    SeatResFunc(1, 7, 4, 4,  eco_buss[0], CBcheck_val, 1.4, 36, bus_rad, [3,8,11], bus_clr)
    SeatResFunc(2, 11, 6, 0, eco_buss[1], CBcheck_val, 1.3, 28, eco_rad, [2,2,10], eco_clr)
    SeatResFunc(3, 14, 6, 0, eco_buss[2], CBcheck_val, 1.3, 28, ecoradd, [2,2,10], eco_clr)
    TopMenu(window, canvas_2, -50) 
'''web=ctk.CTk()
web.geometry('1880x1000')
SeatRes(web)
web.mainloop()'''
