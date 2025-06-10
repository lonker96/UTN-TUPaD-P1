# Inventario de Productos - Proyecto de Búsqueda y Ordenamiento

El codigo del trabajo integrador simula un sistema básico de inventario con funciones de búsqueda y ordenamiento de productos. Cada producto está representado como un diccionario con los campos: `id_producto`, `nombre`, `precio` y `cantidad_en_stock`.

El objetivo del proyecto es aplicar distintas estrategias algorítmicas (búsqueda lineal, búsqueda binaria, ordenamiento Bubble Sort y Quick Sort)

Donde las funciones de ordenamiento van a ordenar de menor a mayor y las funciones de busqueda requieren que se les envie por parametro el id que queremos buscar. Y en el caso de la busqueda binaria tambien requiere que previamente se ordene la lista que le queremos enviar para buscar el id.

# Estructura del Inventario

El inventario se almacena como una lista de diccionarios, donde cada diccionario representa un producto:

inventario = [
    {"id_producto": 1, "nombre": "Guantes", "precio": 950.00, "cantidad_en_stock": 120},
    {"id_producto": 2, "nombre": "Zapatillas Deportivas", "precio": 9800.75, "cantidad_en_stock": 20},
    ...
]

## Forma de uso

# Busca un producto recorriendo el inventario desde el inicio hasta encontrar el ID indicado.
Buscar producto por ID (Búsqueda Lineal):
    buscar_producto_lineal(inventario, id_buscado)

# Ordena los productos del inventario utilizando el método de burbuja de menor a mayor(comparaciones adyacentes).
Ordenar productos por ID (Bubble Sort):
    bubble_sort_por_id(inventario)

# Permite encontrar un producto de manera más eficiente, siempre que el inventario esté previamente ordenado por ID.
Buscar producto en inventario ordenado (Búsqueda Binaria):
    inventario_ordenado = bubble_sort_por_id(inventario.copy())
    busqueda_binaria_por_id(inventario_ordenado, id_buscado)

# Aplica el algoritmo Quick Sort para ordenar el inventario de forma más eficiente en listas grandes.
Ordenar productos por ID (Quick Sort):
quick_sort_por_id(inventario)



# Reflexion del equipo

Durante el desarrollo de este trabajo integrador, cada integrante aplicó sus conocimientos en algoritmos de búsqueda y ordenamiento:

Búsqueda Lineal y Quick Sort: fueron implementados por Florencia con un enfoque en la claridad y comentarios explicativos para reforzar la comprensión de algoritmos recursivos y de recorrido simple.

Bubble Sort y Búsqueda Binaria: estuvieron a cargo de Lucas, quien se enfocó en algoritmos iterativos y su aplicabilidad cuando se requiere precisión en pasos definidos.

Este proyecto nos permitió reforzar conceptos como la eficiencia algorítmica, la recursividad y la importancia de elegir el método adecuado según el contexto (por ejemplo, búsqueda binaria solo funciona si la lista está ordenada).

También fue una buena práctica de trabajo en equipo, asignación de roles y revisión cruzada de código, así como de buenas prácticas de documentación mediante comentarios dentro del código.

# Link al video en Youtube

https://www.youtube.com/watch?v=xWUfF6bRbpA