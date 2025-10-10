import tkinter as tk

def create_app():
    root = tk.Tk()
    root.geometry("700x600+100+100")
    root.title("GUI Product Shop")
    root.iconbitmap("db\images\icon.ico")
    return root

app = create_app()
