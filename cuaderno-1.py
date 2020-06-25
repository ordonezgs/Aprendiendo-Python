#ESTE ES UN MENSAJE DENTRO DEL CODIGO EN PYTHON, se usa el (#)
print('###CLASE 1# -- Comentarios##')
print('Hola Mundo')

#Tipos de datos
print('###CLASE 2 - Tipos de Datos###')
##Strings (No permite ```String de estas comillas``` ni simples)
print('String1')
print("String2")
print("""String3""")
print('''String4''')
##Específica que tipo de dato es, TYPE palabra reservada
type("Hello World")

"Bye" + "World" #Dice "Bye World"
##Numeros
##Integer o entero
print(30)
##Float o decimal
print(30.5)
print(type(30))
##Boolean
True
False #Parece que debe tener si o si la primera en mayus
##List (Tipo de dato para Arrays)
[10, 20, 30, 55]
["Hello", "Bye", "Adios"]
[10, "Hello", True]
##Tuplas [Datos inmutables], es decir, fijos y no cambian [Arrays que no cambian]
(10, 20, 30, 55)
##Diccionarios (Solo datos de la misma entidad) [Otro tipo de array]
{
	"nombre de la persona":"Ryan",
	"apellido":"Ray",
	"apodo":"Fazt"
}
{
	"lat": 20192,
	"long": 2020
}
##Tipo de datos vacíos (Palabra reservada)
None
#Variables y Constantes
print('###CLASE 3 - Variables y Const###')

##Ejemplo de Variables
name = "Fast"
_Var2 = "Fast"
Var2_cont = "Fast"
name1, _Var2 = _Var2, 100 #Valores en 2 variables (Primer var antes de coma es la def)

##Ejemplo de Constantes
TODOMAYUSCULA = "Esto es una constante"
MY_NAME = "Esto tambien es una constante"

##Trabajando con variables, reasignando Valores
name = "Fast cambiado"
#Trabajando con Strings
print('###CLASE 4 - Strings###')
myStr = "Hola Mundo"
##Palabra reservada dir, para ver que hacer con ese tipo de dato
dir(myStr)
print(dir(myStr)) ##Ver propiedades y metodos de mi variables o en este caso de mi string
print(myStr.upper()) #con el metodo que busqué con el dir, usa el metodo uppr para convertir el texto a mayuscula
print(myStr.lower()) #convierte el texto a minusculas
print(myStr.swapcase()) #Convierte el texto minuscula a mayus y viceversa
print(myStr.capitalize())#Primera letra del string a mayus
print(myStr.replace('Hola', 'Adios')) #Busca y reemplaza el texto de mi string seleccionado
print(myStr.replace('Hola', 'Adios').upper())#Ejecuta lo de arriba y lo pasa a mayus
print(myStr.count('o'))#Me busca y pregunta la cantidad de letra especificada en mi string
print(myStr.startswith('hola'))#Retorna un booleano de si el texto empieza con la palabra hola (Case Sensitive) //False
print(myStr.replace('Hola', 'hola').startswith('hola'))#Yo jugando con el código //Retorna true
print(myStr.endswith('Mundo'))# //True
print(myStr.split())#Separa el texto en caracteres en blanco, Retorna una list(array)//['Hola', 'Mundo']
print(myStr.split(','))#Separa el texto a partir de lo designado
print(myStr.find('o'))#Encuentra la posición del caracter en la string
print(len(myStr))#Longitud del string, todas son funciones de python
print(myStr.index('a'))#Basicamente es como el find
print(myStr.isnumeric())#Es numero ?
print(myStr.isalpha())#Es alfa numerico ?
####
print(myStr[4])#Obtiene el indice 4 de mi string
print(myStr[-1])#Obtiene el indice de mi string pero a la inversa, es decir en este caso la ultima letra
####
## Concatenando strings
print('Mi nombre es ' + myStr)
print(f'Mi nombre es {myStr}')#Ver reservado f y las llaves [SOLO DISPONIBLE EN Python 3.6 +]
print('Mi nombre es {0}'.format(myStr))#.format y lo que deba ser interpretrado se referencia por index del format
#Numeros
print('###CLASE 5 - Numeros###')
10
14.4
print(type(9))
print(type(10.1))
###Se soportan todas las operaciones básicas (tipo JS), sumar dividir multiplicar modulo y otras
##Elevando al cuadrado al cuabo etc
2**2# El numero 2 elevado al cuadrado
2**3# El numero 2 elevado al cubo
#Inputs
print('###CLASE 6 - Requiriendole al usuario###')
###Todos los input llegan como strings
edad = input('Solicito su edad, ingrese su edad para almacenarla en la variable "edad":')#input
nueva_edad = int(edad) + 5 ###Le asigne un tipo de dato a edad de Int (numero entero)
print(nueva_edad)#Muestra la edad ingresada + 5
#Listas
print('###CLASE 7 - Listas o Arrays o Arreglos###')
##Ejemplos de listas
lista_demo = [1, 'Hola', 1.34, True, [1, 2, 3, 4]]
colores = ['red', 'green', 'blue']
##Pasando una funcion de python para crear una lista
lista_de_numeros = list((1,2,3,4)) #Se crea una lista, se añade una tupla ya que list solo recibe un argumento
##Usando funcion de python para un rango y pasandola a lista
lista_numeros_x = list(range(1, 10))#Valores del 1 al 9 que se vuelven lista y se almacenan en var Lista_numeros_x
print(lista_numeros_x)
##Viendo datos de una lista
print(type(colores))
print(dir(colores))#Viendo que puedo hacer con una lista
print(len(colores))#Cuantos elementos tiene var colores?
print(colores[1])#Retorna el color 1 de la lista
print(colores[-1])#Retorna el ultimo color de la lista
##Condicional de listas
print('green' in colores) #El color Green esta en var colores ?
print(colores)
##Reemplazando valores en la lista
colores[1] = 'yellow' #Cambiando Verde por Amarillo
print(colores)
colores.append('violet')#Agregando un elemento a la lista, solo recibe 1 elemento
colores.extend(['purple', 'orange'])#Agregando multiples elementos a ala lista
print(colores)
colores.insert(1, 'black') #Agregando un valor al lado de una parte del indice
colores.insert(len(colores), 'gray')#Agregando un color al ultimo
print(colores)
colores.pop()#Elimina el último elemento de la lista
print(colores)
colores.remove('red')#Eliminando el color verde de la lista, solo de la lista original :(
colores.pop(1)#Eliminando elemento segun indice
print(colores)
# colores.clear()#Elimina todos los elementos de la lista
# print(colores)
colores.sort()#Ordena los colores alfab.
#Tuplas
print('###CLASE 8 - Tuplas###')#Datos inmutables o fijos
jeje = (1, 2, 3)
##Pasando una funcion de python para crear una tupla
jeje_u = tuple((1, 2, 3))
##Palabra reservada para borrar definiciones de variables, tuplas, etc...
del jeje_u #Elimina la tupla de jeje_u
# locations = { ##NO SE PERO NO SIRVE ESTE PEDAZO DE CODIGO DA ERROR (AYUDAAAA)
# 	{35.12312, 39.000}:"Tokyo",
# 	{35.12312, 39.000}:"New York"# ejemplo de tupla para coordenada a ciudad
# }
#Sets
print('###CLASE 9 - Sets###') #Usados para definir coleccion que no tiene indice
colores_sets = {"Red", "Green", "Blue"}
print(colores_sets)
print('Red' in colores_sets)
colores_sets.add('Violet')
print(colores_sets)
colores_sets.remove('Red')
print(colores_sets)
colores_sets.clear()
print(colores_sets) #Retorna  al haber borrado el conjunto de datos// .set()
colores_sets = None
del colores_sets
#Trabajando con Diccionarios
print('###CLASE 10 - Diccionarios###')
carrito = {
	"nombre": "libro",
	"precio": 3,
	"cantidad": 4.99
}#Definidiendo el diccionario
persona = {
	"primer_nombre": "ryan",
	"segundo_nombre": "ray"
}
print(dir(persona))#Que puedo hacer con el diccionario
print(persona.keys())#Obteniendo llaves o valores que se han asignado ejemplo primer_nombre etc. Agrupandolo en una tupla
print(persona.items())#Obteniendo items o valores que se han asignado ejemplo el valor de primer_nombre etc. Agrupandolo en una tupla
del persona
##Diccionarios dentro de listas, ejemplo lista de productos
productos = [
	{"nombre": "libro", "precio": 10.99},
	{"nombre": "laptop", "precio": 10000}
]
print(productos)
#Condicionales
print('###CLASE 11 - Condicionales###')
edad = None # Me veo forzado declarar nada en el valor por la anterior declaracion
numerox = 10
##USANDO OPERADORES DE COMPARACION
if numerox < 20:
	print('X es menor que 20')
else:
	print('X es mayor que 20')

colorx = "blue"
if colorx == "red":
	print("El color es rojo")
elif colorx == "blue":
	print("El color es azul")
else:
	print("ni mierda jjajaja")
nombrex = "Julio"
if nombrex == "John":
	if apellido == "Carter":
		print("Hola John")
	else:
		print("Tu no eres John")
else:
	print("Ni mierda")

##OPERADORES LÓGICOS + OPERADORES DE COMPARACION
# OPERADORES : or not Y and
x = 20
if numerox > 2 and x <= 10:
	print("XD")
if numerox > 2 or x <= 10:
	print("XD X2")
# if (not(0 == 0)) #ESTE CODIGO NO FUNCIONA
# 	print("0 no es igual a 0 gracias al not en este condiciional")
#Ciclos
print('###CLASE 12 - FOR & While###')
foods = ["apples", "bread", "cheese", "milk", "bananas"] #Una simple lista
##Despues de la palabra reservada for crea una variable, ejemplo food
for food in foods:#Ciclo de busqueda de items de la lista de foods
	print(food)
	if food == "cheese":#Condicional de item siendo cheese
		print("Tienes que comprar esto: cheese")
		break#Detener el ciclo (Palabra reservada)
	elif not(food == "cheese"):
		continue #Continuar el ciclo (Palabra reservada)
for letra in "Hello":
	print(letra)#Imprime o muestra cada letra de la palabra hello
##Ciclo While
contador = 4
while contador <= 10:
	print(contador)
	contador = contador + 1 #Imprime numeros hasta el 10 desde el 4
#Funciones
print('###CLASE 13 - Funciones###')
##Ejemplos de funciones
# print()
# dir()
# type()
##Definiendo funciones Tipo 1
def hola():
	print("Hola Mundo")

def saludar(nombre):
	print("Hola, " + nombre)
def saludar2(nombre = "no hay nombre"):#Asignando un parametro por defecto
	print("Hola, " + nombre)
saludar("quien quiera que seas")
##Funciones tipo lambda, aunque en JS es como poner Array function
sumar = lambda numero1, numero2: numero1 + numero2
print(sumar(10,20))

#Modulos
print('###CLASE 14 - Modulos o Addons / Librerias###')
print('Existen: 3 tipos de modulos: propios (own modules), moduloes externos(thrid party modules) y los modulos de python(python modules)')
# para añadir modulos se añaden con la palabra reservada "import" y el nombre del modulo

##BUSCAR EN PYPI.ORG  o solo Python Modules en internet

##Ejemplos de importar 

# import datetime #importo todo detatime

# o

# from datetime import timedelta, date #Importo solo timedelta y date de datetime

#