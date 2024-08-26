import customtkinter
from tkinter import *
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("LESGOO")
root.geometry("800x500")
root.anchor("center")

def submit():
    label.configure(text=f'Hello {entry.get()}')
    entry.configure(state="disabled")

def clear():
    entry.configure(state="normal")
    entry.delete(0, END)


label = customtkinter.CTkLabel(root,
                               text="",
                               font=('Helvetica', 24))
label.pack(padx=20, pady=20)

entry = customtkinter.CTkEntry(root,
        placeholder_text="Enter Your name",
        height=100,
        width=200,
        font=("Arial", 24),
        text_color="green",
        corner_radius=25,
        bg_color="Black",
        border_width=10,
        border_color="",
        state="normal",
        fg_color=("blue","lightblue"),
        placeholder_text_color='darkblue')
entry.pack(padx=20, pady=20)

button = customtkinter.CTkButton(root,
                                 text="Submit",
                                 command = submit
                                 )
button.pack(padx=20, pady=20)

clearbtn = customtkinter.CTkButton(root,
                                 text="Clear",
                                 command = clear
                                 )
clearbtn.pack(padx=20, pady=20)

root.mainloop()