import mysql.connector
from tkinter import *
from SQL import *

lconti: int = 0
conti: int = 0
cont: int = 0
cnt: int = 0
c: int = 0
def subir_tabla():
    global r
    print("test")


def locx(x: int, x1: int, x2: int, ls: int):
    res = (x / (x1 + 1) * x2) + ls
    return res

def locy(y: int, y1: int, y2: int, ls: int):
    res = (y / (y1 + 1) * y2) - ls
    return res


def buscar_0(): # ------------------------------ BUSCAR ------------------------------
    #def actualizar_t(event):


    def iterM(event):
        global conti, r
        if conti < len(r):
            conti = conti + 1
        #frame.destroy()
        tabla_18("white", 20, 5, 10, 20, 10, 10, 10)
        print(conti)

    def iterm(event):
        global conti
        if conti > 0:
            conti = conti - 1
        #frame.destroy()
        tabla_18("white", 20, 5, 10, 20, 10, 10, 10)

        print(conti)


    def tabla_18(c: str, l: int, w0: int, w1: int, w2: int, w3: int, w4: int, w5: int):
        global conti, lconti
        if (lconti != conti):
            frame.destroy()

        frame = Frame(p_b, bg="light grey", padx=100, width=500, height=200)
        frame.pack()

        Titulo00 = Label(frame, text="Id", font=('Arial', l), bg='grey', fg='black', bd=0, width=w0).grid(column=0, row=0)
        Titulo01 = Label(frame, text="Titulo", font=('Arial', l), bg='grey', fg='black', bd=0, width=w1).grid(column=1, row=0)
        Titulo02 = Label(frame, text="Descripción", font=('Arial', l), bg='grey', fg='black', bd=0, width=w2).grid(column=2, row=0)
        Titulo03 = Label(frame, text="Monto", font=('Arial', l), bg='grey', fg='black', bd=0, width=w3).grid(column=3, row=0)
        Titulo04 = Label(frame, text="Fecha", font=('Arial', l), bg='grey', fg='black', bd=0, width=w4).grid(column=4, row=0)
        Titulo05 = Label(frame, text="Empleado", font=('Arial', l), bg='grey', fg='black', bd=0, width=w5).grid(column=5, row=0)

        celda000 = Label(frame, text=r[0 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=1)
        celda001 = Label(frame, text=r[1 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=2)
        celda002 = Label(frame, text=r[2 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=3)
        celda003 = Label(frame, text=r[3 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=4)
        celda003 = Label(frame, text=r[4 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=5)
        celda004 = Label(frame, text=r[5 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=6)
        celda005 = Label(frame, text=r[6 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=7)
        celda006 = Label(frame, text=r[7 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=8)
        celda007 = Label(frame, text=r[8 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=9)
        celda008 = Label(frame, text=r[9 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=10)
        celda009 = Label(frame, text=r[10 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=11)
        celda010 = Label(frame, text=r[11 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=12)
        celda011 = Label(frame, text=r[12 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=13)
        celda012 = Label(frame, text=r[13 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=14)
        celda013 = Label(frame, text=r[14 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=15)
        celda014 = Label(frame, text=r[15 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=16)
        celda015 = Label(frame, text=r[16 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=17)
        celda016 = Label(frame, text=r[17 + (conti)][0], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w0).grid(column=0, row=18)

        celda100 = Label(frame, text=r[0 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=1)
        celda101 = Label(frame, text=r[1 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=2)
        celda102 = Label(frame, text=r[2 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=3)
        celda103 = Label(frame, text=r[3 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=4)
        celda104 = Label(frame, text=r[4 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=5)
        celda105 = Label(frame, text=r[5 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=6)
        celda106 = Label(frame, text=r[6 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=7)
        celda107 = Label(frame, text=r[7 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=8)
        celda108 = Label(frame, text=r[8 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=9)
        celda109 = Label(frame, text=r[9 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=10)
        celda110 = Label(frame, text=r[10 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=11)
        celda111 = Label(frame, text=r[11 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=12)
        celda112 = Label(frame, text=r[12 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=13)
        celda113 = Label(frame, text=r[13 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=14)
        celda114 = Label(frame, text=r[14 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=15)
        celda115 = Label(frame, text=r[15 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=16)
        celda116 = Label(frame, text=r[16 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=17)
        celda117 = Label(frame, text=r[17 + (conti)][1], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w1).grid(column=1, row=18)


        celda200 = Label(frame, text=r[0 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=1)
        celda201 = Label(frame, text=r[1 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=2)
        celda202 = Label(frame, text=r[2 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=3)
        celda203 = Label(frame, text=r[3 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=4)
        celda204 = Label(frame, text=r[4 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=5)
        celda205 = Label(frame, text=r[5 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=6)
        celda206 = Label(frame, text=r[6 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=7)
        celda207 = Label(frame, text=r[7 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=8)
        celda208 = Label(frame, text=r[8 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=9)
        celda209 = Label(frame, text=r[9 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=10)
        celda210 = Label(frame, text=r[10 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=11)
        celda211 = Label(frame, text=r[11 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=12)
        celda212 = Label(frame, text=r[12 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=13)
        celda213 = Label(frame, text=r[13 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=14)
        celda214 = Label(frame, text=r[14 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=15)
        celda215 = Label(frame, text=r[15 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=16)
        celda216 = Label(frame, text=r[16 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=17)
        celda217 = Label(frame, text=r[17 + (conti)][2], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w2).grid(column=2, row=18)

        celda300 = Label(frame, text=r[0 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=1)
        celda301 = Label(frame, text=r[1 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=2)
        celda302 = Label(frame, text=r[2 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=3)
        celda303 = Label(frame, text=r[3 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=4)
        celda304 = Label(frame, text=r[4 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=5)
        celda305 = Label(frame, text=r[5 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=6)
        celda306 = Label(frame, text=r[6 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=7)
        celda307 = Label(frame, text=r[7 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=8)
        celda308 = Label(frame, text=r[8 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=9)
        celda309 = Label(frame, text=r[9 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=10)
        celda310 = Label(frame, text=r[10 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=11)
        celda311 = Label(frame, text=r[11 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=12)
        celda312 = Label(frame, text=r[12 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=13)
        celda313 = Label(frame, text=r[13 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=14)
        celda314 = Label(frame, text=r[14 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=15)
        celda315 = Label(frame, text=r[15 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=16)
        celda316 = Label(frame, text=r[16 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=17)
        celda317 = Label(frame, text=r[17 + (conti)][3], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w3).grid(column=3, row=18)

        celda400 = Label(frame, text=r[0 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=1)
        celda401 = Label(frame, text=r[1 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=2)
        celda402 = Label(frame, text=r[2 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=3)
        celda403 = Label(frame, text=r[3 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=4)
        celda404 = Label(frame, text=r[4 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=5)
        celda405 = Label(frame, text=r[5 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=6)
        celda406 = Label(frame, text=r[6 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=7)
        celda407 = Label(frame, text=r[7 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=8)
        celda408 = Label(frame, text=r[8 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=9)
        celda409 = Label(frame, text=r[9 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=10)
        celda410 = Label(frame, text=r[10 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=11)
        celda411 = Label(frame, text=r[11 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=12)
        celda412 = Label(frame, text=r[12 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=13)
        celda413 = Label(frame, text=r[13 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=14)
        celda414 = Label(frame, text=r[14 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=15)
        celda415 = Label(frame, text=r[15 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=16)
        celda416 = Label(frame, text=r[16 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=17)
        celda417 = Label(frame, text=r[17 + (conti)][4], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w4).grid(column=4, row=18)

        celda500 = Label(frame, text=r[0 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=1)
        celda501 = Label(frame, text=r[1 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=2)
        celda502 = Label(frame, text=r[2 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=3)
        celda503 = Label(frame, text=r[3 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=4)
        celda504 = Label(frame, text=r[4 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=5)
        celda505 = Label(frame, text=r[5 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=6)
        celda506 = Label(frame, text=r[6 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=7)
        celda507 = Label(frame, text=r[7 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=8)
        celda508 = Label(frame, text=r[8 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=9)
        celda509 = Label(frame, text=r[9 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=10)
        celda510 = Label(frame, text=r[10 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=11)
        celda511 = Label(frame, text=r[11 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=12)
        celda512 = Label(frame, text=r[12 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=13)
        celda513 = Label(frame, text=r[13 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=14)
        celda514 = Label(frame, text=r[14 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=15)
        celda515 = Label(frame, text=r[15 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=16)
        celda516 = Label(frame, text=r[16 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=17)
        celda517 = Label(frame, text=r[17 + (conti)][5], font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w5).grid(column=5, row=18)




    def crear_celda(t: str, x: int, y: int, w: int, c: str, l: int):
        celda = Label(p_b, text=t, font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w)
        celda.place(x=x, y=y)

    def crear_fila_celda(xf: int, yf: int, id: str, tit: str, des: str, mon: str, date: str, emp: str, c: str, l: int):
        def crear_celda(t: str, x: int, y: int, w: int, c: str, l: int):
            celda = Label(p_b, text=t, font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w)
            celda.place(x=x, y=y)

        crear_celda(id, xf, yf, 7, c, l)
        crear_celda(tit, xf + 85, yf, 15, c, l)
        crear_celda(des, xf + 266, yf, 30, c, l) #diferencia (363-266)=97
        crear_celda(mon, xf + 627, yf, 10, c, l) #diferencia (484-363)=121
        crear_celda(date, xf + 748, yf, 10, c, l) #diferencia (605-484)=121
        crear_celda(emp, xf + 869, yf, 10, c, l)



    def crear_tabla(num: int):
        global r
        crear_fila_celda(100, 80, "Id gasto", "Titulo", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
        for i in range(1, num + 1):
            crear_fila_celda(100, 80 + i*30, r[i-1][0], r[i-1][1], r[i-1][2], r[i-1][3], r[i-1][4], r[i-1][5], "white", 20)

    def crear_sig_tabla(event):
        global r, cnt, c
        c = 0
        print(len(r))
        if cnt < len(r)/12:
            cnt = cnt + 1
            crear_fila_celda(100, 80, "Id gasto", "Titulo", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
            if (cnt+1)*18 > len(r):
                for i in range(cnt*18, len(r), 1):
                    c = c + 1
                    crear_fila_celda(100, 80 + c * 30, r[i][0], r[i][1], r[i][2], r[i][3], r[i][4], r[i][5], "white", 20)
                for i in range(0, 18-c, 1):
                    c = c + 1
                    crear_fila_celda(100, 80 + c * 30, "", "", "", "", "", "", "white", 20)

            else: # falta probar
                for i in range(cnt*18, ((cont+1)*12) + 1):
                    crear_fila_celda(100, 80 + i*30, r[i-1+cnt*12][0], r[i-1+cnt*12][1], r[i-1+cnt*12][2], r[i-1+cnt*12][3], r[i-1+cnt*12][4], r[i-1+cnt*12][5], "white", 20)

    def crear_ant_tabla(event):
        global r, cnt, c
        c = 0
        print(len(r))
        if cnt != 0:
            cnt = cnt - 1
            crear_fila_celda(100, 80, "Id gasto", "Titulo", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
            if (cnt+1)*12 > len(r):
                for i in range(cnt*12, len(r), 1):
                    c = c + 1
                    crear_fila_celda(100, 80 + c * 30, r[i][0], r[i][1], r[i][2], r[i][3], r[i][4], r[i][5], "white", 20)
                for i in range(0, 12-c, 1):
                    c = c + 1
                    crear_fila_celda(100, 80 + c * 30, "", "", "", "", "", "","white", 20)

            else: # falta probar
                for i in range(cnt*12, ((cont+1)*12) + 1):
                    print()
                    #crear_fila_celda(100, 80 + i*30, r[i-1+cnt*12][0], r[i-1+cnt*12][1], r[i-1+cnt*12][2], r[i-1+cnt*12][3], r[i-1+cnt*12][4], "white", 20)


    def bajar_tabla(event):
        global r, cont
        if cont != len(r) - 18:
            cont = cont + 1
        if len(r) > 18 and len(r) - 18 >= cont:
            crear_fila_celda(100, 80, "Id gasto", "Titulo", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
            for i in range(1, 18 + 1):
                crear_fila_celda(100, 80 + i * 30, r[i - 1 + cont][0], r[i - 1 + cont][1], r[i - 1 + cont][2], r[i - 1 + cont][3], r[i - 1 + cont][4], r[i - 1 + cont][5],"white", 20)

    def subir_tabla(event):
        global r, cont
        if cont != 0:
            cont = cont - 1
        if len(r) > 18 and cont >= 0:
            crear_fila_celda(100, 80, "Id gasto", "Titulo", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
            for i in range(1, 18 + 1):
                crear_fila_celda(100, 80 + i * 30, r[i - 1 + cont][0], r[i - 1 + cont][1], r[i - 1 + cont][2], r[i - 1 + cont][3], r[i - 1 + cont][4], r[i - 1 + cont][5],"white", 20)




    global vid, vtit, vdes, vmon, vfch, vemp, r
    p_b = Toplevel()
    p_b.geometry("1200x700")
    p_b.title("Pollos")
    p_b.config(background="light gray")

    t_lb = Label(p_b, text="Resultados", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=10, width=0)
    t_lb.pack()

    frame = Frame(p_b, bg="light grey", padx=100, width=500, height=200)
    #frame.pack()

    if vid == True:
        #global r
        id = b_e0.get()
        r = consulta_gastos_uno_id(conexion, id)
    if vtit == True:
        #global r
        id = b_e0.get()
        r = consulta_gastos_uno_tit(conexion, id)
    if vdes == True:
        #global r
        des = b_e0.get()
        r = consulta_gastos_uno_desc(conexion, des)
    if vmon == True:
        #global r
        mon = b_e0.get()
        r = consulta_gastos_uno_monto(conexion, mon)
    if vfch == True:
        #global r
        fch = b_e0.get()
        r = consulta_gastos_uno_date(conexion, fch)
    if vemp == True:
        #global r
        emp = b_e0.get()
        r = consulta_gastos_uno_emp(conexion, emp)

    if len(r) < 18:

        crear_tabla(len(r))
    else:
        #tabla_18("white", 20,5, 10, 20, 10, 10, 10)
        crear_tabla(18)

    p_b.bind("<Down>", bajar_tabla)
    p_b.bind("<Up>", subir_tabla)
    p_b.mainloop()



def agregar_0(): # ------------------------------ AGREGAR ------------------------------ // comprobar y cerrar ventana
    def agregar_gasto():
        tit = t_ea.get()
        desc = d_ea.get()
        monto = m_ea.get()
        monto = float(monto)
        date = f_ea.get()
        id_emp = e_ea.get()
        id_emp = int(id_emp)

        #id = id_max()

        agregar(conexion, tit, desc, monto, date, id_emp)

        p_a.destroy()

    p_a = Toplevel()
    p_a.geometry("800x600")
    p_a.title("Pollos")
    p_a.config(background="light gray")

    T_la = Label(p_a, text="Agregar", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=30, width=0)
    t_la = Label(p_a, text="Titulo: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0,width=0)
    d_la = Label(p_a, text="Descripción: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    m_la = Label(p_a, text="Monto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    f_la = Label(p_a, text="Fecha: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    e_la = Label(p_a, text="Id Empleado: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)

    t_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)
    d_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)
    m_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)
    f_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)
    e_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)

    a_ba = Button(p_a, text="Agregar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=agregar_gasto)

    T_la.pack()
    t_la.place(x=100, y=110)
    d_la.place(x=100, y=180)
    m_la.place(x=100, y=250)
    f_la.place(x=100, y=320)
    e_la.place(x=100, y=390)

    t_ea.place(x=300, y=110)
    d_ea.place(x=300, y=180)
    m_ea.place(x=300, y=250)
    f_ea.place(x=300, y=320)
    e_ea.place(x=300, y=390)

    a_ba.place(x=450, y=480)

    p_a.mainloop()


def editar_0(): # ------------------------------ EDITAR ------------------------------ // comprobar y cerrar ventana
    def buscar_id_e():
        id = b_ee.get()

        r = consulta_gastos_uno_id(conexion, id)
        tit_e = r[0][1]
        des_e = r[0][2]
        mon_e = r[0][3]
        date_e = r[0][4]
        emp_e = r[0][5]

        t_ee.delete(0, END)
        d_ee.delete(0, END)
        m_ee.delete(0, END)
        f_ee.delete(0, END)
        e_ee.delete(0, END)

        t_ee.insert(0, tit_e)
        d_ee.insert(0, des_e)
        m_ee.insert(0, mon_e)
        f_ee.insert(0, date_e)
        e_ee.insert(0, emp_e)

    def actualizar_e():
        tit = t_ee.get()
        desc = d_ee.get()
        monto = m_ee.get()
        monto = float(monto)
        date = f_ee.get()
        id_emp = e_ee.get()
        id_emp = int(id_emp)
        id = b_ee.get()

        actualizar_todo(conexion, tit, desc, monto, date, id_emp, id)

        p_e.destroy()

    p_e = Toplevel()
    p_e.geometry("800x600")
    p_e.title("Pollos")
    p_e.config(background="light gray")

    T_le = Label(p_e, text="Editar", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=30, width=0)

    t_le = Label(p_e, text="Titulo: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    d_le = Label(p_e, text="Descripción: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    m_le = Label(p_e, text="Monto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    f_le = Label(p_e, text="Fecha: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    e_le = Label(p_e, text="Id Empleado: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0,width=0)
    i_le = Label(p_e, text="Id Gasto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)

    t_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    d_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    m_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    f_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    e_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    b_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=10)

    b_be = Button(p_e, text="Buscar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=buscar_id_e)
    a_be = Button(p_e, text="Actualizar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=actualizar_e)

    T_le.pack()
    t_le.place(x=100, y=130)
    d_le.place(x=100, y=190)
    m_le.place(x=100, y=250)
    f_le.place(x=100, y=310)
    e_le.place(x=100, y=370)
    i_le.place(x=100, y=430)

    t_ee.place(x=300, y=130)
    d_ee.place(x=300, y=190)
    m_ee.place(x=300, y=250)
    f_ee.place(x=300, y=310)
    e_ee.place(x=300, y=370)
    b_ee.place(x=300, y=430)

    b_be.place(x=500, y=430)
    a_be.place(x=500, y=500)


def eliminar_0(): # ------------------------------ ELIMINAR ------------------------------ // comprobar y cerrar ventana
    def buscar_id():
        id = b_ed.get()

        r = consulta_gastos_uno_id(conexion, id)
        tit_e = r[0][1]
        des_e = r[0][2]
        mon_e = r[0][3]
        date_e = r[0][4]
        emp_e = r[0][5]

        t_ed = Label(p_d, text=tit_e, font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")
        d_ed = Label(p_d,text=des_e, font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")
        m_ed = Label(p_d,text=mon_e, font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")
        f_ed = Label(p_d,text=date_e, font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")
        e_ed = Label(p_d,text=emp_e, font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")

        t_ed.place(x=300, y=130)
        d_ed.place(x=300, y=190)
        m_ed.place(x=300, y=250)
        f_ed.place(x=300, y=310)
        e_ed.place(x=300, y=370)

    def eliminar_id():
        id = b_ed.get()
        eliminar_uno(conexion, id)

        p_d.destroy()

    p_d = Toplevel()
    p_d.geometry("800x600")
    p_d.title("Pollos")
    p_d.config(background="light gray")

    T_ld = Label(p_d, text="Eliminar", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=30, width=0)

    t_ld = Label(p_d, text="Titulo: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    d_ld = Label(p_d, text="Descripción: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    m_ld = Label(p_d, text="Monto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    f_ld = Label(p_d, text="Fecha: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    e_ld = Label(p_d, text="Id Empleado: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    i_ld = Label(p_d, text="Id Gasto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)

    t_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    d_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    m_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    f_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    e_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    b_ed = Entry(p_d, font=('Arial', 25), bg="white", fg='black', width=10)

    b_bd = Button(p_d, text="Buscar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=buscar_id)
    d_bd = Button(p_d, text="Eliminar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=eliminar_id)

    T_ld.pack()
    t_ld.place(x=100, y=130)
    d_ld.place(x=100, y=190)
    m_ld.place(x=100, y=250)
    f_ld.place(x=100, y=310)
    e_ld.place(x=100, y=370)
    i_ld.place(x=100, y=430)

    t_ed.place(x=300, y=130)
    d_ed.place(x=300, y=190)
    m_ed.place(x=300, y=250)
    f_ed.place(x=300, y=310)
    e_ed.place(x=300, y=370)
    b_ed.place(x=300, y=430)

    b_bd.place(x=500, y=430)
    d_bd.place(x=500, y=500)


# ------------------------------ MAIN ------------------------------
def update_0():
    global vid, vdes, vmon, vfch, vemp
    if vid == True:
        id_b0 = Button(p, text="Id Gasto", font=('Arial', 15), bg="red", fg="red", activeforeground="red", activebackground="white", width=4, command=id_0)
    else:
        id_b0 = Button(p, text="Id Gasto", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=4, command=id_0)
    if vtit == True:
        tit_b0 = Button(p, text="Titulo", font=('Arial', 15), bg="red", fg="red", activeforeground="red", activebackground="white", width=4, command=tit_0)
    else:
        tit_b0 = Button(p, text="Titulo", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=4, command=tit_0)
    if vdes == True:
        des_b0 = Button(p, text="Descripción", font=('Arial', 15), bg="red", fg="red", activeforeground="red", activebackground="white", width=6, command=des_0)
    else:
        des_b0 = Button(p, text="Descripción", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=6, command=des_0)
    if vmon == True:
        mon_b0 = Button(p, text="Monto", font=('Arial', 15), bg="red", fg="red", activeforeground="red", activebackground="white", width=2, command=mon_0)
    else:
        mon_b0 = Button(p, text="Monto", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=2, command=mon_0)
    if vfch == True:
        fch_b0 = Button(p, text="Fecha", font=('Arial', 15), bg="red", fg="red", activeforeground="red", activebackground="white", width=2, command=fch_0)
    else:
        fch_b0 = Button(p, text="Fecha", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=2, command=fch_0)
    if vemp == True:
        emp_b0 = Button(p, text="Empleado", font=('Arial', 15), bg="red", fg="Red", activeforeground="red", activebackground="white", width=5, command=emp_0)
    else:
        emp_b0 = Button(p, text="Empleado", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=5, command=emp_0)

    id_b0.place(x=locx(1200, 30, 10, 12), y=locy(700, 3, 2, -40))
    tit_b0.place(x=locx(1200, 30, 12, 6), y=locy(700, 3, 2, -40))
    des_b0.place(x=locx(1200, 30, 14, 1), y=locy(700, 3, 2, -40))
    mon_b0.place(x=locx(1200, 30, 16, 14), y=locy(700, 3, 2, -40))
    fch_b0.place(x=locx(1200, 30, 17, 29), y=locy(700, 3, 2, -40))
    emp_b0.place(x=locx(1200, 30, 19, 6), y=locy(700, 3, 2, -40))


def id_0():
    b_e0.delete(0, END)
    global vid, vtit, vdes, vmon, vfch, vemp
    vid = True
    vtit = False
    vdes = False
    vmon = False
    vfch = False
    vemp = False
    update_0()

def tit_0():
    b_e0.delete(0, END)
    global vid, vtit, vdes, vmon, vfch, vemp
    vid = False
    vtit = True
    vdes = False
    vmon = False
    vfch = False
    vemp = False
    update_0()


def des_0():
    b_e0.delete(0, END)
    global vid, vtit, vdes, vmon, vfch, vemp
    vid = False
    vtit = False
    vdes = True
    vmon = False
    vfch = False
    vemp = False
    update_0()


def mon_0():
    b_e0.delete(0, END)
    global vid, vtit, vdes, vmon, vfch, vemp
    vid = False
    vtit = False
    vdes = False
    vmon = True
    vfch = False
    vemp = False
    update_0()


def fch_0():
    b_e0.delete(0, END)
    global vid, vtit, vdes, vmon, vfch, vemp
    vid = False
    vtit = False
    vdes = False
    vmon = False
    vfch = True
    vemp = False
    update_0()


def emp_0():
    b_e0.delete(0, END)
    global vid, vtit, vdes, vmon, vfch, vemp
    vid = False
    vtit = False
    vdes = False
    vmon = False
    vfch = False
    vemp = True
    update_0()


vid = True
vtit = False
vdes = False
vmon = False
vfch = False
vemp = False

p = Tk()
p.geometry("1200x700")
p.title("Pollos")
p.config(background="light gray")

T_l0 = Label(p, text="Gastos", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=30, width=0)
b_e0 = Entry(p, font=('Arial', 25), bg="white", fg="black", width=40)
a_b0 = Button(p, text="Agregar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=agregar_0)
e_b0 = Button(p, text="Editar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=editar_0)
d_b0 = Button(p, text="Eliminar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=eliminar_0)
b_b0 = Button(p, text="Buscar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=buscar_0)

id_b0 = Button(p, text="Id Gasto", font=('Arial', 15), bg="red", fg="red", activeforeground="red", activebackground="white", width=4, command=id_0)
tit_b0 = Button(p, text="Titulo", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=4, command=tit_0)
des_b0 = Button(p, text="Descripción", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=6, command=des_0)
mon_b0 = Button(p, text="Monto", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=2, command=mon_0)
fch_b0 = Button(p, text="Fecha", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=2, command=fch_0)
emp_b0 = Button(p, text="Empleado", font=('Arial', 15), bg="red", fg="black", activeforeground="red", activebackground="white", width=5, command=emp_0)

T_l0.pack()
a_b0.place(x=locx(1200, 3, 1, -50), y=locy(700, 3, 3, 0))
e_b0.place(x=locx(1200, 3, 2, -50), y=locy(700, 3, 3, 0))
d_b0.place(x=locx(1200, 3, 3, -50), y=locy(700, 3, 3, 0))
b_e0.place(x=locx(1200, 3, 1, -50), y=locy(700, 3, 2, 0))
b_b0.place(x=locx(1200, 3, 3, -50), y=locy(700, 3, 2, 0))

id_b0.place(x=locx(1200, 30, 10, 12), y=locy(700, 3, 2, -40))
tit_b0.place(x=locx(1200, 30, 12, 6), y=locy(700, 3, 2, -40))
des_b0.place(x=locx(1200, 30, 14, 1), y=locy(700, 3, 2, -40))
mon_b0.place(x=locx(1200, 30, 16, 14), y=locy(700, 3, 2, -40))
fch_b0.place(x=locx(1200, 30, 17, 29), y=locy(700, 3, 2, -40))
emp_b0.place(x=locx(1200, 30, 19, 6), y=locy(700, 3, 2, -40))


#def si(event):
#    print("si")
#p.bind("<Down>", si)
#p.bind("<Down>", subir_tabla())

p.mainloop()

