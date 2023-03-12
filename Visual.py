from tkinter import *
from tkinter.font import Font
import time

print('\n1 click = zid\n2 click-uri = punct de plecare\n3 click-rui = destinatie\nDestinatia trebuie pusa prima')


dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
savfl = [0 for i in range(1, 1000)]
savfc = [0 for i in range(1, 1000)]
savl = [0 for i in range(1, 1000)]
savc = [0 for i in range(1, 1000)]
nmin = 1000
lt =0
ct = 0
li = 1
ci = 1
a = [[0 for x in range(1, 1000)]for x in range(1, 1000)]
n=0
h=0
btn = [[0 for i in range(1, 1000)]for i in range(1, 1000)]
chck = [[0 for i in range(1, 1000)]for i in range(1, 1000)]

root = Tk()
root.title('Labirint v0.1')
root.geometry("500x450")


#Creare master frame
master_frame=Frame(root)
master_frame.pack()

But_Img1=PhotoImage(file='Images/Img1.png')
But_Img2=PhotoImage(file='Images/Img2.png')
But_Img3=PhotoImage(file='Images/Img3.png')
But_Img4=PhotoImage(file='Images/Img4.png')
But_Img5=PhotoImage(file='Images/Img5.png')

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=1, pady=20)

controls_frame2 = Frame(master_frame)
controls_frame2.grid(row=2, column=1, pady=20)

controls_frame3 = Frame(master_frame)
controls_frame3.grid(row=3, column=1, pady=20)

inputtxt = Text(controls_frame, height=1, width=25, font=Font(size=8), bg="white")
inputtxt.grid(row =0, column =0)

def Buttons(x, y):
    global li, ci, lt, ct
    if chck[x][y]==0:
        btn[x][y].configure(image=But_Img2)
        a[x][y] = 1

    elif chck[x][y]==1:
        btn[x][y].configure(image=But_Img4)
        li=x
        ci=y
        a[x][y]=0

    elif chck[x][y]==2:
        btn[x][y].configure(image=But_Img5)
        lt=x
        ct=y
        a[x][y]=0

    chck[x][y]+=1

def afisare():
    global a, n
    for i in range(1, h+1):
        btn[savl[i]][savc[i]].configure(image=But_Img3)

def cop():
    for i in range(1, h+1):
        savl[i]=savfl[i]
        savc[i]=savfc[i]

def update(x, y, i):
    if i == 1:
        btn[x][y].configure(image=But_Img3)
    else:
        btn[x][y].configure(image=But_Img1)
    root.update()

def backt(l, c, poz, lf, cf):
    global a, dl, dc, n, h, savfl, savfc, nmin
    a[l][c]=poz
    savfl[poz]=l
    savfc[poz]=c

    if l == lf and c == cf:
        if poz < nmin:
            h = poz
            nmin = poz
            cop()
    else:
        for i in range(4):
            if a[l+dl[i]][c+dc[i]]==0 and l+dl[i]>0 and c+dc[i]>0 and l+dl[i]<=n and c+dc[i]<=n:
                update(l, c, 1)
                time.sleep(0.01)
                backt(l+dl[i], c+dc[i], poz+1, lf, cf)
    a[l][c]=0
    update(l, c, 0)

def hub(x, y, z, w, b):
    global chck
    backt(x, y, z, w, b)
    afisare()
    chck = [[0 for i in range(1, 100)] for i in range(1, 100)]

def cit():
    global n, a, btn, li, ci, lt, ct
    INPUT = inputtxt.get("1.0", "end-1c")
    n=INPUT
    try: 
        n = int(n)
    except:
        n=int(n[1])
    if lt<=0:
        lt=n
        ct=n
    a = [[0 for x in range(1, 100)] for x in range(1, 100)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            btn[i][j] = Button(controls_frame2, image=But_Img1, height =20, borderwidth=0, command=lambda x=i, y=j: Buttons(x, y))
            btn[i][j].grid(row=i, column=j)

    Display2 = Button(controls_frame3, height=1, width=7, text="Find Path", command=lambda: hub(li, ci, 1, lt, ct))
    Display2.grid(row=0, column=2)


Display = Button(controls_frame, height=1, width=5, text="Enter", command=lambda: cit())
Display.grid(row =0, column = 2)

root.mainloop()
