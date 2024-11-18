#DestinationsMenu
import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def destinations_menu(frames):
    def hover_effect(btn, font, i):
        font_i, font_s = font, ctk.CTkFont('Georgia', 22, 'normal',slant='italic', underline=True)
        btn.bind('<Enter>', lambda e: btn.configure(font=font_s))
        btn.bind('<Leave>', lambda e: btn.configure(font=font_i))
        hover_effect_lbl(btn, b_img_lbl, i+1)
        
    def btn_cont_creator(text, frm, i):
        btn_cont_font = ctk.CTkFont('Georgia', 22, 'normal',slant='roman', underline=False)
        btn_cont = ctk.CTkButton(frm, text=text, height=35, width=60,
                                 fg_color='black', text_color='#CCD09F', font=btn_cont_font)
        btn_cont.grid(row=i, column=0, padx=0, pady=0, sticky='s')
        hover_effect(btn_cont, btn_cont_font, i)
        
    def img_loader(img_path, sze):
        img = ctk.CTkImage(light_image=Image.open(relative_to_assets(img_path)),
                           dark_image=Image.open(relative_to_assets(img_path)),
                           size=sze)
        return img
    def hover_effect_lbl(lbl, lbl1, i):
        lbl.bind('<Enter>', lambda e: lbl1.configure(image=img_list[i]))
        lbl.bind('<Leave>', lambda e: lbl1.configure(image=img_list[0]))
        #lbl.bind('<Enter>', lambda e: lbl.configure(fg_color='#4684D4'))

    def btn_count_hover_enter(btn, font):
        font.configure(slant='italic', underline=True)
        btn.configure(font=font, border_color='#ACACA6')
    def btn_count_hover_leave(btn, font):
        font.configure(slant='roman', underline=False)
        btn.configure(font=font, border_color='white')
    def btn_count_creator(root, i, v, b, img_path, img_list, font_list):
        font = ctk.CTkFont('STFangsong', 18, "bold")
        font_list.append(font)
        img = ctk.CTkImage(light_image=Image.open(relative_to_assets(img_path)),
                           dark_image=Image.open(relative_to_assets(img_path)),
                           size=(25, 25))
        img_list.append(img)
        btn = ctk.CTkButton(root, text= v, image=img, fg_color='#0B041B', corner_radius=7, border_color='white', border_width=1, font=font, text_color='#CCD09F')
        btn.bind('<Enter>', lambda e,i=i: btn_count_hover_enter(btn, font_list[i]))
        btn.bind('<Leave>', lambda e,i=i: btn_count_hover_leave(btn, font_list[i]))
        
        return btn

    #Divide into two frames
    frms_hw, frms_list = [[630, 330], [900, 330]], []
    for i in range(2):
        frms = ctk.CTkFrame(frames, width=frms_hw[i][0], height=frms_hw[i][1], border_width=0, fg_color='transparent')
        frms.grid(row=0, column=i, padx=30, pady=20)
        frms.pack_propagate(False)
        frms.grid_propagate(False)
        frms_list.append(frms)

    #First frame====================================================================================================================================
    frms_list[0].configure(fg_color='transparent')
    #frms_list[0].grid_propagate(True)
    #frms_list[0].pack_propagate(True)

    head_frm = ctk.CTkFrame(frms_list[0], fg_color='transparent', width=620, height=35)
    head_frm.grid(row=0, column=0, padx=5, pady=10)
    head_frm.grid_propagate(False)
    head_frm.pack_propagate(False)
    head_font = ctk.CTkFont('Georgia', 30, 'normal', slant='roman', underline=False)
    head_label = ctk.CTkLabel(head_frm, text='Our Destinations', font=head_font, text_color='#CCD09F')
    head_label.pack()

    body_frm = ctk.CTkFrame(frms_list[0], fg_color='transparent', width=620, height=260)
    body_frm.grid(row=1, column=0, padx=5, pady=10)
    #body_frm.grid_propagate(False)
    #body_frm.pack_propagate(False)

    b_img_frm = ctk.CTkFrame(body_frm, fg_color='transparent', width=365)
    b_img_frm.grid(row=0, column=0, padx=5, pady=0)

    b_img_lbl = ctk.CTkLabel(b_img_frm,
                              fg_color='transparent',
                              width=400,
                              height=250,
                              text=''
                              )
    b_img_lbl.pack(pady=2, padx=2, anchor='n')

    b_text_frm = ctk.CTkFrame(body_frm, fg_color='transparent', width=200, height=225)
    b_text_frm.grid(row=0, column=1, padx=30, pady=0, sticky='s')
    b_text_frm.grid_propagate(False)
    b_text_frm.pack_propagate(False)

    #Continents Texts
    text_cont_list = [' Europe ', ' Asia & the\nPacific ', ' Americas ', ' Middle East ', ' Africa ']
    for i in range(5):
        btn_cont_creator(text_cont_list[i], b_text_frm, i)
    
    img_list = []
    for i in range(6):
        img = img_loader(f'DestinationsMenu\map{i}.png', (400, 200))
        img_list.append(img)

    b_img_lbl.configure(image=img_list[0])
    
    #Second frame====================================================================================================================================

    header_frm = ctk.CTkFrame(frms_list[1])
    header_frm.pack(padx=10, pady=20)
    font3 = ctk.CTkFont('georgia', 20, slant='italic')
    header_lbl = ctk.CTkLabel(header_frm, text='Countries we Fly to ==>', text_color='#CCD09F', font=font3, fg_color='black')
    header_lbl.pack()

    countries_list = [
    "Afghanistan", "East Timor", "Laos", "Saint Lucia", "Albania", "Ecuador", "Latvia",
    "Saint Vincent and the Grenadines", "Algeria", "Egypt", "Lebanon", "Andorra", 
    "El Salvador", "Lesotho", "Samoa", "Angola", "Equatorial Guinea", "Liberia", 
    "San Marino", "Antigua and Barbuda", "Eritrea", "Libya", "Saudi Arabia", 
    "Estonia", "Liechtenstein", "Senegal", "Argentina", "Eswatini", "Lithuania", 
    "Serbia", "Armenia", "Ethiopia", "Luxembourg", "Seychelles", "Aruba", 
    "European Union", "Sierra Leone", "Australia", "Singapore", "Austria", "Madagascar", 
    "Sint Maarten", "Azerbaijan", "Fiji", "Malawi", "Slovakia", "Finland", 
    "Malaysia", "Slovenia", "France", "Maldives", "Solomon Islands", "Bahamas", 
    "Mali", "Somalia", "Bahrain", "Malta", "South Africa", "Bangladesh", "Gabon", 
    "Marshall Islands", "South Korea", "Barbados", "Gambia", "Mauritania", 
    "South Sudan", "Belarus", "Georgia", "Mauritius", "Spain", "Belgium", "Germany", 
    "Mexico", "Sri Lanka", "Belize", "Ghana", "Micronesia", "Sudan", "Benin", 
    "Greece", "Moldova", "Suriname", "Bhutan", "Grenada", "Monaco", "Sweden", 
    "Bolivia", "Guatemala", "Mongolia", "Switzerland", "Bosnia and Herzegovina", 
    "Guinea", "Montenegro", "Syria", "Guinea-Bissau", "Morocco", "São Tomé and Príncipe", 
    "Botswana", "Guyana", "Brazil", "Mozambique", "Brunei", "Myanmar", "Bulgaria", 
    "Haiti", "Taiwan", "Burkina Faso", "Honduras", "Tajikistan", "Burundi", 
    "Hungary", "Namibia", "Tanzania", "Nauru", "Thailand", "Nepal", "Togo", 
    "Cameroon", "Iceland", "Netherlands", "Tonga", "Canada", "India", "New Zealand", 
    "Trinidad and Tobago", "Cape Verde", "Indonesia", "Nicaragua", "Tunisia", 
    "Central African Republic", "Iran", "Niger", "Turkmenistan", "Iraq", "Nigeria", 
    "Tuvalu", "Chad", "Ireland", "North Korea", "Chile", "Israel", "North Macedonia", 
    "China", "Italy", "Norway", "Uganda", "Colombia", "Ivory Coast", "Ukraine", 
    "Comoros", "United Arab Emirates", "Costa Rica", "Oman", "Croatia", "Jamaica", 
    "United Kingdom", "Cuba", "Japan", "United States of America", "Curaçao", 
    "Jordan", "Pakistan", "Cyprus", "Palau", "Uruguay", "Czech Republic", 
    "Palestine", "Uzbekistan", "Kazakhstan", "Panama", "Papua New Guinea", 
    "Democratic Republic of the Congo", "Kenya", "Vanuatu", "Kiribati", "Paraguay", 
    #"Vatican City",
      "Denmark", "Kosovo", "Peru", "Venezuela", "Djibouti", "Kuwait", 
    "Philippines", "Vietnam", "Dominica", "Kyrgyzstan", "Poland", "Dominican Republic", 
    "Portugal", "Yemen", "Qatar", "Zambia", "Republic of the Congo", "Zimbabwe", 
    "Republic of Türkiye", "Romania", "Russia", "Rwanda"]
    countries_list.sort()

    body_frm = ctk.CTkScrollableFrame(frms_list[1], width=frms_hw[1][0]+200, height=frms_hw[1][1]/1.3, fg_color='transparent')
    body_frm.pack(padx=10, pady=10)
    

    btn_list, types, img_list_2, font_list_2 = [], ['', ' Rounded', ' Circle', ' Square'], [], []
    rr, cc = 0, 0
    '''''''''
    for ii, v in enumerate(countries_list):
        if ii%3==0:
            rr+=1
            cc=0
        img_path_2 = f"Flags\{v}{types[0]}.png"
        btn = btn_count_creator(body_frm ,ii, v, 2, img_path_2, img_list_2, font_list_2)
        btn.grid(row=rr, column=cc, padx=10, pady=5)
        btn_list.append(btn)
        cc+=1
        '''''''''




