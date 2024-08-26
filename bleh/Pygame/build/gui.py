
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\user data\Desktop\DESKTOP\kama 2024\bleh\Pygame\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1880x1000")
window.configure(bg = "#787880")


canvas = Canvas(
    window,
    bg = "#787880",
    height = 1000,
    width = 1880,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    942.0,
    291.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    590.0,
    534.0,
    image=image_image_2
)

canvas.create_text(
    388.070556640625,
    524.0,
    anchor="nw",
    text="5:00",
    fill="#000000",
    font=("Stylish Regular", 20 * -1)
)

canvas.create_text(
    750.6644287109375,
    516.0,
    anchor="nw",
    text="GOI",
    fill="#000000",
    font=("Stylish Regular", 18 * -1)
)

canvas.create_text(
    431.14111328125,
    517.0,
    anchor="nw",
    text="DXB",
    fill="#000000",
    font=("Stylish Regular", 18 * -1)
)

canvas.create_text(
    541.321533203125,
    533.0,
    anchor="nw",
    text="4 hours /Direct Flight",
    fill="#000000",
    font=("Stylish Regular", 14 * -1)
)

canvas.create_text(
    784.72021484375,
    524.0,
    anchor="nw",
    text="9:00",
    fill="#000000",
    font=("Stylish Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=844.8187255859375,
    y=502.0,
    width=357.5857238769531,
    height=64.0
)

button_image_hover_1 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(
        image=button_image_hover_1
    )
def button_1_leave(e):
    button_1.config(
        image=button_image_1
    )

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1208.414306640625,
    y=502.0,
    width=357.5857238769531,
    height=64.0
)

button_image_hover_2 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_2_hover(e):
    button_2.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    button_2.config(
        image=button_image_2
    )

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)


canvas.create_rectangle(
    344.9979248046875,
    586.98779296875,
    834.5967407226562,
    650.5994453430176,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    387.9627685546875,
    607.98779296875,
    anchor="nw",
    text="5:00",
    fill="#000000",
    font=("Stylish Regular", 20 * -1)
)

canvas.create_rectangle(
    468.8956298828125,
    616.98779296875,
    744.6705017089844,
    617.98779296875,
    fill="#A2A371",
    outline="")

canvas.create_text(
    749.6663818359375,
    599.98779296875,
    anchor="nw",
    text="GOI",
    fill="#000000",
    font=("Stylish Regular", 18 * -1)
)

canvas.create_text(
    430.9276123046875,
    600.98779296875,
    anchor="nw",
    text="DXB",
    fill="#000000",
    font=("Stylish Regular", 18 * -1)
)

canvas.create_text(
    540.8375244140625,
    616.98779296875,
    anchor="nw",
    text="4 hours /Direct Flight",
    fill="#000000",
    font=("Stylish Regular", 14 * -1)
)

canvas.create_text(
    783.6386108398438,
    607.98779296875,
    anchor="nw",
    text="9:00",
    fill="#000000",
    font=("Stylish Regular", 20 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    365.9857177734375,
    637.98779296875,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    381.9718017578125,
    638.98779296875,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    399.95947265625,
    637.98779296875,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    421.94232177734375,
    637.98779296875,
    image=image_image_6
)

canvas.create_rectangle(
    345.0,
    576.4999999999997,
    1560.0,
    576.5,
    fill="#000000",
    outline="")

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=843.5894775390625,
    y=585.98779296875,
    width=356.7077331542969,
    height=64.0
)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_3_hover(e):
    button_3.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    button_3.config(
        image=button_image_3
    )

button_3.bind('<Enter>', button_3_hover)
button_3.bind('<Leave>', button_3_leave)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=1206.2923583984375,
    y=585.98779296875,
    width=356.7077331542969,
    height=64.0
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

def button_4_hover(e):
    button_4.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    button_4.config(
        image=button_image_4
    )

button_4.bind('<Enter>', button_4_hover)
button_4.bind('<Leave>', button_4_leave)


canvas.create_rectangle(
    344.9979248046875,
    759.98779296875,
    834.5967407226562,
    823.5994453430176,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    387.9627685546875,
    780.98779296875,
    anchor="nw",
    text="5:00",
    fill="#000000",
    font=("Stylish Regular", 20 * -1)
)

canvas.create_rectangle(
    468.8956298828125,
    789.98779296875,
    744.6705017089844,
    790.98779296875,
    fill="#A2A371",
    outline="")

canvas.create_text(
    749.6664428710938,
    772.98779296875,
    anchor="nw",
    text="GOI",
    fill="#000000",
    font=("Stylish Regular", 18 * -1)
)

canvas.create_text(
    430.9276123046875,
    773.98779296875,
    anchor="nw",
    text="DXB",
    fill="#000000",
    font=("Stylish Regular", 18 * -1)
)

canvas.create_text(
    540.8375244140625,
    789.98779296875,
    anchor="nw",
    text="4 hours /Direct Flight",
    fill="#000000",
    font=("Stylish Regular", 14 * -1)
)

canvas.create_text(
    783.6385498046875,
    780.98779296875,
    anchor="nw",
    text="9:00",
    fill="#000000",
    font=("Stylish Regular", 20 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    365.9857177734375,
    810.98779296875,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    381.9718017578125,
    811.98779296875,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    399.95947265625,
    810.98779296875,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    421.94232177734375,
    810.98779296875,
    image=image_image_10
)

canvas.create_rectangle(
    341.0,
    749.0,
    1560.160888671875,
    750.0,
    fill="#706969",
    outline="")

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=843.5894775390625,
    y=758.98779296875,
    width=356.7077331542969,
    height=64.0
)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_5.png"))

def button_5_hover(e):
    button_5.config(
        image=button_image_hover_5
    )
def button_5_leave(e):
    button_5.config(
        image=button_image_5
    )

button_5.bind('<Enter>', button_5_hover)
button_5.bind('<Leave>', button_5_leave)


button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1206.292236328125,
    y=758.98779296875,
    width=356.7077331542969,
    height=64.0
)

button_image_hover_6 = PhotoImage(
    file=relative_to_assets("button_hover_6.png"))

def button_6_hover(e):
    button_6.config(
        image=button_image_hover_6
    )
def button_6_leave(e):
    button_6.config(
        image=button_image_6
    )

button_6.bind('<Enter>', button_6_hover)
button_6.bind('<Leave>', button_6_leave)


canvas.create_rectangle(
    344.9979248046875,
    673.98779296875,
    834.5967407226562,
    737.5994453430176,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    387.9627685546875,
    694.98779296875,
    anchor="nw",
    text="5:00",
    fill="#000000",
    font=("Stylish Regular", 20 * -1)
)

canvas.create_rectangle(
    468.8956298828125,
    703.98779296875,
    744.6705017089844,
    704.98779296875,
    fill="#A2A371",
    outline="")

canvas.create_text(
    749.6664428710938,
    686.98779296875,
    anchor="nw",
    text="GOI",
    fill="#000000",
    font=("Stylish Regular", 18 * -1)
)

canvas.create_text(
    430.9276123046875,
    687.98779296875,
    anchor="nw",
    text="DXB",
    fill="#000000",
    font=("Stylish Regular", 18 * -1)
)

canvas.create_text(
    540.8375244140625,
    703.98779296875,
    anchor="nw",
    text="4 hours /Direct Flight",
    fill="#000000",
    font=("Stylish Regular", 14 * -1)
)

canvas.create_text(
    783.6385498046875,
    694.98779296875,
    anchor="nw",
    text="9:00",
    fill="#000000",
    font=("Stylish Regular", 20 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    365.9857177734375,
    724.98779296875,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    381.9718017578125,
    725.98779296875,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    399.95947265625,
    724.98779296875,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    421.94232177734375,
    724.98779296875,
    image=image_image_14
)

canvas.create_rectangle(
    341.0,
    663.0,
    1560.160888671875,
    664.0,
    fill="#706969",
    outline="")

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=843.5894775390625,
    y=672.98779296875,
    width=356.7077331542969,
    height=64.0
)

button_image_hover_7 = PhotoImage(
    file=relative_to_assets("button_hover_7.png"))

def button_7_hover(e):
    button_7.config(
        image=button_image_hover_7
    )
def button_7_leave(e):
    button_7.config(
        image=button_image_7
    )

button_7.bind('<Enter>', button_7_hover)
button_7.bind('<Leave>', button_7_leave)


button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=1206.292236328125,
    y=672.98779296875,
    width=356.7077331542969,
    height=64.0
)

button_image_hover_8 = PhotoImage(
    file=relative_to_assets("button_hover_8.png"))

def button_8_hover(e):
    button_8.config(
        image=button_image_hover_8
    )
def button_8_leave(e):
    button_8.config(
        image=button_image_8
    )

button_8.bind('<Enter>', button_8_hover)
button_8.bind('<Leave>', button_8_leave)

window.resizable(False, False)
window.mainloop()
