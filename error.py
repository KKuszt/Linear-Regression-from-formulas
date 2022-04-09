from tkinter import *
from tkinter import ttk

def error(message):
    ws = Tk()
    ws.title('Oopss!')
    ws.geometry('220x200')

    def ok():
        ws.destroy()

    ok_button = Button(ws, text="OK", command=(ok), bg="grey", fg="black")
    ok_button.place(x=70, y=130, width=80, height=26)

    #text



    text_box = Text(
        ws,
        height=5,
        width=20
    )
    text_box.pack()
    text_box.insert('end', message)
    text_box.config(state='disabled')
    ws.mainloop()



