#Spinbox
import customtkinter
from customtkinter import *
from typing import Union, Callable
class WidgetName(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 set_size: 0,
                 ewidth:20,
                 eheight:20,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command
        self.set_size = set_size
        self.configure(fg_color=("#0B041B", "#0B041B"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height, height=height,
                                                       command=self.subtract_button_callback, state='disabled',
                                                       font=('Eras Bold ITC',12),
                                                       fg_color='#26294F',
                                                       bg_color='#0B041B',
                                                       border_color='black',
                                                       border_width=1,
                                                       text_color_disabled='gray',
                                                       )
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=ewidth, height=eheight, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height, height=height,
                                                  command=self.add_button_callback,
                                                  font=('Eras Bold ITC',12),
                                                  fg_color='#26294F',
                                                  bg_color='#0B041B',
                                                  border_color='black',
                                                  border_width=1,
                                                  text_color_disabled='gray',
                                                  )
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)
        # default value
        self.entry.insert(0, "0.0")
        

    def add_button_callback(self):
        val = int(self.entry.get())+1
        
        if val <=6 and val >=self.set_size:
            if self.command is not None:
                self.command()
            try:
                value = int(self.entry.get()) + self.step_size
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
            except ValueError:
                return
            
            if val == 6.0:
                self.add_button.configure(state='disabled')
            if val == self.set_size:
                self.subtract_button.configure(state='disabled')
            if val != self.set_size and val != 6.0:
                self.add_button.configure(state='normal')
                self.subtract_button.configure(state='normal')



    def subtract_button_callback(self):
        val = int(self.entry.get())-1
        if val <=5 and val >=self.set_size:
            if self.command is not None:
                self.command()
            try:
                value = int(self.entry.get()) - self.step_size
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
            except ValueError:
                return
            
            if val == 6.0:
                self.add_button.configure(state='disabled')
            if val == self.set_size:
                self.subtract_button.configure(state='disabled')
            if val != self.set_size and val != 6.0:
                self.add_button.configure(state='normal')
                self.subtract_button.configure(state='normal')

        

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))
#app = customtkinter.CTk()

#spinbox_1 = FloatSpinbox(app, width=150, ewidth=150,eheight=10, step_size=1, set_size=0)
#spinbox_1.pack(padx=20, pady=20)
#spinbox_1.set(0)

#app.mainloop()