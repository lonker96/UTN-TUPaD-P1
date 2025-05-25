def chequear_numero_positivo(numero,mensaje = "Numero"): #funcion para chequear numeros positivos que recibe de argumento un numero y un mensaje para solicitar el numero con un mensaje apropiado en caso de necesitarlo
    while numero < 0: 
        print(f"ERROR! el {mensaje} ingresado/os tiene/en que ser positivo/os")
        numero = float(input("Ingrese un numero positivo: "))
    return numero

def validacion_rango(dato,minimo,maximo,mensaje = "numero"): #funcion para validar un numero dentro de un rango dado que recibe el numero, rango minimo, rango maximo y un mensaje para solicitar el numero en caso de necesitarlo
    while True:
        if dato < minimo or dato > maximo:
            print(f"Parece que ingresaste una {mensaje} irreal")
            dato = float(input(f'vuelve a ingresar la {mensaje} dentro de unos parametros logicos: '))
        else:
            return dato