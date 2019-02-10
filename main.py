from tkinter import *
import math

class Input(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Drawer")
        self.isPi = IntVar()
        self.numenator_get = StringVar()
        self.denominator_get = StringVar()
        self.numenator = Entry(self.parent, width=8, textvariable=self.numenator_get)
        self.denominator = Entry(self.parent, width=8, textvariable=self.denominator_get)
        self.label_numerator = Label(self.parent, text="Числитель:")
        self.label_denominator = Label(self.parent, text="Знаменатель:")
        self.isPi_checker = Checkbutton(text="pi?",variable=self.isPi)
        self.calculate_button = Button(text="Начертить", command=self.prepareToDraw)

        self.label_numerator.pack(anchor=NW,padx=10, pady=10)
        self.numenator.pack(anchor=NW,padx=10)
        self.isPi_checker.pack(anchor=NW, padx=10)
        self.label_denominator.pack(anchor=NW,padx=10, pady=5)
        self.denominator.pack(anchor=NW,padx=10)
        self.calculate_button.pack(anchor=SW, padx=10, pady=20)
    def prepareToDraw(self):
        if self.isPi.get() == 1:
            self.result = (float(self.numenator_get.get())*math.pi)/float(self.denominator_get.get())
        else:
            self.result = float(self.numenator_get.get())/float(self.denominator_get.get())
        Drawer(self.parent, self.result)

class Drawer:
    def __init__(self, parent, result):
        self.parent = parent
        self.slave = Toplevel(parent)
        self.slave.title('Draw')
        self.slave.geometry('200x200')
        self.slave.grab_set()
        self.slave.focus_set()
        self.text = Text(self.slave, background='white')
        self.text.pack(side=TOP, fill=BOTH, expand=YES)
        self.text.insert('0.0', result)
        print(result)

def main():
    root = Tk()
    root.geometry("250x250+500+500")
    app = Input(root)
    root.mainloop()

if __name__ == '__main__':
    main()
