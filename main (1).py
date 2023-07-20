#Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipobool e imprimirla por pantalla para ver su valor. 

Valor_1 = input("Ingrese un valor: ")
Valor_2 = input("Ingrese otro valor: ")
A = Valor_1 > Valor_2
B = Valor_2 > Valor_1
if A:
   print (Valor_1, "." , "es mayor al", ".", Valor_2)
elif B:
 print (Valor_2, "." , "Es mayor al", ".", Valor_1)
  # Punto 2 -- Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.

Con_Vocales= input("Ingrese una letra en minuscula: ")
Vocales = ["a","e","i","o","u"]

if Con_Vocales in Vocales:
  print ("La letra es una vocal")
else:
  print ("La letra no es una vocal")


# Punto 3 -- Repetir pero para la expresión que permite saber si un número es par y menor a 10

numero = int(input ("Ingresar un numero entero: "))

Variable_1 = numero % 2 == 0
Variable_2 = numero < 10

if Variable_1 and Variable_2:
  print ("El numero", ".", (numero), "." "es par y es menor a 10")
elif Variable_1 and not Variable_2:
  print ("El numero", ".", (numero), "." "es par y  mayor a 10")
elif not Variable_1 and Variable_2:
  print ("El numero", ".", (numero), "." "no es par y  es menor a 10")
elif not Variable_1 and not Variable_2:
    print ("El numero", ".", (numero), "." "no es par y  es mayor a 10")
 
# Punto 4 -- Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es el mismo número sin considerar el signo. Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4)

def Valor_Absoluto (entero):
  
  Situacion_1 = entero < 0

  if Situacion_1 :
   print ("El absoluto de"," ",entero," ","es",-entero)
    
  else:
    print ("El absoluto de"," ",entero," ","es",entero)
  
Valor_Absoluto (156)
    
#5Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento vaa ser representado con una letra: R para piedra, P para papel y T para tijera.a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantallala jugada para ganarle. Por ejemplo:¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T) p Tijera. ¡Te gané!ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tieneque hacer (en este caso ingresar alguna de las tres letras).b Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida(distinta de R, P o T)
def jugar():
  print("¡Juguemos! Ingresá piedra(R),papel (P)o tijera (T)")
jugada=input()
if(jugada=='P'):
  print("Tijera") 
elif(jugada=='R'):
  print("papel")
elif(jugada=='T'):
  print("Piedra")
else:
 print("No vale")
jugar()

# Punto 6 -- Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”. Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del usuario, y no solo para 100?.

valor_1 = int(input ("Ingrese un numero entero: "))
valor_2 = int(input ("Ingrese otro numero entero: "))

suma = valor_1 + valor_2 
menor = suma < 100
mayor = suma > 100 
igual = suma == 100
falta = 100 - suma 

if menor:
  print("La suma de ambos numeros es menor a 100")
  print("Para llegar a 100 se necesita",(falta))
elif mayor:
  print ("La suma de ambos numeros es mayor a 100")
elif igual:
  print("La suma de ambos numeros es igual a 100")

#Punto 6 -- Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”. Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del usuario, y no solo para 100?.

valor_1 = int(input ("Ingrese un numero entero: "))
valor_2 = int(input ("Ingrese otro numero entero: "))

suma = valor_1 + valor_2 
menor = suma < 100
mayor = suma > 100 
igual = suma == 100
falta = 100 - suma 

if menor:
  print("La suma de ambos numeros es menor a 100")
  print("Para llegar a 100 se necesita",(falta))
elif mayor:
  print ("La suma de ambos numeros es mayor a 100")
elif igual:
  print("La suma de ambos numeros es igual a 100")

# Punto 7 -- Se tienen letras para representar las estaciones del año: V para verano, O para otoño, I para invierno, P para primavera. Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O, B, V e I.

def Estaciones():
  print("!!Juguemos a sacar una estacion del Año!!")

  jugada = input("Ingresa una Letra en MAYUSCULA: ")
  
  if(jugada =='V'):
   print("V de Verano") 
    
  elif(jugada =='O'):
   print("O de Otoño")
    
  elif(jugada =='I'):
   print("I de Invierno")

  elif(jugada =='P'):
   print("P de Primavera")
  
  else:
   print("Error, ninguna estacion del año comienza con esa letra")
    
Estaciones()

# Punto 8 -- Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control iterativa for

numero = int(input ("Ingresa un numero entero: "))

for numero in range (1,1+numero,):
  print (numero)

#9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora senecesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un número entero e imprima por pantalla la tabla de ese número del 1 al 10.

def tabla(numero):
  for i in range(1,11):
    print(i*numero)
tabla(1) 

#Punto 10 -- Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa cantidad de veces

Veces = int(input("Ingrese un numero entero: "))

cancion = " Que los cumplas feliz " * Veces
print (cancion)

# Punto 11 -- En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago. Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
#> El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
#> 10
#> El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
#> 15
#> El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
#> 5

def cajero(monto):
   print(f"El monto a pagar es de {monto} pesos")
   pago = float(input("Ingrese un monto: "))
   if monto > pago:
      monto -= pago
      cajero(monto)
   elif monto < pago:
      print(f"Gracias por comprar, vuelto: {pago - monto}")
   elif monto == pago:
      print("Gracias por su compra")
cajero(4000)



# Punto 12 --  Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar, imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería:
# > El número 1 es impar.
# > El número 2 es par.

numero = 1
while (numero < 20):
 for numero in range (1,21,):
  Variable_a = numero % 2 == 0
  Variable_b = numero % 2 != 0

  if Variable_a:
   print ("El numero", "" , (numero), "", "es par")
  elif Variable_b:
   print ("El numero", "", (numero), "", "es impar")
numero = numero + 1

# Punto 13 -- Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de fichas, y se quiere hacer una función que imite ese comportamiento. 

# A. Hacer una función que reciba un número que represente el precio de la máquina, e imprima por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de letras F (que representan una ficha), y luego “¡A jugar!” cuando se hayan ingresado todas las fichas necesarias. Por ejemplo, si la función recibe 3, debería tener el siguiente comportamiento:
# > Ingresá 3 fichas para comenzar
# > F
# > Ingresá 3 fichas para comenzar
# > F
# > Ingresá 3 fichas para comenzar
# > B
# > Ingresá 3 fichas para comenzar
# > F
# > ¡A jugar!

# B. Ahora se quiere que se vaya mostrando por pantalla, cuántas fichas FALTAN ingresar para empezar a jugar Es decir:
# > Ingresá 3 fichas (F) para comenzar
# > F
# > Ingresá 2 fichas (F) para comenzar
# > F
# > Ingresá 1 fichas (F) para comenzar
# > B
# > Ingresá 1 fichas (F) para comenzar
# > F
# > ¡A jugar!

def fichas(monto):
   print("Ingrese 3 fichas para jugar")
   pago = int(input("Ingrese su fic: "))
   if monto > pago:
      monto -= pago
      fichas (monto)
   elif monto < pago:
      print(f"Gracias por comprar, vuelto: {pago - monto}")
   elif monto == pago:
      print("Gracias por su compra")
fichas(3)


# C. Agregar a la función el mensaje de error “Por favor solamente ingrese fichas reales (F)” cuando se recibe una letra distinta de F.


print("Ingrese 3 fichas para jugar")
fichas = (3)
pago = int(input("Ingrese su ficha: "))
while pago <= fichas:
  if pago == fichas:
   print("¡A jugar!")
  elif pago < fichas:
   print ("Ingrese", fichas - pago , "fichas para jugar")
  break

#14Crear una función que reciba un número entero e imprima los números primos entre 0 y el númeroingresado.AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para versi es primo hay que ver que el módulo (%) de


primo = int(input ("ingrese un numero entero: "))
for n in range (0, primo+1):
  if n%2 == 0:
    print (n)