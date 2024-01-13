from tkinter import *
import pandas
import random
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_words = pandas.read_csv("data/french_words.csv")
    to_learn = data_words.to_dict(orient="records")
else:
    to_learn = data_words.to_dict(orient="records")



def is_know():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

def next_card():
    global current_card,flip_timer
    windows.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill ="black")
    canvas.itemconfig(card_word, text=french_word, fill ="black")
    canvas.itemconfig(backgrownd_image, image =image_card_front)

    flip_timer = windows.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text = "English", fill ="white" )
    english_word = current_card["English"]
    canvas.itemconfig(card_word, text=english_word, fill ="white" )
    canvas.itemconfig(backgrownd_image, image =image_back_card)




windows = Tk()
windows.title("Flash cards")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = windows.after(3000, func=flip_card)

# -------------images----------------------------
image_right = PhotoImage(file="images/right.png")
image_wrong = PhotoImage(file="images/wrong.png")
image_card_back = PhotoImage(file="images/card_back.png")

# ------------cars-------------------------------
canvas = Canvas(width=800, height=526)
image_card_front = PhotoImage(file="images/card_front.png")
image_back_card = PhotoImage(file="images/card_back.png")

backgrownd_image = canvas.create_image(400, 263, image=image_card_front)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=2)

# ---------------Buttons--------------------------
button_right = Button(image=image_right, highlightthickness=0, command=is_know)
button_right.grid(row=1, column=1)
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=2)

next_card()

windows.mainloop()
