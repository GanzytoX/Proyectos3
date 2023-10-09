import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) # El ancla permite que esté en medio de donde le indiquemos, utiliza la ventana, no pantalla

root.mainloop()