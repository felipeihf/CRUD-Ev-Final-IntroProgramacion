import funciones
import numpy as np

## registros de usuarios, mismos numeros y posiciones para reutilizar numeros ##
## Ej: si felipe se guarda en sitio 1 en nombres, tambien en rut y en telefono ##

regis_nombres = []
for i in range(42):
    regis_nombres.append(None) # Uso none para crear 42 espacios en los 3 registros
regis_rut = []
for i in range(42):
    regis_rut.append(None)
regis_tlf = []
for i in range(42):
    regis_tlf.append(None)

# Mapa de asientos para display a usuario
asientos_gral = np.array(([
    ["1","2","3","4","5","6"],
    ["7","8","9","10","11","12"],
    ["13","14","15","16","17","18"],
    ["19","20","21","22","23","24"],
    ["25","26","27","28","29","30"],
    ["31","32","33","34","35","36"],
    ["37","38","39","40","41","42"],
]))

# Matriz vacía equivalente a matriz completa, para llevar registro de asientos ya tomados. #
asientos_disponibles = np.array([
    ["  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  "],
])



comando_usuario = 0 #Flag / Bandera

while comando_usuario != 5:
    print("""--------------- VUELOS INACAP --------------
            Bienvenid@ a venta de pasajes online.
            (1) Muéstrame los asientos disponibles.
            (2) Deseo comprar un asiento
            (3) Quiero anular mi vuelo
            (4) Quiero modificar mis datos
            (5) Salir""")
    comando_usuario = 0

    try:
        comando_usuario = int(input("Ingrese la opción que desea (Número del 1 al 5, segun corresponda): "))
    except:
        print("          ---------------------------------------------------------         ")
        print("      ERROR: Por favor, ingrese un número con el formato solicitado.        ")
        print("          ---------------------------------------------------------         ")

    if comando_usuario == 1:
        funciones.muestra_asientos(asientos_gral)
    
    elif comando_usuario == 2:
        asiento_usuario = int(input("Ingrese el asiento que desea comprar: "))
        nom_usuario = input("Ingrese su nombre: ")
        rut = input("Ingrese su RUT, sin puntos ni guión: ")
        tlf_usuario = input("Ingrese su número de teléfono: ")
        funciones.comprar_pasaje(asientos_disponibles, asiento_usuario, asientos_gral, regis_nombres, regis_rut, regis_tlf, nom_usuario, rut, tlf_usuario)
    
    elif comando_usuario == 3:
        asiento_cliente = int(input("Ingrese el número del asiento que compró y que será cancelado: "))
        funciones.anulacion(asiento_cliente, asientos_disponibles, asientos_gral, regis_nombres, regis_rut, regis_tlf)

    elif comando_usuario == 4:
        print("Para continuar con su petición, debemos validar su número de asiento y su RUT.")
        asiento_cliente = int(input("Ingrese el número de su asiento: "))
        rut = input("Ingrese el RUT del pasajero que compró el boleto: ")
        funciones.edicion_datos(asiento_cliente, asientos_disponibles, rut, regis_rut, regis_nombres, regis_tlf)
    elif comando_usuario == 5:
        print("Gracias por preferir Vuelos Inacap. Hasta Pronto!")
