import tkinter as tk
from editor import Editor
from sidebar import Sidebar
from statusbar import StatusBar

class SpaceVimApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SpaceVim-Tk v0.1")

        # Configure grid layout
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = Sidebar(root)
        self.sidebar.frame.grid(row=0, column=0, sticky="ns")

        # Editor
        self.editor = Editor(root)
        self.editor.text.grid(row=0, column=1, sticky="nsew")

        # Status Bar
        self.statusbar = StatusBar(root)
        self.statusbar.label.grid(row=1, column=0, columnspan=2, sticky="ew")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpaceVimApp(root)
    root.mainloop()