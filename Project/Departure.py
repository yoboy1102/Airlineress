#Departure

import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Canvas
from TopMenu import TopMenu
from PassengerDetails import PassDetails
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

basic_text = '''\n\n\t# Free Food\t\t\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n# Free Food\n'''
basic_text_b = ['''# Free Food\nfre''', '']

def DepartuePage(window, fromto, listno_pass):
    global ozbool_list
    bvartt = 6
    b_c, b_opt = ['black', 'green', 'red', 'blue', 'grey', 'grey'], ['Basic', 'Value', 'Comfort', 'Deluxe', 'Prime']
    ozbool_list, font_radio  = [], ctk.CTkFont('Georgia', 16, 'bold')       #SCV
    list_d = [1,3,5,7,9,11,13]
    for i in range(bvartt):
        ozbool_list.append(0)

    def passdetails():
        PassDetails(window, listno_pass, 1)

    def rad_command(hhv, vhh):
        test_list[3][hhv].configure(command = lambda: rad_select(hhv, vhh))  #defined it to make the coe shorter

    def rad_select(hhv, vhh):
        test_list[1][vhh].select()        #selecting the radio button
        print(hhv, vhh)
        
#282829
    def test(c, d):
        global test_list, ozbool_list
        if ozbool_list[d]==0:
            test_list = []
            for i in range(6):
                k=[]
                test_list.append(k)  
            
            print('ini', ozbool_list[d])        #TBR
            ozbool_list[d]=1
            print('exi', ozbool_list[d])        #TBR

            radiovar = ctk.StringVar(window,value='')
            f_sz_rad_h, f_sz_rad_w = 315, 215  #SCV
            b_w, ij, c_r = 2, 0, 15 #SCV
            
            h=ctk.CTkFrame(listlist[d][6], border_color=b_c[i],
                           height=f_sz_rad_h+6, width=f_sz_rad_w-70,        #price frame
                           fg_color='transparent', corner_radius=10
                        )   
            h.grid(row=0, column=5, pady=12, padx=8, sticky='')

            h_curr_button_font = ctk.CTkFont('Georgia', 14, 'bold', 'italic')
            h_curr_button = ctk.CTkButton(h, font=h_curr_button_font,
                            hover=False, corner_radius=9, border_width=2,
                            text='Currency Selector', fg_color='transparent',           #Currency selector button
                            border_color='white', state='Disabled', bg_color='transparent',
                    )
#______________________________________________________________________________________________________________________#            
            h_curr_button.grid(row=0, column=0, sticky='ew', pady=5)
            h_emp = ctk.CTkLabel(h)                                     #empty label, TBR, just used for padding       
            h_emp.grid(row=1, column=0, sticky='s', pady=72)
#______________________________________________________________________________________________________________________#   
            
            total_value_label_font = ctk.CTkFont('Georgia', 16, 'bold', 'italic', underline='False')
            total_value_label = ctk.CTkLabel(h,
                text='Total Value',text_color='white',
                font=total_value_label_font, width=f_sz_rad_w-70,
                height=f_sz_rad_h/8, corner_radius=10,       #total value label
                )
            total_value_label.grid(row=2, column=0, sticky='S')
            
            h_frame = ctk.CTkFrame(h, height = f_sz_rad_h/4,
                width=f_sz_rad_w-70, border_width=1, corner_radius=10,
                border_color='white', fg_color='transparent', bg_color='transparent',        #price frame
                )
            h_frame.grid(row=3, column=0, sticky='s')
            price_val = float(1000)
            h_label_font = ctk.CTkFont('georgia', 20, 'normal', 'italic')
            h_label = ctk.CTkLabel( h_frame, text=str(price_val),
                font=h_label_font, width=f_sz_rad_w-70, height=f_sz_rad_h/10,    #price label
                corner_radius=10, text_color='white',
                )
            h_label.pack(padx=2, pady=2)

            h_curr_font = ctk.CTkFont('georgia', 16, 'normal', 'italic')
            h_curr = ctk.CTkLabel(h_frame, font=h_curr_font, 
                width=f_sz_rad_w-70, height=f_sz_rad_h/10,
                corner_radius=10, text_color='white', text='AED',    #currency label
            )
            h_curr.pack(padx=2, pady=2)
            

            for i in range(4):
                q_border=ctk.CTkFrame(listlist[d][6],
                        height=f_sz_rad_h+8, width=f_sz_rad_w+4,  border_color=b_c[i],  #border frame
                        fg_color='transparent', border_width=b_w, corner_radius=10,
                    )
                q_border.grid(row=0, column=i+1, pady=10, padx=10)
                
                q = ctk.CTkFrame(q_border,
                        height=f_sz_rad_h, width=f_sz_rad_w, border_color=b_c[i+1],  #the whole button frame
                        border_width=0, fg_color='transparent', corner_radius=c_r,  
                    )
                q.pack(pady=4, padx=4)
                sticky_rad=['ew', 'w']

                for j  in range(2):
                    rad = ctk.CTkButton(q,
                        height=f_sz_rad_h-2, width=f_sz_rad_w/2-2, text=basic_text_b[j],
                        corner_radius=c_r, fg_color='transparent', text_color='#CCD09F',        #the two buttons, in this for loop you have to add text and the image
                        border_color='white',bg_color='transparent', border_width=1, hover=False,#by configuring
                    )
                    rad.grid(row=0, column=j, padx=0, pady=0, sticky=sticky_rad[j])
                    rad.grid_propagate(False)
                    
                    test_list[2].append(q_border)
                    test_list[3].append(rad)
                                
                    rad_command(ij, i)
                    ij+=1

                radio_frame = ctk.CTkFrame(q, fg_color='transparent', corner_radius=0)
                radio_frame.grid(row=0, column=0,pady=5, padx=5, sticky='wn')       #top frame to contain the radio button

                radio_button = ctk.CTkRadioButton(radio_frame, text=b_opt[i],
                    text_color='white', variable=radiovar, font=font_radio      #radio button
                )
                radio_button.grid(row=0, column=0,pady=5, padx=5)
                
                # first button (for text), ==>
                
                test_list[1].append(radio_button)
                test_list[0].append(q)
                
                test_list[1][0].select()
                
        elif ozbool_list[d]==1:
            ozbool_list[d]=0    
            test_list=[[],[],[],[]]  #SCV
            listlist[d][6].destroy()    #closes the frame

            listlist[d][6] = ctk.CTkFrame(main_frame_ticket, width=1420-(1420/14), height=2,
               fg_color='transparent',border_color='grey', border_width=1, corner_radius=0,  #creates a frame that looks like a line
            )
            listlist[d][6].grid(row=list_d[d], column = 0,padx = 0)

    canvas_2 = Canvas( window, bg = "#1E1E1E", relief = "ridge",
        height = 1000, width = 1880, bd = 0, highlightthickness = 0,
      )
    canvas_2.place(x = 0, y = 0)
    canvas_2.pack_propagate(False)

    canvas_3 = Canvas( window, bg = "#1E1E1E", relief = "ridge",
        height = 1000, width = 1880, bd = 0, highlightthickness = 0,
      )
    canvas_3.place(x = 0, y = 93)
    canvas_3.pack_propagate(False)

    image_image_Departure = ctk.CTkImage(
        light_image=Image.open(relative_to_assets("Departure_bg_2.png")),
        dark_image=Image.open(relative_to_assets("Departure_bg_2.png")),
        size=(1880, 395))
    bg_image_pg_2 = ctk.CTkLabel(canvas_3, image=image_image_Departure,text='')
    bg_image_pg_2.pack()
    
    main_frame_ticket = ctk.CTkScrollableFrame(canvas_3, height = 445,
        width = 1444, border_width=1, corner_radius=1,
        fg_color='#1E1E1E', border_color='#CCD09F', bg_color='#1E1E1E',
            )
    #main_frame_ticket.place(x=200, y=522)
    main_frame_ticket.pack(pady=20, ipadx=10, ipady=5)   

    buttonsss_fonta = ctk.CTkFont('Georgia', 18, weight='bold', underline=True)
    buttonsss_fontb = ctk.CTkFont('Felix titling', 12, weight='bold', underline=False)

    texta = f'{fromto[0]} ______________________________________________________________________ {fromto[1]}\n5:00\t\t\t\t\t\t\t6:00'
    textaa = f'\tGOI\t\t\t\tDXB\n\t5:00    \t\t\t\t\t\t       6:00'
    textb = f' From  500 '
    listlist = []

    for i in range(bvartt):
        emplist = ['img','tkct_label','','','','','','','']
        listlist.append(emplist)
    
    hh=0
    for k,v in enumerate(listlist):
        
        v[5] = ctk.CTkFrame(main_frame_ticket,
            fg_color='transparent', border_color='black', border_width=0
        )
        v[5].grid(row=hh, column = 0, pady=5)
        hh+=1

        v[0] = ctk.CTkImage(
            light_image=Image.open(relative_to_assets("tktct_bg_3.jpeg")),
            dark_image=Image.open(relative_to_assets("tktct_bg_3.jpeg")),
            size=(225, 30))
        v[1] = ctk.CTkLabel(v[5], width=623, height=70, corner_radius=20, text=texta,
          text_color='#CCD09F', fg_color='black', bg_color='transparent', font=buttonsss_fontb
            )
        v[1].grid(row=k, column=0, padx=20, pady=3)
        
        v[2]=ctk.CTkFont('Georgia', 11, 'normal',slant='roman', underline=False)

        v[3] = ctk.CTkFrame(v[5], fg_color='transparent')
        v[3].grid(row=k, column=1, padx=25, pady=0, sticky='e')
        
        ff = 4
        for i in range(2):
            
            v[ff] = ctk.CTkButton(v[3], fg_color='#26294F',border_color='black',text_color='#CCD09F',
                text=textb, font=buttonsss_fonta, width=363, height=64, corner_radius=10, border_width=3,)
            v[ff].grid(row=0, column=i+1, padx=8, pady=3)
            ff=7
            
        hour_label = ctk.CTkLabel(v[1], image=v[0], font=v[2],
            text="____________________________________\n5 hours / Direct\n\n",
            fg_color='transparent', bg_color='black', text_color='#CCD09F', )
        hour_label.place(x=165, y=21)   

        v[6] = ctk.CTkFrame(main_frame_ticket,
            width=1420-(1420/14), height=2, border_width=1,
            fg_color='transparent',border_color='grey',)
        v[6].grid(row=hh, column = 0, pady=0, padx=3, sticky='')
        hh+=1
    
    next_btn_font=ctk.CTkFont('Georgia', 16, 'bold', slant='italic')
    next_btn = ctk.CTkButton(window,width=170, height=50, corner_radius=10, border_width=7, hover=False,
                             text_color='#D8EADF', border_color='Black', 
                             bg_color='#1E1E1E', fg_color='#26294F' , font=next_btn_font,
                             text = 'Continue =>', command=lambda :passdetails())
    next_btn.place(x=1690, y=900)

    TopMenu(window, canvas_2, 88)
    ccc=1
    for i in range(2):
        ccc+=3
        for i in range(len(listlist)):
            listlist[i][ccc].configure(command = lambda c=1, d=i: test(c=c, d=d))

'''''''''
web = ctk.CTk()
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
web.geometry("1880x1000")
#web.configure(bg = "#FCFFDD")
DepartuePage(web, ['goa', 'dxb'], [4,5,1])

web.mainloop()
'''''''''
