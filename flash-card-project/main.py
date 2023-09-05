from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
LABEL_FONT = ("Arial", 20, "bold")
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# Get the language of choice
# def check_language_choice():
#     lang_choice = language_entry.get().lower()
#     if not os.path.exists(f"data/{lang_choice}_words.csv"):
#         print("Error: This language does not exist in our archives!")



# Read CSV data
try:
    data = pd.read_csv("data/french_words_save.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    words_list_of_dicts = data.to_dict(orient="records")
    print(len(words_list_of_dicts))

# Function that chooses a random French word
def next_card():
    global flip_timer, current_card
    # Cancel previous wait if the next_card() function is triggered
    window.after_cancel(flip_timer)
    current_card = random.choice(words_list_of_dicts)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    # Wait 3 seconds before flipping card
    flip_timer = window.after(3000, flip_card, current_card)

# Function that flips the card to reveal the word in English
def flip_card(words_pair):
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=words_pair["English"], fill="white")

# Remove known word pairs from the word list of dictionaries
def is_known():
    try:
        words_list_of_dicts.remove(current_card)
    # For the first instance, the card will be blank
    except NameError as error_message:
        print(f"{error_message}: Does not exist in list of dictionaries")
    finally:
        next_card()

# Save the progress by editing the csv file. Force exit the window to effect the save.
def save_progress():
    print(len(words_list_of_dicts))
    save_data = pd.DataFrame(words_list_of_dicts)
    save_data.to_csv("data/french_words_save.csv")
    window.destroy()

# Reset the progress by retrieving the original csv file. Force exit the window to effect the reset.
def reset_progress():
    os.remove("data/french_words_save.csv")
    window.destroy()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card, {"French": "", "English": ""})

canvas = Canvas(width=800, height=526)

# Create image on Canvas
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(
    (400, 263),
    image=card_front_img
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=2, column=0, columnspan=4)

# Create text on Canvas
card_title = canvas.create_text(
    (400, 150),
    text="",
    font=LANG_FONT
)
card_word = canvas.create_text(
    (400, 263),
    text="",
    font=WORD_FONT
)

# # Language choice entry
# language_label = Label(text="Choice of Language: ", font=LABEL_FONT, background=BACKGROUND_COLOR)
# language_label.grid(row=0, column=0, sticky="EW")
# language_label.config(padx=2, pady=10)
#
# language_entry = Entry()
# language_entry.grid(row=0, column=1, columnspan=3, sticky="EW")
#
# language_submit = Button(text="Start", highlightbackground=BACKGROUND_COLOR, command=check_language_choice)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=3, column=1)

tick_img = PhotoImage(file="images/right.png")
known_button = Button(image=tick_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=3, column=2)

save_button = Button(text="Save Progress", highlightbackground=BACKGROUND_COLOR, command=save_progress)
save_button.grid(row=1, column=0)
save_button.config(pady=5)

reset_button = Button(text="Reset Progress", highlightbackground=BACKGROUND_COLOR, command=reset_progress)
reset_button.grid(row=1, column=3)
reset_button.config(pady=5)

window.mainloop()