from metodos import metodos
from sensores import sensores # La clase Producto

menu = """ PROGRAMA DE CRUD MONGODB
1 - INSERTAR DATO
2 - VER DATOS
3 - ACTTUALIZAR DATO
4 - ELIMINAR DATO
5 - SALIR
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
        id = metodos.insertar(dato)
        print("-----------------------------")
        print("El id del dato insertado es: ", id)
        print("-----------------------------")
    elif opc is 2:
        print("Obteniendo datos...")
        for dato in metodos.obtener():
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
        datos_actualizados = metodos.actualizar(id, dato)
        print("Número de datos actualizados: ", datos_actualizados)

    elif opc is 4:
        print("Eliminar")
        id = input("Dime el id: ")
        datos_eliminados = metodos.eliminar(id)
        print("Número de datos eliminados: ", datos_eliminados)