import tkinter as tk

win = tk.Tk()
icon = tk.PhotoImage(file='GUI\icon.png')
win.iconphoto(False, icon)
win.config(bg='yellow')
win.title('My first GUI project')
win.geometry('500x600+800+100')
win.resizable(False, False)


btn1=tk.Button(win,text='Hello1')
btn2=tk.Button(win,text='Hello2')
btn3=tk.Button(win,text='Hello3')
btn4=tk.Button(win,text='Hello4')

btn1.grid(row=0,column=0,sticky='w')
btn2.grid(row=0,column=1,sticky='e')
btn3.grid(row=1,column=0,columnspan=2,sticky='we')
btn4.grid(row=0,column=2,rowspan=2,sticky='ns')
win.grid_columnconfigure(0, minsize=70)

for i in range(2,7):
    for j in range(3,5):
        tk.Button(win, text=f"Hello {i} {j}").grid(row=i, column=j)

win.mainloop()