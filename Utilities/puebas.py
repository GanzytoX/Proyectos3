from tkinter import *
from tkcalendar import Calendar
window = Tk()
fechaInicio = Calendar(window,day=12,month=12,year=2022)
fechaInicio.grid()

window.mainloop()