#PassengerDetails

import customtkinter as ctk
from customtkinter import CTkFrame,CTkButton,CTkLabel,CTkImage,CTkScrollableFrame,CTkFont,CTkComboBox,CTkEntry 
from PIL import Image, ImageTk
from pathlib import Path
import tkinter
from tkinter import Canvas
from TopMenu import TopMenu
from time import *
from SeatReservation import SeatRes

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def PassDetails(window, list_no_pass, count_pass):

    def update_time():
        current_time = strftime('%H:%M:%S %p')
        time_lbl.configure(text=current_time)
        time_lbl.after(1000, update_time)
    def seatres():
        SeatRes(window, list_no_pass, count_pass)

    canvas_3 = Canvas(window, bg = "#D9D9D9", bd = 0,  height = 1000, width = 1880, highlightthickness = 0)
    canvas_3.place(x = 0, y = 0)
    H_W, H_H = 1600, 180
    V_W, V_H = 1880-H_W+2, 1000-92

    horiz_top = CTkFrame(window,
                         height=H_H, width=H_W,
                         fg_color='#071B41', corner_radius=0)
    horiz_top.place(x=0, y=92)
    horiz_top.grid_propagate(False)

    vert_top = CTkFrame(window, height=V_H, width=V_W,
                         fg_color='#071B41', corner_radius=0)#'#05191A', '#071B41', 1D618B
    vert_top.place(x=H_W-1, y=92)
    vert_top.pack_propagate(False)

    S_H, S_W =1000-92-H_H, 1880-V_W

    pass_sclr_frame = CTkScrollableFrame(window, height=S_H, width=S_W, fg_color='#3860A1',
                                          border_color='#CCD09F', border_width=0, corner_radius=0)#223A60
    pass_sclr_frame.place(x=0, y=92+H_H)

    
    lineimg = CTkImage(light_image=Image.open(relative_to_assets('Line 1.png')),
                           dark_image=Image.open(relative_to_assets('Line 1.png')),
                           size=(3, S_H))
    linelbl = CTkLabel(window, image=lineimg, fg_color='transparent', text='')
    linelbl.place(x=S_W/2, y=92+H_H)
    #canvas_4 = Canvas(window, bd=0, height=S_H, width=4, background='grey', bg='grey',)
    #canvas_3.create_line(S_W/2-3, S_H, S_W/2+2, 1000, width=3)
    #canvas_4.create_line(2, 5, 2, S_H, width=7, fill='grey')
    #canvas_4.place(x=S_W/2, y=92+H_H)
    #canvas_4.pack()

    frm_c = CTkFrame(horiz_top,
                         #height=1, width=1,
                               fg_color='transparent')
    frm_c.grid(row=0, column=0, sticky='w', padx=85, pady=35)
    p_head_text_l = ['Passenger Information',
                 '''   Enter the required information for each traveler, and be sure                 \nthat it exactly matches the government-issued ID presented at the airport.''']
    font=('Ami R', 12)
    font1=CTkFont('Georgia', 30, 'bold', underline=True)
    font2=CTkFont('Ami R', 20, 'bold','italic')

    pas_det_lbl1 = CTkLabel(frm_c, text=p_head_text_l[0].upper(), font=font1, text_color='#CCD09F')
    pas_det_lbl1.pack(anchor='w')  

    pas_det_lbl2 = CTkLabel(frm_c, text=p_head_text_l[1], font=font2, text_color='#C6C9C5')
    pas_det_lbl2.pack(pady=37, anchor='w')
    


    time_lbl = CTkLabel(horiz_top, text='', font=('Arial', 50), text_color='#D8EADF')
    time_lbl.grid(row=0, column=1, sticky='wn', padx=300, pady=60)
    update_time()

    emp_space = CTkFrame(vert_top, height=100, fg_color='transparent'   )
    emp_space.pack(pady=30)
    emp_space_2 = CTkFrame(vert_top, height=100, fg_color='transparent')
    emp_space_2.pack(pady=20)

    luggage_lim = CTkFrame(vert_top, #fg_color='#071B41'
                           )
    luggage_lim.pack(pady=10, padx=10)

    luggage_lim_lbl = CTkLabel(luggage_lim, text='Luggage Limit', font=('Georgia', 18, 'bold'), 
                        #text_color='#A6ACAC'
                        )
    luggage_lim_lbl.pack()

    luggage_lim_frm = CTkFrame(luggage_lim, fg_color='transparent')
    luggage_lim_frm.pack(pady=10, padx=10)

    lug_txt_amt = ['20 Kg', '10 Kg', '5 Kg']
    lug_txt = ['Adult', 'Child', 'Toddler']

    for i in range(3):
        
        
        lug_txt_i = CTkLabel(luggage_lim_frm, text=lug_txt[i], font=('Georgia', 18, 'bold'), 
                        #text_color='#A6ACAC'
                        )
        lug_txt_i.grid(row=0, column=i, sticky='w', padx=10 ,pady=10)
    for i in range(3):

        lug_txt_amt_i = CTkLabel(luggage_lim_frm, text=lug_txt_amt[i], font=('Georgia', 18, 'bold'), 
                        #text_color='#A6ACAC'
                        )
        lug_txt_amt_i.grid(row=1, column=i, sticky='w', padx=10 ,pady=10)
        
        


    luggage_img = CTkImage(light_image=Image.open(relative_to_assets('Luggage.png')),
                           dark_image=Image.open(relative_to_assets('Luggage.png')),
                           size=(V_W-10, (V_W-10)*1.2))
    luggage_lbl = CTkLabel(vert_top, image=luggage_img, fg_color='transparent', text='')
    luggage_lbl.pack(pady=35)


    continue_btn_font=ctk.CTkFont('Georgia', 18, 'bold', slant='italic')
    continue_btn = ctk.CTkButton(vert_top ,width=175, height=60, corner_radius=10, border_width=7, hover=False,
                             text_color='#D8EADF', border_color='Black', 
                            bg_color='#1E1E1E', fg_color='#26294F' , font=continue_btn_font,
                             text = 'Continue =>' ,command=lambda :seatres())
    
    continue_btn.pack(pady=10, padx=20)

    list_frm=[]
    fgbb = '#D9EBE0'
    fgbb='transparent'
    nsew='ns'
    pdx=65
    for i in range(2):

        frm_l_r = CTkFrame(pass_sclr_frame, fg_color=fgbb, height=1000)
        frm_l_r.grid(row=0, column=i, sticky=nsew, padx=pdx, pady=40)
        list_frm.append(frm_l_r)
    
    txt_l_0 = ['Adult', 'Child', 'Toddler']
    no_adults, no_children, no_toddlers = list_no_pass[0], list_no_pass[1], list_no_pass[2]
    no_l =[no_adults, no_children, no_toddlers]
    k0 = 0
    cc,ccc=0, 0
    frm_m,bb,pas_l,ent_list=[],[],[],[]


    for j in range(3):
        print('j',j, txt_l_0[j])
        bbb,frm_m0_l=[],[]
        for i in range(no_l[j]):
            
            frm_m0 = CTkFrame(list_frm[k0], fg_color='#4A74BA',corner_radius=20,
                              border_color='#071B41', border_width=2)#'#D9EBE0'
            frm_m0.pack(pady=25, ipady=5, ipadx=5)
            bbb.append(k0)
            if k0 == 0:
                     k0=1
            elif k0 == 1:
                     k0=0
            frm_m0_l.append(frm_m0)
        frm_m.append(frm_m0_l)
        print(bbb)
        bb.append(bbb)

        
        for k in range(no_l[j]):
                cc+=1
                print(len(bb),'k',k, bb[j][k], bb[j][k])
                
                txt_pas = 'Passenger '+str(cc)+' ('+ txt_l_0[j] + ') '
                frm_head = CTkFrame(frm_m[j][k], fg_color='transparent',)
                frm_head.pack(pady=10, fill='x', padx=10)

                font_head = CTkFont('georgia', 20, 'bold', underline=True)
                pas_lbl_0 = CTkLabel(frm_head,
                                         text=txt_pas,
                                         font=font_head, text_color='black')
                pas_lbl_0.grid(row=0, column=0, sticky='w')
                pas_l.append(pas_lbl_0)


                font_body=('Times',16, )
                ent_text_l1 = ['First Name*','Middle Name', 'Last Name*']
                ent_text_l2 = ['DOB', 'Email Address*']
                title_var = ctk.StringVar()
                title_vals = ['Mr', 'Mrs', 'Miss', 'Ms','Undisclosed']


                frm_body = CTkFrame(frm_m[j][k], fg_color='transparent')
                frm_body.pack(pady=10)
                s_hei, s_wid = 50, 200
                title_m = CTkComboBox(frm_body, height=s_hei-10,font=font_body,
                                          width=s_wid-10, values=title_vals, border_width=1, fg_color='#D8EADF',
                                          variable=title_var, button_color='#A1B0CC', border_color='#A1B0CC' )
                title_m.grid(row=0, column=0, sticky='w', padx=10, pady=10)
                

                ent_emp =[]
                for i in range(3):
                      ent = CTkEntry(frm_body, 
                                         placeholder_text=ent_text_l1[i],
                                         height=s_hei, width=s_wid,
                                         font=('Helvetica', 14), corner_radius=6,
                                         border_color='#A1B0CC', border_width=1,
                                         fg_color='#D8EADF'
                                         )
                      ent.grid(row=1, column=i, padx=10, pady=5)
                      ent_emp.append(ent)

                for i in range(2):
                      ent = CTkEntry(frm_body, 
                                         placeholder_text=ent_text_l2[i],
                                         height=s_hei, width=s_wid,
                                         font=('Helvetica', 14), corner_radius=6,
                                         border_color='#A1B0CC', border_width=1,
                                         fg_color='#D8EADF'
                                         )
                      ent.grid(row=2, column=i, padx=10, pady=5)

                      ent_emp.append(ent)
                ent_list.append(ent_emp)

    TopMenu(window, canvas_3, -88)

    window.resizable(False, False)

    pass
    print(V_W, V_H, S_W, S_H, H_W, H_H)

''''''''''''
web = ctk.CTk()
web.geometry('1880x1000')
PassDetails(web, [4,5,2], 1)
web.mainloop()
''''''''''''