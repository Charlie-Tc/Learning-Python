# módulo tkinder: Es un módulo de python que proporciona una interfaz gráfica de usuario(GUI) para la biblioteca
# Tcl/Tk. Es la interfaz por defecto python para el kit de herramientas de GUI TK.

# widgets: Son bloques de construcción esenciales para crear GUI interactiva y funcional en aplicaciones python,
# permitiendo a los usuarios a interactuar con la aplicación de manera intuitiva.

from tkinter import *

# 1.- Label(): un widget que muestra texto o imágenes. Puede ser utilizado para proporcionar información o instrucciones al usuarios.
    # 1.- Métodos:
        # config(**options): Permite configurar atributos del widget.
        # pack(**options): Coloca el widget en la ventana usando el administrador de geometría "pack".
        # grid(**options): Coloca el widget en la ventana usando el administrador de geometría "grid".
        # place(**options): Coloca el widget en la ventana usando el administrador de geometría "place".
        # bind(event, handler): Vincula una función de controlador a un evento específico.
        # unbind(event): Desvincula un controlador de un evento.
    # 2.- Atributos:
        # text: El texto que se muestra en el widget Label.
        # font: La fuente utilizada para el texto.
        # bg (background): El color de fondo del widget.
        # fg (foreground): El color del texto del widget.
        # width: El ancho del widget.
        # height: La altura del widget.
        # image: Una imagen que se muestra en lugar de texto.
        # relief: El estilo del borde del widget (por ejemplo, "flat", "raised", "sunken").
        # anchor: La posición de anclaje del texto dentro del widget.
        # justify: La alineación del texto dentro del widget ("left", "center", "right").

def widget_label():
    ventana = Tk()

    label = Label(ventana, text='!Hola Mundo')
    label.pack()

    ventana = mainloop()


# 2.- Button(boton): Un widget que se puede hacer click para realizar una acción.
    # 1.- Métodos:
        # .pack(): Coloca el widget en el administrador de geometría de empaquetado.
        # .grid(): Coloca el widget en el administrador de geometría de grilla.
        # .place(): Coloca el widget en coordenadas específicas.
        # .config(**options): Configura las opciones del widget.
        # .bind(event, handler): Vincula un controlador de eventos a un evento específico.
        # .unbind(event): Desvincula un controlador de eventos de un evento específico.
        # .invoke(): Simula un clic en el botón, activando su función asociada.
    # 2.- Atributos:
        # text: El texto que se muestra en el botón.
        # command: La función que se ejecuta cuando se hace clic en el botón.
        # state: El estado del botón ('normal', 'disabled', 'active').
        # bg / background: El color de fondo del botón.
        # fg / foreground: El color del texto del botón.
        # font: La fuente utilizada para el texto del botón.
        # width: Ancho del botón en caracteres.
        # height: Altura del botón en caracteres.

def widget_button():
    ventana = Tk()

    def button_click():
        print('hiciste click en el boton')

    button = Button(ventana, text='Haga click aqui', command=button_click)
    button.pack()

    ventana = mainloop()


# 3.- Entry(): Un widget que permite ingresar texto al usuario.
    # 1.- Métodos:
        # get(): Devuelve el contenido actual del widget Entry.
        # delete(first, last=None): Elimina caracteres desde la posición "first" hasta la posición "last".
        # insert(index, string): Inserta la cadena "string" en la posición "index".
        # icursor(index): Establece la posición del cursor en la posición "index".
        # index(index): Devuelve la posición del cursor o el índice especificado.
        # select_range(start, end): Selecciona el texto entre las posiciones "start" y "end".
        # select_clear(): Borra la selección de texto actual.
        # xview(*args): Permite desplazar el contenido horizontalmente.
    # 2.- Atributos:
        # textvariable: Permite vincular una variable StringVar a la entrada para obtener y establecer su valor.
        # show: Puede utilizarse para mostrar un carácter diferente en lugar de los caracteres reales (por ejemplo, para contraseñas).
        # state: Puede ser 'normal' (editable), 'readonly' (solo lectura) o 'disabled' (desactivado).
        # width: Define el ancho del widget en caracteres.
        # validate y validatecommand: Utilizados para validar la entrada según ciertas condiciones.

def widget_entry():
    ventana = Tk()

    entry = Entry(ventana)
    entry.pack()

    ventana = mainloop()


# 4.- Text: Un widget que permite al usuario a ingresar texto en varias lineas.
    # Métodos:
        # insert(index, text): Inserta el texto en la posición especificada por el índice.
        # delete(start, end=None): Elimina el texto desde la posición de inicio hasta la posición de finalización.
        # get(start, end=None): Obtiene el texto desde la posición de inicio hasta la posición de finalización.
        # index(index): Obtiene la posición indexada de un índice dado.
        # search(pattern, start, stop=None): Busca un patrón en el texto entre las posiciones de inicio y finalización.
        # tag_add(tagName, start, end): Agrega una etiqueta a una porción de texto.
        # tag_remove(tagName, start, end): Elimina una etiqueta de una porción de texto.
        # tag_configure(tagName, options): Configura las opciones de una etiqueta.
        # tag_ranges(tagName): Obtiene las posiciones de inicio y finalización de una etiqueta.
        # see(index): Desplaza la vista del widget para mostrar el índice especificado.
    # Atributos:
        # background: Establece el color de fondo del widget.
        # foreground: Establece el color del texto.
        # font: Establece la fuente del texto.
        # height: Establece la altura del widget en número de líneas.
        # width: Establece el ancho del widget en número de caracteres.
        # state: Establece el estado del widget (NORMAL, DISABLED).
        # wrap: Establece el comportamiento de ajuste de línea (NONE, CHAR, WORD).

def widger_text():
    ventana = Tk()

    text = Text(ventana)
    text.pack()

    ventana = mainloop()


# 5.- Frame(Marco): Un widget que se utiliza para agrupar otros widgets juntos.
    # Métodos:

        # __init__(self, master=None, cnf={}, **kw): Constructor para el widget Frame.
        # destroy(self): Destruye el widget Frame y sus descendientes.
        # pack(self, cnf={}, **kw): Organiza y muestra el widget utilizando el algoritmo de empaquetado.
        # grid(self, cnf={}, **kw): Organiza y muestra el widget utilizando el sistema de rejilla.
        # place(self, cnf={}, **kw): Organiza y muestra el widget utilizando el sistema de posicionamiento absoluto.
        # config(self, cnf={}, **kw): Configura atributos del widget.
        # update(self): Actualiza el widget y sus descendientes.
        # bind(self, sequence=None, func=None, add=None): Vincula una función a un evento.
    # Atributos:

        # master: El widget padre (ventana principal o un widget contenedor superior).
        # background (bg): Color de fondo del widget.
        # borderwidth (bd): Ancho del borde del widget.
        # cursor: Cursor que se muestra cuando el ratón está sobre el widget.
        # height: Altura del widget en píxeles.
        # width: Ancho del widget en píxeles.
        # relief: Tipo de relieve del borde del widget (por ejemplo, "flat", "raised", "sunken").
        # highlightbackground: Color del borde cuando el widget no tiene el foco.
        # highlightcolor: Color del borde cuando el widget tiene el foco.
        # highlightthickness: Grosor del borde cuando el widget tiene el foco.
        # takefocus: Indica si el widget puede recibir el foco del teclado.

def widget_frame():
    ventana = Tk()

    frame = Frame(ventana)
    frame.pack()

    label = Label(frame, text='Este es un marco')
    label.pack()

    ventana = mainloop()


# 6.- CheckButton(casilla de verificación): Un widget que permite al usuario a seleccionar una o varias opciones.
    # Métodos:
        # deselect(): Desmarca la casilla de verificación.
        # select(): Marca la casilla de verificación.
        # toggle(): Alterna el estado de selección de la casilla de verificación.
        # state([newstate]): Obtiene o establece el estado de la casilla de verificación (normal, deshabilitado, seleccionado, etc.).
        # invoke(): Activa la casilla de verificación, ejecutando su función asociada (si está configurada).
        # flash(): Hace que la casilla de verificación parpadee temporalmente.
        # destroy(): Destruye la casilla de verificación y la elimina de la GUI.
    # Atributos:
        # variable: Un objeto tkinter IntVar, StringVar u otro tipo de variable que almacena el valor actual de la casilla de verificación.
        # onvalue: El valor asignado a la variable cuando la casilla de verificación está marcada.
        # offvalue: El valor asignado a la variable cuando la casilla de verificación no está marcada.
        # text: Texto que se muestra junto a la casilla de verificación.
        # command: Una función que se ejecuta cuando se hace clic en la casilla de verificación.
        # state: El estado inicial de la casilla de verificación (normal, deshabilitado, seleccionado, etc.).

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
    # Métodos:
        # .deselect(): Desmarca el botón de opción (RadioButton).
        # .select(): Marca el botón de opción (RadioButton).
        # .configure(**options): Permite configurar varias opciones del botón de opción.
        # .invoke(): Activa el botón de opción como si fuera presionado por el usuario.
        # .pack(**options): Coloca el botón de opción utilizando el administrador de geometría pack.
        # .grid(**options): Coloca el botón de opción utilizando el administrador de geometría grid.
        # .place(**options): Coloca el botón de opción utilizando el administrador de geometría place.
        # .destroy(): Destruye el botón de opción y elimina su ventana.
    # Atributos:
        # text: El texto que se muestra junto al botón de opción.
        # variable: Una variable de control asociada al botón de opción. Puede ser una instancia de IntVar, StringVar, etc.
        # value: El valor que se asocia a este botón de opción cuando se selecciona.
        # command: Una función que se llama cuando el botón de opción se selecciona.
        # indicatoron: Si es True, se muestra solo el indicador del botón sin el texto.
        # padx, pady: Espacio interno horizontal y vertical dentro del botón de opción.
        # state: El estado inicial del botón de opción (normal, deshabilitado, seleccionado).
        # font: La fuente del texto en el botón de opción.
        # bg (background), fg (foreground): El color de fondo y el color del texto del botón de opción.

def widget_radio_button():
    ventana = Tk()

    # selección por defecto
    var = StringVar(value="Opción 2")

    radiobutton1 = Radiobutton(ventana, text="Opción 1", variable=var, value="Opción 1")
    radiobutton1.pack()

    radiobutton2 = Radiobutton(ventana, text="Opción 2", variable=var, value="Opción 2")
    radiobutton2.pack()

    radiobutton3 = Radiobutton(ventana, text="Opción 3", variable=var, value="Opción 3")
    radiobutton3.pack()

    ventana = mainloop()




# 8.- Scale(): Un widget que permite al usuario a seleccionar un valor dentro de un rango determinado.
    # Métodos:
        # get(): Retorna el valor actual del Scale.
        # set(value): Establece el valor del Scale al valor proporcionado.
        # config(**options): Permite configurar opciones del Scale.
        # pack(**options), place(**options), grid(**options): Métodos de administración de geometría para mostrar el Scale en la ventana.
    # Atributos (opciones que se pueden configurar):
        # from_: Valor mínimo del Scale.
        # to: Valor máximo del Scale.
        # variable: Variable asociada al valor del Scale.
        # orient: Orientación del Scale, puede ser 'horizontal' o 'vertical'.
        # length: Longitud del Scale en píxeles.
        # showvalue: Si se muestra el valor actual junto al Scale.
        # resolution: Incremento mínimo entre valores.
        # sliderlength: Longitud del indicador de deslizamiento.
        # label: Etiqueta que se muestra junto al Scale.
        # command: Función llamada cada vez que el valor del Scale cambia.

def widget_scale():
    ventana = Tk()

    scale = Scale(ventana, from_=0, to=100, orient=HORIZONTAL)
    scale.pack()

    ventana = mainloop()


# 9.- Menu(): Un widget que muestra opciones en forma de menú desplegable.
    # Métodos:
        # add_command(label, command): Agrega un elemento de comando al menú con la etiqueta especificada y la función a ejecutar cuando se selecciona.
        # add_separator(): Agrega un separador visual entre los elementos del menú.
        # add_cascade(label, menu): Agrega un submenú con la etiqueta especificada y el menú asociado.
        # delete(index): Elimina el elemento del menú en el índice dado.
        # entryconfig(index, option=value): Configura las opciones de un elemento del menú específico.
        # insert_separator(index): Inserta un separador en el menú en el índice dado.
        # invoke(index): Simula la selección de un elemento del menú, ejecutando su función asociada.
    # Atributos:
        # tearoff: Un valor booleano que determina si el menú desplegable puede ser arrancado (torn off) para flotar como una ventana separada. Por defecto, es 1 (verdadero).

def widget_menu():
    ventana = Tk()

    def do_nothing():
        pass

    menu_bar = Menu(ventana)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Abrir", command=do_nothing)
    file_menu.add_command(label="Guardar", command=do_nothing)
    file_menu.add_separator() # separador
    file_menu.add_command(label="Salir", command=ventana.quit)  # cierra la ventana

    menu_bar.add_cascade(label="Archivo", menu=file_menu)   # menu desplegable de "Archivo"

    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Cortar", command=do_nothing)
    edit_menu.add_command(label="Copiar", command=do_nothing)
    edit_menu.add_command(label="Pegar", command=do_nothing)

    menu_bar.add_cascade(label="Editar", menu=edit_menu)    # menu desplegable de "Archivo"

    ventana.config(menu=menu_bar)

    ventana = mainloop()



# 10.- Listbox(): Un widget que muestra una lista de elementos.
    # 1.- Métodos:
        # insert(index, *elements): Inserta uno o más elementos en el índice especificado.
        # delete(first, last=None): Elimina elementos desde el índice first hasta el índice last.
        # get(index): Obtiene el contenido del elemento en el índice especificado.
        # curselection(): Devuelve una tupla que contiene los índices de los elementos seleccionados.
        # selection_set(first, last=None): Marca como seleccionados los elementos desde el índice first hasta el índice last.
        # selection_clear(first, last=None): Desmarca la selección en los elementos desde el índice first hasta el índice last.
        # size(): Devuelve la cantidad de elementos en la lista.
        # activate(index): Activa el elemento en el índice especificado.
    # 2.- Atributos:
        # selectmode: Define el modo de selección. Puede ser SINGLE (un solo elemento), BROWSE (un solo elemento pero puedes deseleccionar), MULTIPLE (múltiples elementos), o EXTENDED (múltiples elementos con teclas de modificación).
        # height: Define la cantidad visible de elementos en la lista.

def widget_listbox():
    ventana = Tk()

    listbox = Listbox(ventana)
    listbox.pack()

    listbox.insert(1, "Elemento 1")
    listbox.insert(2, "Elemento 2")
    listbox.insert(3, "Elemento 3")

    ventana = mainloop()


# 11.- Scrollbar(): Un widget que se utiliza para desplazarse por otro widgets, como un widget de texto o lista.
    # Métodos:
        # get(): Obtiene la posición actual del scrollbar.
        # set(): Establece la posición del scrollbar.
        # activate(): Activa el scrollbar para interactuar con él.
        # delta(): Devuelve la cantidad de desplazamiento que el scrollbar debe moverse.
    # Atributos:
        # orient: Especifica la orientación del scrollbar ("horizontal" o "vertical").
        # command: Define la función o método que se llama cuando el scrollbar se mueve.
        # activebackground: Color de fondo cuando el scrollbar está activo.
        # bg o background: Color de fondo del scrollbar.
        # troughcolor: Color del canal a través del cual se desplaza el scrollbar.
        # highlightcolor: Color del resaltado del scrollbar cuando está enfocado.
        # width: Ancho del scrollbar.
        # elementborderwidth: Ancho del borde del elemento del scrollbar.
        # sliderlength: Longitud del control deslizante en el scrollbar.
        # sliderrelief: Tipo de relieve para el control deslizante.

def widget_scrollbar():
    ventana = Tk()

    scrollbar = Scrollbar(ventana)
    scrollbar.pack(side=RIGHT, fill=Y)

    text = Text(ventana, yscrollcommand=scrollbar.set)

    # tk.BOTH se utiliza para especificar que un widget debe expandirse en ambas direcciones
    text.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=text.yview())

    ventana = mainloop()


# 12.- Canvas(x1, y1, x2, y2, fill="color"): Un widget que se utiliza para dibujar gráficos y figuras.
    # Métodos:
        # get(): Obtiene la posición actual del scrollbar.
        # set(): Establece la posición del scrollbar.
        # activate(): Activa el scrollbar para interactuar con él.
        # delta(): Devuelve la cantidad de desplazamiento que el scrollbar debe moverse.
    # Atributos:
        # orient: Especifica la orientación del scrollbar ("horizontal" o "vertical").
        # command: Define la función o método que se llama cuando el scrollbar se mueve.
        # activebackground: Color de fondo cuando el scrollbar está activo.
        # bg o background: Color de fondo del scrollbar.
        # troughcolor: Color del canal a través del cual se desplaza el scrollbar.
        # highlightcolor: Color del resaltado del scrollbar cuando está enfocado.
        # width: Ancho del scrollbar.
        # elementborderwidth: Ancho del borde del elemento del scrollbar.
        # sliderlength: Longitud del control deslizante en el scrollbar.
        # sliderrelief: Tipo de relieve para el control deslizante.

def widget_canvas():
    ventana = Tk()

    canvas = Canvas(ventana, width=200, height=200)
    canvas.pack()

    canvas.create_rectangle(50, 50, 150, 150, fill="blue")

    lienzo = Canvas(ventana, width=200, height=200)
    lienzo.pack()

    # Dibuja un óvalo (forma redonda) con relleno azul
    lienzo.create_oval(50, 50, 150, 150, fill="red")

    ventana = mainloop()



# 13.- MenuButton(): Un widget que muestra opciones en forma de menú desplegable.
    # Métodos:
        # add_radiobutton(): Agrega un botón de opción a un menú.
        # add_checkbutton(): Agrega un botón de verificación a un menú.
        # add_command(): Agrega un comando a un menú.
        # delete(): Elimina una opción de un menú.
        # entryconfig(): Configura una entrada en el menú.
        # post(): Muestra el menú desplegable.
    # Atributos:
        # menu: El menú que se asocia con el MenuButton.
        # text: El texto que se muestra en el MenuButton.
        # underline: Índice del carácter subrayado en el texto (para crear atajos de teclado).
        # state: Estado del MenuButton ("normal", "disabled" u otros).
        # width: Ancho del MenuButton.

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
        # anchor: Establece la posición del texto dentro del widget.
        # bg: Establece el color de fondo del widget.
        # bitmap: Establece el mapa de bits que se muestra en el widget.
        # borderwidth: Establece el ancho del borde del widget.
        # cursor: Establece el cursor que se muestra cuando el ratón está sobre el widget.
        # font: Establece la fuente utilizada para el texto.
        # fg: Establece el color del texto.
        # height: Establece la altura del widget.
        # highlightbackground: Establece el color del borde cuando el widget no tiene el foco.
        # highlightcolor: Establece el color del borde cuando el widget tiene el foco.
        # highlightthickness: Establece el ancho del borde cuando el widget tiene el foco.
        # image: Establece la imagen que se muestra en lugar del texto.
        # justify: Establece la justificación del texto dentro del widget. Los valores posibles son: LEFT, CENTER y RIGHT.
        # padx: Establece el relleno horizontal del widget.
        # pady: Establece el relleno vertical del widget.
        # relief: Establece el tipo de borde del widget. Los valores posibles son: FLAT, SUNKEN, RAISED, GROOVE y RIDGE.
        # text: Establece el texto que se muestra en el widget.
        # textvariable: Enlaza una variable a la propiedad text del widget. Si la variable cambia, también lo hace el texto mostrado en el widget.
        # underline: Indica qué carácter está subrayado en el texto. El valor predeterminado es -1, lo que significa que ningún carácter está subrayado.
        # width: Establece la anchura del widget.

def widget_message():
    ventana = Tk()

    message = Message(ventana, text="Este es un mensaje emergente")
    message.pack()

    ventana = mainloop()


# 15.- Spinbox(): Un widget que permite al usuario a seleccionar un valor dentro de un rango determinado utilizando botones de flecha.
    # Métodos:
        # delete(start, end): Elimina los caracteres en el rango especificado.
        # get(): Obtiene el valor actual del Spinbox en formato de cadena.
        # insert(index, string): Inserta la cadena en la posición especificada.
        # invoke(element): Llama al comando asociado al elemento especificado (si existe).
        # select_range(start, end): Selecciona el rango de caracteres entre las posiciones especificadas.
    # Atributos:
        # from_: El valor mínimo permitido en el Spinbox.
        # to: El valor máximo permitido en el Spinbox.
        # increment: La cantidad en la que el valor cambia cuando se utiliza la flecha de aumento/disminución.
        # values: Una lista de valores permitidos en el Spinbox.
        # textvariable: Variable asociada que se actualiza con el valor del Spinbox.
        # state: Puede ser "readonly" o "normal" para controlar si el Spinbox es editable o no.
        # format: Un formato de cadena opcional para mostrar los valores.

def widget_spinbox():
    ventana = Tk()

    spinbox = Spinbox(ventana, from_=0, to=10)
    spinbox.pack()

    ventana = mainloop()



# 16.- Treeview(): Un widget que muestra datos en forma de árbol jerárquico.
    # Métodos:
        # insert(parent, index, iid=None, **kw): Inserta un nuevo elemento en el árbol.
        # delete(*items): Elimina uno o más elementos del árbol.
        # detach(item): Desvincula un elemento del árbol sin eliminarlo.
        # move(item, parent, index): Mueve un elemento a una nueva ubicación en el árbol.
        # item(item, option=None, **kw): Configura o consulta las propiedades de un elemento.
        # selection(): Devuelve una lista de los elementos seleccionados en el árbol.
        # focus(item=None): Establece o devuelve el elemento con el foco.
        # see(item): Asegura que un elemento sea visible en la vista.
        # scroll(amount, what): Desplaza el contenido del widget.
    # Atributos:
        # columns: Define las columnas en el árbol.
        # heading(column, option=None, **kw): Configura o consulta las propiedades de encabezado de columna.
        # selection(): Devuelve una lista de las entradas seleccionadas.
        # focus(): Devuelve el elemento con el foco.
        # insert(parent, index, iid=None, **kw): Inserta un nuevo elemento en el árbol.

def widget_treeview():
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()

    tree = ttk.Treeview(root)
    tree.pack()

    padre = tree.insert("", "end", text="Elemento 1", values=("valor1", "valor2"))
    tree.insert(padre, "end", text="Subelemento 1")
    hijo = tree.insert(padre, "end", text="elemento hijo")
    tree.insert(hijo, "end", text="Subelemento nieto 1")
    tree.insert(hijo, "end", text="subelemento nieto 2")

    root.mainloop()

def otra():
    import tkinter as tk
    from tkinter import ttk

    ventana = tk.Tk()
    ventana.title("Ejemplo Treeview")

    # Crear el Treeview
    tree = ttk.Treeview(ventana)

    # Definir las columnas y encabezados
    tree["columns"] = ("column1", "column2")
    tree.heading("#0", text="Elementos", anchor="w")
    tree.heading("column1", text="Columna 1")
    tree.heading("column2", text="Columna 2")

    # Agregar elementos y valores
    parent = tree.insert("", "end", text="Padre", values=("Valor 1", "Valor 2"))
    hijo1 = tree.insert(parent, "end", text="Hijo 1", values=("Valor 1", "Valor 2"))
    tree.insert(parent, "end", text="Hijo 2", values=("Valor 1", "Valor 2"))
    tree.insert(hijo1, "end", text="Nieto 1", values=("Valor 1", "Valor 2"))
    tree.insert(hijo1, "end", text="Nieto 2", values=("Valor 1", "Valor 2"))

    # Agregar subelementos al nieto 1
    nieto1 = tree.get_children(hijo1)[0]  # Obtener el ID del nieto 1
    tree.insert(nieto1, "end", text="Subnieto 1", values=("Valor 1", "Valor 2"))
    tree.insert(nieto1, "end", text="Subnieto 2", values=("Valor 1", "Valor 2"))

    tree.pack()

    ventana.mainloop()




# 17.- Combobox(): el widget Combobox es parte del módulo ttk. Aquí tienes algunos métodos y atributos comunes del widget Combobox:
    # Métodos:
        # current(index): Establece el elemento actualmente seleccionado en base al índice proporcionado.
        # set(value): Establece el valor de la caja de entrada del Combobox en el valor proporcionado.
        # get(): Devuelve el valor actualmente seleccionado en la caja de entrada del Combobox.
        # values(*values): Establece los valores que aparecerán en la lista desplegable del Combobox.
        # state(state): Configura el estado del Combobox. Puede ser "normal", "readonly" o "disabled".
        # delete(start, end): Borra el texto entre las posiciones de inicio y fin en la caja de entrada.
        # insert(position, value): Inserta el valor proporcionado en la posición especificada en la caja de entrada.
    # Atributos:
        # values: Lista de valores que se mostrarán en la lista desplegable del Combobox.
        # state: Estado actual del Combobox, que puede ser "normal", "readonly" o "disabled".
        # textvariable: Variable de control asociada a la caja de entrada del Combobox.
        # current: Índice del elemento actualmente seleccionado en la lista desplegable.
        # get(): Método para obtener el valor actualmente seleccionado.

def widget_combobox():
    import tkinter as tk
    from tkinter import ttk

    def on_combobox_select(event):
        selected_item = combobox.get()
        result_label.config(text=f"Seleccionaste: {selected_item}")

    app = tk.Tk()
    app.title("Ejemplo de Combobox")

    # Crear un Combobox
    combobox = ttk.Combobox(app, values=["Opción 1", "Opción 2", "Opción 3"])
    combobox.pack(padx=20, pady=20)

    # Etiqueta para mostrar el resultado
    result_label = ttk.Label(app, text="options")
    result_label.pack()

    # Asociar una función al evento de selección del Combobox
    combobox.bind("<<ComboboxSelected>>", on_combobox_select)

    app.mainloop()


# 18.- Toplevel(): El widget `Toplevel` es una ventana que se utiliza para crear una ventana encima de todas las demás ventanas.
# Puede proporcionar información adicional al usuario y también cuando nuestro programa trata con más de una aplicación.
    # Los siguientes son algunos de los métodos y atributos comunes del widget `Toplevel`:
        #  iconify()`: convierte la ventana en un icono.
        #  deiconify()`: convierte el icono en una ventana.
        #  state: El estado actual de la ventana ("normal", "iconic" o "withdrawn").
        #  withdraw()`: elimina la ventana de la pantalla.
        #  title()`: define el título para la ventana.
        #  frame()`: devuelve un identificador de ventana que es específico del sistema.
        #  destroy(): Cierra y destruye la ventana Toplevel.
        #  geometry(geometry_string): Establece la geometría de la ventana en función de la cadena proporcionada (por ejemplo, "400x300").
        #  transient(master): Establece la ventana principal sobre la cual la ventana Toplevel aparece como una ventana modal.
        #  focus_set(): Establece el enfoque en la ventana Toplevel.
        #  update(): Actualiza la ventana Toplevel y sus widgets secundarios.
        #  wait_window(window): Espera hasta que la ventana window sea destruida antes de continuar.
        #  protocol(name, function): Asocia una función con el protocolo de ventana especificado (por ejemplo, "WM_DELETE_WINDOW").
# Además, el widget `Toplevel` también admite los siguientes parámetros opcionales:
        # root`: ventana raíz (opcional).
        # bg`: color de fondo.
        # fg`: color del primer plano.
        # bd`: ancho del borde.
        # height`: altura del widget.
        # width`: ancho del widget.
        # font`: tipo de fuente del texto.
        # cursor`: cursor que aparece en el widget, que puede ser una flecha, un punto, etc.

def widget_toplevel():
    import tkinter as tk
    from tkinter import ttk

    def open_popup():
        ventana = tk.Toplevel(root)
        ventana.title("Ventana Emergente")
        ventana.geometry("300x200")

        label = ttk.Label(ventana, text="¡Esto es una ventana emergente!")
        label.pack(pady=20)

        close_button = ttk.Button(ventana, text="Cerrar", command=ventana.destroy)
        close_button.pack()

    root = tk.Tk()
    root.title("Ventana Principal")

    open_popup_button = ttk.Button(root, text="Abrir Ventana Emergente", command=open_popup)
    open_popup_button.pack(pady=20)

    root.mainloop()



# tkinter.simpledialog: proporciona principalmente la función askstring() para crear cuadros de diálogo simples que permiten a
# los usuarios ingresar texto. No tiene métodos o atributos propios más allá de los argumentos que se pueden pasar a la función askstring().
# Aquí tienes una descripción de los parámetros admitidos por askstring():
#
# askstring(title, prompt, **kwargs):
#
#     title: El título del cuadro de diálogo.
#     prompt: El mensaje o la pregunta que se muestra al usuario.
#     **kwargs: Argumentos adicionales que se pueden utilizar para personalizar el cuadro de diálogo.
#
# askstring() devuelve la cadena de texto ingresada por el usuario. Si el usuario hace clic en "Aceptar",
# el valor ingresado se devuelve como resultado. Si el usuario cierra el cuadro de diálogo sin ingresar nada o hace clic en "Cancelar",
# el valor devuelto será None.
#
# Aparte de los parámetros mencionados, no existen métodos ni atributos adicionales en el módulo tkinter.simpledialog.
# El módulo se centra en proporcionar una forma rápida y sencilla de obtener texto del usuario.
def module_medialog():
    import tkinter as tk
    from tkinter import simpledialog

    def show_name():
        name = simpledialog.askstring("Nombre", "Por favor, ingresa tu nombre:")
        if name:
            label.config(text=f"Hola, {name}!")

    root = tk.Tk()
    root.title("Ejemplo de askstring")

    button = tk.Button(root, text="Ingresa tu nombre", command=show_name)
    button.pack()

    label = tk.Label(root, text="")
    label.pack()

    root.mainloop()