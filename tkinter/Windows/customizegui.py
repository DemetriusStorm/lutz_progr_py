from tkinter import mainloop
from tkinter.messagebox import showerror
from tkinter102 import MyGui


class CustmoGui(MyGui):  # Наследует метод __init__ замещает метод reply
    def reply(self):
        showerror(title='popup', message='OUCH!!! ERROR!!!')


if __name__ == '__main__':
    CustmoGui().pack()
    mainloop()
