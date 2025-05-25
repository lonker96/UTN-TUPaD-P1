"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
def imprimir_hola_mundo():#funcion que ejecuta el hola mundo
    print("Hola Mundo!")#funcion print para mostrar por consola el mensaje

def main(): #funcion main que ejecuta las funciones pertinentes
    imprimir_hola_mundo() #llamada a la funcion hola mundo

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
=====================================================================================================================
"""
"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
def saludar_usuario(nombre):#funcion que ejecuta el hola mundo
    print(f"Hola {nombre}!")#funcion print para mostrar por consola el saludo a un nombre pasado como argumento

def main():#funcion main que ejecuta las funciones pertinentes
    saludar_usuario("Lucas")

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro
"""
=====================================================================================================================
"""
"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
def informacion_personal(nombre, apellido, edad, residencia): #funcion de saludo 
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def pedir_datos_usuario(): #Funcion que pide los datos al usuario
        nombre_usuario = input("Ingresa tu nombre: ")
        apellido_usuario = input("Ingresa tu apellido: ")
        edad_usuario = input("Ingresa tu edad: ") 
        residencia_usuario = input("Ingresa tu lugar de residencia: ")
        return nombre_usuario,apellido_usuario,edad_usuario,residencia_usuario

def main(): #funcion main que ejecuta las funciones pertinentes
    nombre, apellido, edad, residencia = pedir_datos_usuario() #Adignacion multiple de variables usando el iterable que devuelve pedir_datos_usuario()
    informacion_personal(nombre, apellido, edad, residencia) #Llamada a la funcion que imprime el msj en consola con los datos en cada variable

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() #al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro
"""
=====================================================================================================================
"""
"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""
import math,tools
def calcular_area_circulo(radio): #Funcion para devolver el area
  area = math.pi * (radio ** 2)
  return area

def calcular_perimetro_circulo(radio): #Funcion para devolver el perimetro
  perimetro = 2 * math.pi * radio
  return perimetro

def solicitar_radio(): # funcion para solicitar el radio al usuario
    radio = float(input("Ingrese el radio del circulo: "))
    radio = tools.chequear_numero_positivo(radio,"radio")
    return radio

def main(): #funcion main que ejecuta las funciones pertinentes
    radio = solicitar_radio()
    print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)} y el area del circulo es {calcular_area_circulo(radio)}")
if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() #al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro
"""
=====================================================================================================================
"""
"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""
import tools
def segundos_a_horas(segundos): #funcion para transformar segundos en horas
    horas = segundos / 3600
    horas = round(horas,2)
    return horas

def solicitar_segundos(): #funcion para solicitar segundos al usuario
    segundos = float(input("Ingrese los segundos: "))
    segundos = tools.chequear_numero_positivo(segundos,"Segundos")
    return segundos

def main(): #funcion main que ejecuta las funciones pertinentes
    print(f"La cantidad de HORA/AS equivalentes a los segundos ingresados es: {segundos_a_horas(solicitar_segundos())}")
if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() #al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
=====================================================================================================================
"""
"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
import tools

def tabla_multiplicar(numero):
    numero = int(numero)
    for i in range(1,11):
       print(f"{numero} * {i} = {numero * i}")
    
def solicitar_numero():
    numero = int(input("Ingrese un numero que desea saber su tabla de multiplicar: "))
    numero = tools.chequear_numero_positivo(numero)
    return numero


def main(): #funcion main que ejecuta las funciones pertinentes
    tabla_multiplicar(solicitar_numero())
if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() #al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""
                #funciones basicas con los dos numeros
def suma_de_dos_numeros(a,b):
    return a + b

def resta_de_dos_numeros(a,b):
    return a - b

def multiplicacion_de_dos_numeros(a,b):
    return a * b

def division_de_dos_numeros(a,b):
    return a / b

def operaciones_basicas(a, b): #funcion que llama a las funciones de las operaciones basicas y devuelve la tupla con los resultados
    suma = suma_de_dos_numeros(a,b)
    resta = resta_de_dos_numeros(a,b)
    multiplicacion = multiplicacion_de_dos_numeros(a,b)
    division = division_de_dos_numeros(a,b)
    return suma,resta,multiplicacion,division

def pedir_dos_numeros(): # funcion para pedirle al usuario dos numeros que devuelve una tupla con los dos numeros 
    a = float(input("Ingrese un numero: "))
    b = float(input("Ingrese otro numero: "))
    return a,b

def mostrar_por_consola(a,b,suma,resta,multiplicacion,division):# funcion para mostrar de manera clara por consola los resultados
    print(f"La suma de {a} + {b} es: {suma}\nLa resta de {a} - {b} es: {resta}\nLa multiplicacion de {a} * {b} es: {multiplicacion}\nLa division de {a} / {b} es: {division}\n ")

def main(): #funcion main que ejecuta las funciones pertinentes
    a,b = pedir_dos_numeros() # guardando en variables los numeros que trae la tupla
    suma,resta,multiplicacion,division = operaciones_basicas(a,b) # guardando en variables los numeros que trae la tupla
    mostrar_por_consola(a,b,suma,resta,multiplicacion,division) #llamado a la funcion para mostrar por consola los resultados
    
if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() #al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
=====================================================================================================================
"""

"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""
import tools

def validacion_kg(peso): #funcion de validacion de kg
    peso = tools.validacion_rango(peso,5,300,"peso") #llamada a la funcion de tools que valida un numero entre unos rangos dados
    return peso #retorna el peso validado

def validacion_mt(altura): #funcion de validacion de mt
    altura = tools.validacion_rango(altura,0.30,2.50,"altura") #llamada a la funcion de tools que valida un numero entre unos rangos dados
    return altura #retorna altura validada

def solicitar_datos(): #funcion para solicitar los datos y validarlos
    altura_mt = float(input("Ingrse su altura en metros: "))
    altura_mt = validacion_mt(altura_mt) 
    peso_kg = float(input("Ingrse el peso en kilogramos: "))
    peso_kg = validacion_kg(peso_kg) 
    return altura_mt,peso_kg #retorna los datos validados

def calcular_imc(altura,peso): #funcion para calcular el IMC
    imc = peso / (altura**2)
    print(f"El IMC con una altura de {altura} y un peso de {peso} es: {round(imc,2)}") #muestra por consola el resultado

def main(): #funcion main que ejecuta las funciones pertinentes
    altura,peso=solicitar_datos() #asigna a las variables los datos de la tupla que devuelve la funcion
    calcular_imc(altura,peso) # llamada a la funcion que dara el resultado del ejercicio enviando las variables como argumentos

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() #al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
=====================================================================================================================
"""

"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.

"""
def solicitar_temperatura_celsius(): #Funcion que solicita los grados en Celsius
    celsius= float(input("Ingrese la temperatura en grados Celsius: "))
    return celsius #retorna la variable con los grados

def celsius_a_fahrenheit(celsius): #funcion que transforma de celsius a fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit #retorna los grados en fahrenheit

def mostrar_mensaje(celsius,fahrenheit): #funcion que muestra el msj por consola
    print(f"La temperatura en Celsius : {celsius} ∘C es equivalente a {fahrenheit} ∘F") 

def main(): #funcion main que ejecuta las funciones pertinentes
    celsius = solicitar_temperatura_celsius() #variable en la que guardamos los grados celsius
    mostrar_mensaje(celsius,celsius_a_fahrenheit(celsius)) #llamada a la variable que muestra el msj por consola que recibe una variable y una funcion como argumento

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() #al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
=====================================================================================================================
"""

"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
def solicitar_numeros():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    c = float(input("Ingrese el tercer numero: "))
    return a,b,c

def calcular_promedio(a, b, c): #debe mostrar el resultado
    promedio = (a + b + c) / 3
    print(f"El promedio de {a} + {b} + {c} es: {round(promedio,2)}")
def main():
    a,b,c = solicitar_numeros()
    calcular_promedio(a,b,c)
if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() #al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro