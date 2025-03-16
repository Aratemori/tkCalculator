from tkinter import *

# Made by Aratemori

def main():
    root = Tk()
    root.title("A Simple Calculator")
    root.resizable(False,False)
    root.geometry("300x450");

    # functional
    global a,b
        # buttons with numbers

    def add_digit(digit):
        ent.insert(END, str(digit))

    def NineAdd():
        ent.insert(END, "9")
    def EightAdd():
        ent.insert(END, "8")
    def SevenAdd():
        ent.insert(END, "7")
    def SixAdd():
        ent.insert(END, "6")
    def FiveAdd():
        ent.insert(END, "5")
    def FourAdd():
        ent.insert(END, "4")
    def ThirdAdd():
        ent.insert(END, "3")
    def SecondAdd():
        ent.insert(END, "2")
    def FirstAdd():
        ent.insert(END, "1")
    def ZeroAdd():
        ent.insert(END,"0")
    def DotAdd():
        ent.insert(END,".")

        # operations
    def Plus():
        global a,b
        a = float(ent.get())
        try:
            c = float(a)
            ent.delete(0,END)
            b = "+"
        except ValueError:
            pass

    def Minus():
        global a,b
        a = float(ent.get())
        try:
            ent.delete(0,END)
            b = "-"
        except ValueError:
            pass

    def Clear():
        ent.delete(0,END)

    def PorM():
        global a
        a = float(ent.get())
        try:
            ent.delete(0,END)
            ent.insert(0,str(-a))
        except ValueError:
            pass
        
    def Percentage():
        global a
        a = float(ent.get())
        try:
            c = float(a) / 100
            ent.delete(0,END)
            ent.insert(END,str(c))
        except ValueError:
            pass
        
    def Divide():
        global a,b
        a = float(ent.get())
        try:
            ent.delete(0,END)
            b = "/"
        except ValueError:
            pass
            
    def Multiple():
        global a,b
        a = float(ent.get())
        try:
            ent.delete(0,END)
            b = "x"
        except ValueError:
            pass

    def Equal():
        global a,b
        c = float(ent.get())
        try:
            ent.delete(0,END)
        except ValueError:
            pass
            
        if b == '+':
            try:
                result = a+c
                ent.insert(END,str(result))
            except ValueError:
                ent.delete(0,END)
                ent.insert(END,"ERROR")
        if b == '-':
            try:
                result=a-c
                ent.insert(END,str(result))
            except ValueError:
                ent.delete(0,END)
                ent.insert(END,"ERROR")
        if b == 'x':
           try:
               result=a*c
               ent.insert(END,str(result))
           except ValueError:
               ent.delete(0,END)
               ent.insert(END,"ERROR")
        if b == '/':
            try:
                result = a/c
                ent.insert(END,str(result))
            except ValueError:
                ent.delete(0,END)
                ent.insert(END,"ERROR")
        if b == '%':
            try:
                result = float(c) / 100;
                ent.insert(END,str(result))
            except ValueError:
                ent.delete(0,END)
                ent.insert(END,"ERROR")
        if b == '+/-':
            try:
                result = float(c);
                ent.insert(END,str(-result))
            except ValueError:
                ent.delete(0,END)
                ent.insert(END,"ERROR")
        
    # visual
    ent = Entry(justify=RIGHT,
                background="black",
                font="Calibri 25",
                foreground="white",
                highlightbackground="black",
                borderwidth=0)
    ent.place(x=20,y=30,width=260,height=70)

    btnC = Button(text="C",
                  justify=CENTER,
                  command=Clear,
                  background="gray",
                  foreground="black",
                  borderwidth=0,
                  font='14')
    btnC.place(x=20,y=140,width=50,height=50)

    btnPorM = Button(text="+/-",
                     justify=CENTER,
                     command=PorM,
                     background="gray",
                     foreground="black",
                     borderwidth=0,
                     font='14')
    btnPorM.place(x=80,y=140,width=50,height=50)

    btnPercent = Button(text="%",
                        justify=CENTER,
                        command=Percentage,
                        background="gray",
                        foreground="black",
                        borderwidth=0,
                        font='14')
    btnPercent.place(x=140,y=140,width=50,height=50)

    btnDivision = Button(text="/",
                         justify=CENTER,
                         command=Divide,
                         background="orange",
                         foreground="white",
                         borderwidth=0,
                         font='14')
    btnDivision.place(x=200,y=140,width=80,height=50)
    
    btnSeven = Button(text="7",
                      justify=CENTER,
                      command=SevenAdd ,
                      background="gray32",
                      foreground="white",
                      borderwidth=0,
                      font='14')
    btnSeven.place(x=20,y=200,width=50,height=50)

    btnEight = Button(text="8",
                      justify=CENTER,
                      command=EightAdd,
                      background="gray32",
                      foreground="white",
                      borderwidth=0,
                      font='14')
    btnEight.place(x=80,y=200,width=50,height=50)

    btnNine = Button(text="9",
                     justify=CENTER,
                     command=NineAdd,
                     background="gray32",
                     foreground="white",
                     borderwidth=0,
                     font='14')
    btnNine.place(x=140,y=200,width=50,height=50)

    btnMultiple = Button(text="x",
                         justify=CENTER,
                         command=Multiple,
                         background="orange",
                         foreground="white",
                         borderwidth=0,
                         font='14')
    btnMultiple.place(x=200,y=200,width=80,height=50)
    
    btnFour = Button(text="4",
                     justify=CENTER,
                     command=FourAdd,
                     background="gray32",
                     foreground="white",
                     borderwidth=0,
                     font='14')
    btnFour.place(x=20,y=260,width=50,height=50)

    btnFive = Button(text="5",
                     justify=CENTER,
                     command=FiveAdd,
                     background="gray32",
                     foreground="white",
                     borderwidth=0,
                     font='14')
    btnFive.place(x=80,y=260,width=50,height=50)

    btnSix = Button(text="6",
                    justify=CENTER,
                    command=SixAdd,
                    background="gray32",
                    foreground="white",
                    borderwidth=0,
                    font='14')
    btnSix.place(x=140,y=260,width=50,height=50)

    btnMinus = Button(text="-",
                     justify=CENTER,
                     command=Minus,
                     background="orange",
                     foreground="white",
                     borderwidth=0,
                     font='14')
    btnMinus.place(x=200,y=260,width=80,height=50)
    
    btnFirst = Button(text="1",
                      justify=CENTER,
                      command=FirstAdd,
                      background="gray32",
                      foreground="white",
                      borderwidth=0,
                      font='14')
    btnFirst.place(x=20,y=320,width=50,height=50)

    btnSecond = Button(text="2",
                       justify=CENTER,
                       command=SecondAdd,
                       background="gray32",
                       foreground="white",
                       borderwidth=0,
                       font='14')
    btnSecond.place(x=80,y=320,width=50,height=50)

    btnThird = Button(text="3",
                      justify=CENTER,
                      command=ThirdAdd,
                      background="gray32",
                      foreground="white",
                      borderwidth=0,
                      font='14')
    btnThird.place(x=140,y=320,width=50,height=50)

    btnPlus = Button(text="+",
                     justify=CENTER,
                     command=Plus,
                     background="orange",
                     foreground="white",
                     borderwidth=0,
                     font='14')
    btnPlus.place(x=200,y=320,width=80,height=50)
    
    btnDot = Button(text=".",
                    justify=CENTER,
                    command=DotAdd,
                    background="gray32",
                    foreground="white",
                    borderwidth=0,
                    font='14')
    btnDot.place(x=140,y=380,width=50,height=50)

    btnEqual = Button(text="=", 
                      justify=CENTER,
                      command=Equal,
                      background="orange",
                      foreground="white",
                      borderwidth=0,
                      font='14')
    btnEqual.place(x=200,y=380,width=80,height=50)

    btnZero = Button(text="0",
                     justify=LEFT,
                     command=ZeroAdd,
                     background="gray32",
                     foreground="white",
                     borderwidth=0,
                     font='14')
    btnZero.place(x=20,y=380,width=110,height=50)

    root.config(background="black")
    root.mainloop()
    
if __name__ == '__main__':
    main()
