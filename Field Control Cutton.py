from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Label, Style
from tkinter.ttk import Entry
#from tkinter import *
#from tkinter import ttk

#class Frame:
    #frame = Frame(self, relief=RAISED, borderwidth=1)
    #frame.pack(fill=BOTH, expand=1)

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent

        self.initUI()
  
    def initUI(self):
        self.parent.title("Calculator")
        
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
            
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)
        self.columnconfigure(5, pad=3)
        self.rowconfigure(0, pad=3)

        entry1 = Entry(self)
        #entry.grid(row=0, columnspan=4, sticky=W+E)
        entry1.insert(0, "0")

        entry2 = Entry(self)
        entry2.insert(0, "0")

        Team_1_Score = 0
        Team_2_Score = 0


        def Addition_1():
            nonlocal Team_1_Score
            Team_1_Score += 1
            entry1.delete(0, 3)
            entry1.insert(0, Team_1_Score)
            F = open("Team1.txt", "w")
            F.write(str(Team_1_Score))
            F.close()

        def Substraction_1():
            nonlocal Team_1_Score
            Team_1_Score -= 1
            entry1.delete(0, 3)
            entry1.insert(0, Team_1_Score)
            F = open("Team1.txt", "w")
            F.write(str(Team_1_Score))
            F.close()

        def Addition_2():
            nonlocal Team_2_Score
            Team_2_Score += 1
            entry2.delete(0, 3)
            entry2.insert(0, Team_2_Score)
            F = open("Team2.txt", "w")
            F.write(str(Team_2_Score))
            F.close()

        def Substraction_2():
            nonlocal Team_2_Score
            Team_2_Score -= 1
            entry2.delete(0, 3)
            entry2.insert(0, Team_2_Score)
            F = open("Team2.txt", "w")
            F.write(str(Team_2_Score))
            F.close()

        def display_1():
            return Team_1_Score
        def display_2():
            return Team_2_Score


        One_Pls = Button(self, text="+", command = Addition_1)
        One_Pls.grid(row=0, column=0) 
        One_Mns = Button(self, text="-", command = Substraction_1)
        One_Mns.grid(row=0, column=1) 
        #One_Display = Button(self, text="=", command = display_1)
        entry1.grid(row=0, column=2)
        Two_Pls = Button(self, text="+", command = Addition_2)
        Two_Pls.grid(row=0, column=3) 
        Two_Mns = Button(self, text="-", command = Substraction_2)
        Two_Mns.grid(row=0, column=4) 
        #Two_Display = Button(self, text="=", command = display_2)
        entry2.grid(row=0, column=5)

        self.pack()

def main():
  
    root = Tk()
    app = Calculator(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  














