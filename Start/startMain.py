import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk
import jstyleson as json
import tkinter as tk
import playsound

#~ Imports from the required configuration location
#~ Global variable as this is prone to change
__JSON_PATH = r"Json\start.jsonc"
with open(__JSON_PATH, "r") as jsonc_file:
    CONFIG = json.load(jsonc_file)

class StartMain(tk.Frame):
    """Combines all the launcher components into this file
    """
    def __init__(self, master: tk.Widget = None, *args, **kwargs):
        """The main class for the launcher. Inherits from Frame which acts as a
        top level widget, (Can be overridden)

        Args:
            master (tk.Widget, optional): Optional master. If given, it will
                Draw this GUI onto the given master. Defaults to None.
        """
        config = CONFIG["main"]
        tk.Frame.__init__(self, master, *args, **kwargs)
        # Master is in case the top level widget is not itself
        # Makes it fill the xy, and has the frame expand if need be on resize
        self.pack(fill = tk.BOTH, expand = True)

        # Plays a tune on initialising
        playsound.playsound

        # Accesses the master and sets configurations
        self.master.iconbitmap(config["iconbitmap"])    # Icon
        self.master.title(config["title"])              # Title
        self.master.resizable(*config["resizable"])     # Resize Window

if __name__ == "__main__":
    StartMain().mainloop()