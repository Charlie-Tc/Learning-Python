import webbrowser

# MODULO WEB_BROWSER
# Permite abrir URLs, buscar en la web y realizar acciones en navegadores instalados en el sistema.

# Métodos principales:
    # open(url, new=0, autoraise=True): Abre la URL especificada en el navegador predeterminado.
    # open_new(url): Abre la URL en una nueva ventana del navegador.
    # open_new_tab(url): Abre la URL en una nueva pestaña del navegador.
    # get(using=None): Devuelve un objeto de navegador web que se puede usar para controlar el navegador en una sesión posterior.

# Atributos principales:
    # webbrowser.Browser: Clase base que representa un navegador web. Puede ser utilizada para crear objetos de navegador personalizados.

# Parámetros comunes:
    # url: La URL que deseas abrir en el navegador.
    # new: Un valor que indica cómo se debe abrir la URL. Puede ser 0 para la misma ventana, 1 para una nueva ventana y 2 para una nueva pestaña.
    # autoraise: Si es True, intenta traer la ventana del navegador a primer plano.

# Clases:
    # webbrowser.Browser: Clase base que puede ser subclasificada para crear objetos de navegador personalizados.
    # No se utilizan comúnmente directamente.

def ejemplo():
    url = "www.youtube.com"

    abrir_url = webbrowser.open(url, new=2, autoraise=False)
    print(abrir_url)
ejemplo()