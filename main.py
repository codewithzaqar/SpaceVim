import tkinter as tk
from editor import Editor
from sidebar import Sidebar
from statusbar import StatusBar
from commands import Commands

class SpaceVimApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SpaceVim-Tk v0.1.1")
        self.root.geometry("800x600")

        # Configure grid layout
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = Sidebar(root)
        self.sidebar.frame.grid(row=0, column=0, sticky="ns")

        # Editor
        self.editor = Editor(root, self.update_status)
        self.editor.text.grid(row=0, column=1, sticky="nsew")

        # Status Bar
        self.statusbar = StatusBar(root)
        self.statusbar.label.grid(row=1, column=0, columnspan=2, sticky="ew")

        # Command Pelette
        self.commands = Commands(root)

        # Bind shortcuts
        self.root.bind("<Control-p>", self.show_command_palette)
        self.root.bind("<Control-b>", self.toggle_sidebar)

    def update_status(self, event=None):
        line, col = self.editor.text.index(tk.INSERT).split(".")
        self.statusbar.label.config(text=f"Ln {line}, Col {col}")

    def toggle_sidebar(self, event=None):
        if self.sidebar.frame.winfo_viewable():
            self.sidebar.frame.grid_remove()
        else:
            self.sidebar.frame.grid()

    def show_command_palette(self, event=None):
        self.commands.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpaceVimApp(root)
    root.mainloop()