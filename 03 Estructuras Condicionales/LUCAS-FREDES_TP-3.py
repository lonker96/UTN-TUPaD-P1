"""
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input('Ingrese su edad: '))
if edad < 0 : 
    print('Ingreso una edad invalida porfavor ingrese su edad denuevo: ') 
    edad = int(input('Ingrese su edad: '))
if edad > 18:
    print("Es mayor de edad")
===========================================================================================
"""

"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.

nota = float(input('Ingrese su nota: '))
if nota >= 6 : 
    print("Aprobado")
else: 
    print("Desaprobado")
==============================================================================================    
"""

"""
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar

numero = int(input('Ingrese un numero: '))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
==================================================================================================
"""

"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.

edad = int(input("ingrese su edad: "))
if edad >= 30 :
    print("Adulto/a")
elif edad >=18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 12 and edad < 18:
    print("Adolescente")
else: 
    print("Niño/a")
==================================================================================================
"""
"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string. 

contraseña = str(input('Ingrese una contraseña de entre 8 y 14 caracteres por favor: '))
if len(contraseña) >= 8 and len(contraseña) <= 14 : 
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
==================================================================================================
"""
"""
6) Escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode,median,mean
import random
numeros_aleatorios= [random.randint(1,100) for i in range(50)]
valor_mas_repetido = mode(numeros_aleatorios)
promedio = mean(numeros_aleatorios)
valor_central = median(numeros_aleatorios)

if promedio > valor_central and valor_central > valor_mas_repetido:
    print("Hay sesgo positivo")
elif promedio < valor_central and valor_central < valor_mas_repetido:
    print("Hay sesgo negativo")
elif promedio == valor_central and valor_central == valor_mas_repetido:
    print("No hay sesgo")
==================================================================================================
"""
"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. 

frase = str(input("Ingrese una frase: "))
vocal = ['A','a','E','e','I','i','O','o','U','u']
for i in vocal:
    if i == frase[-1]:
        frase = frase + '!'
print(frase)
==================================================================================================
"""
"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 

nombre = str(input("Ingrese su nombre: "))
opcion = int(input("elije una opcion:\n 1. Si quiere su nombre en mayúsculas \n 2. Si quiere su nombre en minúsculas \n 3. Si quiere su nombre con la primera letra mayúscula \n opcion seleccionada: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
==================================================================================================
"""

"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud >=0 and magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >=3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud < 5:
    print("Moderado (sentido por personas")
elif magnitud >=5 and magnitud < 6:
    print("Fuerte(puede causar daños en estructuras débiles).")
elif magnitud >=6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >=7:
    print("Extremo (puede causar graves daños a gran escala).")
else:
    print("ERROR! ingreso un valor de magnitud incorrecto")
==================================================================================================
"""

"""
10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. 

from datetime import datetime

emisferio = input("Ingrese el emisferio Sur = S / Norte = N: ")
fecha = input("Ingrese la fecha actual usando el siguiente formato: DD-MM-YYYY: ")
formato = "%d-%m-%Y"
fecha = datetime.strptime(fecha, formato)

if emisferio == 'S':
    if fecha >= datetime.strptime("21-12-2024", formato) and fecha <= datetime.strptime("20-03-2025", formato):
        print("estas en Verano ")
    elif fecha >= datetime.strptime("21-03-2025", formato) and fecha <= datetime.strptime("20-06-2025", formato):
        print("estas en Otoño ")
    elif fecha >= datetime.strptime("21-06-2025", formato) and fecha <= datetime.strptime("20-09-2025", formato):
        print("estas en Invierno ")
    elif fecha >= datetime.strptime("21-09-2025", formato) and fecha <= datetime.strptime("20-12-2025", formato):
        print("estas en Primavera ")
    else:
        print("Ingresaste una fecha invalida")
elif emisferio == 'N':
    if fecha >= datetime.strptime("21-12-2024", formato) and fecha <= datetime.strptime("20-03-2025", formato):
        print("estas en Invierno ")
    elif fecha >= datetime.strptime("21-03-2025", formato) and fecha <= datetime.strptime("20-06-2025", formato):
        print("estas en Primavera ")
    elif fecha >= datetime.strptime("21-06-2025", formato) and fecha <= datetime.strptime("20-09-2025", formato):
        print("estas en Verano ")
    elif fecha >= datetime.strptime("21-09-2025", formato) and fecha <= datetime.strptime("20-12-2025", formato):
        print("estas en Otoño ")
    else:
        print("Ingresaste una fecha invalida")
else:
    print("Ingresaste un emisferio invalido!")
"""