FONT=("Arial", 20, "normal")

from tkinter import *

def clicked():
    num_miles = float(input.get())
    num_km = int(round(num_miles*1.609, 0))
    km_counter.config(text=str(num_km))

window = Tk()
window.title("Miles to Kilometres Converter")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

input = Entry(width=7, font=FONT)
input.grid(column=1, row=0)
input.insert(END, string="0")

is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

km_counter = Label(text="0", font=FONT)
km_counter.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=clicked, font=FONT, width=5)
calculate_button.grid(column=1, row=2)

miles_label = Label(text="miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="km", font=FONT)
km_label.grid(column=2, row=1)


window.mainloop()