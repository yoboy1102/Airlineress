import customtkinter as ctk
from customtkinter import CTkFrame,CTkButton,CTkLabel,CTkImage 
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Canvas


# Define paths for assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

# Helper function to get relative path to assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def tckt_dtls(window,y, w, pass_details, tckt_details):
    
    
    # Calculate dimensions for the main content frame
    M_w = 1880-w
    M_frame = CTkFrame(window, 
                       width=M_w,
                       height=1000-92,
                       fg_color='#D9D9D9',
                       border_width=2, border_color='black', corner_radius=0)
    M_frame.place(x=w+1, y=y)
    
    # Create three sub-frames
    frms_l, frm_clr = [], ['#d9d9d9', '#0b015e', 'transparent']
    for f in range(3):
        frm_from_to = CTkFrame(M_frame, 
                       width=M_w,
                       height=40+92,
                       fg_color=frm_clr[f],corner_radius=0
                       )
        frm_from_to.grid(row=f, column=0)
        frm_from_to.columnconfigure(index=0,weight=0)
        frms_l.append(frm_from_to)

    # Create top labels for flight routes
    
    from_to_text = [tckt_details[0][0][0], tckt_details[0][0][1]]
    text_top, top_list,  = [f'{from_to_text[0]}     →    {from_to_text[1]}', "Feb 25 | 7:00AM", 'Mar 21 | 12:15PM'], []
    for i in range(3):
        #sze = M_w/3
        sze = M_w/2 if i==0 else (M_w-M_w/2)/2
        from_to = CTkLabel(frms_l[0],
                        width=sze,
                        height=72,
                        fg_color='#05191A',
                        text=text_top[i],
                        font=('gerogia', 20, 'bold'),
                        text_color='#CCD09F', corner_radius=0
                        )
        from_to.grid(row=0, column=i)
        top_list.append(from_to)
    
        
    loc_text1 = tckt_details[1][0].split(':')[0] #+ '' + tckt_details[1][0].split(',')[1].split(':')[0] 
    loc_text2 = tckt_details[1][1].split(':')[0]
    loc_text = [loc_text1, loc_text2]
    print(loc_text1, loc_text2)
    loc ,top_list= [f'{loc_text[0]}\t\t{loc_text[1]}', 'Departure', 'Return'],[]
    for j in range(3):
        sze = M_w/2 if i==0 else (M_w-M_w/2)/2
        place = CTkLabel(frms_l[0],
                        width=sze,
                        #height=40,
                        fg_color='#05191A',
                        text=loc[j],
                        font=('Georgia', 12),
                        text_color='#D9D9D9', corner_radius=0
                        )
        place.grid(row=1, column=j, sticky='we')
        
    
    # Create frames for Economy and Business classes
    ecbs_l, ec_bc_text, ecbs_det_l = [], ['Economy', 'Business'], []

    for j in range(2):
        # Create frame for each class
        ecbs_frm = CTkFrame(frms_l[1],
                                width=M_w/2,
                                height=(1000-92)-((92+6)*2),
                                fg_color='#1E1E1E', corner_radius=0
                                )
        ecbs_frm.grid(row=0 , column=j, pady=1, padx=0)
        ecbs_frm.pack_propagate(False)
        ecbs_frm.grid_propagate(False)
        
        ecbs_l.append(ecbs_frm)

        # Add seat images for each class
        ecbs_img = CTkImage(light_image=Image.open(relative_to_assets(ec_bc_text[j]+' Seats.png')),
                                dark_image=Image.open(relative_to_assets(ec_bc_text[j]+' Seats.png')),
                                size=(M_w/2.3, 155))
        ecbs_seat_label = CTkLabel(ecbs_frm, image=ecbs_img, text='')
        ecbs_seat_label.pack(pady=20, padx=((M_w/2)-(M_w/2.3))/2)

        # Create information frame for each class
        ecbs_det_frm = CTkFrame(ecbs_frm,
                               width=M_w/2.3, fg_color='#1E1E1E', corner_radius=0,
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
                fg_color='#1E1E1E',
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
    btn_xy = [[M_w -275, 25], [M_w -130, 25]]
    btn_text, btn_list = ["Save And Close", "Payment Method"], []
    # Create buttons and align them
    for i in range(2):   
        btn = CTkButton(passenger_frame,
        text=btn_text[i], width=120, height=40)
        btn.place(x=btn_xy[i][0], y=btn_xy[i][1])  
        btn_list.append(btn)
    

# Create the main window
'''''''''''''''''''''
web = ctk.CTk()
web.geometry("1880x908")
web.configure(bg="#1E1E1E")
tckt_dtls(web, 0, 1221, ['sayed', 'rizvi', 'bbc@bbc.bbc'], [[['MAD', 'ATH'], ['ATH', 'MAD']], ['Madrid, Spain:(MAD)', 'Athens, Greece:(ATH)']])
web.mainloop()
'''''''''''''''''''''
