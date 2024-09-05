#Departure

import customtkinter as ctk
import PIL
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from ExploreMenu import continents_explore
from TopMenu import TopMenu
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")
basic_text = '''\n\n\t# Free Food\t\t\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n'''
basic_text_b = '''# Free Food\nfre'''
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def DepartuePage(window):
    test_list = []
    for i in range(4):
        k=[]
        test_list.append(k)
    global one_zero_bool_list
    bvartt = 6
    border_color_ = ['black', 'green', 'red', 'blue', 'grey', 'bwown']
    one_zero_bool_list = []
    bussiness_opt = ['Basic', 'Value', 'Comfort', 'Deluxe', 'Prime']
    font_radio = ctk.CTkFont('Georgia', 16, 'bold')
    list_d = [1,3,5,7,9,11,13]
    for i in range(bvartt):
        one_zero_bool_list.append(0)
    def rad_command(hhv, vhh):
        test_list[3][hhv].configure(command = lambda: rad_select(hhv, vhh))
        

    def rad_select(hhv, vhh):
        test_list[1][vhh].select()
        print(hhv, vhh)
        

    def test(c, d):
        global one_zero_bool_list
        if one_zero_bool_list[d]==0:
            print('ini', one_zero_bool_list[d])
            one_zero_bool_list[d]=1
            print('exi', one_zero_bool_list[d])

            radiovar = ctk.StringVar(window,value='')
            frame_size_rad_h = 280
            frame_size_rad_w = 220
            c_radius = 2
            b_width = 2
            ij = 0
            for i in range(4):
                q_border=ctk.CTkFrame(
                        listlist[d][6],
                        height=frame_size_rad_h+4,
                        width=frame_size_rad_w+4,
                        border_color=border_color_[i],
                        fg_color='transparent',
                        #fg_color=border_color_[i+1],
                        border_width=b_width,
                        corner_radius=c_radius,
                    )
                q_border.grid(row=0, column=i, pady=10, padx=10)
                
                q = ctk.CTkFrame(
                    q_border,
                    #listlist[d][6],
                    height=frame_size_rad_h,
                    width=frame_size_rad_w,
                    #border_color=border_color_[i],
                    fg_color='transparent',
                    #fg_color=border_color_[i+1],
                    #border_width=b_width,
                    corner_radius=c_radius,
                    
                )
                #q.grid(row=0, column=i, pady=10, padx=10)
                q.pack(pady=2, padx=2)
                sticky_rad=['e', 'w']
                for j  in range(2):
                    
                    rad = ctk.CTkButton(
                        q,
                        height=frame_size_rad_h-2,
                        width=frame_size_rad_w/2-2,
                        fg_color='transparent',
                        corner_radius=c_radius,
                        text=basic_text_b,
                        text_color='#CCD09F',
                        hover=False,
                        border_color='white',
                        border_width=0,
                    )
                    rad.grid(row=0, column=j, padx=0, pady=0, sticky=sticky_rad[j])
                    #rad.place(x=b_width+(j*(frame_size_rad_w/2-2)), y=b_width)
                    test_list[3].append(rad)
                    #rad_command(i, i)
                    
                    rad_command(ij, i)
                    ij+=1
                    

                radio_frame = ctk.CTkFrame(
                    q,
                    fg_color='transparent',
                    corner_radius=0
                )
                radio_frame.grid(row=0, column=0,pady=5, padx=5, sticky='wn')
                radio_button = ctk.CTkRadioButton(
                    radio_frame,
                    text=bussiness_opt[i],
                    text_color='white',
                    variable=radiovar,
                    font=font_radio
                )
                radio_button.grid(row=0, column=0,pady=5, padx=5)
                label = ctk.CTkLabel(
                    q,
                    text=basic_text,
                    text_color='#CCD09F'
                )
                #label.grid(row=1, column=0,pady=5, padx=5)
                
                test_list[2].append(label)
                test_list[1].append(radio_button)
                test_list[0].append(q)
                
            #test_list[3][0].configure(command = lambda: test_list[1][0].select())
                
        elif one_zero_bool_list[d]==1:
            one_zero_bool_list[d]=0
            #test_list[0].destroy()
            listlist[d][6].destroy()
            listlist[d][6] = ctk.CTkFrame(
            main_frame_ticket,
            width=1111+80,
            height=2,
            fg_color='transparent',
            border_color='#CCD09F',
            border_width=1,
            corner_radius=0
            )
            listlist[d][6].grid(row=list_d[d], column = 0,padx = 0)

    canvas_2 = Canvas(
        window,
        bg = "#0B041B",
        height = 1000,
        width = 1880,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_2.place(x = 0, y = 0)

    image_image_Departure = ctk.CTkImage(
        light_image=Image.open(relative_to_assets("Departure_bg_2.png")),
        dark_image=Image.open(relative_to_assets("Departure_bg_2.png")),
        size=(1880, 411))
    bg_image_pg_2 = ctk.CTkLabel(
        window, 
        image=image_image_Departure,
        text=''
    )
    bg_image_pg_2.place(x=0, y=93)

    main_frame_ticket = ctk.CTkScrollableFrame(
        window,
        height = 445,
        width = 1235,
        fg_color='#282829', 
        corner_radius=0,
        border_color='#CCD09F',
        border_width=0
                )
    main_frame_ticket.place(x=325, y=522)

    buttonsss_fonta = ctk.CTkFont('Georgia', 18, weight='bold', underline=True)
    buttonsss_fontb = ctk.CTkFont('Felix titling', 12, weight='bold', underline=False)

    '''________________________________________________, ___________________________________________________________
       '''
    texta = f'GOI ___________________________________________________________ DXB\n5:00\t\t\t\t\t\t6:00'
    textaa = f'\tGOI\t\t\t\tDXB\n\t5:00    \t\t\t\t\t\t       6:00'
    textb = f' From  500 '
    listlist = []
    for i in range(bvartt):
        emplist = ['img','tkct_label','','','','','','','']
        listlist.append(emplist)
    
    hh=0
    for k,v in enumerate(listlist):
        
        v[5] = ctk.CTkFrame(
            main_frame_ticket,
            fg_color='transparent',
            border_color='black',
            border_width=0
        )
        v[5].grid(row=hh, column = 0, pady=5)
        hh+=1

        v[0] = ctk.CTkImage(
            light_image=Image.open(relative_to_assets("tktct_bg_3.jpeg")),
            dark_image=Image.open(relative_to_assets("tktct_bg_3.jpeg")),
            size=(225, 30))
        v[1] = ctk.CTkLabel(
            v[5],
            width=550,
            height=70,
            #image=v[0],
            text=texta,
            font=buttonsss_fontb,
            text_color='#CCD09F',
            fg_color='black',
            bg_color='transparent',
            corner_radius=20
        )
        v[1].grid(row=k, column=0, padx=3, pady=3)
        
        v[2]=ctk.CTkFont('Georgia', 11, 'normal',slant='roman', underline=False)

        v[3] = ctk.CTkFrame(
            v[5],
            fg_color='transparent'
                )
        v[3].grid(row=k, column=1, padx=18, pady=0)
        ff = 4
        for i in range(2):
            
            v[ff] = ctk.CTkButton(
                v[3],
                fg_color='#26294F',#220B56',
                #bg_color='black',
                width=320,
                height=64,
                text=textb,
                font=buttonsss_fonta,
                text_color='#CCD09F',
                corner_radius=10,
                border_color='black',
                border_width=3,
                )
            v[ff].grid(row=0, column=i+1, padx=2, pady=3)
            ff=7
            
            '''hour_label = ctk.CTkLabel(
            buttonsss,
            text="__________________________\n4 hours /Direct Flight ",
            fg_color='transparent',
            bg_color='black',
            font=fontsst,
            text_color='#CCD09F'
            )
            hour_label.place(x=190, y=16)'''

        hour_label = ctk.CTkLabel(
            v[1],
            text="____________________________________\n5 hours\n\n",
            image=v[0],
            fg_color='transparent',
            bg_color='black',
            font=v[2],
            text_color='#CCD09F',
            
        )
        hour_label.place(x=165, y=21)   

        v[6] = ctk.CTkFrame(
            main_frame_ticket,
            width=1161,
            height=2,
            fg_color='transparent',
            border_color='#CCD09F',
            border_width=1
        )
        v[6].grid(row=hh, column = 0, pady=0, padx=3, sticky='')
        hh+=1

        #v[4].configure(command=lambda : test(c=1, d=k))

    

    TopMenu(window, canvas_2)
    #web.mainloop
    A=listlist[0]
    B=listlist[1]
    C=listlist[2]
    D=listlist[3]
    E=listlist[4]
    F=listlist[5]

    G=listlist[0]
    H=listlist[1]
    I=listlist[2]
    J=listlist[3]
    K=listlist[4]
    L=listlist[5]

    A[4].configure(command=lambda : test(c=1, d=0))
    B[4].configure(command=lambda : test(c=1, d=1))
    C[4].configure(command=lambda : test(c=1, d=2))
    D[4].configure(command=lambda : test(c=1, d=3))
    E[4].configure(command=lambda : test(c=1, d=4))
    F[4].configure(command=lambda : test(c=1, d=5))

web = ctk.CTk()
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
web.geometry("1880x1000")
web.configure(bg = "#FCFFDD")
DepartuePage(web)

web.mainloop()
