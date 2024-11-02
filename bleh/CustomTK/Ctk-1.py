


import customtkinter as ctk
from customtkinter import CTkFrame,CTkButton,CTkLabel,CTkImage 
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Canvas


# Define paths for assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\transfer\Desktop\Airlineress-main\Airlineress-main\build\assets\frame0")

# Helper function to get relative path to assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def tckt_dtls(window, x, y, w):
    # Create main frame
    emp_frame = CTkFrame(window, fg_color='grey', height=908, width=1240)
    emp_frame.place(x=0, y=0)
    
    # Calculate dimensions for the main content frame
    M_w = 1880-w
    M_frame = CTkFrame(window, 
                       width=M_w,
                       height=1000-92,
                       fg_color='transparent',
                       border_width=2, border_color='black')
    M_frame.place(x=w+1, y=0)
    
    # Create three sub-frames
    frms_l = []
    for f in range(3):
        frm_from_to = CTkFrame(M_frame, 
                       width=M_w,
                       height=40+92,
                       fg_color='transparent',
                       )
        frm_from_to.grid(row=f, column=0)
        frms_l.append(frm_from_to)

    # Create top labels for flight routes
    text_top, top_list=['DXB     →    GOA', "Feb 25 | 7:00AM", 'Mar 21 | 12:15PM'],[]
    for i in range(3):
        from_to = CTkLabel(frms_l[0],
                        width=M_w/3,
                        height=88,
                        fg_color='#1E1E1E',
                        text=text_top[i],
                        font=('gerogia', 20, 'bold'),
                        text_color='#CCD09F'
                        )
        from_to.grid(row=0, column=i)
        top_list.append(from_to)
        

    loc ,top_list= ['Dubai, UAE              Goa, India', 'Departure', 'Arrival'],[]
    for j in range(3):
        place = CTkLabel(frms_l[0],
                        width=M_w / 3,
                         height=40,
                         fg_color='#1E1E1E',
                         text=loc[j],
                         font=('Georgia', 12),
                         text_color='#A9B83C')
        if j == 0:
            place.grid(row=1, column=0)  
        elif j == 1:
            place.grid(row=1, column=1)  
        else:
            place.grid(row=1, column=2)
    
    # Create frames for Economy and Business classes
    ecbs_l, ec_bc_text, ecbs_det_l = [], ['Economy', 'Business'], []

    for j in range(2):
        # Create frame for each class
        ecbs_frm = CTkFrame(frms_l[1],
                                width=M_w/2,
                                height=(1000-92)-((92+40)*2),
                                fg_color='#1E1111',
                                )
        ecbs_frm.grid(row=0 , column=j)
        
        ecbs_l.append(ecbs_frm)

        # Add seat images for each class
        ecbs_img = CTkImage(light_image=Image.open(relative_to_assets(ec_bc_text[j]+' Seats.png')),
                                dark_image=Image.open(relative_to_assets(ec_bc_text[j]+' Seats.png')),
                                size=(M_w/2.3, 155))
        ecbs_seat_label = CTkLabel(ecbs_frm, image=ecbs_img, text='')
        ecbs_seat_label.pack(pady=20, padx=((M_w/2)-(M_w/2.3))/2)

        # Create information frame for each class
        ecbs_det_frm = CTkFrame(ecbs_frm,
                               width=M_w/2.3, fg_color='black',
                               height=(1000-92)-(((92+30)*2)+(155+20+10)),
                            )
        ecbs_det_frm.pack(pady=5)
        ecbs_det_frm.pack_propagate(False)
        ecbs_det_l.append(ecbs_det_frm)

        # for Economy
        if j == 0:
            
            seat_features = [
                ("Economy", "Georgia", 25, 'bold', '#CCD09F', M_w / 2.3),
                ("\nRest and recharge during your", "Georgia", 20, None, 'white', M_w / 2.3),
                ("flight with extended leg room,", "Georgia", 20, None, 'white', M_w / 2.3),  
                ("personalized service,and a", "Georgia", 20, None, 'white', M_w / 2.3), 
                ("multi-course meal service", "Georgia", 20, None, 'white', M_w / 2.3), 
                ("\n\n• Built-in entertainment system", "Georgia", 15, None, 'white', M_w / 2.3),
                ("\n• Complimentary snacks and drinks", "Georgia", 15, None, 'white', M_w / 2.3),
                ("\n• One free carry-on and personal item", "Georgia", 15, None, 'white', M_w / 2.3),
               
              
                
            ]
            #for business class
        else:
            seat_features = [
                ("Business", "Georgia", 25, 'bold', '#CCD09F', M_w / 2.3),
                ("\nRest and recharge during your", "Georgia", 20, None, 'white', M_w / 2.3),
                ("flight with extended leg room,", "Georgia", 20, None, 'white', M_w / 2.3),  
                ("personalized service,and a", "Georgia", 20, None, 'white', M_w / 2.3), 
                ("multi-course meal service", "Georgia", 20, None, 'white', M_w / 2.3), 
                ("\n\n• Extended leg room", "Georgia", 15, None, 'white', M_w / 2.3),
                ("\n• Priority boarding", "Georgia", 15, None, 'white', M_w / 2.3),
                ("\n• Personalized service", "Georgia", 15, None, 'white', M_w / 2.3),
                ("\n• Enhanced food and drink service", "Georgia", 15, None, 'white', M_w / 2.3),
                ("\n• Seats that recline 40% more", "Georgia", 15, None, 'white', M_w / 2.3),
                ("   than economy", "Georgia", 15, None, 'white', M_w / 2.3),
                
                
                
                
                ]
        for text, font, size, weight, color, wrap_width in seat_features:
            feature_label = CTkLabel(
                ecbs_det_frm,
                text=text,
                font=(font, size, weight) if weight else (font, size),
                fg_color='black',
                text_color=color,
                anchor='w',
                width=wrap_width 
            )
            feature_label.pack(anchor="w") 
    
    # Configure the bottom frame
    frms_l[-1].configure(fg_color='#A9B83C')


    # Create and position the passenger details section
    passenger_frame = CTkFrame(frms_l[-1], fg_color='#FFF0F0', width=M_w/3, height=92)  # Use full width
    passenger_frame.grid(row=1, column=0, sticky="nsew")  # Make it fill the bottom

    # Create passenger details in the passenger frame
    canvas = Canvas(passenger_frame, bg="#FFF0F0", height=92, width=M_w)
    canvas.pack(fill="both", expand=True)

    canvas.create_text(
        28.0,
        23.0,
        anchor="nw",
        text="Passenger 1",
        fill="#7B8DB0",
        font=("NunitoSans Regular", 14 * -1)
    )

    canvas.create_text(
        28.0,
        48.0,
        anchor="nw",
        text="Sayed Muhammed",
        fill="#6D7391",
        font=("NunitoSans SemiBold", 18 * -1)
    )

    canvas.create_text(
        M_w / 2 - 50,
        23.0,
        anchor="nw",
        text="Seat number",
        fill="#7B8DB0",
        font=("NunitoSans Regular", 14 * -1)
    )

    canvas.create_text(
        M_w / 2 - 50,
        48.0,
        anchor="nw",
        text="4A",
        fill="#6D7391",
        font=("NunitoSans SemiBold", 18 * -1)
    )

    # Create buttons and align them
    button_1 = CTkButton(
        passenger_frame,
        text="Save And Close",
        command=lambda: print("Button 1 clicked"),
        width=120,
        height=40
    )
    button_1.place(x=M_w -275, y=25)  

    button_2 = CTkButton(
        passenger_frame,
        text="Payment Method",
        width=120,
        height=40
    )
    button_2.place(x=M_w - 130, y=25) 

# Create the main window
web = ctk.CTk()
web.geometry("1880x908")
web.configure(bg="#FCFFDD")
tckt_dtls(web, 0, 0, 1200)
web.mainloop()
