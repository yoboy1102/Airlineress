#Payment_Page

import customtkinter as ctk
from pathlib import Path
from PIL import Image, ImageTk
from tkinter import Canvas
import random as rn

# quick path setup
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Pay_page(window, fromto, dates, listno_pass, tripway, pass_details, seatres_details):

    window.geometry("1460x680")
    window.configure(bg="#E8E9F3")
    #window.resizable(False, False)
    canvas = Canvas(window, bg="#FFFFFF", height=600, width=1200)
    canvas.place(x=0, y=0)
    
    container = ctk.CTkFrame(window, fg_color="#E8E9F3", corner_radius=0, bg_color="#E8E9F3")
    container.pack(fill="both", expand=True)

    # Create main frames
    left = ctk.CTkFrame(container, fg_color="#EEF0F8", width=500, corner_radius=0, bg_color="#E8E9F3", border_width=0)
    middle = ctk.CTkFrame(container, fg_color="#F4F5FA", width=460, corner_radius=0, bg_color="#E8E9F3", border_width=0)
    right = ctk.CTkFrame(container, fg_color="#EEF0F8", width=700, corner_radius=0, bg_color="#E8E9F3", border_width=0)
    left.pack(side="left", padx=0, pady=0, fill="both", expand=True)
    middle.pack(side="left", padx=0, pady=0, fill="both", expand=False)
    right.pack(side="left", padx=0, pady=0, fill="both", expand=True)

    #----------------------------------------
    # Left Frame - Payment Section
    #----------------------------------------
    title_font = ctk.CTkFont("Arial", 34, "bold",'italic', underline=True)
    title = ctk.CTkLabel(left, text="YOUR PAYMENT INFORMATION".title(), font=title_font, text_color="#FF6B8B")  # Warm pink
    title.pack(anchor="w", pady=(40,20), padx=25)
    
    ctk.CTkLabel(left, text="💳 Card", text_color="#666B8F", font=('', 22)).pack(anchor="e", pady=(10, 25), padx=20)

    ent_height, ent_width, ent_list = 44, 400, []
    text11 = ["Cardholder Name", "Card Number", "Expiry Date", "CVV"]
    text22 = ["e.g: Sayed Mohammed", "e.g: 09518-2270-1721-4", "MM/YY", "***"]
    for i in range(4):
        ctk.CTkLabel(left, text=text11[i], text_color="#666B8F", font=('', 16)).pack(anchor="w", padx=33)
        entry = ctk.CTkEntry(left, width=ent_width, height=ent_height,
                                fg_color="#F8F9FF",  # Very light background
                                text_color="#505887",  # Darker blue-gray
                                border_color="#B4BEFF",  # Soft blue border
                                placeholder_text_color="#A0A7CC",
                                placeholder_text=text22[i] 
                                )  # Lighter text for placeholder
        entry.configure(show='*')
        entry.pack(anchor="w", pady=(5, 15), padx=(35,0))
        ent_list.append(entry)
        
    pay_button = ctk.CTkButton(left, text="Pay Now",
                              fg_color="#FF6B8B",  # Warm pink
                              hover_color="#FF8FA3",  # Lighter pink on hover
                              text_color="#FFFFFF",
                              height=55, width=225, font=('Georgia', 22, 'bold', 'italic'))
    pay_button.pack(anchor="center", pady=(45, 0))


    mid_img = ctk.CTkImage(light_image=Image.open(relative_to_assets("Pay_Img.png")),
                           dark_image=Image.open(relative_to_assets("Pay_Img.png")),
                           size=(466, 680))  


    img_label = ctk.CTkLabel(middle, image=mid_img, text='')
    
    img_label.pack(pady=0, padx=0, fill="both")
    #----------------------------------------
    # Right Frame - Flight Details
    #----------------------------------------    
    ctk.CTkLabel(right, text="READY TO FLY!", font=("Arial", 33, "bold"), 
                text_color="#FF6B8B").pack(anchor="center", pady=(10, 20))  # Warm pink

    flights = ctk.CTkScrollableFrame(right, fg_color="transparent")  # Slightly darker than parent frame
    flights.pack(fill="both", expand=True)
    
    sides = ["left", "right"]
    for j in range(tripway+1):
        root = ctk.CTkFrame(flights, fg_color="#E9E9FD")
        root.pack(side=sides[j], fill="both", expand=True, padx=(10, 0))
        ctk.CTkLabel(root, text="ECONOMY", fg_color="#4A90E2", text_color="white",
            corner_radius=5, font=('Georgia', 16,'bold')).pack(anchor="w", pady=(0, 10))
        ctk.CTkLabel(root, text=f"{fromto[j][0]} ✈ {fromto[j][1]}", font=("Georgia", 18)).pack(anchor="w")
        ctk.CTkLabel(root, text="5 Flight Tickets", font=("Arial", 18, "bold")).pack(anchor="w", pady=(10, 0))
        for i in range(sum(listno_pass)):

            
            #all details
            name = f'{pass_details[i][0]}'
            
            flight_no = ''
            for k in range(8):
                kv = str(rn.randint(0, 9))
                flight_no+=kv
            flight_no=int(flight_no)

            terminals = ["Terminal 1", "Terminal 2", "Terminal 3", "Terminal AA", "Terminal D"]
            kv = rn.randint(0, len(terminals)-1)
            print(kv)
            terminal = terminals[kv] if j==0 else '---'

            date=dates[j]
            seat=seatres_details[i] if j==0 else '---'
            Class='Economy'

            end='------------------'
        
            # outbound details
            out_details = ctk.CTkFrame(root, fg_color="transparent")
            out_details.pack(fill="x", pady=10)
            
            # left column
            out_left = ctk.CTkFrame(out_details, fg_color="transparent")
            out_left.pack(side="left", fill="both", expand=True)
            
            # passenger info
            ctk.CTkLabel(out_left, text="Passenger").pack(anchor="w", pady=(10, 0))
            ctk.CTkLabel(out_left, text="Date").pack(anchor="w")
            ctk.CTkLabel(out_left, text="Flight").pack(anchor="w", pady=(10, 0))
            ctk.CTkLabel(out_left, text="Terminal").pack(anchor="w")
            ctk.CTkLabel(out_left, text="Class").pack(anchor="w", pady=(10, 0))
            ctk.CTkLabel(out_left, text="Seat").pack(anchor="w")

            ctk.CTkLabel(out_left, text=end).pack()
            
            # right column
            out_right = ctk.CTkFrame(out_details, fg_color="transparent")
            out_right.pack(side="right", fill="both", expand=True)
            
            # flight info
            ctk.CTkLabel(out_right, text=name).pack(anchor="w", pady=(10, 0))
            ctk.CTkLabel(out_right, text=date).pack(anchor="w")
            ctk.CTkLabel(out_right, text=flight_no).pack(anchor="w", pady=(10, 0))
            ctk.CTkLabel(out_right, text=terminal).pack(anchor="w")
            ctk.CTkLabel(out_right, text=Class).pack(anchor="w", pady=(10, 0))
            ctk.CTkLabel(out_right, text=seat).pack(anchor="w")

            ctk.CTkLabel(out_right, text=end).pack()
        '''ctk.CTkLabel(ret, text="IND ✈ SHJ", font=("Georgia", 18)).pack(anchor="w")
        ctk.CTkLabel(ret, text="5 Flight Tickets", font=("Arial", 18, "bold")).pack(anchor="w", pady=(10, 0))
        
        # return details
        ret_details = ctk.CTkFrame(ret, fg_color="transparent")
        ret_details.pack(fill="x", pady=10)
        
        # left column
        ret_left = ctk.CTkFrame(ret_details, fg_color="transparent")
        ret_left.pack(side="left", fill="both", expand=True)

        # passenger info
        ctk.CTkLabel(ret_left, text="Passenger").pack(anchor="w", pady=(10, 0))
        ctk.CTkLabel(ret_left, text="Sayed Muhammed").pack(anchor="w")
        ctk.CTkLabel(ret_left, text="Flight").pack(anchor="w", pady=(10, 0))
        ctk.CTkLabel(ret_left, text="67853858").pack(anchor="w")
        ctk.CTkLabel(ret_left, text="Class").pack(anchor="w", pady=(10, 0))
        ctk.CTkLabel(ret_left, text="Economy").pack(anchor="w")
        
        # right column
        ret_right = ctk.CTkFrame(ret_details, fg_color="transparent")
        ret_right.pack(side="right", fill="both", expand=True)
        
        # flight info
        ctk.CTkLabel(ret_right, text="Date").pack(anchor="w", pady=(10, 0))
        ctk.CTkLabel(ret_right, text="15 Mar 2025").pack(anchor="w")
        ctk.CTkLabel(ret_right, text="Gate").pack(anchor="w", pady=(10, 0))
        ctk.CTkLabel(ret_right, text="---").pack(anchor="w")
        ctk.CTkLabel(ret_right, text="Seats").pack(anchor="w", pady=(10, 0))
        ctk.CTkLabel(ret_right, text="12D - 18D").pack(anchor="w")
'''

web=ctk.CTk()
Pay_page(web,[["SHJ", "IND"],["IND", "SHJ"]],["2024-09-13", "2024-09-14"], [1, 1, 2], 1, [["Sayed", "Mohammed"], ["Nitin", "Prakash"], ["Haadi", "Faisal"], ["Aravind", "Raj"]],["32B", "32A", "32C", "32D"])
web.mainloop()