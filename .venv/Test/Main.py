import tkinter as tk

root = tk.Tk()
root.title('окно')
root.minsize(600, 500)


# Верхний фрейм с заголовком
frmTitle = tk.Frame(master=root, relief=tk.RAISED, borderwidth=1)
frmTitle.pack(fill='x')

lblTitle = tk.Label(
    master=frmTitle,
    text='текст',
    anchor='center',
    height = 2
)
lblTitle.pack(fill=tk.X, expand=True)

frmText = tk.Frame(master= root)
frmText.pack(fill=tk.BOTH, expand=True)

lbl1 = tk.Label(
    master=frmText,
    text= 'Название образовательного учреждения',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl1.pack(side = tk.LEFT, fill='both', expand=True)
lbl2 = tk.Label(
    master=frmText,
    text= 'Проектирование нейроинтерфейсов',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl2.pack(side = tk.LEFT, fill='both', expand=True)
lbl3 = tk.Label(
    master=frmText,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl3.pack(side = tk.LEFT, fill='both', expand=True)

frmTitle2 = tk.Frame(master=root, relief=tk.RAISED, borderwidth=1)
frmTitle2.pack(fill='x')

lblTitle2 = tk.Label(
    master=frmTitle2,
    text='текст',
    anchor='center',
    height = 2
)
lblTitle2.pack(fill=tk.X, expand=True)

frmConn = tk.Frame(master= root)
frmConn.pack(fill=tk.BOTH, expand=True)

lblConn = tk.Label(
    master=frmConn,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200)
lblConn.pack(side=tk.LEFT, fill='both', expand=True)

lblGraph = tk.Label(
    master=frmConn,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200)
lblGraph.pack(side=tk.LEFT, fill='both', expand=True)

frmConn1 = tk.Frame(master= root)
frmConn1.pack(fill=tk.BOTH, expand=True)

lblConn1 = tk.Label(
    master=frmConn1,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200)
lblConn1.pack(side=tk.LEFT, fill='both', expand=True)
lblGraph1 = tk.Label(
    master=frmConn1,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200)
lblGraph1.pack(side=tk.LEFT, fill='both', expand=True)

root.mainloop()