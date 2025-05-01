"""
Ejercicio 1: Cálculo del área y el perímetro de un rectángulo 
Objetivo: Calcular el área y el perímetro a partir de medidas dadas por el usuario.
"""
"""
 Instrucciones:
1. Pedir al usuario que ingrese el ancho y el alto de un rectángulo. 
2. Calcular el área usando la fórmula: ancho * alto. 
3. Calcular el perímetro con la fórmula: (ancho * 2) + (alto * 2). 
4. Mostrar ambos resultados en pantalla. 
"""
bandera = True # Una bandera inciada en True para usar en el siclo while para asegurar que se repita hasta que el usuario ingrese numeros correctos

while bandera: # Ciclo que se repite mientras el usuario ingrese numeros incorrectos para ser utilizados 

    ancho = float(input("Ingrese un numero positivo para el ancho del rectangulo: ")) # se solicita al usuario un numero
    alto = float(input("Ingrese un numero positivo para el alto del rectangulo: ")) # se solicita al usuario un numero

    if ancho > 0 and alto > 0: # if que revisa si los numeros ingresados son positivos
        bandera = False # Salida TRUE : da vuelta la bandera para salir del ciclo while
    else:
        print("Alguno de los datos ingresados es invalido, reingreselos nuevamente. Recuerda que no son validos ni numeros negativos ni caracteres") # mensaje de error para avisar porque debe seguir ingresando numeros el usuario

perimetro = (ancho *2) + (alto * 2) #calculo del perimetro
print(perimetro) # mostrar el perimetro en consola

"""
Preguntas de reflexión: 
• ¿Qué sucede si se ingresan valores negativos? 
    Si se ingresa un numero negativo afectaria al calculo del perimetro devolviendo un perimetro negativo, en el codigo que escribi verifica primero si se ingresaron numeros negativos para no operarlos.
• ¿Podría adaptarse este cálculo a otras figuras geométricas? 
    Si, se podria adaptar para calcular area, volumen, superficie etc. Y se podria adaptar con mas variables para agregar dimensiones.
"""

"""
================================================================================================================================================================================================================================================

Ejercicio 2: Conversión de grados Celsius a Fahrenheit 
Objetivo: Realizar la conversión de temperatura de Celsius a Fahrenheit.
"""
"""
Instrucciones: 
1. Solicitar al usuario una temperatura en grados Celsius. 
2. Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32. 
3. Mostrar el resultado en pantalla.
"""

try: #enmarcando el codigo en un try para manejar los errores

    # pedir al usuario los grados en celsius
    Grados_Celsius = float(input("Ingrese la temperatura en grados Celsius: "))

    # 2. Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32.
    Grados_Fahrenheit = (Grados_Celsius * 9/5) + 32

    # 3. Mostrar el resultado en pantalla.
    print(f"{Grados_Celsius}°C equivalen a {Grados_Fahrenheit}°F")

    # Mensaje para los errores como por ejemplo ingresar un caracter en lugar de un numero
except ValueError:
    print("Error: Por favor, ingrese un valor numérico válido para la temperatura en Celsius.")

"""
Preguntas de reflexión: 
• ¿Qué resultado se obtiene al ingresar 0°C? 
    En el caso de esta aplicacion devuelve 32 °F porque es la conversion exacata. 
• ¿Cómo se adaptaría este ejercicio para convertir a Kelvin? 
    Se podria agregar una variable que contenga Grados_Celsius + 273.15 lo que seria la conversion a Kelvin
"""
"""
================================================================================================================================================================================================================================================
Ejercicio 3: Uso de booleanos 
Objetivo: Manipular variables booleanas y aplicar operadores lógicos.
"""
"""
Instrucciones: 
1. Declarar dos variables booleanas: a = True, b = False. 
2. Realizar e imprimir los resultados de las operaciones: 
o a and b 
o a or b 
o not a, not b
"""

# 1. Declarar dos variables booleanas: a = True, b = False.
a = True
b = False

# 2. Realizar e imprimir los resultados de las operaciones:

resultado_and = a and b #guardando en la variable el resultado de a and b
print(f"a and b: {resultado_and}") #mostrando el resultado por consola

resultado_or = a or b #guardando en la variable el resultado de a or b
print(f"a or b: {resultado_or}") #mostrando el resultado por consola

resultado_not_a = not a #guardando en la variable not a
print(f"not a: {resultado_not_a}") #mostrando el resultado por consola

resultado_not_b = not b # guardando en la variable not b
print(f"not b: {resultado_not_b}") #mostrando el resultado por consola

"""
Preguntas de reflexión: 
• ¿Cuál es la utilidad de los operadores lógicos en programas más 
complejos? 
    Para el control de flujo del codigo, tambien para seleccionar datos de una lista por ejemplo : traeme este dato si cumple con estas condiciones Y(and) estas otras condiciones.
• ¿Qué representa cada operación?
    and = conjuncion (TRUE si ambos operandos son TRUE)
    or = disyuncion (TRUE si al menos uno de los operandos es TRUE)
    not = negacion (devuelve el valor booleano opuesto del operando (si es TRUE devuelve FALSE))
"""
"""
================================================================================================================================================================================================================================================
Ejercicio 4: Prueba de escritorio 
Objetivo: Analizar el funcionamiento del código y predecir su resultado.
"""
"""
Instrucciones: 
1. Leer el siguiente código: 
a = 5   
b = 3   
c = a + b   
a = 2   
print(c) 
2. Realizar una prueba de escritorio paso a paso. 
3. Determinar qué imprime el programa y por qué. 
"""

a = 5  #valor de la variable a
b = 3   #valor de la variable b
c = a + b   #valor de la variable c la suma de a + b
a = 2   #valor de la variable a
print(c) #mostrar el valor de c por consola

"""
Preguntas de reflexión: 
• ¿Por qué el cambio en a no afecta al valor de c?
    Porque si bien a esta modificado antes de mostrar c, la variable c no se vuelve a modificar para aplicar los cambios de a
• ¿Qué pasa si se imprime a y b al final?
    mostrara a = 2 y b = 3
"""
"""
================================================================================================================================================================================================================================================
Ejercicio 5: Diagrama de flujo  Cuadrado de un número 
Objetivo: Representar visualmente un algoritmo sencillo.
"""
"""
Instrucciones: 
1. Dibujar un diagrama de flujo para un programa que: 
o Pide al usuario un número. 
o Calcula su cuadrado. 
o Muestra el resultado. 
2. Implementar el programa en código si lo deseás. 
"""
n = int(input("Ingrese un numero: "))
c = n ** 2
print(c)

"""
Preguntas de reflexión: 
• ¿Qué ventajas tiene el uso de diagramas de flujo? 
    Permite planificar mejor el codigo y saber detectar cuando no entendemos bien algo, si podemos dibujarlo bien es porque entendemos el paso a paso del codigo bien.
• ¿Cómo se representa una operación matemática en un diagrama?
    Con un rectangulo donde dentro ponemos la operacion matematica
"""

"""
================================================================================================================================================================================================================================================
Ejercicio 6: Intercambio de variables 
Objetivo: Intercambiar valores sin usar una variable temporal.
"""
"""
Instrucciones: 
1. Declarar dos variables: x = 10, y = 20. 
2. Intercambiar sus valores usando operaciones aritméticas. 
3. Mostrar los valores antes y después del intercambio.
"""

# 1. Declarar dos variables: x = 10, y = 20.
x = 10
y = 10

# 3. Mostrar los valores antes del intercambio.
print(f"Valores antes del intercambio: x = {x}, y = {y}")

# 2. Intercambiar sus valores usando operaciones aritméticas.
x = x + y  # x ahora contiene la suma de los valores originales (10 + 20 = 30)
y = x - y  # y ahora contiene el valor original de x (30 - 20 = 10)
x = x - y  # x ahora contiene el valor original de y (30 - 10 = 20)

# 3. Mostrar los valores después del intercambio.
print(f"Valores después del intercambio: x = {x}, y = {y}")

"""
Preguntas de reflexión: 
• ¿Cómo funciona el intercambio sin variable auxiliar?
    Se van manipulando los valores de las variables con las operaciones hasta terminar con los valores originales pero en las variables cambiadas
• ¿Qué pasa si los valores iniciales son iguales? 
    Los valores son intercambiados sin problemas aunque enrrealidad no cambian el programa funciona sin problemas.
"""
"""
================================================================================================================================================================================================================================================
Ejercicio 7: Cálculo del IMC (Índice de Masa Corporal) 
Objetivo: Aplicar fórmulas con variables numéricas ingresadas por el usuario. 
"""
"""
Instrucciones: 
1. Solicitar al usuario su peso en kg y su altura en metros. 
2. Calcular el IMC con la fórmula: IMC = peso / (altura ** 2). 
3. Mostrar el resultado con un mensaje como: "Tu IMC es: 22.5". 
"""
peso = float(input("Ingrese su peso en kg : "))
altura = float(input("Ingrese su altura en metros : "))
calcular_IMC = peso / (altura ** 2 )
print(f"Segun tu {peso} y tu {altura} tu IMC es {calcular_IMC}")

"""
Preguntas de reflexión: 
• ¿Qué rango se considera saludable para el IMC? 
    Segun la OMS un rango saludable esta entre 18.5 y 24.9
• ¿Cómo podrías dar una recomendación según el resultado? 
    segun el rango que brinda la OMS, podrias usar el resultado para saber si estas bajo de peso, estas saludable o tienes sobrepeso.
"""
"""
================================================================================================================================================================================================================================================
"""
"""
Ejercicio 8: Contador de caracteres en un nombre 
Objetivo: Aplicar operaciones con cadenas de texto.
"""
"""
Instrucciones: 
1. Pedir al usuario que ingrese su nombre completo. 
2. Calcular y mostrar: 
o La cantidad total de letras (sin contar espacios). 
o Las primeras 3 letras del nombre. 
o El nombre con letras en mayúsculas y minúsculas alternadas 
(ejemplo: "JuAn PeReZ").
"""

nombre_completo = input("Ingrese tu nombre completo: ") #Solicitando el nombre al usuario
total_letras = 0 #Inicializando contador para la cantidad de letras
nombre_alternado = "" #variable str para depositar las variables alternadas
alternar = True #bandera para ir alternando entre mayusculas y minusculas
    #Recorrer cada letra del nombre
for letra in (nombre_completo):
    #verifica que letra no sea un espacio
    if letra != ' ':
        total_letras += 1 # sumar 1 al contador para contar la cantidad de letras
primeras_tres_letras = nombre_completo[:3] #guardando en una variable las primeras 3 letras del nombre
    #Recorrer el nombre completo
for letra in nombre_completo: 
    #Verifica que letra no sea un espacio vacio
    if letra != ' ': 
        if alternar: # si bandera es TRUE
            nombre_alternado += letra.upper() #Inserta la letra en la variable pero en mayuscula 
        else: # Si bandera es FALSE
            nombre_alternado += letra.lower() #Inserta la letra en la variable pero en minuscula
        alternar = not alternar  # Cambiar el estado para la siguiente letra
    else:
        nombre_alternado += ' '  # Mantener los espacios como están
    #Mostrando todo por consola
print(f"La cantidad de letras del nombre sin contar espacios son: {total_letras}")
print(f"Las primera tres lestras del nombre son: {primeras_tres_letras}")
print(f"Alternando las letras entre mayusculas y minusculas sin contar espacios quedaria asi: {nombre_alternado}")

"""
Preguntas de reflexión: 
• ¿Qué técnicas de manipulación de strings estás usando?
    Estoy usando input para ingresar el nombre, for para recorrer y tomar cada letra y if para diferenciarlo, y upper y lower para ir ingresando cada letra en otra variable.
• ¿Cómo podrías extender este ejercicio para apellidos?
    El usuario simplemente podria ingresar su apellido junto al nombre completo.
"""
"""
================================================================================================================================================================================================================================================
Ejercicio 9: Operaciones con números flotantes 
Objetivo: Realizar distintas operaciones matemáticas con decimales.
"""
"""
Instrucciones: 
1. Declarar: 
o a = 7.5 
o b = 3.2 
2. Calcular y mostrar: 
o La suma (a + b) 
o El redondeo de la división (a / b) a 2 decimales 
o La potencia (a ** b)
"""
a = 7.5
b = 3.2
suma = a + b
division = a / b
potencia = a ** b
redondeo = round(division,2)
print(f"la suma de {a} y {b} es: {suma}")
print(f"El redondeo de la division ({a} / {b}) a 2 decimales es: {redondeo}")
print(f"la potendia de ({a} ** {b}) es: {potencia}")

"""
Preguntas de reflexión: 
• ¿Qué ocurre si redondeás a más decimales?
    Te muestra mas decimales hacia la derecha del numero
• ¿Cuándo conviene usar math.pow()? 
    el modulo math.pow() siempre devuelve un numero flotante aunque sea un entero, en algunas situaciones puede ser necesario que el resultado sea un float
"""
"""
================================================================================================================================================================================================================================================
"""
"""
Ejercicio 10: Descuento sobre precio original 
Objetivo: Aplicar porcentajes y mostrar el resultado.
"""
"""
Instrucciones: 
1. Pedir al usuario el precio original de un producto. 
2. Pedir el porcentaje de descuento. 
3. Calcular el precio final: 
precio_final = precio_original * (1 - (descuento / 100)) 
4. Mostrar el precio con descuento. 
5. (Opcional) Dibujar un diagrama de flujo del proceso.
"""
precio_original = float(input("Ingrese el precio original: ")) #Ingresa el precio original
descuento = float(input("Ingrese el porcentaje de descuento: ")) #Ingrese el porcentaje de descuento
    # Calcular el precio final
precio_final = precio_original * (1 - (descuento / 100 )) #formula para el descuento
print(f"el precio final es : {precio_final}") #mostrar el precio final por consola
"""
Preguntas de reflexión: 
• ¿Qué ocurre si el descuento es mayor a 100%? 
    Si se ingresa un porcentaje mayor a 100% devolveria como resultado un precio final negativo lo que no seria util en un ambito comercial.
• ¿Cómo podrías mostrar el monto ahorrado? 
    Se podria crear otra variable mas donde guardamos la resta del precio final al precio original y mostrarlo por consola.
"""