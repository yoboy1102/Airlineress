#TopMenu
import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
from ExploreMenu import continents_explore
from LogInSignUp import LogIn_SignUp

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def TopMenu(window, canva, yy):
    canva.create_rectangle( 0.0, 0.0, 1880.0, 92.0, fill="#0B031A", outline="")
    
    global hover_image_list, button_image_list, button_list
    button_list, hover_sel, hover_image_list, button_image_list = [], [0, 3, 4, 5, 6], [], []
    btn_sizes_hover = [(167, 39), (84, 57), (85, 57), (127, 57), (140, 57)]
    btn_sizes = [(167, 39), (100, 74), (100, 80), (84, 57), (85, 57), (127, 57), (140, 57)]
    btn_coord = [(1650, 27), (95, yy), (95, 1) , (316, 16), (440, 16), (576, 17), (735, 18)]

    def button_creator(k):
        b_i = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_"+str(k)+".png")),
                           dark_image=Image.open(relative_to_assets("button_"+str(k)+".png")),
                           size=btn_sizes[k-1])
        button_image_list.append(b_i)
        v = ctk.CTkButton(window, image=b_i, border_width=0,
                text='',bg_color='#0B041B',hover_color='#0B041B',
                 border_color='#0B041B', fg_color='transparent',
            )
        v.place(x=btn_coord[k-1][0], y=btn_coord[k-1][1])
        button_list.append(v)

    for i in range(7):
        button_creator(i+1)

    framev = ['frame_1','frame_2','frame_3','frame_4']
    colors = ['#0B041B','#26294F','#CCD09F','green','brown']
    global frame_bool_list, my_y_list, frames
    frame_bool_list, my_y_list, frames = [], [], []

    for i, v in enumerate(framev):
        v = ctk.CTkFrame(window, fg_color=colors[i], border_color='#CCD09F',
                width=1880, corner_radius=0, height=420, border_width=1,)
        v.place(x=0,y=1004)   
        frames.append(v)
        frame_bool_list.append(False)
        my_y_list.append(1004)
    frame_inner_explore = ctk.CTkFrame(frames[0], fg_color=colors[0], width=1600, height=200,)
    frame_inner_explore.place(x=135, y=18)

    for i in range(5):
        v = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_hover_"+str(i+1)+".png")),
                        dark_image=Image.open(relative_to_assets("button_hover_"+str(i+1)+".png")),
                        size=btn_sizes_hover[i])
        hover_image_list.append(v)
    
    def button_hover(e, i, kv):
        button_list[kv].configure(image=hover_image_list[i])
    def button_leave(e, i, kv):
        button_list[kv].configure(image=button_image_list[kv])

    for i in range(5):
        kv = hover_sel[i]
        button_list[kv].bind('<Enter>', lambda e, i=i, kv=kv: button_hover(e, i, kv))
        button_list[kv].bind('<Leave>', lambda e, i=i, kv=kv: button_leave(e, i, kv))
        if kv!=0:
            button_list[kv].configure(command=lambda kk=kv-3:btn(frames[kk], kk))

    button_list[0].configure(command=lambda :LogIn_SignUp(window))
    continents_explore(frames=frame_inner_explore)
    window.resizable(False, False)
    #______________________________________________________________________________________________________________________________________#
global my_y
my_y = 1004
def btn(frm, fv):
    global frame_bool_list
    global my_y_list

    if frame_bool_list[fv] == False:
        frame_bool_list[fv]=True

        if my_y_list[fv] > 93: 

            my_y_list[fv]=93
            frm.place(x=0, y=my_y_list[fv])
            button_list[fv+3].configure(image=hover_image_list[fv+1])  

        for i, each in enumerate(frame_bool_list):
            if i == fv:
                pass
            else:
                if each == True:
                    my_y_list[i]=1004
                    frames[i].place(x=0, y=my_y_list[i])
                    button_list[i].configure(image=button_image_list[i])
                    frame_bool_list[i] = False

    elif frame_bool_list[fv] == True:
        frame_bool_list[fv] = False
        if my_y_list[fv] < 1004:      
            my_y_list[fv]=1004
            frm.place(x=0, y=my_y_list[fv])
