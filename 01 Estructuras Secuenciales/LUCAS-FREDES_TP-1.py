"1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”"
#print('Hola Mundo')

"2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando"
#nombre = input('Ingrese su nombre: ')
#print(f"Hola {nombre}!")

"3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados"
#nombre = input('Ingrese su nombre: ')
#apellido = input('Ingrese su apellid: ')
#edad = int(input('Ingrese su edad: '))
#residencia = input('Ingrese su pais de residencia: ')
#print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

"4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro"
#pi = 3.14159
#radio = float(input("Ingrese el radio del circulo "))
#area = pi * radio ** 2
#perimetro = 2 * pi * radio
#print (f"El area del circulo es: {area} y el perimetro es: {perimetro}")

"5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale."
#segundos = int(input("ingrese la cantidad de segundos: "))
#if segundos < 3600:
#    minutos = segundos // 60
#    print(f'ingresaste una cantidad de segundos menor a una hora, son: {minutos} minutos')
#else:
#    horas = segundos // 3600
#    print(f"s0
#n: {horas} horas")

"6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número."
#numero = int(input('Ingrese el numero para saber su tabla: '))
#for i in range (1,11):
#    result = numero * i
#    print(f"{numero} x {i} = {result}")

"7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."
#numero1= int(input('ingrese un numero distinto de 0: '))
#while numero1 == 0:
#    numero1= int(input('ingresaste 0, porfavor ingresa un numero distinto de 0:  '))
#numero2= int(input('ingrese otro numero distinto de 0: '))
#while numero2 == 0:
#    numero2= int(input('ingresaste 0, porfavor ingresa un numero distinto de 0:  '))
#resultado = numero1 + numero2
#print(resultado)

"8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:"
#altura = float(input('Ingresa tu altura en metros: '))
#peso = float(input('Ingresa tu peso en kilogramos: '))
#imc = peso / (altura ** 2)
#print(f"Su indice de masa corporal es {round(imc,2)}")

"9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: "
#celsius= float(input('Ingresa la temperatura en Celsius: '))
#Fahrenheit = (celsius * 9/5) + 32 
#print(f"La temperatura en Fahrenheit es: {Fahrenheit} ")
" 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de  dichos números."
#numero1= float(input('Ingrese el primer numero: '))
#numero2= float(input('Ingrese el segundo numero: '))
#numero3= float(input('Ingrese el tercer numero: '))
#promedio = numero1 + numero2 + numero3 / 3
#print(f"El promedio de los tres numeros es: {round(promedio,2)}")