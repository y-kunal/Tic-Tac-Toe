from tkinter import *

# window and fram configuration
root=Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
mainframe=Frame(root)
Frm1=Frame(mainframe)
Frm2=Frame(mainframe)
Frm3=Frame(mainframe)
str1=""
str2=""

#board buttons 
btn=[0]
ButtonFrame=Frame(root)
r=[0,0,0,0,1,1,1,2,2,2]
c=[0,0,1,2,0,1,2,0,1,2]
play=1
counter = 0

# fonts for widgets
fonts=("Comic Sans MS",20)
btnfont=("Comic Sans MS",20)
titlefont=("Comic Sans MS",30,"bold")
entryfont=("Comic Sans Ms",15)
menufont=("Comic Sans Ms",10)

# heading
label1=Label(root,text="Tic Tac Toe",font=titlefont,bg="lightblue")
label1.pack(anchor=N,side=TOP)
mainframe.pack()

# check all winning condition
def win():

    # check win condition horzontally 
    
    if btn[1].cget('text')==btn[2].cget('text') and btn[2].cget('text')==btn[3].cget('text'): 
        return 1
    elif btn[4].cget('text')==btn[5].cget('text') and btn[5].cget('text')==btn[6].cget('text'):
        return 1
    elif btn[7].cget('text')==btn[8].cget('text') and btn[8].cget('text')==btn[9].cget('text'):
        return 1
    
    # check win condition diagonally
    elif btn[1].cget('text')==btn[5].cget('text') and btn[5].cget('text')==btn[9].cget('text'):
        return 1
    elif btn[3].cget('text')==btn[5].cget('text') and btn[5].cget('text')==btn[7].cget('text'):
        return 1
    # check win condi'text'tion vertically
    elif btn[1].cget('text')==btn[4].cget('text') and btn[4].cget('text')==btn[7].cget('text'):
        return 1
    elif btn[2].cget('text')==btn[5].cget('text') and btn[5].cget('text')==btn[8].cget('text'):
        return 1
    elif btn[3].cget('text')==btn[6].cget('text') and btn[6].cget('text')==btn[9].cget('text'):
        return 1
    else:
        return -1

def btn_click(c):
    global play
    global counter

    mark=""
    if play%2:
        play= 1
    else:
        play=2
    if play==1:
        mark="X"
    else:
        mark="O"

    btn[c].config(text=mark,state="disabled")
    play=play+1
    counter = counter + 1

    winner=win()
    if winner==1:
        play-=1
        win_name=str1 if play==1 else str2
        ButtonFrame.pack_forget()
        print(win_name+" Won")
    elif counter == 9:
        # ButtonFrame.pack_forget()
        print("Pheww draw ")


#board design
def board():

    # btntxt=StringVar()
    # btntxt.set(" ")
    ButtonFrame.pack(pady=50) 
    for i in range(1,10):
        btn.append(Button(ButtonFrame,text=str(i),bg="lightgreen",width=10,height=5,command=lambda count=i :btn_click(count),bd=5,relief=SUNKEN))
        btn[i].grid(row=r[i],column=c[i])


def navbar():
    menuframe=Frame(root)
    menuframe.pack()
    menubar=Menu(menuframe,font=menufont)
    game=Menu(menubar,tearoff=0,font=menufont)
    game.add_command(label="New Board",command=board)
    game.add_command(label="Return")
    game.add_separator()
    game.add_command(label="Exit",command=root.quit)
    menubar.add_cascade(label="Game",menu=game)

    about=Menu(menubar,font=menufont,tearoff=0)
    about.add_command(label="About us")
    menubar.add_cascade(label="About",menu=about)

    contact=Menu(menubar,font=menufont,tearoff=0)
    contact.add_command(label="Contact us")
    menubar.add_cascade(label="Contact",menu=contact)

    help=Menu(menubar,tearoff=0,font=menufont)
    help.add_command(label="Help")
    menubar.add_cascade(label="Help",menu=help)
    root.config(menu=menubar)

    
#play button defination
def playbutton():
    global str1,str2
    mainframe.pack_forget()
    label1.pack_forget()
    navbar()
    gameframe1=Frame()
    gameframe1.pack()

#players name header    
    str1=player1Name.get()
    str2=player2Name.get()

    str=str1+" Vs "+str2
    playerlabel=Label(gameframe1,text=str,font=titlefont,bg="lightblue")
    playerlabel.pack()
    board()

def NewBoard():
    
    ButtonFrame.pack(pady=50) 
    for i in range(1,10):
        btn.append(Button(ButtonFrame,text=str(i),bg="lightgreen",width=10,height=5,command=lambda count=i :btn_click(count),bd=5,relief=SUNKEN))
        btn[i].config(State = "enabled")
        btn[i].grid(row=r[i],column=c[i])

    board()

# For taking player 1 name
lbl1=Label(Frm1,text="Player 1 <<X>> Name :   ",font=fonts,bg="lightblue")
lbl1.pack(anchor=NW,side=LEFT,pady=30)

player1Name=StringVar()
player1=Entry(Frm1,font=entryfont,width=15,textvariable=player1Name,bd=3,selectbackground="green")
player1.pack(anchor=NW,side=LEFT,pady=30)
Frm1.pack(anchor=NW)

# For taking player 2 name
lbl2=Label(Frm2,text="Player 2 <<O>> Name :  ",font=fonts,bg="lightblue")
lbl2.pack(anchor=N,side=LEFT)

player2Name=StringVar()
player2=Entry(Frm2,font=entryfont,textvariable=player2Name,width=15,bd=3,selectbackground="green")
player2.pack(side=LEFT)
Frm2.pack(anchor=NW)

# play and quit button'
playbtn=Button(Frm3,text="Play",font=btnfont,bg="lightgreen",command=playbutton)
playbtn.pack(side=LEFT,pady=70)
exit=Button(Frm3,text="Exit",font=btnfont,bg="red")
exit.pack(pady=70)
Frm3.pack() 

# background color
Frm1.config(bg="lightblue")
Frm2.config(bg="lightblue")
Frm3.config(bg="lightblue")
mainframe.config(bg="lightblue")
root.config(bg="lightblue") 
root.mainloop()