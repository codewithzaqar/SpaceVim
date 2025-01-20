import tkinter as tk
from tkinter import font

class Editor:
    def __init__(self, root):
        self.text = tk.Text(root, wrap="none", undo=True, font=("Courier", 12))
        self.text.insert("1.0", "Welcome to SpaceVim-Tk v0.1\n")
        self.text.configure(bg="#1e1e2e", fg="#cdd6f4", insertbackground="#89b4fa")

        # Scrollbars
        self.scroll_y = tk.Scrollbar(root, command=self.text.yview)
        self.scroll_y.grid(row=0, column=2, sticky="ns")
        self.text.configure(yscrollcommand=self.scroll_y.set)