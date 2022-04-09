from tkinter import *
from tkinter import ttk
from error import error


def table():
    x = []
    y = []
    global c
    ws = Tk()
    ws.title('Data Table')
    ws.geometry('500x500')

    set = ttk.Treeview(ws)
    set.pack()

    set['columns'] = ('id', 'X', 'Y')
    set.column("#0", width=0, stretch=NO)
    set.column("id", anchor=CENTER, width=80)
    set.column("X", anchor=CENTER, width=80)
    set.column("Y", anchor=CENTER, width=80)

    set.heading("#0", text="", anchor=CENTER)
    set.heading("id", text="ID", anchor=CENTER)
    set.heading("X", text="X", anchor=CENTER)
    set.heading("Y", text="Y", anchor=CENTER)

    global count
    count = 0

    Input_frame = Frame(ws)
    Input_frame.pack()

    X = Label(Input_frame, text="X")
    X.grid(row=0, column=1)

    Y = Label(Input_frame, text="Y")
    Y.grid(row=0, column=2)

    X_entry = Entry(Input_frame)
    X_entry.grid(row=1, column=1)

    Y_entry = Entry(Input_frame)
    Y_entry.grid(row=1, column=2)


    Pred_frame = Frame(ws)
    Pred_frame.place(x=150, y=350)

    pred_entry = Entry(Pred_frame)
    pred_entry.grid(row=1, column=2)
    pred_label = Label(Pred_frame, text="Y(X=?) X := ")
    pred_label.grid(row=1, column=1)

    def input_record():
        global count
        try:
            float(X_entry.get())
            float(Y_entry.get())
        except ValueError:
            error('''The character enter-ed is not a number  or 
entry is missing''')
            return 0
        set.insert(parent='', index='end', iid=count, text='',
                   values=(count+1, float(X_entry.get()), float(Y_entry.get())))
        x.append(float(X_entry.get()))
        y.append(float(Y_entry.get()))
        count += 1

        X_entry.delete(0, END)
        Y_entry.delete(0, END)

    def del_record():
        for selected_item in set.selection():
            set.delete(selected_item)

    def save():
        global c
        c = pred_entry.get()
        if count<2:
            error('The minimum number  of records is 2!')
            return 0
        try:
            c = float(c)
        except ValueError:
            error('The character enter-ed is not a number!')
            return 0
        ws.destroy()



    # button - input
    Input_button = Button(ws, text="Input Record", command=(input_record),bg="green", fg="white")
    Input_button.place(x=140, y=300, width=80, height=25)

    # button - del
    del_button = Button(ws, text="Delete Record", command=(del_record), bg="red", fg="white")
    del_button.place(x=280, y=300, width=80, height=25)

    # button - save
    sv_button = Button(ws, text="Calculate", command=(save), bg="purple", fg="white")
    sv_button.place(x=210, y=400, width=80, height=25)



    ws.mainloop()

    return x, y, c
