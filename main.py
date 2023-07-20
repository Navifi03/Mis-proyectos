x = 20
print(x)
print(type(x))
x = 20
y = 10
Suma = 20 + 10
print(Suma)
print(type(Suma))
Resta = 20 - 10
print(Resta)
print(type(Resta))
Multiplicacion = 20 * 10
print(Multiplicacion)
print(type(Multiplicacion))
Division = 20 / 10
print(Division)
print(type(Division))
valor = int(input("colocar aqui un numero entero:"))
valor = int(input("colocar aqui un numero entero:"))
if valor % 4 == 0:
  print("El numero es par")
else:
  print("El numero es Impar")


def mostrar_anterior_posterior(año):
  print(año - 1)
  print(año + 1)


mostrar_anterior_posterior(1994)
numero = int(input("ingrese un numero "))
otro_numero = int(input("ingrese otro numero "))
otro_numero2 = int(input("ingrese otro numero "))
otro_numero3 = int(input("ingrese otro numero "))
otro_numero4 = int(input("ingrese otro numero "))
suma = numero + otro_numero + otro_numero2 + otro_numero3 + otro_numero4
print(suma)
Resultado = suma / 5
print(Resultado)


def mostrar_anterior_posterior(numero):
  print(numero - 1)
  print(numero + 1)


mostrar_anterior_posterior(10)
nombre = str(input("Coloca aqui tu nombre: "))
apellido = str(input("Coloca aqui tu apellido: "))
edad = int(input("Coloca aqui tu numero de edad: "))

print(apellido + "," + nombre + ".", "tienes:", edad)


def resto_cociente(entero):
  resto = print(entero % entero)
  cociente = print(entero / entero)
  return resto, cociente


resto_cociente(10)
nombre = input("Coloca tu nombre aqui: ")
apellido = input("Coloca tu apellido aqui: ")
nombre_completo = ("{},{}".format(apellido, nombre))
print(nombre_completo)
palabra = input("Escribe una palabra: ")
cantidad = len(palabra)
print(cantidad)

Palabra = input("Coloca una palabra de mas de 5 caracteres: ")
Palabra_corta = Palabra[:5:]
print(Palabra)
Palabra = input("Introdusca una palabra: ")
Palabra_sin_A = "Aa"
nuevapalabra = ""
for letra in range(len(Palabra)):
  if Palabra[letra] not in Palabra_sin_A:
    nuevapalabra += Palabra[letra]
print(nuevapalabra)
