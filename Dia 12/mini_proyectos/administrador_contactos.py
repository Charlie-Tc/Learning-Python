from tkinter import *

class UserData():
    def __init__(self, name, age, nro_tel, city, email):
        self.name = name
        self.age = age
        self.nro_tel = nro_tel
        self.city = city
        self.email = email




def add_contact():
    # ventana emergente de agregar contacto
    ventana = Toplevel(program)
    ventana.title("Agregar Contacto")
    ventana.geometry("273x180")
    ventana.resizable(False, False)

    # label
    label_datos = Label(ventana, text="Ingresa tus Datos")
    label_datos.pack()

    # label nombre
    label_nombre = Label(ventana, text="Nombre y Apellido:")
    label_nombre.pack()

    # ingresar numbre y apellido
    enter_name = Entry(ventana)
    enter_name.pack()

    # panel de edad, numero telefonico y ciudad
    data = Frame(ventana)
    data.pack()

    datas = ["Edad:\t", "Nro. telefónico:\t", "Ciudad:"]
    columnas = 0
    index = 0


    for d in datas:
        Label(data, text=datas[index]).grid(row=0, column=columnas)
        Entry(data, width=12).grid(row=1, column=columnas)
        columnas += 1
        index += 1




    # label correo
    label_correo = Label(ventana, text="Correo Electrónico")
    label_correo.pack()

    # ingresar correo
    enter_email = Entry(ventana)
    enter_email.pack()


    ventana.mainloop()



def edit_contact():
    pass

def remove_contact():
    pass

def save_contact():
    pass

# crear la ventana
program = Tk()
program.title("Administrador de Contactos")
program.geometry("233x397")
program.resizable(False, False)




# Lista de contactos
list_of_contacts = Listbox(program, width=35, selectmode=SINGLE, height=13)
list_of_contacts.pack()

# panel botones
button_panel = Frame(program)
button_panel.pack(pady=13)

# botones
agregar_contacto = Button(button_panel, text="Agregar Contacto", command=add_contact, pady=7, padx=10, bd=3)
agregar_contacto.grid(row=0, column=0)

editar_contacto = Button(button_panel, text="Editar Contacto", command=edit_contact, pady=7, padx=15, bd=3)
editar_contacto.grid(row=1, column=0)

eliminar_contacto = Button(button_panel, text="Eliminar Contacto", command=remove_contact, pady=7, padx=10, bd=3)
eliminar_contacto.grid(row=2, column=0)

guardar_contacto = Button(button_panel, text="Guardar Contacto", command=save_contact, pady=7, padx=10, bd=3)
guardar_contacto.grid(row=3, column=0)



# cerrar la ventana
program.mainloop()
