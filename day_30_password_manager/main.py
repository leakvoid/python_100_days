from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
#import pyperclip
import json

#--- Password generator ---#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(2,3))]

    pwd_list = password_letters + password_numbers + password_symbols
    shuffle(pwd_list)

    password_str = "".join(pwd_list)
    password_entry.insert(0, password_str)

    #pyperclip.copy(password_str) # ??????

#--- save password ---#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    my_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Make sure you filled all of the fields")
    else:
        try:
            with open("data.json", "r") as my_file:
                data = json.load(my_file)
        except FileNotFoundError:
            with open("data.json", "w") as my_file:
                json.dump(my_data, my_file, indent=4)
        else:
            data.update(my_data)

            with open("data.json", "w") as my_file:
                json.dump(data, my_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#--- find password ---#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as my_file:
            data = json.load(my_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

#--- UI ---#
window = Tk()
window.title("Password manager")
window.config(padx=70, pady=70)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./ex_30_password_manager/logo.png")
canvas.create_image(90, 90, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
pwd_label = Label(text="Password:")
pwd_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dmitry@example.com")
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# buttons
search_button = Button(text="search", width=12, command=find_password)
search_button.grid(row=1, column=2)
gen_password_button = Button(text="generate password", command=generate_password)
gen_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()