# MODULE NUMPY
 # Proporciona una estructura de datos de matriz multidimensional de alto rendimiento.
 # Numpy es el núcleo de muchas bibliotecas de ciencia de datos y aprendizaje automático populares, como SciPy, Pandas y Scikit-Learn.

# Métodos
    # array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0): crea una matriz a partir de una lista, una tupla o una secuencia de números.
    # zeros(shape, dtype=float, order='C'): crea una matriz de ceros.
    # ones(shape, dtype=None, order='C'): crea una matriz de unos.
    # full(): crea una matriz llena con un valor especificado.
    # linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None): crea una matriz de números espaciados uniformemente.
    # arange([start, ]stop, [step, ]dtype=None): crea una matriz de números secuenciales.
# Atributos
    # ndim: el número de dimensiones de la matriz.
    # shape: la forma de la matriz, como una tupla de enteros.
    # size: el número de elementos de la matriz.
    # dtype: el tipo de datos de la matriz.
# Parámetros
    # numpy.seterr(): establece las opciones de manejo de errores.
    # numpy.set_printoptions(): establece las opciones de impresión de matrices.
    # numpy.set_module(): establece la ruta al módulo NumPy.
    # object: El objeto iterable (como una lista o tupla) que se va a convertir en un arreglo NumPy.
    # dtype: El tipo de datos del arreglo (por ejemplo, int, float, complex, etc.).
    # shape: La forma del arreglo, especificada como una tupla de enteros que representan las dimensiones.
    # axis: El eje a lo largo del cual se realizarán las operaciones (por defecto, None para operaciones en todo el arreglo).
'EJEMPLO'
import numpy as np

# Crea una matriz de ceros de 3 x 2
matrix = np.zeros((3, 2))

# Imprime la matriz
print(matrix)



