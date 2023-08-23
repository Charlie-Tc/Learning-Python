# módulo tkinder: Es un módulo de python que proporciona una interfaz gráfica de usuario(GUI) para la biblioteca
# Tcl/Tk. Es la interfaz por defecto python para el kit de herramientas de GUI TK.

# widgets: Son bloques de construcción esenciales para crear GUI interactiva y funcional en aplicaciones python,
# permitiendo a los usuarios a interactuar con la aplicación de manera intuitiva.

from tkinter import *

# 1.- Label(): un widget que muestra texto o imágenes. Puede ser utilizado para proporcionar información o instrucciones al usuarios.

def widget_label():
    ventana = Tk()

    label = Label(ventana, text='!Hola Mundo')
    label.pack()

    ventana = mainloop()


# 2.- Button(boton): Un widget que se puede hacer click para realizar una acción.

def widget_button():
    ventana = Tk()

    def button_click():
        print('hiciste click en el boton')

    button = Button(ventana, text='Haga click aqui', command=button_click)
    button.pack()

    ventana = mainloop()


# 3.- Entry(): Un widget que permite ingresar texto al usuario.

def widget_entry():
    ventana = Tk()

    entry = Entry(ventana)
    entry.pack()

    ventana = mainloop()


# 4.- Text: Un widget que permite al usuario a ingresar texto en varias lineas.

def widger_text():
    ventana = Tk()

    text = Text(ventana)
    text.pack()

    ventana = mainloop()


# 5.- Frame(Marco): Un widget que se utiliza para agrupar otros widgets juntos.

def widget_frame():
    ventana = Tk()

    frame = Frame(ventana)
    frame.pack()

    label = Label(frame, text='Este es un marco')
    label.pack()

    ventana = mainloop()


# 6.- CheckButton(casilla de verificación): Un widget que permite al usuario a seleccionar una o varias opciones.

def widget_checkbutton():
    ventana = Tk()

    var1 = IntVar()
    var2 = IntVar()

    checkbutton1 = Checkbutton(ventana, text='Opción 1', variable=var1)
    checkbutton1.pack()

    checkbutton2 = Checkbutton(ventana, text='Opción 2', variable=var2)
    checkbutton2.pack()

    ventana = mainloop()


# 7.- RadioButton(botones de opcion): Un widget que permite al usuario a seleccionar una o varias opciones mutuamente excluyentes.

def widget_radio_button():
    ventana = Tk()

    # valor por defecto
    var = StringVar(value="Opción 2")

    radiobutton1 = Radiobutton(ventana, text="Opción 1", variable=var, value="Opción 1")
    radiobutton1.pack()

    radiobutton2 = Radiobutton(ventana, text="Opción 2", variable=var, value="Opción 2")
    radiobutton2.pack()

    radiobutton3 = Radiobutton(ventana, text="Opción 3", variable=var, value="Opción 3")
    radiobutton3.pack()

    ventana = mainloop()



# 8.- Scale(): Un widget que permite al usuario a seleccionar un valor dentro de un rango determinado.

def widget_scale():
    ventana = Tk()

    scale = Scale(ventana, from_=0, to=100, orient=HORIZONTAL)
    scale.pack()

    ventana = mainloop()



# 9.- Menu(): Un widget que muestra opciones en forma de menú desplegable.

def widger_menu():
    ventana = Tk()

    def do_nothing():
        pass

    menu_bar = Menu(ventana)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Abrir", command=do_nothing)
    file_menu.add_command(label="Guardar", command=do_nothing)
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=ventana.quit)

    menu_bar.add_cascade(label="Archivo", menu=file_menu)

    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Cortar", command=do_nothing)
    edit_menu.add_command(label="Copiar", command=do_nothing)
    edit_menu.add_command(label="Pegar", command=do_nothing)

    menu_bar.add_cascade(label="Editar", menu=edit_menu)

    ventana.config(menu=menu_bar)

    ventana = mainloop()


# 10.- Listbox(): Un widget que muestra una lista de elementos.

def widget_listbox():
    ventana = Tk()

    listbox = Listbox(ventana)
    listbox.pack()

    listbox.insert(1, "Elemento 1")
    listbox.insert(2, "Elemento 2")
    listbox.insert(3, "Elemento 3")

    ventana = mainloop()



# 11.- Scrollbar(): Un widget que se utiliza para desplazarse por otro widgets, como un widget de texto o lista.

def widget_scrollbar():
    ventana = Tk()

    scrollbar = Scrollbar(ventana)
    scrollbar.pack(side=RIGHT, fill=Y)

    text = Text(ventana, yscrollcommand=scrollbar.set)

    # tk.BOTH se utiliza para especificar que un widget debe expandirse en ambas direcciones
    text.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=text.yview())

    ventana = mainloop()


# 12.- Canvas(): Un widget que se utiliza para dibujar gráficos y figuras.

def widget_canvas():
    ventana = Tk()

    canvas = Canvas(ventana, width=200, height=200)
    canvas.pack()

    canvas.create_rectangle(50, 50, 150, 150, fill="blue")

    ventana = mainloop()


# 13.- MenuButton(): Un widget que muestra opciones en forma de menú desplegable.

def widget_menubutton():
    ventana = Tk()

    menu_button = Menubutton(ventana, text="Opciones")
    menu_button.pack()

    menu = Menu(menu_button)
    menu.add_command(label="Opción 1", command=lambda : print("Seleccionaste la opción 1"))
    menu.add_command(label="Opción 2", command=lambda : print("Seleccionaste la opción 2"))

    menu_button.config(menu=menu)

    ventana = mainloop()


# 14.- Message(): Un widget que muestra un mensaje en una ventana emergente.

def widget_message():
    ventana = Tk()

    message = Message(ventana, text="Este es un mensaje emergente")
    message.pack()

    ventana = mainloop()


# 15.- Spinbox(): Un widget que permite al usuario a seleccionar un valor dentro de un rango determinado utilizando botones de flecha.

def widget_spinbox():
    ventana = Tk()

    spinbox = Spinbox(ventana, from_=0, to=10)
    spinbox.pack()

    ventana = mainloop()



# 16.- Treeview(): Un widget que muestra datos en forma de árbol jerárquico.

def widget_treeview():
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()

    tree = ttk.Treeview(root)
    tree.pack()

    tree.insert("", "0", "item1", text="Elemento 1")
    tree.insert("item1", "end", text="Subelemento 1")
    tree.insert("", "1", "item2", text="Elemento 2")

    root.mainloop()


# PARAMETROS QUE SE PUEDEN UTILIZAR EN TKINTER


# anchor: Especifica cómo se posiciona un widget dentro de su contenedor.
# bg: Establece el color de fondo del widget.
# bd: Establece el ancho del borde del widget.
# command: Especifica la función que se ejecutará cuando se haga clic en un botón.
# fg: Establece el color del texto o los elementos gráficos dentro del widget.
# font: Establece la fuente utilizada para el texto dentro del widget.
# height: Establece la altura del widget en píxeles.
# image: Especifica una imagen que se mostrará dentro del widget.
# justify: Especifica cómo se justifica el texto dentro del widget.
# padx: Establece el relleno horizontal dentro del widget.
# pady: Establece el relleno vertical dentro del widget.
# relief: Especifica el tipo de borde que se utilizará para el widget.
# text: Establece el texto que se mostrará dentro del widget.
# width: Establece el ancho del widget en píxeles.
# state: Establece el estado del widget como “normal”, “desactivado” o “solo lectura”.
# underline: Especifica qué letra del texto del widget se subrayará.
# variable: Especifica una variable que se utilizará para almacenar el valor del widget.
# wraplength: Establece la longitud máxima de línea antes de que se produzca un salto de línea automático.
