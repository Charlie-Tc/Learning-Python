import pandas as pd
import numpy as np
import pytz

def creacion_Df():

    # Métodos para la creación DataFrames y series:
    # 1.- pd.DataFrame(): Crea un DataFrame vacío.
    df = pd.DataFrame()
    print("DataFrame: ", df)

    # 2.- pd.Series(): Crea una Serie vacía.
    serie = pd.Series()
    print("Series: ", serie)

    # 3.- pd.read_csv(): Lee un archivo CSV y lo carga en un DataFrame.
    df = pd.read_csv('registro.csv')
    print("read_scv: ", df)

    # 4.- pd.read_excel(): Lee un archivo Excel y lo carga en un DataFrame.
    df = pd.read_excel('archivo.xlsx')
    print("read_excel: ", df)

    # 5.- pd.read_json(): Lee un archivo JSON y lo carga en un DataFrame.
    df = pd.read_json('contacts.json')
    print("read_json: ", df)


def inspeccion_Df():
    # Métodos para la inspeccion de DataFram y Series:
    # 1.- df.head(): Muestra las primeras filas del DataFrame.

    # Crear un DataFrame de ejemplo
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Edad': [25, 30, 35, 40, 45]}
    df = pd.DataFrame(data)

    # Mostrar las primeras 3 filas del DataFrame
    print("head: ", df.head(3))
    print("*"* 45)

    # 2.- df.tail(): Muestra las últimas filas del DataFrame.
    # Crear un DataFrame de ejemplo
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Edad': [25, 30, 35, 40, 45]}
    df = pd.DataFrame(data)

    # Mostrar las últimas 2 filas del DataFrame
    print("tail: ", df.tail(2))
    print("*" * 45)

    # 3.- df.info(): Proporciona información sobre el DataFrame.
    # Crear un DataFrame de ejemplo
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Edad': [25, 30, None, 40, 45]}
    df = pd.DataFrame(data)

    # Mostrar información detallada del DataFrame
    df.info()
    print("*" * 45)

    # 4.- df.describe(): Calcula estadísticas descriptivas del DataFrame.
    # Crear un DataFrame de ejemplo
    data = {'Edad': [25, 30, 35, 40, 45]}
    df = pd.DataFrame(data)

    # Calcular estadísticas descriptivas
    print("describe: ", df.describe())


def filtrado_datos():
    # Métodos para la selección y filtrado de datos.

    data = {'Nombre': ['Ana', 'Carlos', 'Luis', 'Sofía'],
            'Edad': [25, 30, 22, 28],
            'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}

    df = pd.DataFrame(data)
    print("*" * 45)

    # 1.- df['columna']: Selecciona una columna específica por nombre.
    nombres = df['Nombre']
    print("columna: ", nombres)
    print("*" * 45)

    # 2.- df.loc[]: Acceso basado en etiquetas.
    fila = df.loc[1]
    print("loc: ", fila)
    print("*" * 45)

    # 3.- df.iloc[]: Acceso basado en índices enteros.
    fila = df.iloc[2]
    print("iloc: ", fila)
    print("*" * 45)

    # 4.- df.query(): Filtra filas que cumplan con una condición.
    resultado = df.query('Edad > 25')
    print("query: ", resultado)
    print("*" * 45)

    # 5.- df[(condición)]: Filtra filas basado en una condición booleana.
    mayores_de_25 = df[df['Edad'] > 25]
    print("condición: ", mayores_de_25)


def manipulacion_deDatos():
    # Métodos para la manipulación de datos.
    # 1.- df.drop(): Elimina filas o columnas.
    # Crear un DataFrame de ejemplo
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)

    # Eliminar la columna 'B'
    df = df.drop('B', axis=1)

    print(df)

    # 2.- df.rename(): Cambia el nombre de columnas.
    # Crear un DataFrame de ejemplo
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)

    # Cambiar el nombre de la columna 'A' a 'X'
    df = df.rename(columns={'A': 'X'})

    print(df)

    # 3.- df.sort_values(): Ordena el DataFrame por valores de una o más columnas.
    # Crear un DataFrame de ejemplo
    data = {'A': [3, 1, 2], 'B': [6, 4, 5]}
    df = pd.DataFrame(data)

    # Ordenar el DataFrame por la columna 'A'
    df = df.sort_values(by='A')

    print(df)

    # 4.- df.groupby(): Agrupa datos por una o más columnas.
    # Crear un DataFrame de ejemplo
    data = {'A': ['foo', 'foo', 'bar', 'bar'], 'B': [1, 2, 3, 4]}
    df = pd.DataFrame(data)

    # Agrupar por la columna 'A' y calcular la suma
    grouped = df.groupby('A')['B'].sum()

    print(grouped)

    # 5.- df.pivot_table(): Crea una tabla pivote.
    # Crear un DataFrame de ejemplo
    data = {'A': ['foo', 'foo', 'bar', 'bar'],
            'B': ['one', 'one', 'one', 'two'],
            'C': [1, 2, 3, 4]}

    df = pd.DataFrame(data)

    # Crear una tabla pivote
    pivot = df.pivot_table(values='C', index='A', columns='B', aggfunc='sum')

    print(pivot)

    # 6.- df.melt(): Derrite el DataFrame de ancho a largo.


def calculos_yestadisticas():
    # Métodos para cálculos y estadísticas:
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
            'Edad': [25, 30, 22, 35],
            'Puntuación': [85, 92, 78, 88]}

    df = pd.DataFrame(data)


    # 1.- df.mean(): Calcula la media de las columnas numéricas.
    # Calcula la media de la columna 'Edad'
    media_edad = df['Edad'].mean()
    print("Media de Edades:", media_edad)

    # Calcula la media de la columna 'Puntuación'
    media_puntuacion = df['Puntuación'].mean()
    print("Media de Puntuaciones:", media_puntuacion)
    print("*" * 45)

    # 2.- df.sum(): Calcula la suma de las columnas numéricas.
    # Calcula la suma de la columna 'Edad'
    suma_edad = df['Edad'].sum()
    print("Suma de Edades:", suma_edad)

    # Calcula la suma de la columna 'Puntuación'
    suma_puntuacion = df['Puntuación'].sum()
    print("Suma de Puntuaciones:", suma_puntuacion)
    print("*" * 45)

    # 3.- df.min(), df.max(): Encuentra el valor mínimo y máximo.
    # Encuentra el valor mínimo en la columna 'Edad'
    minima_edad = df['Edad'].min()
    print("Edad Mínima:", minima_edad)

    # Encuentra el valor mínimo en la columna 'Puntuación'
    minima_puntuacion = df['Puntuación'].min()
    print("Puntuación Mínima:", minima_puntuacion)
    print("*" * 45)

    # 4.- df.count(): Cuenta valores no nulos en cada columna.
    # Cuenta el número de elementos no nulos en la columna 'Edad'
    conteo_edad = df['Edad'].count()
    print("Número de Edades no Nulas:", conteo_edad)

    # Cuenta el número de elementos no nulos en la columna 'Puntuación'
    conteo_puntuacion = df['Puntuación'].count()
    print("Número de Puntuaciones no Nulas:", conteo_puntuacion)
    print("*" * 45)


def visualizacion_deDatos():
    # Métodos para la visualización de Datos:
    import numpy as np
    import matplotlib.pyplot as plt

    # Creemos un DataFrame de ejemplo
    data = {'A': np.random.rand(100),
            'B': np.random.rand(100),
            'C': np.random.rand(100)}
    df = pd.DataFrame(data)


    # 1.- df.plot(): Crea gráficos a partir de los datos en el DataFrame.
    df.plot(x='A', y='B', kind='scatter')
    plt.title('Gráfico de dispersión')
    plt.show()
    print("*" * 45)

    # 2.- df.hist(): Crea histogramas.
    df['A'].hist(bins=20, color='skyblue', edgecolor='black')
    plt.title('Histograma de la columna A')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.show()
    print("*" * 45)

    # 3.- df.boxplot(): Crea gráficos de caja y bigote.
    df.boxplot(column=['A', 'B', 'C'])
    plt.title('Gráfico de caja y bigote')
    plt.ylabel('Valores')
    plt.show()
    print("*" * 45)

    # 4.- df.scatter_matrix(): Crea una matriz de gráficos de dispersión.
    from pandas.plotting import scatter_matrix
    scatter_matrix(df, alpha=0.5, figsize=(8, 8), diagonal='hist')
    plt.suptitle('Matriz de gráficos de dispersión')
    plt.show()


def manipulacion_fechasTiempos():
    # Método para la manipulación de fechas y tiempos(para columnas tipo datetime.):
    # pd.to_datetime(): Convierte una columna en un formato de fecha y hora.
    # Crear un DataFrame de ejemplo
    data = {'Fecha': ['2023-09-01', '2023-09-02', '2023-09-03']}
    df = pd.DataFrame(data)

    # Convertir la columna 'Fecha' a tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    # Verificar el tipo de datos después de la conversión
    print(df.dtypes)

    # df.dt.year, df.dt.month, etc.: Accede a componentes de fecha y hora.
    # Crear un DataFrame de ejemplo con una columna datetime
    data = {'Fecha': ['2023-09-01', '2023-09-02', '2023-09-03']}
    df = pd.DataFrame(data)
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    # Obtener el año de la columna 'Fecha'
    df['Año'] = df['Fecha'].dt.year

    # Mostrar el DataFrame resultante
    print(df)

    # Crear un DataFrame de ejemplo con una columna datetime
    data = {'Fecha': ['2023-09-01', '2023-10-02', '2023-11-03']}
    df = pd.DataFrame(data)
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    # Obtener el mes de la columna 'Fecha'
    df['Mes'] = df['Fecha'].dt.month

    # Mostrar el DataFrame resultante
    print(df)



def fusion_concatenacionDf():
    # Métodos para fusión y concatenación de DataFrames:
    # 1.-  pd.concat(): Combina DataFrames vertical u horizontalmente.
    # Crear dos DataFrames
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                        'B': ['B0', 'B1', 'B2']})

    df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                        'B': ['B3', 'B4', 'B5']})

    # Concatenar verticalmente (a lo largo de las filas)
    result = pd.concat([df1, df2])

    print(result)

    # Crear dos DataFrames
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                        'B': ['B0', 'B1', 'B2']})

    df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                        'D': ['D0', 'D1', 'D2']})

    # Concatenar horizontalmente (a lo largo de las columnas)
    result = pd.concat([df1, df2], axis=1)

    print(result)
    print("*" * 45)

    # 2.- pd.merge(): Realiza operaciones de combinación similar a SQL.
    # Crear dos DataFrames
    df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                        'value1': [1, 2, 3, 4]})

    df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                        'value2': [5, 6, 7, 8]})

    # Realizar una combinación (merge) basada en la columna 'key'
    result = pd.merge(df1, df2, on='key', how='inner')

    print(result)


def manipulacion_valoreNull():
    import numpy as np

    # Métodos para la manipulación de valores nulos:
    # 1.- df.dropna(): Elimina filas con valores nulos.

    # Crear un DataFrame de ejemplo con valores nulos
    data = {'A': [1, 2, np.nan, 4],
            'B': [np.nan, 2, 3, 4],
            'C': [1, 2, 3, 4]}
    df = pd.DataFrame(data)

    # Mostrar el DataFrame original
    print("DataFrame original:")
    print(df)

    # Eliminar filas con al menos un valor nulo
    df_sin_nulos = df.dropna()

    # Mostrar el DataFrame resultante
    print("\nDataFrame sin filas nulas:")
    print(df_sin_nulos)
    print("*" * 45)

    # 2.- df.fillna(): Rellena valores nulos con un valor específico.

    # Crear un DataFrame de ejemplo con valores nulos
    data = {'A': [1, 2, np.nan, 4],
            'B': [np.nan, 2, 3, 4],
            'C': [1, 2, 3, np.nan]}
    df = pd.DataFrame(data)

    # Mostrar el DataFrame original
    print("DataFrame original:")
    print(df)

    # Rellenar los valores nulos con ceros
    df_con_ceros = df.fillna(0)

    # Mostrar el DataFrame resultante
    print("\nDataFrame con valores nulos reemplazados por ceros:")
    print(df_con_ceros)


def save_Df_files():
    # Métodos para guardar DataFrame en archivos:
    # 1.- df.to_csv(): Guarda el DataFrame en un archivo CSV.
    # Crear un DataFrame de ejemplo
    data = {'Nombre': ['Juan', 'María', 'Pedro'],
            'Edad': [25, 30, 35],
            'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}

    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv('mi_archivo.csv', index=False)

    # 2.- df.to_excel(): Guarda el DataFrame en un archivo Excel.
    # Crear un DataFrame de ejemplo
    data = {'Nombre': ['Juan', 'María', 'Pedro'],
            'Edad': [25, 30, 35],
            'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}

    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo Excel
    nombre_archivo = 'mi_archivo_excel.xlsx'
    df.to_excel(nombre_archivo, index=False, sheet_name='Hoja1')


def others_methods():

    # f.apply(): Aplica una función a lo largo de un eje del DataFrame.
    data = {'Numbers': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)

    # Definimos una función personalizada para calcular el cuadrado
    def calcular_cuadrado(numero):
        return numero ** 2

    # Aplicamos la función a la columna 'Numbers' usando apply
    df['Cuadrado'] = df['Numbers'].apply(calcular_cuadrado)

    print(df)

    # df.isnull(), df.notnull(): Verifica valores nulos o no nulos.
    import numpy as np

    data = {'A': [1, 2, np.nan, 4, 5],
            'B': [np.nan, 2, 3, np.nan, 5]}
    df = pd.DataFrame(data)

    # Verificamos si hay valores nulos en el DataFrame
    valores_nulos = df.isnull()

    print(valores_nulos)


def ejamples():
    fecha_inicio = '2023-01-01'
    fechas = pd.date_range(start=fecha_inicio, periods=30, freq='D')

    datos = np.arange(30)
    serie_diaria = pd.Series(datos, index=fechas)
    serie_mensual = serie_diaria.resample('M').mean()

    #print(serie_mensual)

    fecha = pd.date_range(start=fecha_inicio, periods=5)
    serie_sin_tz = pd.Series([1, 2, 3, 4, 5], index=fecha)
    serie_sin_tz.tz_localize('US/Eastern')
    #print(serie_sin_tz)

    fechita = pd.date_range(start=fecha_inicio, periods=5, tz='US/Eastern')
    serie_us_eastern = pd.Series([1, 2, 3, 4, 5], index=fechita)
    serie_london = serie_us_eastern.tz_convert('Europe/London')
    #print(serie_london)

    '''for tz in pytz.all_timezones:
        print(tz)'''

    # perido mensual
    periodo_mensual = pd.Period('2023-09', freq='M')
    # periodo anual
    periodo_anual = pd.Period('2023', freq='A')
    # periodo diario
    periodo_diario = pd.Period('2023-09-26', freq='D')
    #print("periodo mensual: ",periodo_mensual)
    #print("periodo anual: ", periodo_anual)
    #print("periodo diario: ",periodo_diario)

    from datetime import timedelta, datetime
    timestam = pd.Timestamp(datetime.now())
    #print(datetime)
    tm_delta = timedelta(days=7, minutes=5)
    #print(tm_delta)
    new_date = timestam + tm_delta
    #print(new_date)

    # crear un DataFrame
    my_friends = {"names": ["Liz", "Sandra Ma", "Gloria"],
                  "ages": [23, 34, 32],
                  "city": ["Buenos Aires", "Shagai", "Kamsan"]
                  }
    df_friend = pd.DataFrame(my_friends)
    #print(df_friend)

    other_list = [{"name": "Charly", "age": 23, "city": "Cusco"},
                  {"name": "Carlos", "age": 21, "city": "Lim"},
                  {"name": "Caleb", "age": 28, "city": "Ica"}]
    df_other_list = pd.DataFrame(other_list)
    #print(df_other_list.columns)

    # cargar un archivo csv
    file_csv = pd.read_csv("most24hour.csv")

    # imprime todas las columnas
    #print(file_csv.columns)

    # imprime las 5 primeras valores de la columna especificado
    #print(file_csv["Likes"].head(5))

    columnas_enteras = file_csv.select_dtypes(include="Float64")

    # imprime las valores enteras del dicho DataFrame
    #print(columnas_enteras)

    # crear una nueva columna
    file_csv["time"] = "23min"

    # crear una nueva columna en other_list
    df_other_list["Profession"] = ["None", "Comunity Manager", "Mechanic"]
    #print(df_other_list)

    # eliminar una columna
    remove_column_time = file_csv.drop("time", axis=1)
    #print(remove_column_time)

    # imprime una columna que cumpla con cierta condición
    column_v = file_csv.loc[:, file_csv.columns.str.startswith('V')]
    print(column_v)



