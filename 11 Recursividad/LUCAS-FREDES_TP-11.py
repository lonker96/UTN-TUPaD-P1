"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario

"""
import tools
def factorial_recu(n): #funcion recursiva para obtener factoriales
    return 1 if n == 0 else n * factorial_recu(n - 1) # forma declaratoria de operador ternario para usar una sola linea en el llamado a la recursividad

def listado_factoriales(n): #funcion para iterar desde 1 hasta el numero ingresado por el usuario para obtener sus factoriales
    for i in range(1,n+1):
        print(f"El factorial de {i} es {factorial_recu(i)}")
    
def main(): #funcion main que ejecuta las funciones pertinentes
    listado_factoriales(tools.pedir_numero()) #funcion de listado de factoriales que recibe el numero ingresado por el usuario

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
==========================================================================================================================================================================
"""
"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""
import tools

def fibonacci_recu(n): #funcion recursiva para calcular el valor de la serie de fibonacci de un numero dado por el usuario
    return n if n == 0 or n == 1 else fibonacci_recu(n-1) + fibonacci_recu(n-2)

def serie_completa(n): #funcion para iterar desde 1 hasta el numero ingresado por el usuario
    for i in range(0,n+1):
        print(f"El fibonacci de {i} es {fibonacci_recu(i)}")

def main(): #funcion main que ejecuta las funciones pertinentes
    serie_completa(tools.pedir_numero())

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
==========================================================================================================================================================================
"""

"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n 𝑚 = n * n (𝑚-1) . Prueba esta función en un algoritmo general.

"""
def expo_recu(numero,exponente): #funcion recursiva para calcular la potencia de un numero elevado al exponente recibiendo ambos valroes como argumentos
    if exponente == 0:
        return 1
    elif exponente == 1:
        return numero
    else:
        return numero * expo_recu(numero,exponente-1)


def main(): #funcion main que ejecuta las funciones pertinentes
    print(f"2 elevado a 0 es: {expo_recu(2, 0)}")    #distintos casos de uso
    print(f"5 elevado a 1 es: {expo_recu(5, 1)}")    
    print(f"2 elevado a 3 es: {expo_recu(2, 3)}")    
    print(f"3 elevado a 4 es: {expo_recu(3, 4)}")    
    print(f"10 elevado a 2 es: {expo_recu(10, 2)}")  

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
==========================================================================================================================================================================
"""

"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""
import tools #importamos mi modulo de herramientas 
def decimal_a_binario_recur(decimal):  #funcion recursiva para pasar un numero a representacion en binario
    if decimal == 0: #si el decimal recibido es == 0 devuelve str(0)
        return "0"
    elif decimal == 1:  #si el decimal recibido es == 1 devuelve str(1)
        return "1"
    else:
        resto = decimal % 2 #obtenemos el ultimo digito del numero decimal
        cociente = decimal // 2 #le quitamos el ultimo digito al numero decimal
        return decimal_a_binario_recur(cociente) + str(resto) #retornamos concatenando los distintos 1s y 0s

def main(): #funcion main que ejecuta las funciones pertinentes
    print(decimal_a_binario_recur(tools.pedir_numero()))
if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro
"""
==========================================================================================================================================================================
"""

"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()
"""

def es_palindromo(palabra): #funcion recursiva para ver si una palabra recibida por argumento es palindromo
    if len(palabra) <= 1: #si la longitus de la palabra es <=1 devuelve True
        return True
    if palabra[0] != palabra[len(palabra)-1]: #si la primera letra de la palabra es distinta de la ultima letra de la palabra devuelve False
        return False 
    return es_palindromo(palabra[1:len(palabra)-1]) #hacemos el llamado recursivo donde le quitamos la primera y la ultima letra a la palabra para seguir evaluando las demas

def mensaje(resultado): #funcion para mostrar el mensaje por consola si es o no un palindromo
    if resultado:
        print("Es Palindromo")
    else:
        print("No es palindromo")

def main(): #funcion main que ejecuta las funciones pertinentes
    palabra = "oso"
    mensaje(es_palindromo(palabra)) # Lo que devuelve la funcion recursiva es un valos Booleano 'True' o 'False' en caso de que sea o no un palindromo
if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro
"""
==========================================================================================================================================================================
"""

"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
"""
import tools #importamos mi modulo de herramientas
def suma_digitos(n): # Funcion recursiva que toma el ultimo digito del numero y los va sumando
    if n == 0: 
        return n
    else:
        print(n)
        return n % 10 + suma_digitos(n//10) # en el llamado recursivo obtenemos y sumamos el ultimo digito con el resultado del llamado recursivo que es llamado enviadole como argumento el numero con un digito menos al final
    
def mostrar_resultado(numero,resultado): #Funcion para mostrar por consola el numero a evaluar y su resultado
    print(f"La suma de todos los digitos de {numero} es: {resultado}")

def main(): #funcion main que ejecuta las funciones pertinentes
    numero = tools.pedir_numero()
    mostrar_resultado(numero,suma_digitos(numero))

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro

"""
==========================================================================================================================================================================
"""
"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
"""

import tools #importamos mi modulo de herramientas

def contar_bloques(n): #Funcion recursiva para contar los bloques que se requieren para una primide
    if n == 0:
        return n
    else:
        return n + contar_bloques(n-1) # el llamado recursivo lo hacemos enviandole como argumento el mismo valor-1 para ir sumando los distintos niveles de la piramide
    
def mostrar_resultado(bloques,resultado): #Funcion para mostrar por consola el numero a evaluar y su resultado
    print(f"Dada que la base de la piramide es: {bloques} bloques, la totalidad de bloques que necesita para hacer la piramide es: {resultado}")

def main(): #funcion main que ejecuta las funciones pertinentes
    bloques = tools.pedir_numero()
    mostrar_resultado(bloques,contar_bloques(bloques))


if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro
"""
==========================================================================================================================================================================
"""
"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
 
SERIA UNA COMBINACION DEL 6 Y 7
"""
import tools #importamos mi modulo de herramientas
def contar_digito(numero, digito): #Funcion que recibe un numero y un digito para evaluar 
    if numero == 0: #cuando el numero que recibe sea == 0 devuelve 0
        return 0
    ultimo_digito = numero % 10 #obtenemos el ultimo digito del numero recibido
    contador_actual = 0 #inicializamos el contador en 0
    if ultimo_digito == digito: #evaluamos si el ultimo digito es == al digito que queremos comparar
        contador_actual = 1 # le asignamos 1 a la variable contador 
    return contador_actual + contar_digito(numero // 10, digito) # si el numero recibido no es == 0 devuelve suma y devuelve lo que tiene la variable contador, sumando todos los contadores de las distintas llamadas recursivas

def main(): #funcion main que ejecuta las funciones pertinentes
    numero = tools.pedir_numero()
    print(contar_digito(numero,5))

if __name__ == "__main__": #Solo se ejecuta la funcion main si el scrip se este ejecutando directamente como el programa principal
    main() # al ser TRUE se ejecuta la funcion main con todas las funciones que tenga dentro