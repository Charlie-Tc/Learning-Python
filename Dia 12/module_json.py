import json

# JSON: Es un formato ligero para el intercambio de datos que es facilmente legible tanto como para humanos como para máquinas.
     # 1.- json.dumps(): Esta función toma un objeto Python y lo convierte en una cadena JSON (serialización).
        # Puedes pasarle varios argumentos para personalizar la salida, como indent para la indentación y separators para definir los separadores entre elementos.

     # 2.- json.dump(): Similar a dumps(), pero en lugar de devolver una cadena, esta función escribe el JSON en un archivo.

     # 3.- json.loads(): Esta función toma una cadena JSON y la convierte en un objeto Python (deserialización).

     # 4.- json.load(): Similar a loads(), pero en lugar de tomar una cadena, esta función carga el JSON desde un archivo.

     # 5.- json.JSONEncoder: Esta es una clase que se utiliza para personalizar la codificación de objetos en JSON.
        # Puedes heredar de ella y modificar su comportamiento para adaptarlo a tus necesidades.

     # 6.- json.JSONDecoder: Similar a JSONEncoder, esta clase te permite personalizar la decodificación de JSON en objetos Python.

     # 7.- Control de Tipos: La función json.dumps() admite un argumento llamado default que puede ser una funcón que
        # ayuda a serializar objetos personalizados que no son nativos de JSON.

     # 8.- json.JSONDecodeError: Una excepción que se levanta cuando hay un error al decodificar una cadena JSON.

# dumps()

# Crear un diccionario
data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ejemploville"
}

# Convertir el diccionario a JSON
json_data = json.dumps(data, indent=4)
print("JSON generado:")
print(json_data)

# Convertir el JSON de vuelta a un diccionario
parsed_data = json.loads(json_data)
print("\nDiccionario resultante:")
print(parsed_data)



# dump()
contact =  {
    "name": 'Liz',
    "age": 18,
    "Nro tlf": 987265789,
    "city": 'Taiwan',
    "email": 'love_liz@mail.tw'
}

# crea un archivo Json con el objeto contact
with open("contact.json", 'w') as archivo:
    json.dump(contact, archivo)

# leer el archivo JSON y convertirlo en en diccionario
with open("contact.json", "r") as leer_archivo:
    letter = json.load(leer_archivo)
    print("Resultado de la conversion de archivo JSON: ",letter)


# JSONEncoder()
class MiEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

data = {
    "nombres": {"Juan", "María", "Carlos"},
    "edad": 23
}

json_data = json.dumps(data, indent=4, cls=MiEncoder)
print(json_data)

