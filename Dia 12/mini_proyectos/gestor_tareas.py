from tkinter import *

def agregar_tarea():
    add = var_empty.get()
    list_taks.insert(END, add)
    var_empty.set("")

def completar_tarea():
    selectd = list_taks.curselection()
    if selectd:
        selectd_index = selectd[0]
        selectd_items = list_taks.get(selectd_index)
        list_taks.delete(selectd_index)
        completed_task_list.insert(END, selectd_items)

def eliminar_tarea():
    selectd = list_taks.curselection()
    if selectd:
        selectd_index = selectd[0]
        list_taks.delete(selectd_index)


# iniciar tkinter
aplicacion = Tk()
aplicacion.geometry('400x600')
aplicacion.title('Gestor de Tareas')
aplicacion.config(bg='dark gray')

# panel de escribir tarea
var_empty = StringVar()
write_task = Entry(aplicacion, width=50, textvariable=var_empty)
write_task.pack()

# boton agregar tarea
add_task = Button(aplicacion, text="Agregar tarea", command=agregar_tarea)
add_task.pack()


# lista de tarea agregada
list_taks = Listbox(aplicacion, width=50, selectmode=SINGLE)
list_taks.pack()



# boton completar tarea
add_task = Button(aplicacion, text="Completar tarea", command=completar_tarea)
add_task.pack()

# boton eliminar tarea
add_task = Button(aplicacion, text="Eliminar tarea", command=eliminar_tarea)
add_task.pack()


# lista de tarea completada
completed_task_list = Listbox(aplicacion, width=50)
completed_task_list.pack()


# finalizar el bucle principal
aplicacion.mainloop()
