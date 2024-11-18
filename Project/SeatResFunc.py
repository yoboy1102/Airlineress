#SeatResFunc
from pathlib import Path
import customtkinter as ctk
import csv
from PIL import Image
import random
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"c:\Users\Arubaaa\OneDrive\Desktop\DESKTOP\kama 2024")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def CB(bools, p, q, alph, n__0, b, d):
    print(p,q+1,alph[q][0])
global n0, n_0
n0, n_0=1, 1

class SeatResFunc():
    def __init__(self, boolv ,m, n, o, eco_buss, CBcheck_val, fff, ww, er, pdx, clr):
        global  n0, n_0
        self.let_list = []
        with open(relative_to_assets('Project\LETTER.csv'), 'r') as cc:
            reader=csv.reader(cc)
            next(reader)
            for row in reader:
                    self.let_list.append(row)
        clr_l_s = ['grey', 'grey']
        l, k=0, 1
        self.ww=ww
        self.hh = ww+10
        self.er = er
        for i in range(m):
            self.ff, v=0, []
            self.let_new = self.let_list[0:n]
            self.let_new.insert(int(n/2), '    ')
            slctd_no = random.randint(-o, n-1)
            
            for j in range(n):
                self.var = ctk.IntVar(eco_buss)  
                self.ff+=fff
                if i==0:
                    self.le_lbll=ctk.CTkLabel(eco_buss, text=self.let_new[int(self.ff-1)],
                                        font=('Arial Rounded MT Bold',pdx[2]+6,))
                    self.le_lbll.grid(row=i, column=int(self.ff), sticky='s', padx=0)
                else:
                    self.emp_labela = ctk.CTkLabel(eco_buss, text='   ')
                    self.emp_labela.grid(row=i, column=0) 

                self.radd = ctk.CTkCheckBox(eco_buss, fg_color=clr[0], hover_color=clr[1], border_color=clr[0], 
                            checkbox_height=self.hh, checkbox_width=ww, border_width=ww/8, variable=self.var,
                            corner_radius=8, text=None,  textvariable=None, hover=True, height=20, width=0, )
                if j == slctd_no:
                    self.radd.select()
                    self.radd.configure(fg_color=clr_l_s[0], border_color=clr_l_s[1], state='disabled') 
                #ED5E7A
                self.radd.configure(command=lambda i=i, j=j, n_0=n_0: 
                                    CBcheck_val(boolv, i, j, self.er, self.let_list[0:n], n_0, clr))
                self.radd.grid(row=i+1, column=int(self.ff), padx=pdx[0], pady=pdx[2], sticky='w')
                v.append(self.radd)
                
            self.n0_lbll = ctk.CTkLabel(eco_buss, text=str(n0)+'  ', font=('Arial Black',pdx[2]+6,'bold'))
            self.n0_lbll.grid(row=i+1, column=int(n/2+1), padx=pdx[1], pady=pdx[2])

            self.emp_label = ctk.CTkLabel(eco_buss, text=self.let_new[int(n/2)])
            self.emp_label.grid(row=0, column=(int(n/2+1)))
            
            self.er.append(v)
            n0+=1
        n_0 = 1
        n_0+=n0-1
'''        
web = ctk.CTk()
eco_buss = []
eco_rad=[]
bus_clr, eco_clr, extr_clr = ['#3DCCB2', '#84FFE9'], ['#ED5B80', '#F6C0CF'], ['#5E7FDE', '#9FC9FF']
exit_row_img = ctk.CTkImage(light_image=Image.open(relative_to_assets(r'build\assets\frame0\Exit row.png')),
                            dark_image=Image.open(relative_to_assets(r'build\assets\frame0\Exit row.png')),
                            size=(200, 20)) 

for i in range(3*2):
    if i%2 == 0:
        v = ctk.CTkFrame(web,
                           width=185-8, height=250,
                           corner_radius=25,
                           fg_color='white',
                           bg_color='transparent',
                           )
        v.grid(row=i, column=0, padx=4, pady=5)
        eco_buss.append(v)
        print(i, i%2, 'a')
    else:
        v = ctk.CTkLabel(web,
                         image=exit_row_img, text='')
        v.grid(row=i, column=0, padx=0, pady=0, sticky='w')
        print(i,i%2, 'b')

SeatResFunc(1, 6, 4, 4, eco_buss[0], CB, 1.4, 36, eco_rad, [3,8,11], bus_clr)
SeatResFunc(2, 2, 6, 0, eco_buss[1], CB, 1.3, 28, eco_rad, [2,2,10], extr_clr)
web.mainloop()
'''