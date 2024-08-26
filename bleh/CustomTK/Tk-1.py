import tkinter as tk
from tkinter import messagebox

class Mygui():
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        #1
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="close", command=exit)
        self.menubar.add_cascade(menu=self.filemenu, label='File')
        #2
        self.Runmenu = tk.Menu(self.menubar, tearoff=0)
        self.Runmenu.add_command(label="Run", command=self.on_closing)
        self.menubar.add_cascade(menu=self.Runmenu, label='Run')

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your Message", font = ('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10,pady=10)
        
        self.c_s = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show messagebox", font=('Arial', 16), variable=self.c_s)
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root, text="Show Msg", font=("Arial", 16), command=self.show_msg)
        self.button.pack(padx=10,pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10,pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_msg(self):
        if self.c_s.get() == 0:
            fr = self.textbox.get('1.0', tk.END)
            print(fr)
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    def shortcut(self, event):
        if event.state == 12 and event.keysym == 'Return':
            self.show_msg()
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are You Sure?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.1', tk.END)
Mygui()