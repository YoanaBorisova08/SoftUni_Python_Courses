import tkinter as tk

from canvas import app
from helpers import clean_screen
from products import render_products_screen

def login(username, password):
    with open("db\\user_credentials.txt") as file:
        data = file.readlines()
        for line in data:
            name, pwd = line.strip().split(", ")
            if name == username and pwd == password:
                with open("db\\current_user.txt", 'w') as f:
                    f.write(name)
                render_products_screen()
                return
    render_login_screen(error="Invalid username or password")



def render_login_screen(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)

    tk.Button(app,
              text="Enter",
              bg="green",
              fg="black",
              command=lambda: login(username.get(), password.get())).grid(row=2, column=0)

    if error:
        tk.Label(app, text=error).grid(row=3, column=0)

def render_main_enter_screen():
    tk.Button(app,
              text="Login",
              bg="green",
              fg="white",
              command=render_login_screen
    ).grid(row=0, column=0)
    tk.Button(app,
              text="Register",
              bg="yellow",
              fg="black"
    ).grid(row=0, column=1)

