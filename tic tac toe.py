from tkinter import *
import tkinter.messagebox
from typing import Sized

tac = Tk()
tac.title("Tic Tac Toe")
tac.geometry('800x600')

playerA = StringVar()
playerB = StringVar()
p1 =StringVar()
p2 =StringVar()

label1 = Label(tac,text='Enter player A Name').grid(row=1,column=1)
player1name = Entry(tac,textvariable=p1, bd=5).grid(row=1,column=2)
label2 = Label(tac,text='Enter player B Name').grid(row=2,column=1)
player2name = Entry(tac,textvariable=p2, bd=5).grid(row=2,column=2)

bclick = True
turn = 0
button = StringVar()

def btnclick(button):
    global bclick,turn,player1name,player2name,playerA,playerB
    if(button["text"]==" " and bclick ==True):
         button["text"]="x"
         bclick = False
         playerB = p2.get() +" wins!"
         playerA = p1.get() +" wins!"
         turn +=1
         possiblities()
       
        
    elif(button["text"] ==" " and bclick ==False):
        button["text"]="o"
        bclick = True
        turn +=1
        possiblities()

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Buttons already clicked!...")

def possiblities():
    if(button1["text"]=='x' and button2["text"]=='x' and button3["text"]=='x' or 
    button4["text"]=='x' and button5["text"]=='x' and button6["text"]=='x' or
    button7["text"]=='x' and button8["text"]=='x' and button9["text"]=='x' or
    button1["text"]=='x' and button4["text"]=='x' and button7["text"]=='x' or
    button2["text"]=='x' and button5["text"]=='x' and button8["text"]=='x' or
    button3["text"]=='x' and button6["text"]=='x' and button9["text"]=='x' or
    button1["text"]=='x' and button5["text"]=='x' and button9["text"]=='x' or
    button3["text"]=='x' and button5["text"]=='x' and button7["text"]=='x'):
     tkinter.messagebox.showinfo("Tic-Tac-Toe",playerA)
    
    elif turn==8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Match Drawn")

    elif(button1["text"]=='o' and button2["text"]=='o' and button3["text"]=='o' or 
    button4["text"]=='o' and button5["text"]=='o' and button6["text"]=='o' or
    button7["text"]=='o' and button8["text"]=='o' and button9["text"]=='o' or
    button1["text"]=='o' and button4["text"]=='o' and button7["text"]=='o' or
    button2["text"]=='o' and button5["text"]=='o' and button8["text"]=='o' or
    button3["text"]=='o' and button6["text"]=='o' and button9["text"]=='o' or
    button1["text"]=='o' and button5["text"]=='o' and button9["text"]=='o' or
    button3["text"]=='o' and button5["text"]=='o' and button7["text"]=='o'):
     tkinter.messagebox.showinfo("Tic-Tac-Toe",playerB)


button1 = Button(tac,text=" ",font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button1))
button1.grid(row=3,column=3)
button2 = Button(tac,text=' ',font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button2))
button2.grid(row=3,column=4)
button3 = Button(tac,text=' ',font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button3))
button3.grid(row=3,column=5)
button4 = Button(tac,text=' ',font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button4))
button4.grid(row=4,column=3)
button5 = Button(tac,text=' ',font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button5))
button5.grid(row=4,column=4)
button6 = Button(tac,text=' ',font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button6))
button6.grid(row=4,column=5)
button7 = Button(tac,text=' ',font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button7))
button7.grid(row=5,column=3)
button8 = Button(tac,text=' ',font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button8))
button8.grid(row=5,column=4)
button9 = Button(tac,text=' ',font='calibri',bg='gray',fg='white',height=4,width=10,command=lambda:btnclick(button9))
button9.grid(row=5,column=5)

tac.mainloop()