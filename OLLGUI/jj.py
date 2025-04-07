import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')
c = tk.Label(root, text='CCC', background='#fc0')
d = tk.Label(root, text='DDD', background='#0c9')
e = tk.Label(root, text='EEE', background='#ccc')

a.grid(column=0, row=0, sticky=tk.W+tk.S)
b.grid(column=1, row=0, ipady=20)
c.grid(column=0, row=1, sticky=tk.E+tk.N)
d.grid(column=1, row=1, ipady=20)
e.grid(column=0, row=2, padx=20)

root.mainloop()