#Departure

import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Canvas, PhotoImage
from TopMenu import TopMenu
from PassengerDetails import PassDetails
import random as rn
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def file_path(path: str) -> Path:
    return OUTPUT_PATH / Path(path)
global kcvr
kcvr=0
def dep(window, fromto, listno_pass, text_date):    
    global kcvr
    kcvr+=1
    DepartuePage(window, fromto, listno_pass, 0, text_date)
    
def DepartuePage(window, fromto, listno_pass, tripway, text_date):
    global ozbool_list, in_all_amt_changed, all_amt_changed
    bvartt = 6
    e_c, e_opt = ['blue', '#EB5757', '#007B65', 'red', 'grey'], ['Basic', 'Comfort', 'Basic Luxury', 'Executive', 'Extra']
    b_c, b_opt = ['yellow', 'green', '#5CD6C0', '#407AEA', 'grey', 'grey'], ['Value', 'Comfort', 'Deluxe', 'Premium', 'Prime']
    all_c, all_opt, all_ebtext = [e_c, b_c], [e_opt, b_opt], ['Economy Text', 'Business Text']
    ozbool_list, font_radio  = [], ctk.CTkFont('Georgia', 16, 'bold')       #SCV
    list_d= [1,3,5,7,9,11,13]
    curr_rate_aed = [1, 2, 3, 4]
    in_all_amt, prc_tag_l = [[80, 150, 250, 300], [180, 300, 500, 600]], []
    in_all_amt_changed = in_all_amt
    
    for i in range(2):
        kk=[]
        for i in range(bvartt):
            kk.append(0)
        ozbool_list.append(kk)

    def passdetails():
        PassDetails(window, listno_pass, fromto)

    def rad_command(hhv, vhh):
        test_list[3][hhv].configure(command = lambda: rad_select(hhv, vhh))  #defined it to make the coe shorter

    def rad_select(hhv, vhh):
        test_list[1][vhh].invoke()        #selecting the radio button
        print(hhv, vhh)

    def add_price(price_lbl, c, i, j, d, in_amt):
        global all_amt_changed, in_all_amt_changed
        print(c, i, j, d, all_amt_changed)
        tt = all_amt_changed[d][c]
        ss = in_all_amt_changed[c][i]
        #ss = ss.split(' ')
        print(tt, ss)
        new_prc = float(tt)+float(ss)
        price_lbl.configure(text=str(new_prc))
        return all_amt_changed, in_all_amt_changed

    def curr_converter(u, c, d, i, ii, j, price_lbl, price, in_amt, in_lbl, cn, rad):
        global all_amt_changed, in_all_amt_changed
        print(f'\n\nu={u} c={c} d={d} i={i} ii={ii} j={j}\n all_amt_changed={all_amt_changed}\n, in_amt={in_amt}\n, in_all_amt={in_all_amt}\n, in_all_amt_changed={in_all_amt_changed}\n\n')
        all_amt_changed[ii][c] = u*curr_rate_aed[ii] 
        price_lbl.configure(text=cn[ii])
        price.configure(text=str(all_amt_changed[ii][c]))
        for k in range(len(in_lbl)):
            in_all_amt_changed[c][k] = in_all_amt[c][k]*curr_rate_aed[ii]
            in_lbl[k].configure(text=f'{str(in_all_amt_changed[c][k])}  {cn[c]}')
        for ri,r in enumerate(rad):
            #if r.cget('value')=='1':
            print(ri, r.cget('value'), r.cget('text'), r.cget('variable'))
            #add_price(price_lbl, c, ri, j, d, in_amt)
        return all_amt_changed, in_all_amt_changed
    

    def img_cur_load(i):
        type_img = ['', 'Rounded', 'Square', 'Circle']
        place_name = ['United Arab Emirates', 'European Union', 'United States of America', 'India']
        img = ctk.CTkImage(light_image=Image.open(relative_to_assets(f"Flags\{place_name[i]} {type_img[1]}.png")),
                            dark_image=Image.open(relative_to_assets(f"Flags\{place_name[i]} {type_img[1]}.png")),
                            size=(30, 20))
        return img


#282829
    def create_frame(c, d, amt):
        global test_list, ozbool_list
        test_list = []
        for i in range(6):
            k=[]
            test_list.append(k)  
            
        ozbool_list[c][d]=1
        radiovar = ctk.StringVar(window,value='')
        f_sz_rad_h, f_sz_rad_w = 315, 200  #SCV
        b_w, ij, c_r = 2, 0, 22 #SCV
        
        h=ctk.CTkFrame(listlist[d][6], border_color=b_c[i],
                        height=f_sz_rad_h+6, width=f_sz_rad_w-70,        #price frame
                        fg_color='transparent', corner_radius=10
                    )   
        h.grid(row=0, column=5, pady=12, padx=8, sticky='')

        h_curr_button_font = ctk.CTkFont('Georgia', 14, 'bold', 'italic')
        h_curr_button = ctk.CTkButton(h, font=h_curr_button_font,
                        hover=False, corner_radius=9, border_width=2,
                        text='Currency Selector', fg_color='transparent',           #Currency selector button
                        border_color='white', state='Disabled', bg_color='transparent',)
        h_curr_button.grid(row=0, column=0, sticky='new', pady=5)
        curr_btns, curr_names = [], ["AED", "EUR", "USD", "INR"]
        
        for i in range(len(curr_names)):
                    img = img_cur_load(i)
                    btn = ctk.CTkButton(h, font=h_curr_button_font, corner_radius = 0,
                                border_width=2, text=curr_names[i], image=img)
                    btn.grid(row=i+1, column=0, pady=3)
                    curr_btns.append(btn) 
        
        total_value_label_font = ctk.CTkFont('Georgia', 16, 'bold', 'italic', underline='False')
        total_value_label = ctk.CTkLabel(h,
            text='Total Value',text_color='white',
            font=total_value_label_font, width=f_sz_rad_w-70,
            height=f_sz_rad_h/8, corner_radius=10,       #total value label
            )
        total_value_label.grid(row=len(curr_names)+1, column=0, sticky='S')
        
        h_frame = ctk.CTkFrame(h, height = f_sz_rad_h/4, fg_color='transparent', bg_color='transparent',
            width=f_sz_rad_w-70, border_width=1, corner_radius=10, border_color='white')
        h_frame.grid(row=len(curr_names)+2, column=0, sticky='s')
        price_val = float(amt)
        
        h_label_font = ctk.CTkFont('georgia', 20, 'normal', 'italic')
        h_label = ctk.CTkLabel(h_frame, text=str(price_val), font=h_label_font, width=f_sz_rad_w-70,
            height=f_sz_rad_h/10, corner_radius=10, text_color='white',)
        h_label.pack(padx=2, pady=2)
        
        curr_text = 'AED'
        h_curr_font = ctk.CTkFont('georgia', 16, 'normal', 'italic')
        h_curr = ctk.CTkLabel(h_frame, font=h_curr_font, width=f_sz_rad_w-70, height=f_sz_rad_h/10,
            corner_radius=10, text_color='white', text=curr_text)
        h_curr.pack(padx=2, pady=2)


        for i in range(4):

            with open(file_path(f'Text Files\\{all_ebtext[c]}\\{all_opt[c][i]}.txt'), 'r') as ff:
                ff.readline()
                basic_text_b = ff.read()
                print(basic_text_b)
            
            q_border=ctk.CTkFrame(listlist[d][6],
                    height=f_sz_rad_h+8, width=f_sz_rad_w+4,  border_color=all_c[c][i],  #border frame
                    fg_color='transparent', border_width=b_w, corner_radius=c_r,
                )
            q_border.grid(row=0, column=i+1, pady=10, padx=10)
            
            q = ctk.CTkFrame(q_border,
                    height=f_sz_rad_h, width=f_sz_rad_w, border_color=all_c[c][i+1],  #the whole button frame
                    border_width=3, fg_color='transparent', corner_radius=c_r,  
                )
            q.pack(pady=2, padx=2)
            
            sticky_rad, sizes = ['ew', 'e'], [f_sz_rad_w/1, 30]


            for j  in range(2):

                clr='transparent' if j==0 else all_c[c][i]
                
                kjj=1
                add = 'buss1.png' if kjj==0 else f'buss{i+1}.jpg'
                img = ctk.CTkImage(light_image=Image.open(relative_to_assets(add)),
                            dark_image=Image.open(relative_to_assets(add)),
                            size=(93,300))
                img = img if j==1 else None

                rad = ctk.CTkButton(q,
                    height=f_sz_rad_h+20, width=sizes[j], text='', image=img,
                    corner_radius=c_r, fg_color=clr, text_color='#CCD09F', 
                    border_color='white',bg_color='transparent', border_width=0, hover=False, compound='right')
                rad.grid(row=0, column=j, padx=0, pady=0, sticky=sticky_rad[j])
                rad.grid_propagate(False)
                
                if j==0:

                    txt = basic_text_b.split('\n')
                    txts = ''
                    #Adjusting spaces
                    for u in txt:
                        eq1, eq2, kck='', '', len(u)
                        #Adjusting spaces
                        if len(u)>18:   
                                while True:

                                    if u[kck-1]==' ':
                                        vdk=len(u[kck-1:])
                                        kdv=len(u[:kck-1])
                                        while vdk<=18-2:
                                                eq1+=' '
                                                vdk+=1
                                        while kdv<=18-1:
                                            eq2+=' '
                                            kdv+=1
                                            
                                        u = u[:kck]+eq2+'\n'+'  '+u[kck:]+eq1
                                        break
                                    kck-=1
                                
                        else:
                            for v in range(18-len(u)):
                                u+= ' '
                        u+='\n\n'
                        txts+=u

                    font_txt = ctk.CTkFont('HYGraphic-Medium', 12, 'bold', 'roman')
                    txt_btn = ctk.CTkButton(q, text=txts, corner_radius=0, fg_color=clr, text_color='#D8D4A9', border_color='white',
                    bg_color='transparent', border_width=0, hover=False, font=font_txt, anchor='we')
                    txt_btn.place(x=10, y=55)
                    txt_btn.configure(command=lambda i=i, ij=ij: rad_select(ij, i))
               
                else:
                    rad.configure(background_corner_colors=(clr, '#1E1E1E', '#1E1E1E', clr))
                    
                test_list[2].append(q_border)
                test_list[3].append(rad)
                            
                rad_command(ij, i)
                ij+=1

            radio_frame = ctk.CTkFrame(q, fg_color='transparent', corner_radius=0)
            radio_frame.grid(row=0, column=0,pady=5, padx=5, sticky='wn')       #top frame to contain the radio button

            radio_button = ctk.CTkRadioButton(radio_frame, text=all_opt[c][i],
                text_color='white', variable=radiovar, font=font_radio, corner_radius=c_r, value=0)
            radio_button.grid(row=0, column=0, pady=5, padx=5)

            in_amt, in_curr = in_all_amt[c][i], 'AED'
            price_frame = ctk.CTkFrame(q, fg_color='transparent', bg_color='transparent')
            price_frame.place(x=35, y=f_sz_rad_h-30)
            
            price_tag_font = ctk.CTkFont('HYGungSo-Bold', 15, 'normal', 'italic')
            price_tag = ctk.CTkButton(price_frame, text=f'{str(in_amt)}  {in_curr}', 
                text_color='#D8EADF', fg_color='transparent', width=sizes[0]-60 , font=price_tag_font, bg_color='transparent',
                border_width=2, hover=False, border_color='black')
            price_tag.grid(row=0, column=0, padx=0, pady=0)
            prc_tag_l.append(price_tag)
            
            radio_button.configure(command=lambda c=c, d=d, ii=i, jj=j: add_price(h_label, c, ii, jj, d, None))
            
            test_list[1].append(radio_button)
            test_list[0].append(q)
            
        for ii in range(len(curr_names)):
            curr_btns[ii].configure(command=lambda i=i,j=j,ii=ii, h=h_curr, l=h_label, c=c, d=d, ic=in_all_amt[c], ic_lbl=prc_tag_l, cn=curr_names, rad=test_list[1]: curr_converter(price_val, c, d, i, ii ,j, h, l, ic, ic_lbl, cn, rad))


    def destroy_frame(c, d):

        global test_list, ozbool_list
        ozbool_list[c][d]=0    
        test_list=[[],[],[],[]]  #SCV
        listlist[d][6].destroy()    #closes the frame

        listlist[d][6] = ctk.CTkFrame(main_frame_ticket, width=1420-(1420/14), height=2,
            fg_color='transparent',border_color='grey', border_width=1, corner_radius=0,  #creates a frame that looks like a line
        )
        listlist[d][6].grid(row=list_d[d], column = 0,padx = 0)
        
    def test(c, d, amt):
        global test_list, ozbool_list
        if ozbool_list[c][d]==0:
            c_val = c+1 if c==0 else c-1
            if ozbool_list[c_val][d]==1:
                destroy_frame(c_val, d)
                create_frame(c, d, amt)
            else:   
                create_frame(c, d, amt)
             
        elif ozbool_list[c][d]==1:
            destroy_frame(c, d)

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
    global kcvr
    image_image_Departure = ctk.CTkImage(
        light_image=Image.open(relative_to_assets(f"Departure_bg_{kcvr}.png")),
        dark_image=Image.open(relative_to_assets(f"Departure_bg_{kcvr}.png")),
        size=(1880, 395))
    bg_image_pg_2 = ctk.CTkLabel(canvas_3, image=image_image_Departure,text='')
    bg_image_pg_2.pack()
    
    main_frame_ticket = ctk.CTkScrollableFrame(canvas_3, height = 445, width = 1444, border_width=1,
        corner_radius=1, fg_color='#1E1E1E', border_color='#CCD09F', bg_color='#1E1E1E')
    main_frame_ticket.pack(pady=20, ipadx=10, ipady=5)   

    buttonsss_fonta = ctk.CTkFont('Georgia', 18, weight='bold', underline=True)
    buttonsss_fontb = ctk.CTkFont('Felix titling', 12, weight='bold', underline=False)
   
    texta = f'{fromto[0][tripway][0]} {"_"*70} {fromto[0][tripway][1]}\n5:00\t\t\t\t\t\t\t6:00'
    listlist, all_amt, all_amt_changed = [], [], []

    for i in range(bvartt):
        emplist = ['','','','','','','','','']
        listlist.append(emplist)
    
    hh=0
    for k,v in enumerate(listlist):
        
        v[5] = ctk.CTkFrame(main_frame_ticket, fg_color='transparent')
        v[5].grid(row=hh, column = 0, pady=5)
        hh+=1

        v[0] = ctk.CTkImage(
            light_image=Image.open(relative_to_assets("tktct_bg_3.jpeg")),
            dark_image=Image.open(relative_to_assets("tktct_bg_3.jpeg")),
            size=(225, 30))
        v[1] = ctk.CTkLabel(v[5], width=623, height=70, corner_radius=20, text=texta,
          text_color='#CCD09F', fg_color='black', bg_color='transparent', font=buttonsss_fontb)
        v[1].grid(row=k, column=0, padx=20, pady=3)
        
        v[2]=ctk.CTkFont('Georgia', 11, 'normal',slant='roman', underline=False)
        v[3] = ctk.CTkFrame(v[5], fg_color='transparent')
        v[3].grid(row=k, column=1, padx=25, pady=0, sticky='e')


        amt_e_rn_i, amt_e_rn_f = 34, 77
        amt_b_rn_i, amt_b_rn_f = 90, 180
        amt_e, amt_b = rn.randint(amt_e_rn_i, amt_e_rn_f)*10, rn.randint(amt_b_rn_i, amt_b_rn_f)*10
        amt_t_e , amt_t_b= f' From  {amt_e} ', f' From {amt_b}'
        amt_t, amt = [amt_t_e, amt_t_b], [amt_e, amt_b]
        all_amt.append(amt)
        all_amt_changed.append(amt)

        ff = 4
        for i in range(2):
            
            v[ff] = ctk.CTkButton(v[3], fg_color='#26294F',border_color='black',text_color='#CCD09F',
                text=amt_t[i], font=buttonsss_fonta, width=363, height=64, corner_radius=10, border_width=3)
            v[ff].grid(row=0, column=i+1, padx=8, pady=3)
            ff=7
            
        hour_label = ctk.CTkLabel(v[1], image=v[0], font=v[2], fg_color='transparent', bg_color='black',
            text="____________________________________\n5 hours / Direct\n\n", text_color='#CCD09F')
        hour_label.place(x=165, y=21)   

        v[6] = ctk.CTkFrame(main_frame_ticket,
            width=1420-(1420/14), height=2, border_width=1, fg_color='transparent',border_color='grey')
        v[6].grid(row=hh, column = 0, pady=0, padx=3, sticky='')
        hh+=1
    
    next_txt = 'Continue =>' if tripway==0 else 'Next =>'
    next_btn_font=ctk.CTkFont('Georgia', 16, 'bold', slant='italic')
    next_btn = ctk.CTkButton(window,width=170, height=50, corner_radius=10, border_width=7, hover=False,
                             text_color='#D8EADF', border_color='Black', text = next_txt,
                             bg_color='#1E1E1E', fg_color='#26294F' , font=next_btn_font,)
    next_btn.place(x=1690, y=900)
    
    if tripway==0:
        next_btn.configure(command=lambda :passdetails())
    else:
        next_btn.configure(command=lambda :dep(window, fromto, listno_pass, text_date))

    TopMenu(window, canvas_2, 88)

    ccc, ppp = 1, 0
    for i in range(2):
        ccc+=3
        for i in range(len(listlist)):
            listlist[i][ccc].configure(command = lambda c=ppp, d=i: test(c=c, d=d, amt=all_amt[d][c]))
        ppp+=1


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
web = ctk.CTk()
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
web.geometry("1880x1000")
#web.configure(bg = "#FCFFDD")
DepartuePage(web, [['(goa)','(dxb)'], ['(dxb)','(goa)']], [4,5,1], 1, ["",""])

web.mainloop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''