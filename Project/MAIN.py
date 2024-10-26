#figd_nLghGDLAXTFp9eS3-_JWIiJGCAK9nL3sb1uZshxp
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Canvas, PhotoImage
from TopMenu import TopMenu
from Departure import DepartuePage
from Spinbox import FloatSpinbox
from PassengerDetails import PassDetails
from tkcalendar import Calendar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")
#-----------------------------------------------------------------------------------------------------------
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

web = ctk.CTk()
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
web.geometry("1880x1000")
web.configure(bg = "#FCFFDD")

canvas = Canvas(web, bg="#FCFFDD", relief="ridge", height=1000, width=1880, bd=0, highlightthickness=0)
canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(file = relative_to_assets("image_1.png"))
image_1 = canvas.create_image(940.0, 500.0, image=image_image_1)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def twoway_arr():
    global image_ar, image_two, departure_date, return_date, calendar_date_d, cal_tabview
    image_two.place(x=288,y=77)
    image_ar.place(x=288,y=-50)
    departure_date.place(x=30, y=153)
    return_date.place(x=342, y=153)
    calendar_date_d.place(x=293, y=158)
    try:
        cal_tabview.add('Return')
        cal_ret = Calendar(cal_tabview.tab('Return'), selectmode='day', cursor="hand2", date_pattern='y-mm-dd',
             borderwidth=0, showweeknumbers=False, year=2024, background='#26294F', selectbackground='#0B041B',)
        cal_ret.place(x=5, y=9)
    except:
        pass
#-----------------------------------------------------------------------------------------------------------------
def oneway_arr ():
    global image_ar, image_two, departure_date, return_date, calendar_date_d, cal_tabview
    image_ar.place(x=288,y=75)
    image_two.place(x=288,y=-50)
    departure_date.place(x=170, y=155)
    return_date.place(x=0, y=400)
    calendar_date_d.place(x=433, y=158)
    try:
        cal_tabview.delete('Return')
    except:
        pass
    
def service_not_available():
    messagebox.showinfo('Service', 'Service Not Available')
   
global my_y_pass
my_y_pass = 1004
def pass_frame_place(frm):
    global my_y_pass
    if my_y_pass > 38:        
        my_y_pass=38
        frm.place(x=643, y=my_y_pass)
    elif my_y_pass < 1004:      
        my_y_pass=1004
        frm.place(x=643, y=my_y_pass)

global my_y_cal, my_x_book
my_y_cal,my_x_book = 400, 630
def calendar_date():
    global my_y_cal
    global my_x_book
    if my_y_cal == 400 and my_x_book == 630:
        my_y_cal, my_x_book = 47, 400
        cal_frame.place(x=610, y=my_y_cal)
        booking_button.place(x=my_x_book, y=220)

        departure_date.configure(text='DD/MM/YYYY', text_color='grey',font=('Georgia', 11, 'bold'))
        return_date.configure(text='DD/MM/YYYY', text_color='grey',font=('Georgia', 11, 'bold'))

    elif my_y_cal == 47 and my_x_book == 400:
        my_y_cal, my_x_book = 400, 630
        cal_frame.place(x=610, y=my_y_cal)
        booking_button.place(x=my_x_book, y=220)

        departure_date.configure(text='Departure date -->', text_color='#A6ACAC',font=('Georgia', 12))
        return_date.configure(text='Return date -->', text_color='#A6ACAC',font=('Georgia', 12))

def radconf(i):
    print(i)
    global tpw
    if i == 0:
        tpw=0
        oneway_arr()
    elif i == 1:
        tpw=1
        twoway_arr()

def departure_page():
    global tpw
    ccc, dd, vv=0, [], []
    for i in ages:
        vv.append(i.get())
    for i in range(2):
        for j in range(10):
            if entries_home[i].get() == ''*j:
                ccc+=1
                break
        else:
            print(entries_home[i].get())
            
            dd.append(entries_home[i].get())
            
            continue

    if ccc==0:
        dddd = [dd, dd[::-1]]
        print(dddd, tpw)
        DepartuePage(web, fromto=dddd, listno_pass=vv, tripway=tpw)
    else:
        messagebox.showerror('DetailError', 'Details not filled')

TopMenu(web, canvas, 88)   

#Tab View  ----------------------------------------------------------------------------------------------------------
bookframe = ctk.CTkFrame(web, corner_radius=15, width=1300, height=400, fg_color='#0B041B', bg_color='green' )
bookframe.place(x=150,y=567)

hometab = ctk.CTkTabview(bookframe, width=880, height=340, corner_radius=7, border_width=0,text_color='#CCD09F',
     fg_color='#0B031A', bg_color='#0B031A', border_color='#0B031A', segmented_button_fg_color='#0B031A',
     segmented_button_selected_color='#0B031A', segmented_button_selected_hover_color='#0B031A',
     segmented_button_unselected_color='#26294F', segmented_button_unselected_hover_color='#26294F',)
hometab.pack()

hometablist = ['      Book a Flight     ', '      Manage Booking    ',
               '        Check-in        ', '      Flight Status     ']
for i, v in enumerate(hometablist):
     hometab.add(v)
#-----------------------------------------------------------------------------------------------------------------
hometab.set(hometablist[0])
hometabcustomfont = ctk.CTkFont("Georgia", 20, 'bold')
hometab._segmented_button.configure( corner_radius=7, font=hometabcustomfont)

#Booking Tab  ----------------------------------------------------------------------------------------------------

radioname, radiobuttons, radiovar = ['One-way', 'Round Trip'], [], ctk.StringVar(web,value='')
for i,v in enumerate(radioname):
     v = ctk.CTkRadioButton(hometab.tab(hometablist[0]),
                    text=radioname[i], text_color='white', 
                    variable=radiovar, font=('Arial', 16, 'bold'),
                    border_width_checked=6,border_width_unchecked=2,
                    border_color='#26294F',fg_color='#26294F',
                    hover_color='#26294F', command=lambda i=i: radconf(i)
                    )
     if i == 0:
        v.grid(row=0, column=i, padx=50, pady=12, sticky='ew')  
     else:
        v.place(x=200,y=12)
     radiobuttons.append(v)

entryname_home, entries_home, homeroot = ['From', 'To'], [], hometab.tab(hometablist[0])

for i, v in enumerate(entryname_home):
    v = ctk.CTkEntry(homeroot, placeholder_text=entryname_home[i], width=250, height=50,
                      fg_color='#26294F', bg_color='#0B041B', border_color='black', text_color='white',)
    v.grid(row=2, column=i, padx=30, pady=20, sticky='w')
    entries_home.append(v)

pass_frame = ctk.CTkFrame(homeroot ,fg_color = '#26294F', border_color = 'black',
                    border_width = 5, corner_radius = 15, width = 122, height = 155)
pass_frame.place(x=0, y=1004)
#-----------------------------------------------------------------------------------------------------------------
btn_img_ps = ctk.CTkImage(
    light_image=Image.open(relative_to_assets("button_9.png")),
    dark_image=Image.open(relative_to_assets("button_9.png")),
    size = (122, 18))
button_pass = ctk.CTkButton(homeroot, image=btn_img_ps, width=122.0, height=20.0, border_width=2, text='', 
    command=lambda :pass_frame_place(pass_frame),
    
    fg_color='transparent', bg_color='#0B041B',
    hover_color='#0B041B', border_color='#A6ACAC',
)
button_pass.place(x=665,y=11.0,)

image_hover_pass = ctk.CTkImage(
    light_image=Image.open(relative_to_assets("button_hover_6.png")),
    dark_image=Image.open(relative_to_assets("button_hover_6.png")),
    size = (122, 18)
    )
def button_pass_hover(e):
    button_pass.configure(
        image=image_hover_pass,
        #border_color='#A6ACAC'
    )
def button_pass_leave(e):
    button_pass.configure(
        image=btn_img_ps,
        #border_color='white'
    )

button_pass.bind('<Enter>', button_pass_hover)
button_pass.bind('<Leave>', button_pass_leave)

for i in range(1):
    iclr="#A6ACAC"
    fontir = ctk.CTkFont('georgia', 14, 'bold')
    age_adult = FloatSpinbox(pass_frame, width=21, height=21,eheight=21,ewidth=25, step_size=1, set_size=1)
    age_adult.grid(row=0, column=1, padx=9,pady=10)
    age_adult.set(1)

    age_adult_text = ctk.CTkLabel(pass_frame, width=20, height=20, text='Adults', text_color=iclr, font=fontir)
    age_adult_text.grid(row=0, column=0, padx=8,pady=10)

    age_child = FloatSpinbox(pass_frame, width=21, height=21,eheight=21,ewidth=25, step_size=1, set_size=0)
    age_child.grid(row=1, column=1, padx=9,pady=10)
    age_child.set(0)

    age_child_text = ctk.CTkLabel(pass_frame, width=20, height=20, text=' Children', text_color=iclr, font=fontir)
    age_child_text.grid(row=1, column=0, padx=8,pady=10)

    age_toddler = FloatSpinbox(pass_frame, width=21, height=21,eheight=21,ewidth=25, step_size=1, set_size=0,)
    age_toddler.grid(row=2, column=1, padx=9,pady=10)
    age_toddler.set(0)

    age_toddler_text = ctk.CTkLabel(pass_frame, width=20, height=20, text='Toddlers', text_color=iclr,font=fontir)
    age_toddler_text.grid(row=2, column=0, padx=8,pady=10)

    ages = [age_adult, age_child, age_toddler]
#-----------------------------------------------------------------------------------------------------------------
departure_date_img = ctk.CTkImage(
    light_image=Image.open(relative_to_assets("Label.png")),
    dark_image=Image.open(relative_to_assets("Label.png")),
    size = (250,50.0)
    )
calendar_date_img = ctk.CTkImage(
    light_image=Image.open(relative_to_assets("button_11.png")),
    dark_image=Image.open(relative_to_assets("button_11.png")),
    size = (28, 28)
    )

departure_date = ctk.CTkLabel(hometab.tab(hometablist[0]),
                image=departure_date_img, text='Departure date -->', text_color='#A6ACAC',
                font=('Georgia', 12), width=250, height=50, anchor='w'
                              )
departure_date.grid(row=3, column=0, padx=30, pady=15, sticky='w')

calendar_date_d = ctk.CTkButton(hometab.tab(hometablist[0]),
                              image=calendar_date_img, command=calendar_date,
                              text='', fg_color='black', bg_color='#26294F', border_color='black',
                              border_width=0, corner_radius=0, width=28, height=28, hover=False, 
                              )
calendar_date_d.place(x=293, y=158)

return_date = ctk.CTkLabel(hometab.tab(hometablist[0]),
                image=departure_date_img, text='Return date -->', text_color='#A6ACAC',
                font=('Georgia', 12), width=250, height=50, anchor='w'
                              )
return_date.grid(row=3, column=1, padx=30, pady=15, sticky='w')

cal_frame = ctk.CTkFrame(hometab.tab(hometablist[0]), bg_color='#0B041B', fg_color='#0B041B')
cal_frame.place(x=69, y=400)

dep_opt_font = ctk.CTkFont('Inter', 12, 'bold')
ret_opt_font = ctk.CTkFont('Inter', 12, 'bold')

cal_tabview = ctk.CTkTabview(cal_frame, height=300, width=250, corner_radius=7, border_width=0,
     fg_color='#0B031A', text_color='white', bg_color='#0B031A', border_color='#26294F',
     segmented_button_fg_color='#26294F', segmented_button_selected_hover_color='#0B031A',
     segmented_button_selected_color='#0B031A',segmented_button_unselected_color='#26294F',
     segmented_button_unselected_hover_color='#26294F',
     )
cal_tabview.pack()

cal_tabview.add('Departure')
cal_tabview.add('Return')
cal_tabview.set('Departure')
#-----------------------------------------------------------------------------------------------------------------
cal_dep = Calendar(cal_tabview.tab('Departure'),
            selectmode='day', showweeknumbers=False,
            cursor="hand2", date_pattern= 'y-mm-dd',
            borderwidth=0, year=2024, background='#26294F',
            selectbackground='#0B041B' )
cal_dep.place(x=5, y=9)

booking_button_font = ctk.CTkFont('Arial', 16, slant='italic' )
booking_button = ctk.CTkButton(hometab.tab(hometablist[0]),width=180,
                    text='Search Flights', text_color='#A6ACAC', fg_color='#26294F',
                    border_color='Black', bg_color='#0B041B', height=40,
                    corner_radius=4, border_width=4, hover=False, 
                    font=booking_button_font, command=departure_page
                    )
booking_button.place(x=630, y=220)

def booking_hover_enter(e):
    booking_button_font.configure(slant='italic', underline=True)
    booking_button.configure(text_color = '#CCD09F')
def booking_hover_leave(e):
    booking_button_font.configure(slant='italic', underline=False)
    booking_button.configure(text_color = '#A6ACAC')

booking_button.bind('<Enter>', booking_hover_enter)
booking_button.bind('<Leave>', booking_hover_leave)
#-----------------------------------------------------------------------------------------------------------------
image_image_ar = ctk.CTkImage(
        light_image=Image.open(relative_to_assets("Arrow_.png")),
        dark_image=Image.open(relative_to_assets("Arrow_.png")),
        size=(42, 18)
        )
image_ar = ctk.CTkLabel(hometab.tab(hometablist[0]), text='', image=image_image_ar)

image_image_two = ctk.CTkImage(
        light_image=Image.open(relative_to_assets("Arrow.png")),
        dark_image=Image.open(relative_to_assets("Arrow.png")),
        size=(43, 27)
        )
image_two = ctk.CTkLabel(hometab.tab(hometablist[0]),text='',image=image_image_two)

radconf(0)

#Manage booking Tab ----------------------------------------------------------------------------------------------------------
manage_label_font = ctk.CTkFont('Georgia', 18, underline=True, slant='italic')

manage_label = ctk.CTkLabel(hometab.tab(hometablist[1]), fg_color='#0B041B',
                    text='Enter your booking details to manage your itinerary -->',
                    text_color='#A6ACAC', bg_color='#0B041B', font=manage_label_font,)
manage_label.place(x=25, y=25)


entryname_manage = ['Booking Reference No.', 'Last Name']
sticky_manage=['e','w']
entries_manage = []
#-----------------------------------------------------------------------------------------------------------------
for i, v in enumerate(entryname_manage):
    v = ctk.CTkEntry(hometab.tab(hometablist[1]),
            width=300, height=60, border_width=6, corner_radius=8,
            fg_color='#26294F', bg_color='#0B041B', border_color='black',
            placeholder_text=entryname_manage[i],)
    v.place(x=50+(i*350), y=90)
    entries_manage.append(v)

retrieve_booking_button_font = ctk.CTkFont('Georgia', 16, 'bold', slant='italic')
retrieve_booking_button = ctk.CTkButton(hometab.tab(hometablist[1]),
                            width=200, height=50, corner_radius=7, border_width=7, hover=False,
                            text='Retrieve Booking', text_color='#A6ACAC', border_color='Black', 
                            bg_color='#0B041B', fg_color='#26294F',
                            font=retrieve_booking_button_font, command=service_not_available)
retrieve_booking_button.place(x=630, y=170)

def retrieve_hover_enter(e):
    retrieve_booking_button_font.configure(slant='italic', underline=True)
    retrieve_booking_button.configure(text_color='#CCD09F')
def retrieve_hover_leave(e):
    retrieve_booking_button_font.configure(slant='italic', underline=False)
    retrieve_booking_button.configure(text_color='#A6ACAC')

retrieve_booking_button.bind('<Enter>', retrieve_hover_enter)
retrieve_booking_button.bind('<Leave>', retrieve_hover_leave)

#Check-in Tab  ----------------------------------------------------------------------------------------------------------

check_label_font = ctk.CTkFont('Georgia', 18, underline=True, slant='italic')
check_label = ctk.CTkLabel(hometab.tab(hometablist[2]),
                    text='Online check-in opens 30 hours before your flight -->',
                    text_color='#A6ACAC', bg_color='#0B041B', fg_color='#0B041B',
                    font=check_label_font,)
check_label.place(x=25, y=25)

entryname_checkin = ['Booking Reference No./Ticket No.', 'Last Name']
sticky_checkin, entries_checkin=['e','w'],[]

for i, v in enumerate(entryname_checkin):
    v = ctk.CTkEntry(hometab.tab(hometablist[2]),
                width=300, height=60, border_width=6, corner_radius=8,
                fg_color='#26294F', bg_color='#0B041B', border_color='black',
                placeholder_text=entryname_checkin[i],)
    v.place(x=50+(i*350), y=90)
    entries_checkin.append(v)
#-----------------------------------------------------------------------------------------------------------------
checkin_button_font = ctk.CTkFont('Georgia', 16, 'bold', slant='italic')
checkin_button = ctk.CTkButton(hometab.tab(hometablist[2]),
                width=150, height=50, corner_radius=7, border_width=7, hover = False,
                text='Check - In', text_color='#A6ACAC', border_color='Black',
                bg_color='#0B041B', fg_color='#26294F',
                command = service_not_available, font=checkin_button_font,)
checkin_button.place(x=630, y=170)

def checkin_hover_enter(e):
    checkin_button_font.configure(slant='italic', underline=True)
    checkin_button.configure(text_color='#CCD09F')
def checkin_hover_leave(e):
    checkin_button_font.configure(slant='italic', underline=False)
    checkin_button.configure(text_color='#A6ACAC')

checkin_button.bind('<Enter>', checkin_hover_enter)
checkin_button.bind('<Leave>', checkin_hover_leave)

disablecustomfont = ctk.CTkFont("Georgia", 19, 'bold', overstrike=True, slant='italic')
flight_status_disabled = ctk.CTkButton(bookframe, text='Flight Status',
                    text_color='#CCD09F', bg_color='#0B041B', fg_color='#26294F',
                    state='normal', width=196, height=26, hover=False, corner_radius=5,
                    command=service_not_available, font=disablecustomfont,
                    )
flight_status_disabled.place(x=658, y=13)
#-----------------------------------------------------------------------------------------------------------------
#web.wm_attributes('-transparentcolor','green')
#_____________________________________________________________________Values___________________________________________________________________________________#

Top_Attributes = {
             1 : ('home', ''),
               2 : ('explore', ''),
                 3 : ('book', None),
                   4 : ('experience', ''),
                     5 : ('destinations', ''),
                       6 : ('sign/log', ''),
                     }
Book_Frame_Attributes = {
           0 : ('option_way_type', ''),
             1 : ('from', ''),
               2 : ('to', ''),
                 3 : ('departure', ''),
                   4 : ('return', ''),
                     5 : ('destinations', ''),
                       6 : ('sign/log', ''),
}
web.mainloop()
