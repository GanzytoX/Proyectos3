import tkinter as tk
from tkinter import Tk, ttk

from tkinter import messagebox
import mysql.connector
from Crud.CRUD_Usuario import CrudEmpleado, Empleado
from Crud.CRUD_Rol import *
from Utilities.ListFrames import NoImageFrame
from Utilities.twoSideWindow import twoSideWindow


class CUInterface(twoSideWindow):
    def __init__(self):
        super().__init__(window_name="Empleados", size="1200x700", resizable=False,
                         background_image="../img/Empleado.png")
        self.__conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )

        self.__userManager = CrudEmpleado(self.__conection)
        self.__rolManager = CrudRol(self.__conection)
        self.protocol("WM_DELETE_WINDOW", self.__cerrar_ventana)

        # para ver si la interfaz ya ha sido activada
        self.__singleActivated = False

        # Boton para agregar empleado
        self.get_agregar_elemento_button().configure(text="Agregar empleado", background="#2ED741", command=self.__configureAgregarEmpleado)

        #Agregar todos los empleados posibles:
        self.__updateEmpleados()

        # Configura la grid para poder poner datos de un empleado
        self.__marginUnEmpleado = tk.Frame(self)
        self.__marginUnEmpleado.grid(column=1, row=0, padx=(30, 50), pady=50, ipadx=30, ipady=20, sticky="ewns")
        self.__marginUnEmpleado.columnconfigure(0, weight=3)
        self.__marginUnEmpleado.columnconfigure(1, weight=3)
        self.__marginUnEmpleado.columnconfigure(2, weight=3)

        # Declara todos los widgets para ir poniendo los datos o verlos de empleados en específico
        self.__isAdmin = tk.IntVar()
        self.__labelName = tk.Label(self.__marginUnEmpleado, text="Nombre: ")
        self.__inputName = tk.Entry(self.__marginUnEmpleado)
        self.__labelLastname1 = tk.Label(self.__marginUnEmpleado, text="Apellido Paterno: ")
        self.__inputLastname1 = tk.Entry(self.__marginUnEmpleado)
        self.__labelLastname2 = tk.Label(self.__marginUnEmpleado, text="Apellido Materno: ")
        self.__inputLastname2 = tk.Entry(self.__marginUnEmpleado)
        self.__labelCel = tk.Label(self.__marginUnEmpleado, text="Celular: ")
        self.__inputCel = tk.Entry(self.__marginUnEmpleado)
        self.__labelSueldo = tk.Label(self.__marginUnEmpleado, text="Sueldo: ")
        self.__inputSueldo = tk.Entry(self.__marginUnEmpleado)
        self.__labelRol = tk.Label(self.__marginUnEmpleado, text="Rol: ")
        self.__inputRol = ttk.Combobox(self.__marginUnEmpleado)
        self.__inputRol['state'] = 'readonly'
        self.__labelContraseña = tk.Label(self.__marginUnEmpleado, text="Contraseña: ")
        self.__inputContraseña = tk.Entry(self.__marginUnEmpleado)
        self.__radioAdmin = tk.Checkbutton(self.__marginUnEmpleado, text="Admin", variable=self.__isAdmin, onvalue=1,
                                           offvalue=0)

        # Boton para agregar empleado
        self.__agregarEmpleadoButton = tk.Button(self.__marginUnEmpleado, text="Agregar Empleado",
                                          command=self.__agregarEmpleado)

        # Es el boton para poder mandar a editar un empleado
        self.__editEmpleadoButton = tk.Button(self.__marginUnEmpleado, text="Editar empleado", command=self.__editEmpleado)

        # Boton para poder mandar a eliminar un empleado
        self.__deleteEmpleadoButton = tk.Button(self.__marginUnEmpleado, text="Eliminar empleado",
                                              command=self.__deleteEmpleado)

        self.__roles = []
        self.__empleadoActivo = None

        # Configurar busqueda
        self.get_boton_buscar().config(command=self.__search)


    # Esta funcion se manda a llamar cuando clickean algo de la lista y pone los datos del empleado
    def __showEmpleado(self, empleado):
        self.__agregarEmpleadoButton.grid_forget()
        self.__displayMenu()
        self.__inputName.insert(0, empleado.getNombre())
        self.__inputLastname1.insert(0, empleado.getApellido_paterno())
        self.__inputLastname2.insert(0, empleado.getApellido_paterno())
        self.__inputCel.insert(0, empleado.getCelular())
        self.__inputSueldo.insert(0, empleado.getSueldo())
        roles = self.__updateRoles()
        self.__inputRol.set(roles[roles.index(empleado.getIdRol())])
        if empleado.getContraseña() is not None:
            self.__inputContraseña.insert(0, empleado.getContraseña())
        self.__isAdmin.set(empleado.getAdministrador())
        self.__radioAdmin.update()
        self.__empleadoActivo = empleado
        self.__editEmpleadoButton.grid(column=0, row=10, pady=20, sticky="w")
        self.__deleteEmpleadoButton.grid(column=1, row=10, pady=20, sticky="w")


    def __displayMenu(self):
        # Si no se ha activado el panel que muestra un solo empleado, entonces lo despliega
        if not self.__singleActivated:
            self.__labelName.grid(column=0, row=0)
            self.__inputName.grid(column=0, row=1)
            self.__labelLastname1.grid(column=1, row=0)
            self.__inputLastname1.grid(column=1, row=1)
            self.__labelLastname2.grid(column=3, row=0)
            self.__inputLastname2.grid(column=3, row=1)
            self.__labelCel.grid(column=0, row=2)
            self.__inputCel.grid(column=0, row=3, columnspan=4, sticky="ew")
            self.__labelSueldo.grid(column=0, row=4)
            self.__inputSueldo.grid(column=0, row=5, columnspan=4, sticky="ew")
            self.__labelRol.grid(column=0, row=6)
            self.__inputRol.grid(column=0, row=7, columnspan=4, sticky="ew")
            self.__labelContraseña.grid(column=0, row=8)
            self.__inputContraseña.grid(column=0, row=9, columnspan=2, sticky="ew")
            self.__radioAdmin.grid(column=3, row=9, columnspan=4, sticky="ew")
        else:
            self.__inputName.delete(0, tk.END)
            self.__inputLastname1.delete(0, tk.END)
            self.__inputLastname2.delete(0, tk.END)
            self.__inputCel.delete(0, tk.END)
            self.__inputSueldo.delete(0, tk.END)
            self.__inputContraseña.delete(0, tk.END)
            self.__isAdmin.set(0)
        roles = self.__updateRoles()
        self.__inputRol["values"] = roles
        self.__inputRol.update()
        self.__singleActivated = True
    def __configureAgregarEmpleado(self):
        self.__displayMenu()
        self.__editEmpleadoButton.grid_forget()
        self.__deleteEmpleadoButton.grid_forget()
        self.__agregarEmpleadoButton.grid(column=0, row=10, pady=20, sticky="w")

    def __createEmpleadoObject(self) -> Empleado:
        if self.__inputContraseña == "":
            empleado = Empleado(
                str(self.__inputName.get()),
                str(self.__inputLastname1.get()),
                str(self.__inputLastname2.get()),
                str(self.__inputCel.get()),
                float(self.__inputSueldo.get()),
                int(self.__findRol(self.__inputRol.get())),
                bool(self.__isAdmin.get()),
                'V'
            )
            print("Empleado sin contraseña creado")

        else:
            empleado = Empleado(
                str(self.__inputName.get()),
                str(self.__inputLastname1.get()),
                str(self.__inputLastname2.get()),
                str(self.__inputCel.get()),
                float(self.__inputSueldo.get()),
                self.__findRol(self.__inputRol.get()),
                bool(self.__isAdmin.get()),
                'V',
                str(self.__inputContraseña.get())

            )
            print("Empleado con contraseña creado")
        return empleado

    def __agregarEmpleado(self):
        empleado = self.__createEmpleadoObject()
        self.__userManager.Create(empleado)
        self.__updateEmpleados()
        self.__displayMenu()

    def __updateRoles(self):
        self.__roles = self.__rolManager.Read()
        rolesNombre = []
        for rol in self.__roles:
            rolesNombre.append(rol.getNombre())
        return rolesNombre

    def __findRol(self, nombre: str):
        for rol in self.__roles:
            if rol.getNombre() == nombre:
                return rol._getId()

    def __updateEmpleados(self):
        self.get_list_elements().clear()
        empleados = self.__userManager.Read()
        for empleado in empleados:
            if empleado.activo == 'V':
                newElement = NoImageFrame(self.get_list_elements(),
                                          f"{empleado.getNombre()} {empleado.getApellido_paterno()} {empleado.getApellido_materno()}",
                                          empleado)
                newElement.addEvent("<Button-1>", self.__showEmpleado)
                self.get_list_elements().add(newElement)
        empleados.clear()


    def __editEmpleado(self):
        empleado = self.__createEmpleadoObject()
        self.__userManager.Update(self.__empleadoActivo.getId(), empleado)
        self.__updateEmpleados()

    def __deleteEmpleado(self):
        self.__userManager.Delete(self.__empleadoActivo.getId())
        self.__empleadoActivo = None
        self.__updateEmpleados()
        self.__displayMenu()
        if self.get_list_elements().countItems() > 0:
            self.__showEmpleado(self.get_list_elements().getItem(0).object)
        else:
            self.__configureAgregarEmpleado()

    def __cerrar_ventana(self):
        self.__conection.close()
        self.destroy()

    def __search(self):
        if len(self.get_navegation_bar().get()) > 0:
            self.get_list_elements().clear()
            empleados = self.__userManager.find_similar(self.get_navegation_bar().get())
            for empleado in empleados:
                newElement = NoImageFrame(self.get_list_elements(),
                                          f"{empleado.getNombre()} {empleado.getApellido_paterno()} {empleado.getApellido_materno()}",
                                          empleado)
                newElement.addEvent("<Button-1>", self.__showEmpleado)
                self.get_list_elements().add(newElement)
            empleados.clear()
        else:
            self.__updateEmpleados()





