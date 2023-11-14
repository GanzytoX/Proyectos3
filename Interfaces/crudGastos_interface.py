import mysql.connector
from tkinter import *
from Crud.CRUD_gastos import *


cont: int = 0
cnt: int = 0
c: int = 0
def subir_tabla():
    global r
    print("test")


def buscar_0(): # ------------------------------ BUSCAR ------------------------------
    def crear_celda(t: str, x: int, y: int, w: int, c: str, l: int):
        celda = Label(p_b, text=t, font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w)
        #celda.destroy()
        celda.place(x=x, y=y)


    def crear_fila_celda(xf: int, yf: int, id: str, des: str, mon: str, date: str, emp: str, c: str, l: int):
        def crear_celda(t: str, x: int, y: int, w: int, c: str, l: int):
            celda = Label(p_b, text=t, font=('Arial', l), bg=c, fg='black', bd=0, padx=0, pady=3, width=w)
            # celda.destroy()
            celda.place(x=x, y=y)

        crear_celda(id, xf, yf, 7, c, l)
        crear_celda(des, xf + 85, yf, 15, c, l)
        crear_celda(mon, xf + 266, yf, 8, c, l)
        crear_celda(date, xf + 363, yf, 10, c, l)
        crear_celda(emp, xf + 484, yf, 10, c, l)

    def crear_tabla(num: int):
        global r
        crear_fila_celda(100, 80, "Id gasto", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
        for i in range(1, num + 1):
            crear_fila_celda(100, 80 + i*30, r[i-1][0], r[i-1][1], r[i-1][2], r[i-1][3], r[i-1][4], "white", 20)

    def crear_sig_tabla(event):
        global r, cnt, c
        c = 0
        print(len(r))
        if cnt < len(r)/12:
            cnt = cnt + 1
            crear_fila_celda(100, 80, "Id gasto", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
            if (cnt+1)*12 > len(r):
                for i in range(cnt*12, len(r), 1):
                    c = c + 1
                    crear_fila_celda(100, 80 + c * 30, r[i][0], r[i][1], r[i][2], r[i][3], r[i][4], "white", 20)
                for i in range(0, 12-c, 1):
                    c = c + 1
                    crear_fila_celda(100, 80 + c * 30, "", "", "", "", "", "white", 20)

            else: # falta probar
                for i in range(cnt*12, ((cont+1)*12) + 1):
                    crear_fila_celda(100, 80 + i*30, r[i-1+cnt*12][0], r[i-1+cnt*12][1], r[i-1+cnt*12][2], r[i-1+cnt*12][3], r[i-1+cnt*12][4], "white", 20)

    def crear_ant_tabla(event):
        global r, cnt, c
        c = 0
        print(len(r))
        if cnt != 0:
            cnt = cnt - 1
            crear_fila_celda(100, 80, "Id gasto", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
            if (cnt+1)*12 > len(r):
                for i in range(cnt*12, len(r), 1):
                    c = c + 1
                    crear_fila_celda(100, 80 + c * 30, r[i][0], r[i][1], r[i][2], r[i][3], r[i][4], "white", 20)
                for i in range(0, 12-c, 1):
                    c = c + 1
                    crear_fila_celda(100, 80 + c * 30, "", "", "", "", "", "white", 20)

            else: # falta probar
                for i in range(cnt*12, ((cont+1)*12) + 1):
                    print()
                    #crear_fila_celda(100, 80 + i*30, r[i-1+cnt*12][0], r[i-1+cnt*12][1], r[i-1+cnt*12][2], r[i-1+cnt*12][3], r[i-1+cnt*12][4], "white", 20)


    def bajar_tabla(event):
        global r, cont
        if cont != len(r) - 12:
            cont = cont + 1
        if len(r) > 12 and len(r) - 12 >= cont:
            crear_fila_celda(100, 80, "Id gasto", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
            for i in range(1, 12 + 1):
                crear_fila_celda(100, 80 + i * 30, r[i - 1 + cont][0], r[i - 1 + cont][1], r[i - 1 + cont][2], r[i - 1 + cont][3], r[i - 1 + cont][4],"white", 20)

    def subir_tabla(event):
        global r, cont
        if cont != 0:
            cont = cont - 1
        if len(r) > 12 and cont >= 0:
            crear_fila_celda(100, 80, "Id gasto", "Descripción", "Monto", "Fecha", "Empleado", "grey", 20)
            for i in range(1, 12 + 1):
                crear_fila_celda(100, 80 + i * 30, r[i - 1 + cont][0], r[i - 1 + cont][1], r[i - 1 + cont][2], r[i - 1 + cont][3], r[i - 1 + cont][4],"white", 20)




    global vid, vdes, vmon, vfch, vemp, r
    p_b = Toplevel()
    p_b.geometry("800x600")
    p_b.title("Pollos")
    p_b.config(background="light gray")

    t_lb = Label(p_b, text="Resultados", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=10, width=0)
    t_lb.pack()

    if vid == True:
        #global r
        id = b_e0.get()
        r = consulta_gastos_uno_id(conexion, id)
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

    if len(r) < 12:
        crear_tabla(len(r))
    else:
        crear_tabla(12)

    p_b.bind("<Down>", bajar_tabla)
    p_b.bind("<Up>", subir_tabla)
    p_b.mainloop()




def agregar_0(): # ------------------------------ AGREGAR ------------------------------ // comprobar y cerrar ventana
    def agregar_gasto():
        desc = d_ea.get()
        monto = m_ea.get()
        monto = float(monto)
        date = f_ea.get()
        id_emp = e_ea.get()
        id_emp = int(id_emp)

        id = id_max()

        agregar(conexion, id, desc, monto, date, id_emp)

        p_a.destroy()

    p_a = Toplevel()
    p_a.geometry("800x600")
    p_a.title("Pollos")
    p_a.config(background="light gray")

    t_la = Label(p_a, text="Agregar", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=30, width=0)
    d_la = Label(p_a, text="Descripción: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    m_la = Label(p_a, text="Monto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    f_la = Label(p_a, text="Fecha: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    e_la = Label(p_a, text="Id Empleado: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)

    d_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)
    m_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)
    f_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)
    e_ea = Entry(p_a, font=('Arial', 25), bg="white", fg='black', width=25)

    a_ba = Button(p_a, text="Agregar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=agregar_gasto)

    t_la.pack()
    d_la.place(x=100, y=150)
    m_la.place(x=100, y=220)
    f_la.place(x=100, y=290)
    e_la.place(x=100, y=360)

    d_ea.place(x=300, y=150)
    m_ea.place(x=300, y=220)
    f_ea.place(x=300, y=290)
    e_ea.place(x=300, y=360)

    a_ba.place(x=450, y=450)

    p_a.mainloop()


def editar_0(): # ------------------------------ EDITAR ------------------------------ // comprobar y cerrar ventana
    def buscar_id_e():
        id = b_ee.get()

        r = consulta_gastos_uno_id(conexion, id)
        des_e = r[0][1]
        mon_e = r[0][2]
        date_e = r[0][3]
        emp_e = r[0][4]

        d_ee.delete(0, END)
        m_ee.delete(0, END)
        f_ee.delete(0, END)
        e_ee.delete(0, END)

        d_ee.insert(0, des_e)
        m_ee.insert(0, mon_e)
        f_ee.insert(0, date_e)
        e_ee.insert(0, emp_e)

    def actualizar_e():
        desc = d_ee.get()
        monto = m_ee.get()
        monto = float(monto)
        date = f_ee.get()
        id_emp = e_ee.get()
        id_emp = int(id_emp)
        id = b_ee.get()

        actualizar_todo(conexion, desc, monto, date, id_emp, id)

        p_e.destroy()

    p_e = Toplevel()
    p_e.geometry("800x600")
    p_e.title("Pollos")
    p_e.config(background="light gray")

    t_le = Label(p_e, text="Editar", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=30, width=0)

    d_le = Label(p_e, text="Descripción: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0,width=0)
    m_le = Label(p_e, text="Monto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    f_le = Label(p_e, text="Fecha: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    e_le = Label(p_e, text="Id Empleado: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0,width=0)
    i_le = Label(p_e, text="Id Gasto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)

    d_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    m_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    f_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    e_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=25)
    b_ee = Entry(p_e, font=('Arial', 25), bg="white", fg='black', width=10)

    b_be = Button(p_e, text="Buscar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=buscar_id_e)
    a_be = Button(p_e, text="Actualizar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=actualizar_e)

    t_le.pack()
    d_le.place(x=100, y=150)
    m_le.place(x=100, y=220)
    f_le.place(x=100, y=290)
    e_le.place(x=100, y=360)
    i_le.place(x=100, y=430)

    d_ee.place(x=300, y=150)
    m_ee.place(x=300, y=220)
    f_ee.place(x=300, y=290)
    e_ee.place(x=300, y=360)
    b_ee.place(x=300, y=430)

    b_be.place(x=500, y=430)
    a_be.place(x=500, y=500)


def eliminar_0(): # ------------------------------ ELIMINAR ------------------------------ // comprobar y cerrar ventana
    def buscar_id():
        id = b_ed.get()

        r = consulta_gastos_uno_id(conexion, id)
        des_e = r[0][1]
        mon_e = r[0][2]
        date_e = r[0][3]
        emp_e = r[0][4]

        d_ed = Label(p_d,text=des_e , font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")
        m_ed = Label(p_d,text=mon_e , font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")
        f_ed = Label(p_d,text=date_e , font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")
        e_ed = Label(p_d,text=emp_e , font=('Arial', 25), bg="white", fg='black', width=25, anchor="w")

        d_ed.place(x=300, y=150)
        m_ed.place(x=300, y=220)
        f_ed.place(x=300, y=290)
        e_ed.place(x=300, y=360)

    def eliminar_id():
        id = b_ed.get()
        eliminar_uno(conexion, id)

        p_d.destroy()

    p_d = Toplevel()
    p_d.geometry("800x600")
    p_d.title("Pollos")
    p_d.config(background="light gray")

    t_ld = Label(p_d, text="Eliminar", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=30, width=0)

    d_ld = Label(p_d, text="Descripción: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    m_ld = Label(p_d, text="Monto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    f_ld = Label(p_d, text="Fecha: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    e_ld = Label(p_d, text="Id Empleado: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)
    i_ld = Label(p_d, text="Id Gasto: ", font=('Arial', 25), bg='light grey', fg='black', bd=5, padx=0, pady=0, width=0)

    d_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    m_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    f_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    e_ed = Label(p_d, font=('Arial', 25), bg="white", fg='black', width=25)
    b_ed = Entry(p_d, font=('Arial', 25), bg="white", fg='black', width=10)

    b_bd = Button(p_d, text="Buscar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=buscar_id)
    d_bd = Button(p_d, text="Eliminar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=eliminar_id)

    t_ld.pack()
    d_ld.place(x=100, y=150)
    m_ld.place(x=100, y=220)
    f_ld.place(x=100, y=290)
    e_ld.place(x=100, y=360)
    i_ld.place(x=100, y=430)

    d_ed.place(x=300, y=150)
    m_ed.place(x=300, y=220)
    f_ed.place(x=300, y=290)
    e_ed.place(x=300, y=360)
    b_ed.place(x=300, y=430)

    b_bd.place(x=500, y=430)
    d_bd.place(x=500, y=500)


# ------------------------------ MAIN ------------------------------
def update_0():
    global vid, vdes, vmon, vfch, vemp
    if vid == True:
        id_b0 = Button(p, text="Id Gasto", font=('Arial', 10), bg="red", fg="red", activeforeground="red", activebackground="white", width=2, command=id_0)
    else:
        id_b0 = Button(p, text="Id Gasto", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=2, command=id_0)
    if vdes == True:
        des_b0 = Button(p, text="Descripción", font=('Arial', 10), bg="red", fg="red", activeforeground="red", activebackground="white", width=5, command=des_0)
    else:
        des_b0 = Button(p, text="Descripción", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=5, command=des_0)
    if vmon == True:
        mon_b0 = Button(p, text="Monto", font=('Arial', 10), bg="red", fg="red", activeforeground="red", activebackground="white", width=1, command=mon_0)
    else:
        mon_b0 = Button(p, text="Monto", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=1, command=mon_0)
    if vfch == True:
        fch_b0 = Button(p, text="Fecha", font=('Arial', 10), bg="red", fg="red", activeforeground="red", activebackground="white", width=1, command=fch_0)
    else:
        fch_b0 = Button(p, text="Fecha", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=1, command=fch_0)
    if vemp == True:
        emp_b0 = Button(p, text="Empleado", font=('Arial', 10), bg="red", fg="Red", activeforeground="red", activebackground="white", width=4, command=emp_0)
    else:
        emp_b0 = Button(p, text="Empleado", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=4, command=emp_0)

    id_b0.place(x=274, y=290)
    des_b0.place(x=322, y=290)
    mon_b0.place(x=388, y=290)
    fch_b0.place(x=430, y=290)
    emp_b0.place(x=472, y=290)


def id_0():
    b_e0.delete(0, END)
    global vid, vdes, vmon, vfch, vemp
    vid = True
    vdes = False
    vmon = False
    vfch = False
    vemp = False
    update_0()


def des_0():
    b_e0.delete(0, END)
    global vid, vdes, vmon, vfch, vemp
    vid = False
    vdes = True
    vmon = False
    vfch = False
    vemp = False
    update_0()


def mon_0():
    b_e0.delete(0, END)
    global vid, vdes, vmon, vfch, vemp
    vid = False
    vdes = False
    vmon = True
    vfch = False
    vemp = False
    update_0()


def fch_0():
    b_e0.delete(0, END)
    global vid, vdes, vmon, vfch, vemp
    vid = False
    vdes = False
    vmon = False
    vfch = True
    vemp = False
    update_0()


def emp_0():
    b_e0.delete(0, END)
    global vid, vdes, vmon, vfch, vemp
    vid = False
    vdes = False
    vmon = False
    vfch = False
    vemp = True
    update_0()


vid = True
vdes = False
vmon = False
vfch = False
vemp = False

p = Tk()
p.geometry("800x600")
p.title("Pollos")
p.config(background="light gray")

t_l0 = Label(p, text="Gastos", font=('Arial', 40, 'bold'), bg='light grey', fg='black', bd=5, padx=0, pady=30, width=0)
b_e0 = Entry(p, font=('Arial', 25), bg="white", fg="black", width=30)
a_b0 = Button(p, text="Agregar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=agregar_0)
e_b0 = Button(p, text="Editar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=editar_0)
d_b0 = Button(p, text="Eliminar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=eliminar_0)
b_b0 = Button(p, text="Buscar", font=('Arial', 25), bg="red", fg="black", activeforeground="red", activebackground="white", width=8, command=buscar_0)

id_b0 = Button(p, text="Id Gasto", font=('Arial', 10), bg="red", fg="red", activeforeground="red", activebackground="white", width=2, command=id_0)
des_b0 = Button(p, text="Descripción", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=5, command=des_0)
mon_b0 = Button(p, text="Monto", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=1, command=mon_0)
fch_b0 = Button(p, text="Fecha", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=1, command=fch_0)
emp_b0 = Button(p, text="Empleado", font=('Arial', 10), bg="red", fg="black", activeforeground="red", activebackground="white", width=4, command=emp_0)

t_l0.pack()
a_b0.place(x=100, y=400)
e_b0.place(x=325, y=400)
d_b0.place(x=549, y=400)
b_e0.place(x=100, y=250)
b_b0.place(x=549, y=250)

id_b0.place(x=274, y=290)
des_b0.place(x=322, y=290)
mon_b0.place(x=388, y=290)
fch_b0.place(x=430, y=290)
emp_b0.place(x=472, y=290)


#def si(event):
#    print("si")
#p.bind("<Down>", si)
#p.bind("<Down>", subir_tabla())

p.mainloop()

