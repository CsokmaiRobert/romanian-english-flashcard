from tkinter import *
from pandas import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/romanian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def change_word():
    global current_card
    current_card = choice(to_learn)

    canvas.itemconfig(language, text="Romanian", fill="black")
    canvas.itemconfig(word, text=current_card["Romanian"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)

    window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill="white")
    canvas.itemconfig(canvas_image, image=back_card)

def is_known():
    to_learn.remove(current_card)
    new_data = DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    change_word()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, flip_card)

current_card = choice(to_learn)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(400, 150, text="Romanian", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=f"{current_card['Romanian']}", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


cross = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross, highlightthickness=0, command=change_word)
cross_button.grid(column=0, row=1)
checkmark = PhotoImage(file="images/right.png")
checkmark_button = Button(image=checkmark, highlightthickness=0, command=is_known)
checkmark_button.grid(column=1, row=1)

window.mainloop()
