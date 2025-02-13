import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

root = tk.Tk()

frmDivTitle = tk.Frame(root)
frmDivTitle.pack(side = tk.TOP, fill = tk.BOTH)

frmTitle = tk.Frame(master=frmDivTitle)
frmTitle.pack(side= tk.LEFT, fill = tk.BOTH, expand = 1)

lblTitle = tk.Label(
    master=frmTitle,
    text='текст',
    anchor='center',
    relief=tk.RAISED,
    borderwidth=1,
    height = 2
)
lblTitle.pack(fill=tk.X)

lbl1 = tk.Label(
    master=frmTitle,
    text= 'Название образовательного учреждения',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl1.pack(side = tk.LEFT, fill='both', expand=True)
lbl2 = tk.Label(
    master=frmTitle,
    text= 'Проектирование нейроинтерфейсов',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl2.pack(side = tk.LEFT, fill='both', expand=True)
lbl3 = tk.Label(
    master=frmTitle,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl3.pack(side = tk.LEFT, fill='both', expand=True)

frmTitle1 = tk.Frame(master=frmDivTitle)
frmTitle1.pack(side = tk.LEFT, fill = tk.BOTH)

lblTitle1 = tk.Label(
    master=frmTitle1,
    text='текст',
    anchor='center',
    relief=tk.RAISED,
    borderwidth=1,
    height = 2
)
lblTitle1.pack(fill=tk.X)

lbl4 = tk.Label(
    master=frmTitle1,
    text= 'Введите данные',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=100
)
lbl4.pack(side = tk.LEFT, fill='both', expand=True)

entSName = tk.Entry(master=frmTitle1, width=30)
entSName.pack()
sname = entSName.get()

entLName = tk.Entry(master=frmTitle1)
entLName.pack()
lname = entSName.get()

def add_text():
    text = entSName.get()
    if text:
        label1 = tk.Label(frmTitle1, text=text)
        label1.pack()
        entSName.pack_forget()
        btnSubmit.pack_forget()
        entSName.delete(1.0, tk.START)
        text1 = entLName.get()
    if text1:
        label2 = tk.Label(frmTitle1, text=text1)
        label2.pack()
        entLName.pack_forget()
        entSName.delete(1.0, tk.START)


btnSubmit = tk.Button(master=frmTitle1, text='Ввод', command=add_text)
btnSubmit.pack()

frmDiv = tk.Frame(root)
frmDiv.pack(fill = tk.BOTH, expand = 1)

frmDivContent = tk.Frame(frmDiv)
frmDivContent.pack(side = tk.LEFT,  fill = tk.BOTH, expand = 1)

frmDivGraph = tk.Frame(frmDivContent)
frmDivGraph.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)


frmGraphEKG = tk.Frame(frmDivGraph, pady= 10, padx = 10, relief=tk.RAISED, borderwidth=1)
frmGraphEKG.pack(side = tk.LEFT, fill = tk.BOTH,expand = 1 )


fig1 = Figure(figsize = (2, 2))
fig1.add_subplot(111).plot([3, 4 ,5], [3,4,5])

canvas = FigureCanvasTkAgg(fig1, master = frmGraphEKG)
canvas.draw()
canvas.get_tk_widget().pack(fill = tk.BOTH, expand = 1)


frmGraphEMG = tk.Frame(frmDivGraph, pady= 10, padx = 10, relief=tk.RAISED, borderwidth=1)
frmGraphEMG.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)


fig2 = Figure(figsize = (2, 2))
fig2.add_subplot(111).plot([3, 4 ,5], [3,4,5])

canvas = FigureCanvasTkAgg(fig2, master = frmGraphEMG)
canvas.draw()
canvas.get_tk_widget().pack(fill = tk.BOTH, expand = 1)

frmInfo = tk.Frame(frmDivContent, pady= 10, padx = 10, relief=tk.RAISED, borderwidth=1)
frmInfo.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1)

txtInfo = tk.Text(frmInfo)
txtInfo.insert(tk.END, 'info')
txtInfo.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1)

frmVideo = tk.Frame(frmDiv, pady= 10, padx= 100, relief=tk.RAISED, borderwidth=1)
frmVideo.pack(side = tk.RIGHT, fill = tk.BOTH, expand = 1)

lblVideo = tk.Label(frmVideo, text='Видео', anchor='center')
lblVideo.pack(fill = tk.BOTH, expand = 1)

root.mainloop()