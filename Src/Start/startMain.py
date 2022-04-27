import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk
import tkinter as tk

class StartMain(tk.Frame):
    """The main class for the launcher. Inherits from Frame which acts as a
    top level widget, but this also allows the widgets to be drawn on another
    master (Other top level)
    """
    def __init__(self, master: tk.Widget = None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        # Master is in case the top level widget is not itself
        self.pack(fill = tk.BOTH, expand = True)
        

if __name__ == "__main__":
    StartMain().mainloop()