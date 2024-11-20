from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/italian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Italian", fill="black")
    canvas.itemconfig(card_word, text=current_card['Italian'], fill="black")
    canvas.itemconfig(img, image=card_image)

    flip_timer = window.after(3000, func=change_image)

def change_image():
    canvas.itemconfig(img, image=back_image)
    canvas.itemconfig(card_title, fill='white', text="English")
    canvas.itemconfig(card_word, fill='white', text=current_card['English'])

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=change_image)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
img = canvas.create_image(400, 263, image=card_image)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)


next_card()


window.mainloop()

