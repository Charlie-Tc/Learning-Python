from tkinter import *

#iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x630')

# evitar maximizar
aplicacion.resizable()

# titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

# color de fondo de la ventana
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side= TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación',  fg='azure4',
                        font=('Dosis', 50), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief= FLAT)
panel_izquierdo.pack(side=LEFT)



# evitar que la pantalla se cierre
aplicacion.mainloop()
