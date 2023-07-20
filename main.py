# 1. Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número 5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0.

lista_numeros1 = list(range(1,11))
print(lista_numeros1)
print(lista_numeros1 [4])

#2. Con la lista del punto anterior, usar la función len() para averiguar su longitud, e imprimirla.

lista_numeros1 = list(range(1,11))
longitud_lista=len(lista_numeros1)
print(longitud_lista)

#3. Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo.


lista_numeros=[1,2,5,7,90,80,100]
numero_maximo = lista_numeros [0]
for numero in lista_numeros:
 if numero > numero_maximo:
  numero_maximo = numero
print(numero_maximo)

numero_minimo = lista_numeros [0]
for numero in lista_numeros:
 if numero < numero_minimo:
  numero_minimo = numero
print(numero_minimo)

#4. Ordenar la secuencia del ejercicio anterior, e imprimirla por pantalla.

lista=[2,1,3,4,5,9,8,7,6]
lista.sort()
print (lista)

# 5.Crear una tupla que guarde tu nombre y tu edad. Luego, imprima por pantalla su edad, accediendo al elemento de la tupla que corresponda.
persona=('Naholy',29)    
print(persona[1])

# 6.Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
# a.Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. ¿Cómo podría saber cuál es el último elemento si no sé la longitud?
# b.Devolver el nombre que esté a dos posiciones del final.
# c.Recorrer la lista e imprimir cada nombre por pantalla.
# d.Imprimir por pantalla la lista con 3 repeticiones, usando el operador repetición(*).

nombres=['pablo','alejandro ','martin','Pedeo','pablo']
nombres[len(nombres)-1]='jose'
print(nombres)
print(nombres[len(nombres)-3])
para nombres en nombres:
   print(nombre)
    nombre+=' '
    Print(nombre*3)

#7. Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación,guardarlas en una lista.Ejercicios con listas y tuplascon el siguiente formato:País: <nombre>Capital: <capital>Continente: <continente>Por ejemplo:País: JapónCapital: TokioContinente: Asia
 persona=('pepe',66)
persona2=('pepa',27)
 persona3=('pepo',9)
todas las personas = [] todasLasPersonas.append(persona) todasLasPersonas.append(persona2)
 todasLasPersonas.append(persona3)
 print (todas las personas)

# 8.Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
# a.Crear una tupla para cada país que contenga su nombre, su capital y el continente donde seencuentra.
# b.Guardar las tuplas en una lista.
# c.Hacer una función que reciba por parámetros la lista, e imprima la información de cada paíscon el siguiente formato:País: <nombre>Capital: <capital>Continente: <continente>
# Por ejemplo: País: Japón Capital: Tokio Continente: Asia

pais=('francia','paris','europa')
pais2=('argentina','buenoaires','sudamerica')
pais3=('japon','tokio','asia')
pais4=('alemania','berlin','europa')
pais5=('peru','lima','sudamerica')
paises=[pais,pais2,pais3,pais4,pais5]
def infoPaís(lista):
 pais,capital,continente=lista
 return f'País: {pais} \nCapital: {capital} \nContinente: {continente}'
a=infoPaís(país2)
 imprimir (a)

# 9.Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la siguiente forma: [“El principito", "It", "Sherlock Holmes”...]. Se quiere saber cuantos libros repetidos tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
libros=["El principito", "It", 'Sherlock Holmes',"it"]
librosFormados=[]
def comprobarRepetidos(libroo):
librooLower=libroo.lower()
para libro en libros:
 librosFormados.append(libro.lower())
print(librosFormados.count(librooLower))
comprobarRepetidos('iT')

# 10.Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos números elevados al cuadradO
lista=[1,2,3,4,5,6,7,8,9,10]
listaAlCuadrado=[]
para num en lista:
listaAlCuadrado.append(num*num)
print(listaAlCuadrado)


# 11.Se tiene la siguiente lista de palabras: [“entender", "pueden", "humanos", "los", "que", "código","escriben”, ”programadores", "buenos", "Los ", "entiende.", "computadora", "una", "que", "código","escribe", "tonto", "Cualquier”]. Hacer una función que reciba una lista, y devuelva una cadena uniendo las palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formar la frase.
# listaDePalabras=["entender", "pueden", "humanos", "los", "que", "código","escriben","programadores", "buenos", "Los", "entiende.", " computadora", "una", "que", "código","escribe", "tonto", "Cualquier"]

def unionReverse(lista):
 oracion=''
 #para palab en lista:
oracion=palabra+ ' '+oracion
#volver oracion

print(unionReverse(listaDePalabras))

# 12.Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que vahaciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e irguardando la información en una lista hasta que ingrese una 'X'.AYUDA: para guardar elementos nuevos en una listausamos el métodoappend().

materias=[]
def almacenes():
materia=''
while(no materia=='x'):
materia=input("que materia queres almacenar? \ncuando no tengas q agregar mas, pone X\n")
materias.append(materia)
 if(materias.contar('x')):
materias.remove('x')
imprimir(materiales)
almacenes()


# 13.Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto,precio).
# a.Hacer una función que reciba la lista y calcule y devuelva el total que hay que pagar.
# b.Ahora se tienen dos entradas. Juntar ambos y volver a calcular el total

ticket=(['cocacola',15],['carne',20],['chicles',2])
ticket2=(['agua',15],['lechuga',20],['almendras',5])
def preciototal(lista):
precioTotal=0
para prodPrecio en lista:
precio=prodPrecio[1]
precioTotal+=precio
devolver precioTotal
print(preciototal(boleto))
def preciostotales(listas):
  imprimir(listas)
precioTotal=0
# para boleto en listas:
#para precioAndProd en ticket:
precio=precioYProd[1] precioTotal+=precio
#devolver precioTotal
print(preciostotales([ticket,ticket2]))
  