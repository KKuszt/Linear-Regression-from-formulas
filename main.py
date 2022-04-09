import math
import matplotlib.pyplot as plt
import numpy as np
from table import table as data
from error import error
from tkinter import *
from PIL import Image, ImageTk
import sys

class Var:
    list = []
    def __init__(self, _list):
        self.list = _list
    def mean(self):
       return sum(self.list)/len(self.list)
    def delt(self, mode):
        delt = []
        #delt
        if(mode == False):
            for i in range(len(self.list)):
                delt.append(self.list[i]-self.mean())
            return delt
        #delt^2
        else:
            for i in range(len(self.list)):
                delt.append((self.list[i]-self.mean())**2)
            return delt
def _dxdy(x,y):
    for i in range(len(x.list)):
        dxdy.append(x.delt(0)[i]*y.delt(0)[i])
def R(x, y):
    sum_dxdy = sum(dxdy)
    # if sum_dxdy == 0:
    #     return 0
    # else:
    r = (sum_dxdy/math.sqrt(sum(x.delt(1))*sum(y.delt(1))))
    return r

def a(x, y):
    sum_dxdy = sum(dxdy)
    return sum(dxdy)/sum(x.delt(1))

def b(x, y):
    b = y.mean() - a * x.mean()
    return b

def predict(new_x):
    y = a * new_x + b
    return y

def plot():
        t2 = list(x.list)
        t2.append(pred)
        t1 = np.arange(min(t2) - 0.1 * (max(t2) - min(t2)), max(t2) + 0.1 * (max(t2) - min(t2)), (max(t2)-min(t2)) / 10)

        plt.figure(figsize=(8,6))
        plt.title('Linear Regression Model')
        plt.plot(t1, predict(t1), 'r--', label='regression line')
        plt.plot(x.list, y.list, 'bo', label = 'data')
        plt.plot(pred, predict(pred), 'ro', label = 'prediction')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend(loc = 4)

        text ='''
        X Mean: {} [u] 
        Y Mean: {}  [u] 
        R: {}
        R^2: {}
        y = {}X + ({})
        Y({}) = {} [u]
        '''.format(round(x.mean(), 2),
                               round(y.mean(), 2),
                               round(R, 4),
                               round(R ** 2, 4),
                               round(a, 3),
                               round(b, 3),
                               pred,
                               round(predict(pred),3))

        plt.annotate(text, xy=(-0, 0.75), xycoords='axes fraction')
        plt.savefig('result.png')

        def exit():
            root.destroy()
            sys.exit()
        root = Tk()
        canvas = Canvas(root, width=800, height=700)
        root.title('Result')
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open("result.png"),master = root)
        canvas.create_image(0, 0, anchor=NW, image=img)
        Input_button = Button(root, text="Done", command=(exit), bg="purple", fg="white")
        Input_button.place(x=360, y=640, width=80, height=25)
        root.mainloop()




dt = data()
#dt= ([22,29,35],[25,28,54], 3) #test
#dt= ([222,329,435],[225,228,354], 66) #test
x = Var(dt[0])
y = Var(dt[1])
pred = dt[2]

dxdy = []
_dxdy(x,y)
if sum(dxdy) == 0:
    error('''Linear regression   function is not def-ined for this data.
Please try again''')
else:
    R = R(x, y)
    a = a(x, y)
    b = b(x, y)
    plot()





