from tkinter import *
from random import *
from tkinter import messagebox

play = Tk()
canvaswidth = 800
canvasheight = 400
colors = ['red','gray','brown','orange','white']

egg_width = 45
egg_height = 55
egg_score = 10

c = Canvas(play,width=canvaswidth,height=canvasheight,background='light green')
c.pack()

catcher = c.create_rectangle(350,360,450,400,outline="black",fill='blue',width=3)

score = 0
scoretext = c.create_text(10,10,anchor="nw",fill="dark blue",text="score:"+str(score))

lives_remaining = 3
livestext = c.create_text(canvaswidth-10,10,fill="dark blue",anchor="ne",text="lives:"+str(lives_remaining))
eggs=[]

def egg():
    x = randrange(10,740)
    y = 40
    f=choice(colors)
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=f,width=0)
    eggs.append(new_egg)
    play.after(5000,egg)

def move():
    for egg in eggs:
        (eggx,eggy,eggx2,eggy2) = c.coords(egg)
        c.move(egg,0,10)
        if eggy2>canvasheight:
            drop(egg)
    play.after(500,move)

def drop(egg):
    eggs.remove(egg)
    c.delete(egg)
    loselife()
    if lives_remaining == 0:
        messagebox.showinfo("Game over","Final score"+str(score))
        play.destroy()

def loselife():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(livestext,text="lives :"+str(lives_remaining))

def scoreplus():
    global score
    score += 5
    c.itemconfigure(scoretext,text="Score :"+str(score))

def catch():
    (catcherx,catchery,catcherx2,catchery2) = c.coords(catcher)
    for egg in eggs:
        (eggx,eggy,eggx2,eggy2) = c.coords(egg)
        if catcherx<eggx and eggx2<catcherx2 and catchery2-eggy2<40:
            eggs.remove(egg)
            c.delete(egg)
            scoreplus()
    play.after(100,catch)

def left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1>0:
        c.move(catcher,-40,0)

def right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2<canvaswidth:
        c.move(catcher,40,0)

c.bind("<Left>",left)
c.bind("<Right>",right)
c.focus_set()
play.after(1000,egg)
play.after(1000,move)
play.after(1000,catch)

play.mainloop()