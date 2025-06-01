def pedir_numero(): #funcion para pedir un numero
    while True:
        numero = int(input("Ingrese un numero entero: "))
        if numero > 0:
            return numero
        else:
            print("Tenes que ingresar un numero positivo")
            continue
