
from bson.objectid import ObjectId # Para crear ObjectId, porque _ID como cadena no funciona
from conexion import obtener_bd #IMPORTAMOS CONEXION

#MEETODOS DE CRUD
class metodos:
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



