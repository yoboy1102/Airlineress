import customtkinter as ctk
import PIL
from PIL import Image, ImageTk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
log_sign_w, f_mov_w = 1400/2-150, 1400/2+150
log_sign_h, f_mov_h = 700-92, 700-92
p_t = [['Enter your Email Adress', 'Enter your Password'], ['Enter your Email Adress', 'Enter your Password']]
log_list = ['log_font', 'log_label',[ 'log_email', 'log_pass'], 'log_button', 'switch_to'] 
sign_list = ['sign_font', 'sign_label',[ 'sign_email', 'sign_pass'], 'sign_button', 'switch_to']
frame_list, f_fg_c = ['fr_top','fr_log','fr_sign', 'fr_mov'], ['#0B041B', '#05191A', '#071B41', 'gray']
hv_list = [" Don't have an account => Sign Up", "Already have an account => Log In"]

global lsm_x, conf, lsos
lsm_x, conf, ss, lstxt_l, b_clr = log_sign_w, True, [''], ['log in', 'sign up'], ['#214446', '#0E2C65']

f_w_h = [[1400, 92], [log_sign_w, log_sign_h], [log_sign_w, log_sign_h], [f_mov_w, f_mov_h]]
f_x_y, log_sign_list  = [[0,0], [0,92], [850, 92], [550, 92]], [log_list, sign_list]
lsos = "Login to MirageFly"
def moveleft(frm, window):
    global lsm_x, conf
    if lsm_x > 0:
        lsm_x -= 11/2
        frm.place(x=lsm_x, y=92)
        window.after(3, lambda :moveleft(frm, window))
def moveright(frm, window):
    global lsm_x, conf
    if lsm_x >= 0 and lsm_x < 550:
        lsm_x += 11/2
        frm.place(x=lsm_x, y=92)
        window.after(2, lambda :moveright(frm, window))
def here(x):
    global lsos
    lsos=lsos+'S'
    x.configure(text=lsos)

def LogIn_SignUp(window):

    for i, v in enumerate(frame_list):

        v = ctk.CTkFrame(
            window,
            width=f_w_h[i][0],
            height=f_w_h[i][1],
            fg_color=f_fg_c[i],
            corner_radius=0
        )
        v.place(x=f_x_y[i][0],y=f_x_y[i][1])
        frame_list[i] = v
#TopMenu
    image_3 = ctk.CTkImage(light_image=Image.open(relative_to_assets("button_3.png")),
                           dark_image=Image.open(relative_to_assets("button_3.png")), size=(100, 77))

    button_3 = ctk.CTkButton(frame_list[0], image=image_3, text='', fg_color='transparent',
                            bg_color='#0B041B', hover=False, command=lambda:print("button_3 clicked"),
                            width=100.0, height=91.0)
    button_3.place(x=77)
#Moving_Frame
    big_lbl_font = ctk.CTkFont('Times', 24, 'bold')

    big_lbl = ctk.CTkLabel(frame_list[-1],
                        text=lsos,
                        font=big_lbl_font,
    )
    big_lbl.place(x=75, y=55)
    btn=ctk.CTkButton(frame_list[-1], command=lambda :here(big_lbl))
    btn.place(x=100, y=100)
    
#frame_login/SignIn
    ff=0
    for s in log_sign_list:
        for j, v in enumerate(ss):
            pp=frame_list[ff+1]
            w=s
            w[0] = ctk.CTkFont('STFangsong', 26, 'bold', 'roman', underline=True)
            w[1] = ctk.CTkLabel(pp,
                text=lstxt_l[ff].title(), 
                font=w[0], text_color='#CCD09F')
            w[1].place(x=230, y=92)
            
            for k in range(2):
                w[2][k] = ctk.CTkEntry(pp,
                    width=320, height=70,
                    placeholder_text=p_t[0][k],
                    corner_radius=10,
                    border_color='#CCD09F', border_width=1
                )
                w[2][k].place(x=275-160, y=230+(k*100))
            w[3] = ctk.CTkButton(pp,
                width=275, height=50,
                text = lstxt_l[ff].title(),
                font = ('georgia', 18),
                fg_color=b_clr[ff], corner_radius=25
            )
            w[3].place(x=137, y=450)

            w4font = ctk.CTkFont('Times', 18, 'bold', underline=True)
            w[4] = ctk.CTkButton(pp,
                text=hv_list[ff], text_color='#CCD09F',
                fg_color='transparent',
                bg_color='transparent',
                font=w4font, hover=False
            )
            w[4].place(x=550-307, y= 700-92-70)
            ff+=1
    log_list[4].configure(command=lambda :moveleft(frame_list[-1],window))
    sign_list[4].configure(command=lambda :moveright(frame_list[-1],window))
    window.resizable(False,False)
'''''''''''''''''''''''''''
web=ctk.CTk()
web.geometry('1400x700')
LogIn_SignUp(web)
web.mainloop()
'''''''''''''''''''''''''''
