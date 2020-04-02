# from numba import jit
# import numpy as np
# import matplotlib.pyplot as plt
# from lupa import LuaRuntime


import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('8-')
        self.master.minsize(300, 200)
        self.pack()

        self.hi_there = tk.Button(self, text="Hello World\n(click me)", command=self.say_hi)
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == '__main__':
    app = App()
    app.mainloop()
