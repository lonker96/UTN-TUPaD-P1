"""
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
range.
"""
lista_multiplos=[] # Crea una lista vacia
for i in range (1,100+1): # Ciclo en el rango 1 - 100 inclusive
    if i % 4 == 0: # verifica todos los multiplos de 4 
        lista_multiplos.append(i) # en caos de ser True los ingresa a la lista
print(lista_multiplos) # muestra por consola la lista de multiplos

"""
==============================================================================================================================================
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
indexing con números negativos! 
"""
lista_elementos=['elemento 1','elemento 2','elemento 3','elemento 4','elemento 5'] #crear lista de elementos
print(lista_elementos[-2]) #mostrar el penultimo o el anteultimo elemento de las lista

"""
==============================================================================================================================================
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
ejemplo: 
lista_vacia = [] 
"""

lista_vacia=[] # crea una lista vacia
for i in range(3): # cicla 3 veces
    palabra = input('Ingrese un nombre: ') # pide un elemento en este caso un nombre
    lista_vacia.append(palabra) #lo ingresa a la lista
print(lista_vacia) #muestra la lista completa por consola

"""
==============================================================================================================================================
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
en los videos o bien investigar cómo funciona el indexing con números negativos! 
animales = ["perro", "gato", "conejo", "pez"]
"""

animales = ["perro", "gato", "conejo", "pez"] # crea lista de animales
animales[-3] = 'loro' #cambia el elemento 
animales[3] = 'oso' #cambia el elemento
print(animales) # muestra por consola la lista final

"""
==============================================================================================================================================
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
"""
numeros = [8,15,3,22,7] #crea una lista de numeros
numeros.remove(max(numeros)) # obtiene el maximo valor de la lista y lo elimina
print(numeros) # muestra por consola la lista final
"""
Dada la lista de numeros la funcion max(Lista de numeros) devolvera el valor mas grande de la lista y la funcion .remove lo eliminara
por ende el conjunto de toda la linea busca el valor mas grande de la lista y lo elimina.
"""

"""
==============================================================================================================================================
6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
pantalla los dos primeros. 
"""
lista_numeros = [] #crea una lista de numeros vacia
for i in range(10,30+1,5): # cicla desde 10 hasta 30 inclusive recorriendo de 5 en 5
    lista_numeros.append(i) # agrega cada elemento a la lista
print(lista_numeros[:2]) # muestra los primeros 2 elementos de la lista

"""
==============================================================================================================================================
7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
cualesquiera. 
"""
autos = ["sedan", "polo", "suran", "gol"] #crea una lista de elementos
for i in range(1,2+1): # cicla sobre el elemetos 1 y 2 inclusive
    autos[i] = f'Reemplazo de valor {i}' #reemplaza el elemento por un texto usando tambien el propio indice del siclo para ello
print(autos) # muestra la lista final con los elementos 1 y 2 de la lista reemplazados

"""
==============================================================================================================================================
8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
directamente. Imprimir la lista resultante por pantalla.
"""
dobles = [] # crea una lista vacia
dobles.append(10) # agrega el elementos
dobles.append(20) # agrega el elementos
dobles.append(30) # agrega el elementos
print(dobles) #muestra la lista final por consola

"""
==============================================================================================================================================
9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]] 
a) Agregar "jugo" a la lista del tercer cliente usando append. 
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
c) Eliminar "pan" de la lista del primer cliente.  
d) Imprimir la lista resultante por pantalla 
"""
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]  # crea un conjunto de listas anidadas 
compras[2].append("jugo") # agrega el elemento a la sublista 2
compras[1][1] = "tallarines" #reemplaza el elemento en la sublista 1
compras[0].remove("pan") #elimina el elemento de la sublista 0
print(compras) # muestra el conjusto de listas anidadas resultante

"""
==============================================================================================================================================
10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 
Imprimir la lista resultante por pantalla. 
"""

valor0= [15] #crea una lista
valor1= [True] #crea una lista
lista2=[25.5,57.9,30.6] #crea una lista
valor3= [False] #crea una lista
lista_anidada= valor0 + valor1 + [lista2] + valor3 # une todos los elementos de las listas dentro de otra lista pero la lista2 se guarda como una lista dentro de la lista principal
print(lista_anidada) # mostrar la lista y su sublista por consola