"""
author  :   deus
app name:   lolapm
date    :   7/16/2022
purpose :   lightweight apm monitor overlay for league of legends

todo    : 
            add apm monitor (either inject into desktop apm process OR use pynput)
            get game resolution to approprietly position the overlay so that it's not in the way
            add post game statistics ? 
            add documentation
"""

import tkinter as tk

class App():

    def quit_program(self, e):
        self.root.destroy()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x100")
        self.root.attributes('-alpha', 0.5)
        self.root.bind('<Control-x>', self.quit_program)
        self.root.overrideredirect(True)
        self.root.mainloop()



a = App()