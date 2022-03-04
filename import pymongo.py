import certifi
import pymongo


from sensores import sensores # La clase Producto

from bson.objectid import ObjectId # Para crear ObjectId, porque _ID como cadena no funciona


def obtener_bd():
    
    base_de_datos = "Sensores"
    client = pymongo.MongoClient('mongodb+srv://zairdeltamx:ZAIR@sandbox.dcgxy.mongodb.net/Sensores?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    return client[base_de_datos]



def insertar(dato):
    base_de_datos = obtener_bd()
    datos = base_de_datos.datos
    return datos.insert_one({
        "Temperatura": dato.Temperatura,
        "Humedad": dato.Humedad,
        }).inserted_id

def obtener():
    base_de_datos = obtener_bd()
    return base_de_datos.datos.find()

def actualizar(id, dato):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.datos.update_one(
        {
        '_ID': ObjectId(id)
        }, 
        {
            '$set': {
                "temperatura": dato.Temperatura,
                "humedad": dato.Humedad,
            }
        })
    return resultado.modified_count

def eliminar(id):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.datos.delete_one(
        {
        '_ID': ObjectId(id)
        })
    return resultado.deleted_count




menu = """ PROGRAMA DE CRUD MONGODB
1 - INSERTAR DATO
2 - VER DATOS
3 - ACTTUALIZAR DATO
4 - ELIMINAR DATO
5 - DALIR
------------"""
opc = None

while opc is not 5:
    print(menu)
    opc = int(input("Elige: "))
    if opc is 1:
        print("Insertar")
        Temperatura = float(input("Temperatura del sensor: "))
        Humedad = float(input("Huemdad del sensor: "))
        dato = sensores(Temperatura, Humedad)
        id = insertar(dato)
        print("-----------------------------")
        print("El id del dato insertado es: ", id)
        print("-----------------------------")
    elif opc is 2:
        print("Obteniendo datos...")
        for dato in obtener():
            print("-----------------------------")
            print("Id: ", dato["_ID"])
            print("temperatura: ", dato["Temperatura"])
            print("humedad: ", dato["Humedad"])
            print("-----------------------------")
    elif opc is 3:
        print("Actualizar")
        id = input("Dime el id: ")
        Temperatura = float(input("Nuevo temperatura del sensor: "))
        Humedad = float(input("Nueva humedad del sensor: "))
        dato = sensores(Temperatura, Humedad)
        datos_actualizados = actualizar(id, dato)
        print("Número de datos actualizados: ", datos_actualizados)

    elif opc is 4:
        print("Eliminar")
        id = input("Dime el id: ")
        datos_eliminados = eliminar(id)
        print("Número de datos eliminados: ", datos_eliminados)