
# INVENTARIO INICIAL
# el inventario es una lista de productos donde cada producto es un diccionario con las siguientes propiedades:
# ID, nombre, precio y cantidad en stock

# Lista de diccionarios que representan productos
inventario = [
    {"id_producto": 8, "nombre": "Remera", "precio": 2500.00, "cantidad_en_stock": 50},
    {"id_producto": 5, "nombre": "Pantalón Jean", "precio": 6000.50, "cantidad_en_stock": 30},
    {"id_producto": 2, "nombre": "Zapatillas Deportivas", "precio": 9800.75, "cantidad_en_stock": 20},
    {"id_producto": 4, "nombre": "Campera", "precio": 15000.00, "cantidad_en_stock": 10},
    {"id_producto": 3, "nombre": "Medias Pack x3", "precio": 800.00, "cantidad_en_stock": 100},
    {"id_producto": 6, "nombre": "Gorra", "precio": 1200.00, "cantidad_en_stock": 75},
    {"id_producto": 7, "nombre": "Bufanda", "precio": 1850.50, "cantidad_en_stock": 40},
    {"id_producto": 1, "nombre": "Guantes", "precio": 950.00, "cantidad_en_stock": 120},
    {"id_producto": 9, "nombre": "Mochila", "precio": 7200.00, "cantidad_en_stock": 25},
    {"id_producto": 11, "nombre": "Vestido", "precio": 4500.25, "cantidad_en_stock": 35},
    {"id_producto": 15, "nombre": "Short", "precio": 2100.00, "cantidad_en_stock": 60},
    {"id_producto": 12, "nombre": "Sandalias", "precio": 3100.75, "cantidad_en_stock": 80},
    {"id_producto": 10, "nombre": "Cinturón", "precio": 2800.00, "cantidad_en_stock": 45},
    {"id_producto": 14, "nombre": "Billetera", "precio": 3900.50, "cantidad_en_stock": 55},
    {"id_producto": 13, "nombre": "Anteojos de Sol", "precio": 6500.00, "cantidad_en_stock": 28},
]



# BÚSQUEDA LINEAL (YO)
# Busca un producto dentro del inventario, comparando uno por uno hasta encontrar el que tenga el ID que le pedimos.

def buscar_producto_lineal(inventario, id_buscado):
    for producto in inventario:  # Recorre cada producto
        if producto["id_producto"] == id_buscado:  # Compara el ID del producto actual con el que estoy buscando.
            return producto # Si se cumple la condicion devuelve el producto correspondiente a ese "id_producto".
    return None  # Si no lo encuentra, devuelve None.



# ORDENAMIENTO BUBBLE SORT (lucas)
# Ordena el inventario por ID usando Bubble Sort (burbuja)

def bubble_sort_por_id(inventario):
    n = len(inventario)  # n representa la longitud del inventario
    
    for i in range(n):  # Ciclo externo que recorre todo el arreglo n veces.En cada pasada, el valor más grande que aún no está en su lugar sube al final
        
        for j in range(0, n-i-1):  # Ciclo interno que va empujando el mayor valor hacia el final.
            # j	indice actual que compara los productos uno con otro, comparando elementos adyacentes.
            if inventario[j]["id_producto"] > inventario[j+1]["id_producto"]: # Compación de a pares: producto[j] con producto[j+1].
                # Intercambia si están en el orden incorrecto 
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]
    return inventario # Devuelve el inventario ordenado de menor "id_producto" a mayor.


# BÚSQUEDA BINARIA (lucas)
# Solo funciona si la lista ya está ordenada por ID de menor a mayor 
# (La ordenamos previamente con la función "bubble_sort_por_id" guardando su resultado en la variable "inventario_ordenado")
# Buscar un producto por su ID descartando la mitad de la lista en cada paso.

def busqueda_binaria_por_id(inventario_ordenado, id_buscado): # inventario_ordenado(la lista de productos ordenada por ID) id_buscado id que se desa buscar.
    
    inicio = 0 # Representa el primer índice de la parte de la lista que vamos a mirar.
    # fin representa el último índice de inventario_ordenado.
    fin = len(inventario_ordenado) - 1  # desde el principio (índice 0) hasta el último producto (índice n-1).
    
    while inicio <= fin:  # Mientras la búsqueda tenga un rango válido porque si el indice inicio > indice fin, entonces ya revisamos toda la parte posible y no encontramos el ID.
        medio = (inicio + fin) // 2  # Índice medio Calculamos la posición del medio entre inicio y fin. division entera (//) de la suma de los indices innicio y fin.
        
        if inventario_ordenado[medio]["id_producto"] == id_buscado: # Si el producto en el medio tiene el mismo ID que el que se esta buscando.
            return inventario_ordenado[medio]  # devuelve el producto encontrado.
        
        elif inventario_ordenado[medio]["id_producto"] < id_buscado:# Si el ID buscado es mayor que el del medio.
            inicio = medio + 1  # Descartamos la mitad izquierda y avanzamos el inicio para buscar solo en la mitad derecha.
            
        else: # Si el ID buscado es menor que el del medio. El ID buscado está antes del producto del medio.
            fin = medio - 1  # descartamos la mitad derecha y acortamos el fin para buscar en la mitad izquierda.
            
    return None  # Si no se encuentra, devuelve None


# ORDENAMIENTO QUICK SORT POR ID  (YO)
# Algoritmo de ordenamiento que se basa en la idea de dividir la lista en partes más pequeñas y ordenarlas por separado.
# Ordena rápidamente cuando la lista es grande

def quick_sort_por_id(inventario):
    if len(inventario) <= 1: # Caso base si la lista tiene 0 o 1 producto ya está ordenada.
        return inventario # En ese caso devuelve el inventario.
    
    # El pivote es como un "centro" alrededor del cual vamos a comparar a todos los demás elementos.
    pivot = inventario[0] # determinamos un elemento de la lista como Pivote (elemento de indice 0, en este caso, es el primer elemento de la lista).
    
    # Separar los productos menores al pivote.
    # Recorremos todos los productos menos el primero (inventario[1:]).
   
    # Agregamos a una nueva lista llamada menores todos los productos cuyo id_producto sea menor que el del pivote.
    menores = [x for x in inventario[1:] if x["id_producto"] < pivot["id_producto"]]
    
    # Separar los productos mayores al pivote
    # Recorremos todos los productos menos el primero (inventario[1:]).
    # Agregamos a una nueva lista llamada mayores todos los productos cuyo id_producto sea mayor o igual que el del pivote.
    mayores = [x for x in inventario[1:] if x["id_producto"] >= pivot["id_producto"]]
    
    # Ordena RECURSIVAMENTE cada parte y luego las combina
    # Ordena se ordena la lista de productos "menores" al pivote llamando a la misma función quick_sort_por_id(menores).
    # Luego coloca el pivote en el medio.
    # Finalmente ordena la lista mayores también llamando a la misma función quick_sort_por_id(mayores).
    # Se van armando listas cada vez más pequeñas, hasta que todas tengan 0 o 1 elementos, llegando asi al caso base y se detenga la recursividad.
    # Luego combina los resultado intermedios (de atrás hacia delante) hasta reconstruir la lista original, pero en orden correcto.
    return quick_sort_por_id(menores) + [pivot] + quick_sort_por_id(mayores)



# ***EJEMPLOS DE USO***


# Ejemplo de búsqueda lineal.
print("*** Búsqueda Lineal por ID ***")
print(buscar_producto_lineal(inventario, 6))  # Busca producto en el inventario con ID 4.

# Ejemplo de ordenamiento por ID usando Bubble Sort.
print("\n*** Inventario Ordenado por ID (Bubble Sort) ***")
inventario_ordenado = bubble_sort_por_id(inventario.copy()) # Pedimos a la función bubble_sort_por_id ordene el inentario.
# y lo almacene ya orenado en la variable inventario_ordenado.
for producto in inventario_ordenado: 
    print(producto) # con un bucle for recorremos el inentario_ordenado para mostrarlo por patalla más prolijo.

# Ejemplo de búsqueda binaria (requiere que el inventario esté ordenado por ID cosa que ya hizo la función bubble_sort_por_id).
print("\n*** Búsqueda Binaria por ID en Inventario Ordenado ***")
# busca el producto con id 7 en el inventatio_ordenado.
print(busqueda_binaria_por_id(inventario_ordenado, 7)) 

# Ejemplo de ordenamiento del inventario por ID usando Quick Sort.
print("\n*** Inventario Ordenado por ID (Quick Sort) ***")
inventario_ordenado_qs = quick_sort_por_id(inventario.copy()) # llamamos a la función "quick_sort_por_id".
# para que ordene el inventario y almacene el resultado en la variable "inventario_ordenado_qs".
for producto in inventario_ordenado_qs: 
    print(producto) # Con un bucle for mostramos por pantalla el inventario ordenado por su ID usando Quick Sort.

