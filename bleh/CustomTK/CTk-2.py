import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("LESGOO")
root.geometry("800x600")
root.anchor("center")

def lesgoo():
    label.configure(text=button.cget("text"))

button = customtkinter.CTkButton(root,
                                text="LESGOOO",
                                command=lesgoo,
                                height=100,
                                width=200,
                                font=("Arial", 24),
                                text_color="WHITE",
                                fg_color="purple",
                                hover_color="green",
                                corner_radius=50,
                                bg_color="White",
                                border_width=10,
                                border_color="Lime",
                                state="normal"
                                )
button.pack(padx=20, pady=20)

label = customtkinter.CTkLabel(root,
                               text="LESGOO",
                               height=100,
                               width=200,
                               font=("Arial", 24),
                               text_color="WHITE",
                               fg_color="purple",
                               corner_radius=50,
                               bg_color="White",
                               state="normal"
                               )
label.pack(padx=20, pady=20)

root.mainloop()