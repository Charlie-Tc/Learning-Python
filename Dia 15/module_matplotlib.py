import matplotlib.pyplot as plt
import numpy as np

# Métodos para crear y personalizar gráficos:
def crear_personalizar_graficos() :
    # 1.- plt.figure(): Crea una nueva figura de gráfico.

    # Crear una figura
    plt.figure()

    # 2.- plt.plot(): Crea un gráfico de líneas.
    # Crear un gráfico de líneas
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Gráfico de Líneas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')

    # Mostrar el gráfico
    plt.show()

    # 3.- plt.scatter(): Crea un gráfico de dispersión.

    # Crear un gráfico de dispersión
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.scatter(x, y, c='blue', label='Puntos Aleatorios')
    plt.title('Gráfico de Dispersión')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

    # 4.- plt.bar(): Crea un gráfico de barras verticales.

    # Crear un gráfico de barras verticales
    x = ['A', 'B', 'C', 'D']
    y = [3, 7, 1, 5]
    plt.bar(x, y, color='green')
    plt.title('Gráfico de Barras Verticales')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')

    # Mostrar el gráfico
    plt.show()

    # 5.- plt.barh(): Crea un gráfico de barras horizontales.

    # Crear un gráfico de barras horizontales
    x = [3, 7, 1, 5]
    y = ['A', 'B', 'C', 'D']
    plt.barh(y, x, color='orange')
    plt.title('Gráfico de Barras Horizontales')
    plt.xlabel('Valores')
    plt.ylabel('Categorías')

    # Mostrar el gráfico
    plt.show()

    # 6.- plt.hist(): Crea un histograma.

    # Crear un histograma
    data = np.random.randn(1000)
    plt.hist(data, bins=20, color='purple', alpha=0.7)
    plt.title('Histograma')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')

    # Mostrar el gráfico
    plt.show()

    # 7.- plt.boxplot(): Crea un gráfico de caja y bigote.

    # Crear un gráfico de caja y bigote
    data = np.random.randn(100)
    plt.boxplot(data)
    plt.title('Gráfico de Caja y Bigote')

    # Mostrar el gráfico
    plt.show()

    # 8.- plt.pie(): Crea un gráfico de pastel.

    # Crear un gráfico de pastel
    sizes = [15, 30, 45, 10]
    labels = ['A', 'B', 'C', 'D']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'yellow'])
    plt.title('Gráfico de Pastel')

    # Mostrar el gráfico
    plt.show()

    # 9.- plt.imshow(): Muestra una imagen en una figura.
    plt.figure()

    # Mostrar una imagen
    img = plt.imread('imagen.png')
    plt.imshow(img)
    plt.title('Imagen')

    # Mostrar el gráfico
    plt.show()

    # 10.- plt.contour(): Crea un gráfico de contorno.

    # Crear un gráfico de contorno
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
    contours = plt.contour(X, Y, Z, colors='blue')
    plt.clabel(contours, inline=True, fontsize=8)
    plt.title('Gráfico de Contorno')

    # Mostrar el gráfico
    plt.show()


# Métodos para personalizar gráficos:
def personalizar_graficos():
    # Datos de ejemplo
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # Crear un gráfico de líneas
    plt.plot(x, y)

    # 1.- plt.title(): Agrega un título al gráfico.
    # Agregar un título al gráfico
    plt.title('Gráfico de Seno')

    # 2.- plt.xlabel(), plt.ylabel(): Etiqueta los ejes x e y.
    # Etiquetas de los ejes
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')

    # 3.- plt.legend(): Agrega una leyenda al gráfico.
    # Agregar una leyenda
    plt.legend(['Seno'])

    # 4.- plt.grid(): Muestra una cuadrícula en el gráfico.
    # Mostrar una cuadrícula
    plt.grid(True)

    # 5.- plt.xlim(), plt.ylim(): Establece los límites de los ejes.
    # Establecer límites en los ejes x e y
    plt.xlim(0, 2 * np.pi)
    plt.ylim(-1, 1)

    # 6.- plt.xticks(), plt.yticks(): Establece las marcas de los ejes.
    # Cambiar las marcas en los ejes x e y
    plt.xticks([0, np.pi, 2 * np.pi], ['0', '$\pi$', '2$\pi$'])
    plt.yticks([-1, 0, 1])

    # 7.- plt.tight_layout(): Ajusta automáticamente el espacio entre los elementos del gráfico.
    # Ajustar automáticamente el espacio entre los elementos del gráfico
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()



# Métodos para guardar y mostrar gráficos:
def guarda_y_mostrar_graficos():
    # 1.- plt.savefig(): Guarda el gráfico en un archivo.

    # Crear datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 12, 9]

    # Crear un gráfico de líneas
    plt.plot(x, y)

    # Guardar el gráfico en un archivo PNG
    plt.savefig('grafico.png')

    # Cierra la figura (opcional, pero recomendado)
    plt.close()

    # Ahora puedes abrir y mostrar el gráfico desde el archivo
    from PIL import Image
    img = Image.open('grafico.png')
    img.show()

    # 2.- plt.show(): Muestra el gráfico en la pantalla.

    # Crear datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 12, 9]

    # Crear un gráfico de barras
    plt.bar(x, y)

    # Mostrar el gráfico en la pantalla
    plt.show()

    # 3.- plt.close(): Cierra la figura del gráfico actual.

    # Crear datos de ejemplo
    x1 = [1, 2, 3]
    y1 = [10, 15, 7]

    x2 = [4, 5, 6]
    y2 = [8, 6, 11]

    # Crear dos gráficos de dispersión en la misma figura
    plt.figure()

    plt.subplot(1, 2, 1)
    plt.scatter(x1, y1)
    plt.title('Gráfico 1')

    plt.subplot(1, 2, 2)
    plt.scatter(x2, y2)
    plt.title('Gráfico 2')

    # Mostrar el primer gráfico
    plt.show()

    # Cerrar la figura actual
    plt.close()


# Métodos para personalizar colores y estilos:
def personalizar_colores_y_estilos():
    # 1.- plt.color(): Cambia el color de las líneas o puntos en un gráfico.

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Cambiar el color de la línea a rojo
    plt.plot(x, y, color='red', label='Seno(x)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    # 2.- plt.linestyle(): Cambia el estilo de línea en un gráfico.

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Cambiar el estilo de línea a guiones
    plt.plot(x, y, linestyle='--', label='Seno(x)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    # 3.- plt.marker(): Cambia el marcador en un gráfico de dispersión.

    x = np.linspace(0, 10, 30)
    y = np.sin(x)

    # Cambiar el marcador a círculos
    plt.scatter(x, y, marker='o', label='Puntos')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    # 4.- plt.fill_between(): Rellena el área entre dos curvas.

    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # Rellenar el área entre las curvas y=sen(x) e y=cos(x)
    plt.fill_between(x, y1, y2, color='lightblue', alpha=0.5, label='Relleno')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


# Métodos para gráficos 3D:
def metodos_para_graficos_3D():
    # 1.- plt.contourf(): Crea un gráfico de contorno lleno.

    # Crear datos de ejemplo
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

    # Crear un gráfico de contorno lleno
    plt.contourf(X, Y, Z, levels=20, cmap='viridis')

    # Agregar una barra de color para indicar los valores
    plt.colorbar()

    # Título y etiquetas de ejes
    plt.title('Gráfico de Contorno Lleno')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')

    plt.show()
    # Mostrar el gráfico

    # 2.- plt.plot_surface(): Crea una superficie 3D.

    # Crear datos de ejemplo
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

    # Crear un gráfico de superficie 3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis')

    # Agregar una barra de color para indicar los valores
    fig.colorbar(surf)

    # Título y etiquetas de ejes
    ax.set_title('Gráfico de Superficie 3D')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Mostrar el gráfico
    plt.show()



# Métodos para anotar y agregar texto:
def anotar_y_agregar_texto():
    # 1.- plt.annotate(): Agrega una anotación a un punto en el gráfico.

    # Datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 9]

    plt.plot(x, y, marker='o', linestyle='-', label='Datos')

    # Anotación en un punto específico
    plt.annotate('Punto importante', xy=(3, 5), xytext=(4, 8),
                 arrowprops=dict(arrowstyle='->', color='red'))

    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.title('Ejemplo de Anotación')
    plt.grid(True)
    plt.show()

    # 2.- plt.text(): Agrega texto en una posición específica del gráfico.

    # Datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 9]

    plt.plot(x, y, marker='o', linestyle='-', label='Datos')

    # Agregar texto en una posición específica
    plt.text(3, 8, 'Texto de ejemplo', fontsize=12, color='green')

    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.title('Ejemplo de Texto')
    plt.grid(True)
    plt.show()



# Métodos para trabajar con ejes logarítmicos:
def trabajar_con_ejes_logaritmicos():
    # 1.- plt.semilogx(): Crea un gráfico con escala logarítmica en el eje x.

    # Crear datos de ejemplo (exponenciales)
    x = np.linspace(1, 100, 100)
    y = np.exp(x)

    # Crear un gráfico con escala logarítmica en el eje x
    plt.semilogx(x, y, label='Exponencial')

    # Etiquetas de ejes y leyenda
    plt.xlabel('Eje X (log)')
    plt.ylabel('Eje Y')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

    # 2.- plt.semilogy(): Crea un gráfico con escala logarítmica en el eje y.

    # Crear datos de ejemplo (valores pequeños)
    x = np.linspace(1, 100, 100)
    y = 1 / x  # Valores pequeños

    # Crear un gráfico con escala logarítmica en el eje y
    plt.semilogy(x, y, label='Valores Pequeños')

    # Etiquetas de ejes y leyenda
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y (log)')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

    # 3.- plt.loglog(): Crea un gráfico con escala logarítmica en ambos ejes.

    # Crear datos de ejemplo (comportamiento exponencial)
    x = np.linspace(1, 100, 100)
    y = np.exp(x)

    # Crear un gráfico con escala logarítmica en ambos ejes
    plt.loglog(x, y, label='Exponencial')

    # Etiquetas de ejes y leyenda
    plt.xlabel('Eje X (log)')
    plt.ylabel('Eje Y (log)')
    plt.legend()

    # Mostrar el gráfico
    plt.show()



# Métodos para subgráficos:
def metodos_para_subgraficos():
    # 1.- plt.subplots(): Crea una matriz de subgráficos.

    # Crear una figura y una matriz de subgráficos de 2x2
    fig, axs = plt.subplots(2, 2)

    # Crear un gráfico en el primer subgráfico (arriba a la izquierda)
    axs[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3])
    axs[0, 0].set_title('Subgráfico 1')

    # Crear un gráfico en el segundo subgráfico (arriba a la derecha)
    axs[0, 1].bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5])
    axs[0, 1].set_title('Subgráfico 2')

    # Crear un gráfico en el tercer subgráfico (abajo a la izquierda)
    axs[1, 0].scatter([1, 2, 3, 4], [10, 5, 8, 2])
    axs[1, 0].set_title('Subgráfico 3')

    # Crear un gráfico en el cuarto subgráfico (abajo a la derecha)
    axs[1, 1].hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    axs[1, 1].set_title('Subgráfico 4')

    # Ajustar automáticamente los espacios entre subgráficos
    plt.tight_layout()

    # Mostrar la figura
    plt.show()

    # 2.- plt.subplot(): Selecciona un subgráfico específico en la matriz.

    # Crear un subgráfico 1x2 y seleccionar el primer subgráfico
    plt.subplot(1, 2, 1)
    plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
    plt.title('Subgráfico 1')

    # Cambiar al segundo subgráfico
    plt.subplot(1, 2, 2)
    plt.bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5])
    plt.title('Subgráfico 2')

    # Mostrar la figura
    plt.tight_layout()
    plt.show()


# Métodos para colormaps:
def metodos_para_colormaps():
    # plt.cm.: Colormaps predefinidos para personalizar colores en gráficos.

    # Crear datos de ejemplo
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Ejemplo 1: Usar el colormap 'viridis'
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, c=y, cmap='viridis', s=50)
    plt.colorbar(label='Valor de y')
    plt.title('Gráfico de dispersión con colormap "viridis"')
    plt.show()

    # Ejemplo 2: Usar el colormap 'cividis'
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, c=y, cmap='cividis', s=50)
    plt.colorbar(label='Valor de y')
    plt.title('Gráfico de dispersión con colormap "cividis"')
    plt.show()

    # Ejemplo 3: Usar el colormap 'plasma'
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, c=y, cmap='plasma', s=50)
    plt.colorbar(label='Valor de y')
    plt.title('Gráfico de dispersión con colormap "plasma"')
    plt.show()



def personalizar_el_aspecto_general():
    # Métodos para personalizar el aspecto general:
    # 1.- plt.style.use(): Aplica un estilo de gráfico predefinido.

    # Datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 3]

    # Aplicar un estilo de gráfico predefinido (por ejemplo, 'ggplot')
    plt.style.use('ggplot')

    # Crear un gráfico de líneas
    plt.plot(x, y)

    # Mostrar el gráfico
    plt.show()

    # 2.-  plt.rcParams(): Configura las opciones globales de estilo.

    # Configurar el tamaño de fuente global
    plt.rcParams['font.size'] = 12

    # Configurar el color de fondo global
    plt.rcParams['axes.facecolor'] = 'lightgray'

    # Datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 3]

    # Crear un gráfico de barras
    plt.bar(x, y)

    # Mostrar el gráfico
    plt.show()

# Métodos para crear y personalizar gráficos:
# Métodos para personalizar gráficos:
# Métodos para guardar y mostrar gráficos:
# Métodos para personalizar colores y estilos:
# Métodos para gráficos 3D:
# Métodos para anotar y agregar texto:
# Métodos para trabajar con ejes logarítmicos:
# Métodos para subgráficos:
# Métodos para colormaps:
# Métodos para personalizar el aspecto general:

