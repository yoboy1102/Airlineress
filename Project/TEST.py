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
from tkcalendar import Calendar
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")
#-----------------------------------------------------------------------------------------------------------
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

web = ctk.CTk()
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
web.geometry("1880x1000")
web.iconbitmap(relative_to_assets("button_2.png"))

canvas = Canvas(web, bg="#FCFFDD", relief="ridge", height=1000, width=1880, bd=0, highlightthickness=0)
canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(file = relative_to_assets("image_1.png"))
image_1 = canvas.create_image(940.0, 500.0, image=image_image_1)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def twoway_arr():

    global image_ar, image_two, departure_date, return_date, calendar_date_d, cal_tabview

    image_two.place(x=297,y=77)
    image_ar.place(x=297,y=-50)

    departure_date.place(x=30, y=208)
    return_date.place(x=354, y=208)
    calendar_date_d.place(x=299, y=213)
    try:
        cal_tabview.add('Return')
        cal_ret = Calendar(cal_tabview.tab('Return'), selectmode='day', cursor="hand2", date_pattern='y-mm-dd',
             borderwidth=0, showweeknumbers=False, year=2024, background='#26294F', selectbackground='#0B041B',)
        cal_ret.place(x=5, y=9)
        cal_ret.bind('<<CalendarSelected>>', lambda e=E: get_date(e, cal_ret, return_date) )
    except:
        pass
#-----------------------------------------------------------------------------------------------------------------
def oneway_arr ():
    image_ar.place(x=297,y=75)
    image_two.place(x=297,y=-50)
    departure_date.place(x=182, y=208)
    return_date.place(x=0, y=400)
    calendar_date_d.place(x=444, y=213)
    try:
        cal_ret.destroy()
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

def get_date(e, cal, label):
    global text_date
    try:
        text_date = cal.get_date() 
    except:
        text_date = f'DD/MM/YYYY'
    label.configure(text=text_date, text_color='grey',font=('Georgia', 14, 'bold'))

global my_y_cal, my_x_book
my_y_cal,my_x_book = 420, 645
def calendar_date(e):
    global my_y_cal, my_x_book

    if my_y_cal == 420 and my_x_book == 645:
        my_y_cal, my_x_book = 80, 400
        cal_frame.place(x=610, y=my_y_cal)
        booking_button.place(x=my_x_book, y=280)

    elif my_y_cal == 80 and my_x_book == 400:
        my_y_cal, my_x_book = 420, 645
        cal_frame.place(x=610, y=my_y_cal)
        booking_button.place(x=my_x_book, y=280)

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
    global tpw, text_date

    tdp = departure_date.cget('text')
    tdr = return_date.cget('text')
    td = [tdp, tdr]
    print(td)

    for i in range(tpw+1):
        if td[i] == 'DD/MM/YYYY' or td[i]=='Departure date -->' or td[i]=='Return date -->':
            messagebox.showerror('DateError', 'Date not selected')
            return
        else:
            continue
    
    if tdr < tdp:
        messagebox.showerror('DateError', 'Return date cannot be before departure date')
        return

    ccc, dd, vv=0, [], []
    for i in ages:
        vv.append(i.get())

    for i in range(2):
        for j in range(10):
            if entries_home[i].get() == ''*j:
                 ccc+=1
                 break
        else:   
            plc = entries_home[i].get()
            l_br_i = plc.index('(')
            r_br_i = plc.index(')')         
            dd.append(plc[l_br_i+1:r_br_i])
            continue

    if ccc==0:
        dddd = [[dd[::-1], dd], [entries_home[0].get(), entries_home[1].get()]]
        print(dddd, tpw)
        DepartuePage(web, fromto=dddd, listno_pass=vv, tripway=tpw, text_date=td)
    else:
        messagebox.showerror('DetailError', 'Details not filled')

def listbox_update(data, lb):
    lb.delete(0, END)
    for i in data:
        lb.insert(END, i)
def entry_update(e, entry, lb):
    entry.delete(0, END)
    entry.insert(0, lb.get(ACTIVE))

def listbox_select(e, entry, lb):
    entered = entry.get()
    for i in range(10):
        if entered == '':
            data = possible_destinations
    else:
        data = []
        for i in possible_destinations:
            if entered.lower() in i.lower():
                data.append(i)
    listbox_update(data, lb)

def poly_but(sf, xx, but):
    if sf.winfo_y() == 117:
        takeout(E, sf, xx, but)
        print('blabla')
    elif sf.winfo_y() == 600:
        bringin(E, sf, xx, but)
        print('byeye')
    print(sf.winfo_y())
    print('Hi')
def bringin(e, sf, xx, but):
    sf.place(x=xx, y=117)
    but.configure(image=img_l[1])
def takeout(e, sf, xx, but):    
    sf.place(x=xx, y=600)
    but.configure(image=img_l[0])

TopMenu(web, canvas, 88)   

#Tab View  ----------------------------------------------------------------------------------------------------------
bookframe = ctk.CTkFrame(web, corner_radius=15, width=1300, height=400, fg_color='#0B041B', bg_color='green' )
bookframe.place(x=150,y=530)

hometab = ctk.CTkTabview(bookframe, width=880, height=405, corner_radius=7, border_width=0,text_color='#CCD09F',
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

radioname, radiobuttons, radiovar, homeroot = ['One-way', 'Round Trip'], [], ctk.StringVar(web,value=''), hometab.tab(hometablist[0])
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




"""# Connect to the MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="flight_database"
    )
    cursor = conn.cursor()
    print("Successfully connected to the database")

    # Load information from the destinations table
    cursor.execute("SELECT country_name, place_name, place_code FROM destinations")
    destinations = cursor.fetchall()

    # Process the fetched data
    countries = []
    places = []
    place_codes = {}
    for country, place, code in destinations:
        if country not in countries:
            countries.append(country)
        places.append(place)
        place_codes[place] = code

    print(f"Loaded {len(destinations)} destinations")

except mysql.connector.Error as err:
    print(f"Error connecting to the database or fetching data: {err}")

# Function to close the database connection
def close_database():
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Database connection closed")

# Make sure to call close_database() when the application exits
web.protocol("WM_DELETE_WINDOW", lambda: [close_database(), web.destroy()])

# Update the possible_destinations list with the loaded data
possible_destinations = places"""






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
    button_pass.configure(image=image_hover_pass)
def button_pass_leave(e):
    button_pass.configure(image=btn_img_ps,)

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

    age_infant = FloatSpinbox(pass_frame, width=21, height=21,eheight=21,ewidth=25, step_size=1, set_size=0,)
    age_infant.grid(row=2, column=1, padx=9,pady=10)
    age_infant.set(0)

    age_infant_text = ctk.CTkLabel(pass_frame, width=20, height=20, text='infants', text_color=iclr,font=fontir)
    age_infant_text.grid(row=2, column=0, padx=8,pady=10)

    ages = [age_adult, age_child, age_infant]
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
                              image=calendar_date_img, command=lambda e=E:calendar_date(e),
                              text='', fg_color='black', bg_color='#26294F', border_color='black',
                              border_width=0, corner_radius=0, width=28, height=28, hover=False, 
                              )
calendar_date_d.place(x=293, y=158)

return_date = ctk.CTkLabel(hometab.tab(hometablist[0]),
                image=departure_date_img, text='Return date -->', text_color='#A6ACAC',
                font=('Georgia', 12), width=250, height=50, anchor='w'
                              )
return_date.grid(row=3, column=1, padx=30, pady=15, sticky='w')


#=============================================================================================================================================================
possible_destinations = ['Madrid, Spain:(MAD)', 'Athens, Greece:(ATH)', 'Bali, Indonesia:(DPS)', 'Berlin, Germany:(BER)', 'Paris, France:(CDG)', 'Rome, Italy:(FCO)', 'Vienna, Austria:(VIE)']
entryname_home, entries_home, xx, xx_poly , img_add, img_l, lb_l= ['From', 'To'], [], [42, 370], [255, 575], ["Poly down", "Poly up"], [], []
for i, v in enumerate(entryname_home):
    listbox_font = ctk.CTkFont('Georgia', 16, 'bold')
    listbox = Listbox(
        homeroot, 
        font=listbox_font,
        fg='#CCD09F',          # Brighter text color for better readability
        bg='#26294F',          # Matching background with entry fields
        selectforeground='white',    # Selected item text color
        selectbackground='#0B041B',  # Selected item background
        borderwidth=2,              
        relief="solid",
        highlightthickness=1,
        highlightcolor='#A6ACAC',
        highlightbackground='#26294F',
        height=6,                    # Show 6 items at a time
        activestyle='dotbox'         # Better visual feedback for active item
    )
    listbox.place(x=xx[i], y=600)
    
    # Add hover effect for listbox items
    def on_enter(e, lb=listbox):
        current = lb.nearest(e.y)
        lb.selection_clear(0, END)
        lb.selection_set(current)
        lb.activate(current)

    def on_leave(e, lb=listbox):
        lb.selection_clear(0, END)

    listbox.bind('<Motion>', on_enter)
    listbox.bind('<Leave>', on_leave)

    listbox_update(possible_destinations, listbox)
    lb_l.append(listbox)

    v = ctk.CTkEntry(homeroot, placeholder_text=entryname_home[i], width=250, height=50, font=('Times New Roman', 14, 'bold'),
                      fg_color='#26294F', bg_color='#0B041B', border_color='black', text_color='#A6ACAC',)
    v.grid(row=2, column=i, padx=35, pady=20, sticky='w')

    entries_home.append(v)

    img_poly = ctk.CTkImage(
        
        light_image=Image.open(relative_to_assets(img_add[i]+'.png')),
        dark_image=Image.open(relative_to_assets(img_add[i]+'.png')),
        size = (10, 7)
        )
    img_l.append(img_poly)
    img_but = ctk.CTkButton(homeroot, image=img_l[0], text='', fg_color='transparent', bg_color='#26294F', hover=False, width=10, height=7,)
    img_but.place(x=xx_poly[i], y=84)
    img_but.configure(command=lambda i=i, but=img_but, sf=listbox: poly_but(sf, xx[i], but))

    # Bind click event to the main window
    web.bind('<Button-1>', lambda e, sf=listbox, xx=xx[i], but=img_but: 
             takeout(e, sf, xx, but))

    v.bind('<KeyRelease>', lambda e, entry=v, i=i, lb=listbox, sf=listbox: 
           listbox_select(e, entry, lb))
    v.bind('<FocusIn>', lambda e, entry=v, i=i, but=img_but, sf=listbox: 
           bringin(e, sf, xx[i], but))

    listbox.bind('<Button-1>', lambda e, entry=v, lb=listbox: 
                 entry_update(e, entry, lb))
#=============================================================================================================================================================e


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
cal_dep.bind('<<CalendarSelected>>', lambda e=E: get_date(e, cal_dep, departure_date)  )

cal_ret = Calendar(cal_tabview.tab('Return'), selectmode='day', cursor="hand2", date_pattern='y-mm-dd',
             borderwidth=0, showweeknumbers=False, year=2024, background='#26294F', selectbackground='#0B041B',)
cal_ret.place(x=5, y=9)

booking_button_font = ctk.CTkFont('Arial', 16, slant='italic' )
booking_button = ctk.CTkButton(hometab.tab(hometablist[0]),width=180,
                    text='Search Flights', text_color='#A6ACAC', fg_color='#26294F',
                    border_color='Black', bg_color='#0B041B', height=40,
                    corner_radius=4, border_width=4, hover=False, 
                    font=booking_button_font, command=departure_page
                    )
booking_button.place(x=645, y=267)

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

radiobuttons[0].invoke()

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

# Add this new function at the top level
def handle_click_outside(event):
    widget = event.widget
    
    # Check each listbox
    for i, listbox in enumerate(lb_l):
        # Only process if listbox is visible (y=117)
        if listbox.winfo_y() == 117:
            # Get click coordinates relative to the window
            click_x = web.winfo_pointerx() - web.winfo_rootx()
            click_y = web.winfo_pointery() - web.winfo_rooty()
            
            # Get listbox coordinates and dimensions
            lb_x = listbox.winfo_x()
            lb_y = listbox.winfo_y()
            lb_width = listbox.winfo_width()
            lb_height = listbox.winfo_height()
            
            # If click is outside listbox area
            if not (lb_x <= click_x <= lb_x + lb_width and 
                   lb_y <= click_y <= lb_y + lb_height):
                takeout(None, listbox, xx[i], img_l[i])

# Replace the old web.bind line with this (after all listboxes are created):
web.bind('<Button-1>', handle_click_outside)

web.mainloop()