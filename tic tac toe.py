from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.simpledialog import askstring
count=0;
ch=0;
w=False;
buttons = [""] * 9
def checkwiner():
    winpos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
              (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6)]
    for pos in winpos:
        if buttons[pos[0]] == buttons[pos[1]] == buttons[pos[2]] != "":
            button_list[pos[0]].config(bg="green",fg="yellow")
            button_list[pos[1]].config(bg="green",fg="yellow")
            button_list[pos[2]].config(bg="green",fg="yellow")
            return buttons[pos[0]]
    return ""

def change(button):
    global count,w,ch
    if w==True or button_list[button].cget('text')=="X" or button_list[button].cget('text')=="O":
        return
    if(count==0):
        button_list[button].config(text="X",bg="red")
        mee1.config(text="this chance "+play2)
        count=1;
        ch+=1
        buttons[button]="X"
    else:
        button_list[button].config(text="O",bg="darkgoldenrod4")
        mee1.config(text="this chance "+play1)
        count=0;
        ch+=1
        buttons[button]="O"
    win=checkwiner();
    if win=="X":
        w=True;
        mee1.config(text=play1+"  is winner")
        tmsg.showinfo("Winner", play1+" is winner")
        root.destroy()
        #print("x is winner");
    elif win=="O":
        w=True;
        mee1.config(text=play2+"  is winner")
        tmsg.showinfo("Winner", play2+" is winner")
        root.destroy()
        #print("O is winner");
    if ch==9 and not(win=="X" or win=="O"):        #win x condition because when 9chance complete and win in x excute this code so use not oprator
        mee1.config(text=play1+" & "+play2+" are winner")
        tmsg.showinfo("Draw", "Game is draw")
        root.destroy()
        #print("game is draw");
root = Tk()
root.geometry("400x400")
root.title("tic-tac-toe")
root.iconbitmap("icon2.ico")
f1 = Frame(root, bg="darkturquoise")
button_list = []
play1 = askstring('Name', 'Enter Player First Name?')
play1=play1.upper();
play2 = askstring('Name', 'Enter Player Sceond Name?')
play2=play2.upper();
#print(play1,"   ",play2)
mee1 = Label(f1,text=play1+" VS "+play2,bg="darkturquoise",fg="yellow",font="lucida 20 bold")
mee1.pack(padx=18,pady=12)
for i in range(9):
    if i==0 or (i%3==0):
        f1.pack();
        f1 = Frame(root, bg="brown")
    b1 = Button(f1, text=f"{i+1}", font="lucida 25 bold",bg="darkorchid1",command=lambda i=i: change(i)) #i=i use for lambda function it like js callback function it rembeber i
    b1.pack(side=LEFT, padx=18, pady=12)                                                                 #is value because loop not stop i value last index so lambda remember i
    button_list.append(b1)
f1.pack();
f2 = Frame(root, bg="orange")
mee1 = Label(f2,text="this chance "+play1,bg="violetred",fg="yellow",font="lucida 20 bold")
mee1.pack(padx=18,pady=12)
f2.pack();
root.mainloop()
