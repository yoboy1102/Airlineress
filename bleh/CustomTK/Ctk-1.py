import customtkinter as ctk
from customtkinter import CTkFrame,CTkButton,CTkLabel,CTkImage 
from PIL import Image, ImageTk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def tckt_dtls(window, x, y, w):
    emp_frame = CTkFrame(window, fg_color='grey', height=908, width=1240)
    emp_frame.place(x=0, y=0)
    M_w = 1880-w            # ==> Just some calculated values, many more are there in upcoming lines
    M_frame = CTkFrame(window, 
                       width=M_w,
                       height=1000-92,
                       fg_color='transparent',
                       border_width=2, border_color='black')
    M_frame.place(x=w+1, y=0)
    frms_l = []
    for f in range(3):
        frm_from_to = CTkFrame(M_frame, 
                       width=M_w,
                       height=40+92,
                       fg_color='transparent',#1E1E1E'
                       )
        frm_from_to.grid(row=f, column=0)
        frms_l.append(frm_from_to)

    text_top, top_list=['DXB         GOA', 'DXB         G2A', 'DbB         GOA'], []
    for i in range(3):
        from_to = CTkLabel(frms_l[0],       # ==> Top three frames
                        width=M_w/3,
                        height=111,
                        fg_color='#1E1E1E',
                        text=text_top[i],
                        font=('gerogia', 20, 'bold'),
                        text_color='#CCD09F'
                        )
        from_to.grid(row=0, column=i)
        top_list.append(from_to)

    ecbs_l, ec_bc_text, ecbs_det_l = [], ['Economy', 'Business'], []

    for j in range(2):
        ecbs_frm = CTkFrame(frms_l[1],                              # ==> The two class
                                width=M_w/2,
                                height=(1000-92)-((92+40)*2),
                                fg_color='#1E1111',
                                )
        ecbs_frm.grid(row=0 , column=j)
        ecbs_l.append(ecbs_frm)                     # ==> List from where you can acces the frame using indexing 


        ecbs_img = CTkImage(light_image=Image.open(relative_to_assets(ec_bc_text[j]+' Seats.png')),
                                dark_image=Image.open(relative_to_assets(ec_bc_text[j]+' Seats.png')),
                                size=(M_w/2.3, 155))
        ecbs_seat_label = CTkLabel(ecbs_frm, image=ecbs_img, text='')    # ==> Seat images
        ecbs_seat_label.pack(pady=20, padx=((M_w/2)-(M_w/2.3))/2)

        ecbs_det_frm = CTkFrame(ecbs_frm,                       # ==> Information Frame
                               width=M_w/2.3, fg_color='black',
                               height=(1000-92)-(((92+30)*2)+(155+20+10)),
                            )
        ecbs_det_frm.pack(pady=5)
        ecbs_det_l.append(ecbs_det_frm)         # ==> List from where you can acces the info frame using indexing
    frms_l[-1].configure(fg_color='#2E2E2E')

web=ctk.CTk()
web.geometry("1880x908")
web.configure(bg = "#FCFFDD")
tckt_dtls(web,0, 0, 1200)
web.mainloop()
