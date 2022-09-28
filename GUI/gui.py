import tkinter as tk

def say_hello():
    print('hello')

def add_label():
    label = tk.Label(win, text='new lable')
    label.pack()

def counter():
    global count
    count+=1
    btn4['text'] = f'Счетчик: {count}'

count = 0

win = tk.Tk()
icon = tk.PhotoImage(file='GUI\icon.png')
win.iconphoto(False, icon)
win.config(bg='yellow')
win.title('My first GUI project')
win.geometry('500x600+800+100')
win.resizable(False, False)
label_1 = tk.Label(win, text='Hello!',
                   bg='red',
                   fg='white',
                   font=('Arial',15,'bold'),
                   #padx=20,
                   #pady=40,
                   width=20,
                   height=10,
                   anchor='n',#прижать к северу
                   relief=tk.RAISED,#объем кнопки
                   bd=3,#размер объема
                   justify=tk.LEFT)#выравнивание
label_1.pack()

btn1=tk.Button(win,text='Hello',
               command=say_hello)

btn2=tk.Button(win,text='Add new label',
               command=add_label)

btn3=tk.Button(win,text='Add new label lambda',
               command=lambda: tk.Label(win, text='new lable lambda').pack()
               )

btn4=tk.Button(win,text=f'Счетчик: {count}',
               command=counter,
               bg='red',
               activebackground='blue',
               state=tk.NORMAL
               )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()


win.mainloop()