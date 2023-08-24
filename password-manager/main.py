FONT = ("Arial", 14, "normal")

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} "
                                       f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data into Python dictionary
                    data = json.load(data_file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    # Writing new data into a new JSON data file
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Writing updated data into JSON data file
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, "end")
                email_username_entry.delete(0, "end")
                password_entry.delete(0, "end")
                website_entry.focus()
                email_username_entry.insert(0, "angdamian.136a@gmail.com")

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        error_message = "No Data File Found"
        messagebox.showinfo(title="Error", message=error_message)
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            error_message = f"No details for {website} exist."
            messagebox.showinfo(title="Error", message=error_message)
    finally:
        website_entry.delete(0, "end")
        website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

password_search_button = Button(text="Search", command=search_password)
password_search_button.grid(row=1, column=2, sticky="EW")

email_username_label = Label(text="Email/Username:", font=FONT)
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_username_entry.insert(0, "angdamian.136a@gmail.com")

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=save, width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()