"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300

"""

# Diccionario de frutas con sus precios
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Agregando frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
# Mostrarlo por consola
print(precios_frutas)

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
# Dado el codigo anterior, modificar el precio de alguas frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
# Mostrarlo por consola
print(precios_frutas)


"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios
"""
# Agarrando solo las frutas con el metodo .keys() para crear una lista con list()
ista_frutas = list(precios_frutas.keys())
# Mostrarlo por consola
print(ista_frutas)


"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.

"""
# Crear funcion para crear contactos
def crear_agenda_de_contactos():
    # Crear un diccionario vacio
    agenda_telefonica = {}
    # Ciclo que se repite 5 veces (de 0 hasta 4) para ingresar los contactos
    for i in range(5):
        nombre = input(f"\nIngresa el nombre del contacto #{i+1}: ") #Solicita que se ingrese un nombre para usar de 'key' del contacto
        numero = input(f"\nIngresa el número de teléfono de {nombre}: ") #Solicita que se ingrese un telefono para usar de 'value' del contacto
        # Asignando en la 'ubicacion de [i+1] : [el telefono ingresado]'
        agenda_telefonica[nombre] = numero 
    # Mostrar por consola
    return agenda_telefonica

# Crear una funcion para buscar un contacto dentro del listado
def Buscar_contacto(agenda):
    # Guardar en la variable el nombre del contacto a buscar
    contacto_a_buscar = input("\nIngresa el nombre del contacto que quieres buscar: ")
    # Verificar si el contacto esta dentro de la agenda
    if contacto_a_buscar in agenda:
        print(f"\nEl numero de teléfono de {contacto_a_buscar} es: {agenda[contacto_a_buscar]}") # Si es True lo muestra por consola
    else:
        print(f"\nERROR!, el contacto '{contacto_a_buscar}' no se encuentra en la agenda.") # Si es False avisa que no esta en la agenda

# funcion main que ejecuta las funciones pertinentes
def main(): 
    agenda = crear_agenda_de_contactos() # Guarda en la variable la agenda de contactos
    Buscar_contacto(agenda) # Manda la lista por parametro a la funcion buscar para encontrar el contacto en especifico

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro


"""
================================================================================================================================================================================================
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

# Solicita al usuario que ingrese una frase
frase = input("\ningresa una frase porfavor: ")


# Convertir toda la frase en minusculas para poder operarla
frase_limpia = frase.lower()

# Reemplazar todo tipo de signos comunes por espacios para poder dividir las palabras
puntuacion = ['.', ',', ';', ':', '!', '?', '¿', '¡', '(', ')', '[', ']', '{', '}']
for signo in puntuacion: # Recorrer la frase y reemplazar todo por espacios
    frase_limpia = frase_limpia.replace(signo, ' ') 


# Usar split() sin argumentos divide la frase por cada espacio separando cada palabra
palabras = frase_limpia.split()

# Guardando las palabras en un set para eliminar las repetidas
palabras_unicas = set(palabras)

# Contar la cantidad de veces que aparece cada palabra (usando un diccionario)
conteo_palabras = {} #crear un diccionario vacio
for palabra in palabras: # Recorrer cada palabra en el set
    # Si la palabra ya se encuentra en el diccionario incrementa su contador
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    # Si no esta la añade con un contador de 1
    else:
        conteo_palabras[palabra] = 1

# Imprimir los resultados

print("\nPalabras unicas:")
for palabra in palabras_unicas:
    print(f"{palabra}")

print("\nConteo de palabras:")
for palabra, cantidad in conteo_palabras.items():
    print(f"'{palabra}': {cantidad} vez")

"""
================================================================================================================================================================================================
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.

"""
# Funcion para ingresar 3 alumnos y 3 notas para c/u guardandolas en una tupla todo dentro de un diccionario
def ingresar_datos_alumnos():
    alumnos_data = {} # Creamos un diccionario vacio
    for i in range(3): # Recorremos 3 veces para asignar 3 alumnos
        nombre = input(f"\nIngresa el nombre del alumno {i+1}: ")
        notas = [] # creamos una lista de notas para c/u
        print(f"\nAhora ingresa 3 notas para {nombre}:") # Aviso por consola para asignar notas para el alumno ingresado
        for j in range(3): # Recorrer 3 veces para asignar 3 notas 
            nota = float(input(f"\nNota {j+1}: ")) # Asignamos la noma como un Float para poder sacar el promedio
            notas.append(nota) # pendeamos la nota en la lusta de notas
        alumnos_data[nombre] = tuple(notas) # Guarda las notas como una tupla
    return alumnos_data

# Funcion para calcular los promedios 
def calcular_y_mostrar_promedios(alumnos_data):
    for nombre, notas in alumnos_data.items():
        # Sumar todas las notas y dividir por la cantidad de notas
        promedio = round(sum(notas) / len(notas),2)
        print(f"\nEl promedio de {nombre} es: {promedio}") # Formatea a 2 decimales

# funcion main que ejecuta las funciones pertinentes
def main():
    datos_alumnos = ingresar_datos_alumnos() # Guardamos la data de los alumnos en la variable 
    calcular_y_mostrar_promedios(datos_alumnos) # Llamamos la funcion para mostrar los promedios y le mandamos por parametro la data de los alumnos

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
================================================================================================================================================================================================
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

"""

# Dados los dos sets de estudiantes que aprobaron cada parcial
aprobados_parcial1 = {101, 105, 108, 112, 115, 120, 125, 130}
aprobados_parcial2 = {101, 103, 108, 110, 115, 118, 122, 125}

print("--- Análisis de Aprobados ---")


# Usamos el metodo .intersection() para mostrar los aprobados de ambos parciales
aprobados_ambos = aprobados_parcial1.intersection(aprobados_parcial2)
print(f"\nEstudiantes que aprobaron AMBOS parciales: {aprobados_ambos}")


# Usamos el metodo .symmetric_difference() para ver los estudiantes que solo aprobaron un parcial
aprobados_solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
print(f"Estudiantes que aprobaron SOLO UNO de los dos parciales: {aprobados_solo_uno}")

# Usamos el metodo .union() para ver los alumnos que aprobaron al menos un parcial
total_aprobados_al_menos_uno = aprobados_parcial1.union(aprobados_parcial2)
print(f"Lista total de estudiantes que aprobaron AL MENOS UN parcial: {total_aprobados_al_menos_uno}")

"""
================================================================================================================================================================================================
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

stock_productos = {
        "Manzanas": 50,
        "Peras": 30,
        "Naranjas": 20
    }


def agregar_producto(stock):
    producto = input("\n Ingresa el nombre del producto que queres agregar: ")
    cantidad = int(input("\n Ingresa las cantidades del producto que queres agregar: "))
    print("viejo stock",stock)
    stock[producto] = cantidad
    print("Nuevo stock",stock)  


def agregar_unidades(stock):
    producto = input("\n Ingresa el nombre del producto al que le queres agregar cantidades: ")
    cantidad = int(input("\n Ingresa la cantidad del producto que queres agregar: "))
    print("stock actual ",stock)
    if producto in stock:
        stock[producto] += cantidad
        print("stock final",stock)
    else:
        print("ERROR! El nombre de producto ingresado es incorrecto")

def consultar_stock(stock):
    print("\nMostrando el stock actual ")
    for producto, cantidad in stock.items():
        print(f"\n  {producto} = {cantidad}")

# Ejecutar el programa de gestión de stock
if __name__ == "__main__":
    consultar_stock(stock_productos)
    agregar_unidades(stock_productos)
    agregar_producto(stock_productos)

"""
================================================================================================================================================================================================
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
"""
# Iniciando agenda vacia
agenda = {}
# Agregando eventos a la agenda
agenda[("Lunes", 10)] = "Reunion de equipo"
agenda[("Miércoles", 18)] = "Clase de Python"
agenda[("Viernes", 9.30)] = "Tramite en el banco"
agenda[("Sábado", 13)] = "Almuerzo con amigos"

# Mostrar agenda 
print("\n--> Mi Agenda de Eventos <--")
for (dia, hora), evento in agenda.items():
    print(f"El {dia} a las {hora} hs: {evento}")
    # Mostrar evento en concreto de un dia y hora en especifico
print(agenda["Lunes",10])

"""
================================================================================================================================================================================================
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

# Diccionario original: paises como claves, capitales como valores
paises_capitales = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma",
    "Canadá": "Ottawa",
    "Japón": "Tokio"
}

print("\nDiccionario original (País: Capital):")
print(paises_capitales)

# Creamos un nuevo diccionario vacío para dar vuelta el original
capitales_paises = {}

# Iteramos sobre el diccionario original para invertir las claves y valores
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("\nNuevo diccionario (Capital: Pais):")
print(capitales_paises)