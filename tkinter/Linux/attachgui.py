from tkinter import *
from tkinter102 import MyGui

# Main window app
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# Dialog window
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)

MyGui(popup).pack(side=RIGHT)  # Attach widgets
mainwin.mainloop()
