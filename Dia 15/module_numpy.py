import numpy as np

# MODULE NUMPY
 # Proporciona una estructura de datos de matriz multidimensional de alto rendimiento.
 # Numpy es el núcleo de muchas bibliotecas de ciencia de datos y aprendizaje automático populares, como SciPy, Pandas y Scikit-Learn.

# Métodos

# 1 Creación de Arreglos:

# 1.1.- numpy.array(): Crea un arreglo NumPy a partir de una lista u otro secuencia.
def method_array():
    lista = [1, 2, 3, 4, 5]
    arreglo = np.array(lista)

    print(arreglo)


# 1.2.- numpy.zeros(): Crea un arreglo NumPy lleno de ceros.
def method_zeros():

    ceros = np.zeros(5)  # Crea un arreglo de 5 elementos con ceros

    print(ceros)


# 1.3.- numpy.ones(): Crea un arreglo NumPy lleno de unos.
def method_ones():

    unos = np.ones(4)  # Crea un arreglo de 4 elementos con unos

    print(unos)


# 1.4.- numpy.empty(): Crea un arreglo vacio sin inicializar.
def method_empty():

    vacio = np.empty(3)  # Crea un arreglo de 3 elementos vacío

    print(vacio)


# 1.5.- numpy.arange(): Crea un arreglo con valores espaciados uniformemente.
def method_arange():

    rango = np.arange(0, 10, 2)  # Crea un arreglo con valores del 0 al 10, con paso 2

    print(rango)


# 1.6.- numpy.linspace(): Crea un arreglo con valores igualmente espaciados en un rango especificado.
def method_linspace():

    lineal = np.linspace(0, 1, 5)  # Crea un arreglo con 5 valores entre 0 y 1

    print(lineal)


# 1.7.- numpy.logspace(start, stop, num): Crea un arreglo con valores logarítmicamente espaciados en un rango especificado.
def method_logspace():

    logaritmico = np.logspace(0, 2, 5)  # Crea un arreglo con 5 valores espaciados logarítmicamente entre 10^0 y 10^2

    print(logaritmico)
    print(np.__version__)


# 1.8.- numpy.eye(): Crea una matriz identidad.
def method_eye():

    identidad = np.eye(3)  # Crea una matriz identidad de 3x3

    print(identidad)


# 1.9.- numpy.random.rand(): Crea un arreglo de números aleatorios entre o y 1.
def method_random_rand():

    aleatorios = np.random.rand(4)  # Crea un arreglo de 4 elementos con valores aleatorios entre 0 y 1

    print(aleatorios)


# 2 Operaciones con Arreglos:

# 2.1.- ndarray.shape: Devuelve la forma del arreglo.
def method_shape():

    # Crear un arreglo NumPy de ejemplo
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    # Obtener la forma (shape) del arreglo
    shape = np.shape(arr)

    # Imprimir la forma
    print("Forma del arreglo:", shape)


# 2.2.- ndarray.reshape(): Cambia la forma del arreglo.
def method_reshape():

    # Crear un arreglo NumPy de ejemplo
    arr = np.array([1, 2, 3, 4, 5, 6])

    # Cambiar la forma del arreglo a una matriz 2x3
    reshaped_arr = np.reshape(arr, (2, 3))

    # Imprimir el arreglo con la nueva forma
    print("Arreglo reorganizado:")
    print(reshaped_arr)


# 2.3.- ndarray.size: Devuelve el número total de elementos.
def method_size():

    arr = np.array([[1, 2, 3], [4, 5, 6]])
    size = arr.size
    print(size)  # Salida: 6


# 2.4.- ndarray.dtype: Devuelve el tipo de datos de los elementos.
def method_dtype():

    arr = np.array([1, 2, 3])
    dtype = arr.dtype
    print(dtype)  # Salida: int64


# 2.5.- numpy.concatenate(): Concatena arreglos a lo largo de un eje.
def method_concatenate():

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    concatenated = np.concatenate((arr1, arr2))
    print(concatenated)


# 2.6.- numpy.vstack(): Apila arreglos verticalmente.
def method_vstack():

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    stacked = np.vstack((arr1, arr2))
    print(stacked)


# 2.7.- numpy.hstack(): Apila arreglos horizontalmente.
def method_hstack():

    arr1 = np.array([1, 2])
    arr2 = np.array([3, 4])
    stacked = np.hstack((arr1, arr2))
    print(stacked)


# 2.7.- numpy.itemsize(): Devuelve el tamaño en bytes de cada elemento en el arreglo.
def method_itemsize():

    arr = np.array([5, 4, 3], dtype=np.float64)
    itemsize = arr.itemsize
    print(itemsize)  # Salida: 8 (en bytes)



# 3 Operaciones Matemáticas:
#
# 3.1.- numpy.add(): Suma de elementos.
def method_npadd():

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    suma = np.add(arr1, arr2)
    print("Suma de elementos:", suma)


# 3.2.- numpy.subtract(): Resta de elementos.
def method_npsubtract():

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    resta = np.subtract(arr1, arr2)
    print("Resta de elementos:", resta)


# 3.3.- numpy.multiply(): Multiplicación de elementos.
def method_npmultiply():

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    multiplicacion = np.multiply(arr1, arr2)
    print("Multiplicación de elementos:", multiplicacion)


# 3.4.- numpy.divide(): División de elementos.
def method_npdivide():

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    division = np.divide(arr1, arr2)
    print("División de elementos:", division)


# 3.5.- numpy.dot(): Producto escalar o producto punto.
def method_npdot():

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    producto_punto = np.dot(arr1, arr2)
    print("Producto punto:", producto_punto) # (1*4) + (2*5) + (3*6) = 32


# 3.6.- numpy.transpose(): Transpone el arreglo.
def method_nptranspose():

    matriz = np.array([[1, 2], [3, 4]])
    transpuesta = np.transpose(matriz)
    print("Matriz original:")
    print(matriz)
    print("Matriz transpuesta:")
    print(transpuesta)


# 3.7.- numpy.sum(): Suma de elementos en el arreglo.
def method_npsum():

    arr1 = np.array([1, 2, 3])
    suma_total = np.sum(arr1)
    print("Suma total de elementos en arr1:", suma_total)


# 4 Funciones Matemáticas
#
# 4.1.- numpy.exp(): Calcula la exponencial.
def method_npexp():

    arr = np.array([2, 3, 4])
    exponenciacion = np.exp(arr)
    print("Exponenciación de los elementos:", exponenciacion)


# 4.2.- numpy.log(): Calcula el logaritmo natural.
def method_nplog():

    arr = np.array([1, 2, 4])
    logaritmo_natural = np.log(arr)
    print("Logaritmo natural de los elementos:", logaritmo_natural)


# 4.3.- numpy.sqrt(): Calcula la raíz cuadrada.
def method_npsqrt():

    arr = np.array([9, 16, 25])
    raiz_cuadrada = np.sqrt(arr)
    print("Raíz cuadrada de los elementos:", raiz_cuadrada)


# 4.4.- numpy.sin(), numpy.cos(), numpy.tan(): Funciones trigonométricas.
def method_npsin():
    import matplotlib.pyplot as plt

    x = np.linspace(0, 2 * np.pi, 100)
    seno = np.sin(x)

    plt.plot(x, seno)
    plt.title("Gráfico de la función seno")
    plt.xlabel("Ángulo (radianes)")
    plt.ylabel("Valor del seno")
    plt.grid(True)
    plt.show()


# 5 Estadísticas
#
# 5.1.- numpy.mean(): Calcula la media.
def method_npmean():

    arr = np.array([1, 2, 3, 4, 5])
    promedio = np.mean(arr)
    print("Promedio:", promedio)


# 5.2.- numpy.median(): Calcula la mediana.
def method_npmedian():

    arr = np.array([1, 2, 3, 4, 5])
    mediana = np.median(arr)
    print("Mediana:", mediana)


# 5.3.- numpy.std(): Calcula la desviación estándar.
def method_npstd():

    arr = np.array([1, 2, 3, 4, 5])
    desviacion_estandar = np.std(arr)
    print("Desviación Estándar:", desviacion_estandar)


# 5.4.- numpy.var(): Calcula la varianza.
def method_npvar():

    arr = np.array([1, 2, 3, 4, 5])
    varianza = np.var(arr)
    print("Varianza:", varianza) # (1 + 2 + 3 + 4 + 5)/5 = 3 ➡ ((1-3)² + (2-3)² + (3-3)² + (4-3)²  + (5-3)²  ➡ 10/5 = 2


# 5.5.- numpy.percentile(): se utiliza para calcular los percentiles de un arreglo NumPy.
def method_percentile():

    arr = np.array([1, 2, 3, 4, 5])
    percentil_75 = np.percentile(arr, 75)
    print("Percentil 75:", percentil_75)



# 6 Selección y Filtrado:
#
# 6.1.- numpy.argmax(): Devuelve el índice del valor máximo.
def method_npargmax():

    arr = np.array([1, 4, 2, 7, 5])
    indice_max = np.argmax(arr)
    print("Índice del máximo valor:", indice_max)


# 6.2.- numpy.argmin(): Devuelve el índice del valor mínimo.
def method_npargmin():

    arr = np.array([1, 4, 2, 0, 5])
    indice_min = np.argmin(arr)
    print("Índice del mínimo valor:", indice_min)


# 6.3.- numpy.where(): Devuelve índices donde se cumple una condición.
def method_npwhere():

    arr = np.array([1, 2, 3, 4, 5])
    condicion = arr > 2
    indices = np.where(condicion)
    print("Índices donde la condición es verdadera:", indices)


# 6.4.- numpy.extract(): Extrae elementos que cumplen una condición.
def method_npextract():

    arr = np.array([1, 2, 3, 4, 5])
    condicion = arr > 2
    elementos_cumplen = np.extract(condicion, arr)
    print("Elementos que cumplen la condición:", elementos_cumplen)


# 7 Entrada y Salida de Datos
#
# 7.1.- numpy.load(): Carga datos desde un archivo.
def method_npload():

    loaded_arr = np.load('mi_arreglo.npy')
    print(loaded_arr)


# 7.2.- numpy.save(): Guarda datos en un archivo.
def method_npsave():

    arr = np.array([1, 2, 3, 4, 5])
    np.save('mi_arreglo.npy', arr)


# 7.3.- numpy.savetxt(): Guardar un arreglo NumPy en formato CSV.
def method_savetxt():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    np.savetxt('mi_archivo.csv', data, delimiter=',')


# 7.4.- numpy.loadtxt(): Cargar datos desde un archivo CSV en un arreglo NumPy.
def method_loadtext():

    loaded_data = np.loadtxt('mi_archivo.csv', delimiter=',')
    print(loaded_data)


# 7.5.- numpy.fromfile(): Leer datos desde un archivo binario en un arreglo NumPy.
def method_fromfile():

    loaded_data = np.fromfile('datos_binarios.dat', dtype=float)
    print(loaded_data)


# 7.6.- numpy.tofile(): Guardar un arreglo NumPy en un archivo binario.
def method_tofile():

    data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    data.tofile('datos_binarios.dat')


# 8 Álgebra Lineal:
#
# numpy.linalg.inv(): Calcula la matriz inversa.
def method_linalg_inv():

    # Crear una matriz
    A = np.array([[3, 1], [1, 2]])

    # Calcular la matriz inversa
    A_inv = np.linalg.inv(A)

    print("Matriz Original:")
    print(A)

    print("Matriz Inversa:")
    print(A_inv)


# numpy.linalg.det(): Calcula el determinante de una matriz.
def method_linalg_det():

    # Crear una matriz
    B = np.array([[4, 7], [2, 6]])

    # Calcular el determinante
    det_B = np.linalg.det(B)

    print("Matriz:")
    print(B)

    print("Determinante:", det_B)


# numpy.linalg.eig(): Calcula los valores y vectores propios.
def method_linalg_eig():

    # Crear una matriz
    C = np.array([[1, 2], [2, 4]])

    # Calcular valores y vectores propios
    eigenvalues, eigenvectors = np.linalg.eig(C)

    print("Matriz:")
    print(C)

    print("Valores Propios:")
    print(eigenvalues)

    print("Vectores Propios:")
    print(eigenvectors)


# 9 Funciones de Conjuntos:
#
# 9.1.- numpy.intersect1d(): Encuentra la intersección de dos arreglos.
def method_intersect1d():

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([3, 4, 5, 6, 7])

    intersection = np.intersect1d(arr1, arr2)
    print(intersection)  # Output: [3 4 5]


# 9.2.- numpy.union1d(): Encuentra la unión de dos arreglos.
def method_nploadunion1d():

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([3, 4, 5, 6, 7])

    union = np.union1d(arr1, arr2)
    print(union)  # Output: [1 2 3 4 5 6 7]


# 9.3.- numpy.setdiff1d(): Encuentra la diferencia entre dos arreglos.
def method_setdiff1d():

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([3, 4, 5, 6, 7])

    difference = np.setdiff1d(arr1, arr2)
    print(difference)  # Output: [1 2]


# 10 Otras Funciones:
#
# 10.1.- numpy.sort(): Ordena los elementos del arreglo.
def method_npsort():

    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    arr.sort()
    print(arr)


# 10.2.- numpy.unique(): Devuelve los valores únicos en el arreglo.
def method_unique():

    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    unique_values = np.unique(arr)
    print(unique_values)


# 10.3.- numpy.clip(): Limita los valores en el arreglo a un rango específico.
def method_clip():

    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    clipped_arr = np.clip(arr, a_min=2, a_max=6)
    print(clipped_arr)


# 10.4.- numpy.argmax(), numpy.argmin(): Encuentra los índices de los valores máximos y mínimos.
def method_arg_maxmin():

    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    max_value = np.max(arr)
    min_value = np.min(arr)
    print("Máximo:", max_value)
    print("Mínimo:", min_value)



array_num_int = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array_num_float = np.array([0.2,0.23,0.545,0.13,0.643])
array_ones = np.ones(15)
array_res = np.reshape(array_ones, (5, 3))

nums = np.array([1, 2, 3, 4, 5])
nums2 = np.array([5, 4, 3, 2, 1])
add_arrays = np.add(nums, nums2)
subtract_arrays = np.subtract(nums, nums2)
multi_arrays = np.multiply(nums, nums2)
sum_arrays = np.sum(nums2)


