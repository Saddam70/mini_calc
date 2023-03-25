from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class Calculator:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.entery_box = Entry(font='verdana 18 bold', fg='gold', width=18, bd=8 ,justify=RIGHT, bg="darkcyan")
        self.entery_box.insert(0,"0")
        self.entery_box.place(x=30, y=10)

        self.btn_clear = Button(width=4, text='Clr', font="ariel 15 bold", activebackground='green', fg='crimson', bd=6, bg="darkgray", command=self.funClear)
        self.btn_clear.place(x=28, y=70)
        master.bind('<Escape>', lambda event: self.funClear())

        self.btn_del = Button(width=4, text='<', font="ariel 15 bold", activebackground='green', fg='crimson', bd=6, bg="darkgray", command=self.funcDelete)
        self.btn_del.place(x=110, y=70)
        master.bind('<BackSpace>', lambda event: self.funcDelete())

        self.btn_cm = Button(width=4, text='Cf', font="ariel 15 bold", activebackground='green', fg='crimson', bd=6, bg="darkgray", command=self.calc_circumference)
        self.btn_cm.place(x=192, y=70)
        master.bind('p', lambda event: self.calc_circumference())

        self.btn_per = Button(width=5, text='%', font="ariel 15 bold", activebackground='green', fg='crimson', bd=6, bg="darkgray",command=self.perOperator)
        self.btn_per.place(x=275, y=70)
        master.bind('%', lambda event : self.perOperator())

        self.btn_1 = Button(width=4, text='1', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro", command=lambda x = 1:self.enterNumber(x))
        self.btn_1.place(x=28, y=130)
        master.bind('1', lambda event : self.enterNumber(1))

        self.btn_2 = Button(width=4, text='2', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 2:self.enterNumber(x))
        self.btn_2.place(x=110, y=130)
        master.bind('2', lambda event : self.enterNumber(2))

        self.btn_3 = Button(width=4, text='3', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 3:self.enterNumber(x))
        self.btn_3.place(x=192, y=130)
        master.bind('3', lambda event : self.enterNumber(3))

        self.btn_4 = Button(width=4, text='4', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 4:self.enterNumber(x))
        self.btn_4.place(x=28, y=190)
        master.bind('4', lambda event : self.enterNumber(4))

        self.btn_5 = Button(width=4, text='5', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 5:self.enterNumber(x))
        self.btn_5.place(x=110, y=190)
        master.bind('5', lambda event : self.enterNumber(5))

        self.btn_6 = Button(width=4, text='6', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 6:self.enterNumber(x))
        self.btn_6.place(x=192, y=190)
        master.bind('6', lambda event : self.enterNumber(6))

        self.btn_7 = Button(width=4, text='7', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 7:self.enterNumber(x))
        self.btn_7.place(x=28, y=250)
        master.bind('7', lambda event : self.enterNumber(7))

        self.btn_8 = Button(width=4, text='8', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 8:self.enterNumber(x))
        self.btn_8.place(x=110, y=250)
        master.bind('8', lambda event : self.enterNumber(8))

        self.btn_9 = Button(width=4, text='9', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 9:self.enterNumber(x))
        self.btn_9.place(x=192, y=250)
        master.bind('9', lambda event : self.enterNumber(9))

        self.btn_dot = Button(width=4, text='.', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = '.':self.enterNumber(x))
        self.btn_dot.place(x=28, y=310)
        master.bind('.', lambda event : self.enterNumber('.'))

        self.btn_zero = Button(width=4, text='0', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro",command=lambda x = 0:self.enterNumber(x))
        self.btn_zero.place(x=110, y=310)
        master.bind('0', lambda event : self.enterNumber(0))

        self.btn_equal = Button(width=4, text='=', font="ariel 15 bold", activebackground='green', fg='darkgreen', bd=6, bg="gainsboro", command=self.funcOperator)
        self.btn_equal.place(x=192, y=310)
        master.bind('<Return>', lambda event : self.funcOperator())
        master.bind('=', lambda event : self.funcOperator())
        master.bind('q', lambda event : self.quit_win())
        
        self.label1=Label(text=None, font=10)
        self.label1.place(x=110, y=370)

        self.status = Label(root, text="History :", relief=SUNKEN, height=2, anchor=W, font='verdana 11 bold')
        self.status.pack(side=BOTTOM, fill=X)

        self.btn_operator = []
        
        for i in range(4):
            self.btn_operator.append(Button(width=5, font="ariel 15 bold", fg='crimson', activebackground="green", bg="darkgray", bd=6, command= lambda x = i:self.enter_operator(x)))
            
            master.bind('+', lambda event : self.enter_operator(0))
            master.bind('-', lambda event : self.enter_operator(1))
            master.bind('*', lambda event : self.enter_operator(2))
            master.bind('/', lambda event : self.enter_operator(3))

        self.btn_operator[0]['text'] = '+'
        self.btn_operator[1]['text'] = '-'
        self.btn_operator[2]['text'] = '*'
        self.btn_operator[3]['text'] = '/'

        for i in range(4):
            self.btn_operator[i].place(x=274, y=130+i*60)

    result = 0
    history=[]
    def funcOperator(self):
        content = self.entery_box.get()
        result = eval(content)
        self.entery_box.delete(0, END)
        self.entery_box.insert(0, result)
        # self.history.append(content)
        # self.history.reverse()

    
    def perOperator(self):
        leng = len(self.entery_box.get())
        self.entery_box.insert(leng, '/100')
        self.funcOperator()
        # self.status.configure(text="History: " + " | ".join(self.history[0:4]), font='verdana 10 bold')
    
    def calc_circumference(self):
        self.entery_box.insert(0, '6.28*')
        self.funcOperator()

    def enterNumber(self, x):
        if self.entery_box.get()=="0":
            if x == ".":
                self.entery_box.insert(1,'.')
            else:
                self.entery_box.delete(0,'end')
                self.entery_box.insert(0, str(x))
        else:
            length = len(self.entery_box.get())
            self.entery_box.insert(length, str(x))

    btn_operator=['+','-','*','/']

    def enter_operator(self, x):
        self.funcOperator()
        if self.entery_box.get() != "0":
            length = len(self.entery_box.get())
            all_text = self.entery_box.get()
            last_char=all_text[-1]
            if last_char in ['+','-','*','/'] or all_text[-2:] == '**':
                pass
            else:
                self.entery_box.insert(length, self.btn_operator[x]["text"]) 

    def funcDelete(self):
        length = len(self.entery_box.get())
        self.entery_box.delete(length-1, 'end')
        if length == 1:
            self.entery_box.insert(0, "0")

    def funClear(self):
        self.entery_box.delete(0, END)
        self.entery_box.insert(0, "0")

    def quit_win(self):
        answer = messagebox.askyesno('Exit', 'Do you want to exit ?')
        if answer:
            root.quit()
        


root = Tk()
root.title("Calculator")
root.configure(bg='whitesmoke')
root.geometry("380x400+850+20")
root.iconbitmap('Calculator.ico')
path = "calc_img.jpg"
image = PhotoImage(Image.open(path))  
root.resizable(False, False)
abc = Calculator(root)
root.mainloop()