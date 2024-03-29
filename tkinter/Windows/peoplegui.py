"""
Реализация графического интерфейса для просмотра и изменения экземпляров класса,
хранящихся в хранилище;
хранилище находится на том же компьютере, где выполняется сценарий в виде одного
или более локальных файлов;
"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve

shelvename = 'class-people'
fieldname = ('name', 'age', 'job', 'pay')


def make_widgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = dict()

    for key, field_label in enumerate(('key', ) + fieldname):
        label = Label(form, text=field_label)
        ent_entries = Entry(form)
        label.grid(row=key, column=0)
        ent_entries.grid(row=key, column=1)
        entries[field_label] = ent_entries

    Button(window, text='Fetch', command=fetch_record).pack(side=LEFT)
    Button(window, text='Update', command=update_record).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit()).pack(side=RIGHT)

    return window


def fetch_record():
    key = entries['key'].get()
    try:
        record = db[key]  # Execute record by key, print to form
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldname:
           entries[field].delete(0, END)
           entries[field].insert(0, repr(getattr(record, field)))


def update_record():
    key = entries['key'].get()
    if key in db:
        record = db[key]  # changed real record
    else:
        from person import Person  # create/save new record
        record = Person(name='?', age='?')  # eval: string must be in " "

    for field in fieldname:
        setattr(record, field, entries[field].get())
    db[key] = record


db = shelve.open(shelvename)
window = make_widgets()
window.mainloop()
db.close()
