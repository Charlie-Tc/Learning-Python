from tkinter import *
import json



class UserData:
    def __init__(self, program):
        # crear la ventana
        self.program = program
        self.program.title("Administrador de Contactos")
        self.program.geometry("233x397")
        self.program.resizable(False, False)

        # variables
        self.empty_contacts = []
        self.file_json = "contacts.json"

        # Lista de contactos
        self.list_of_contacts = Listbox(program, width=35, selectmode=SINGLE, height=13)
        self.list_of_contacts.pack()
        self.load_contacts()

        # panel botones
        self.button_panel = Frame(program)
        self.button_panel.pack(pady=13)

        # botones
        self.agregar_contacto = Button(self.button_panel, text="Agregar Contacto  ➕", command=self.add_contact, pady=7, padx=10, bd=3)
        self.agregar_contacto.grid(row=0, column=0)

        self.editar_contacto = Button(self.button_panel, text="Editar Contacto 🖊", command=self.edit_contact, pady=7, padx=15, bd=3)
        self.editar_contacto.grid(row=1, column=0)

        self.eliminar_contacto = Button(self.button_panel, text="Eliminar Contacto 🗑", command=self.remove_contact, pady=7, padx=10, bd=3)
        self.eliminar_contacto.grid(row=2, column=0)

        self.guardar_contacto = Button(self.button_panel, text="Guardar Contacto 💾", command=self.save_contact, pady=7, padx=10, bd=3)
        self.guardar_contacto.grid(row=3, column=0)
    def add_contact(self):
        def save_data():
            display_age = int(enter_age.get())
            display_nrotel = int(enter_nrotel.get())
            self.empty_contacts.append({"Name": enter_name.get(), "Age": display_age, "Nro telephone": display_nrotel,
                                        "City": enter_city.get(), "Email": enter_email.get()})

            self.list_of_contacts.insert(END, self.empty_contacts[-1]["Name"])



        # ventana emergente de agregar contacto
        ventana = Toplevel(self.program)
        ventana.title("Agregar Contacto")
        ventana.geometry("273x230")
        ventana.resizable(False, False)

        # label
        label_datos = Label(ventana, text="Ingresa tus Datos", font=("Corbel", 16, "bold"))
        label_datos.pack()

        # label nombre
        label_nombre = Label(ventana, text="Nombre y Apellido:", font="Corbel")
        label_nombre.pack()

        # ingresar numbre y apellido
        enter_name = Entry(ventana)
        enter_name.pack()

        # panel de edad, numero telefonico y ciudad
        data = Frame(ventana)
        data.pack()

        datas = ["    Edad:\t", "     Nro. telefónico:\t", "Ciudad:"]
        columnas = 0
        index = 0

        for d in datas:
            Label(data, text=datas[index], font=("Corbel", 10)).grid(row=0, column=columnas)
            columnas += 1
            index += 1

        # ingresar edad

        enter_age = Entry(data, width=13)
        enter_age.grid(row=1, column=0)

        # ingresar numero telefonico
        enter_nrotel = Entry(data, width=13)
        enter_nrotel.grid(row=1, column=1)

        # ingresar ciudad
        enter_city = Entry(data, width=13)
        enter_city.grid(row=1, column=2)

        # label correo
        label_correo = Label(ventana, text="Correo Electrónico", font="Corbel")
        label_correo.pack()

        # ingresar correo
        enter_email = Entry(ventana, width=25)
        enter_email.pack()

        # espacio vacio
        space_empty = Label(ventana, height=1)
        space_empty.pack()

        # panel de cancelar y guardar
        save_cancel = Frame(ventana)
        save_cancel.pack()

        # botones
        boton_cancel = Button(save_cancel, text="Cancelar", bd=3, padx=12, command=ventana.destroy)
        boton_cancel.grid(row=0, column=0)
        space_empty = Label(save_cancel, width=4)
        space_empty.grid(row=0, column=1)
        boton_guardar = Button(save_cancel, text="Guardar", bd=3, padx=12, command=save_data)
        boton_guardar.grid(row=0, column=2)

    def load_contacts(self):
        with open(self.file_json, "r") as load_files:
            read_load = json.load(load_files)
        for name in read_load:
            self.list_of_contacts.insert(END, name["Name"])

    def edit_contact(self):
        select = self.list_of_contacts.curselection()
        if select:
            index_selected = select[0]
            display_selecte = self.list_of_contacts.get(index_selected)
            search_selected = f"name"

        # ventana emergente de agregar contacto
        ventana = Toplevel(self.program)
        ventana.title("Editar Contacto")
        ventana.geometry("273x230")
        ventana.resizable(False, False)

        # label
        label_datos = Label(ventana, text="Ingresa tus Datos", font=("Corbel", 16, "bold"))
        label_datos.pack()

        # label nombre
        label_nombre = Label(ventana, text="Nombre y Apellido:", font="Corbel")
        label_nombre.pack()

        # ingresar numbre y apellido
        enter_name = Entry(ventana)
        enter_name.pack()

        # panel de edad, numero telefonico y ciudad
        data = Frame(ventana)
        data.pack()

        datas = ["    Edad:\t", "     Nro. telefónico:\t", "Ciudad:"]
        columnas = 0
        index = 0

        for d in datas:
            Label(data, text=datas[index], font=("Corbel", 10)).grid(row=0, column=columnas)
            Entry(data, width=12).grid(row=1, column=columnas)
            columnas += 1
            index += 1


        # label correo
        label_correo = Label(ventana, text="Correo Electrónico", font="Corbel")
        label_correo.pack()

        # ingresar correo
        enter_email = Entry(ventana, width=25)
        enter_email.pack()

        # espacio vacio
        space_empty = Label(ventana, height=1)
        space_empty.pack()

        # panel de cancelar y guardar
        save_cancel = Frame(ventana)
        save_cancel.pack()

        # botones
        boton_cancel = Button(save_cancel, text="Cancelar", bd=3, padx=12, command=ventana.destroy)
        boton_cancel.grid(row=0, column=0)
        space_empty = Label(save_cancel, width=4)
        space_empty.grid(row=0, column=1)
        boton_guardar = Button(save_cancel, text="Guardar", bd=3, padx=12)
        boton_guardar.grid(row=0, column=2)


    def remove_contact(self):
        pass


    def save_contact(self):
        with open(self.file_json, "w") as write_json:
            json.dump(self.empty_contacts, write_json)





if __name__ == "__main__":
    program = Tk()
    UserData(program)
    program.mainloop()
