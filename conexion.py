import certifi
import pymongo
def obtener_bd():
    
    base_de_datos = "Sensores"
    client = pymongo.MongoClient('mongodb+srv://zairdeltamx:ZAIR@sandbox.dcgxy.mongodb.net/Sensores?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    return client[base_de_datos]