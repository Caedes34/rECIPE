


from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, messagebox



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Downloads\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("747x504")
window.configure(bg = "#A46D6D")


canvas = Canvas(
    window,
    bg = "#A46D6D",
    height = 504,
    width = 747,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
     bg="#A46D6D",  # Set to match the canvas background color
    activebackground="#A46D6D",  # Set to match the canvas background color
    bd=0,  # Set border width to 0
    padx=0,  # Remove horizontal padding
    pady=0   # Remove vertical padding
)
button_1.place(
    x=28.0,
    y=81.0,
    width=324.0,
    height=110.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
     bg="#A46D6D",  # Set to match the canvas background color
    activebackground="#A46D6D",  # Set to match the canvas background color
    bd=0,  # Set border width to 0
    padx=0,  # Remove horizontal padding
    pady=0   # Remove vertical padding
)
button_2.place(
    x=28.0,
    y=214.0,
    width=324.0,
    height=110.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
     bg="#A46D6D",  # Set to match the canvas background color
    activebackground="#A46D6D",  # Set to match the canvas background color
    bd=0,  # Set border width to 0
    padx=0,  # Remove horizontal padding
    pady=0   # Remove vertical padding
)
button_3.place(
    x=28.0,
    y=348.0,
    width=324.0,
    height=110.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
     bg="#A46D6D",  # Set to match the canvas background color
    activebackground="#A46D6D",  # Set to match the canvas background color
    bd=0,  # Set border width to 0
    padx=0,  # Remove horizontal padding
    pady=0   # Remove vertical padding
)
button_4.place(
    x=374.0,
    y=348.0,
    width=324.0,
    height=110.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
     bg="#A46D6D",  # Set to match the canvas background color
    activebackground="#A46D6D",  # Set to match the canvas background color
    bd=0,  # Set border width to 0
    padx=0,  # Remove horizontal padding
    pady=0   # Remove vertical padding
)
button_5.place(
    x=374.0,
    y=81.0,
    width=324.0,
    height=110.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
     bg="#A46D6D",  # Set to match the canvas background color
    activebackground="#A46D6D",  # Set to match the canvas background color
    bd=0,  # Set border width to 0
    padx=0,  # Remove horizontal padding
    pady=0   # Remove vertical padding
)
button_6.place(
    x=374.0,
    y=214.0,
    width=324.0,
    height=110.0
)

canvas.create_text(
    395.0,
    30.0,
    anchor="center",
    text="WHATS COOKIN?",
    fill="#CC9318",
    font=("Montserrat Bold", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
