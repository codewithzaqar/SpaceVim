import tkinter as tk

class Sidebar:
    def __init__(self, root):
        self.frame = tk.Frame(root, bg="#1e1e2e", width=150)

        # Dummy buttons
        buttons = ["Explorer", "Search", "Git", "Settings"]
        for idx, text in enumerate(buttons):
            btn = tk.Button(self.frame, text=text, bg="#313244", fg="#cdd6f4", relief="flat")
            btn.pack(fill="x", pady=5, padx=5)