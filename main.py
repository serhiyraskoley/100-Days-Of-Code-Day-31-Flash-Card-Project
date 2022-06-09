from http.client import CannotSendHeader
from tkinter import *
from pandas import *
import json



BACKGROUND_COLOR = "#B1DDC6"
PATH_RIGHT_IMG = "images/right.png"
PATH_WRONG_IMG = "images/wrong.png"
PATH_CARD_FRONT_IMG = "images/card_front.png"
PATH_CARD_BACK_IMG = "images/card_back.png"
FONT = "Arial"
 
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file=PATH_CARD_FRONT_IMG)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"))
canvas.create_text(400, 263, text="word", font=(FONT, 60, "bold"))

cross_image = PhotoImage(file=PATH_WRONG_IMG)
unknow_button = Button(image=cross_image, highlightthickness=0)
unknow_button.grid(row=1, column=0)

check_image = PhotoImage(file=PATH_RIGHT_IMG)
known_button = Button(image=check_image, highlightthickness=0)    
known_button.grid(row=1, column=1)

window.mainloop()