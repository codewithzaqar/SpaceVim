import tkinter as tk

class Commands:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Command Palette")
        self.window.geometry("400x200")
        self.entry = tk.Entry(self.window, font=("Courier", 12))
        self.entry.pack(fill="x", padx=10, pady=10)
        self.window.withdraw()

    def show(self):
        self.window.deiconify()
        self.entry.focus()