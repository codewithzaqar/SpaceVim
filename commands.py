import tkinter as tk

class Commands:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Command Palette")
        self.window.geometry("400x200")
        self.window.configure(bg="#1e1e2e")
        self.window.withdraw()

        self.entry = tk.Entry(self.window, font=("Courier", 12), bg="#313244", fg="#cdd6f4", insertbackground="#89b4fa")
        self.entry.pack(fill="x", padx=10, pady=10)

    def show(self):
        self.window.deiconify()
        self.window.focus()
        self.entry.focus()