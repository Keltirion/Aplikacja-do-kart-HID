from tkinter import *
from tkinter import ttk

class MainWindow:

    def __init__(self, master, text):

        self.label = ttk.Label(master, text = text)
        self.label.grid(row = 0, column = 4, columnspan = 2)
        self.label.config(justify = CENTER)
        ttk.Button(master, text = 'Test').grid(row = 1, column =3)


def main(text):

    root = Tk()
    app = MainWindow(root, text)
    root.mainloop()

if __name__ == '__main__': main()
