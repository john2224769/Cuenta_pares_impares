# Hacer el diagrama de flujo y el programa en python que lea numeros enteros y positivos (uno) en cada lectura y que averigue e imprima cuantos son pares y cuantos son impares.
# Para terminar utilizaremos el registro centinela cuado el valor del numero leido sea cero 

from os import system
print("\n----------------------------------------------------")
print("------- Programa para contar pares e impares ---------")
print("----------------------------------------------------\n")

#input

n=int(input("Ingrese un numero entero positivo "))

#processing

cont_pares=0
cont_impares=0

while n!=0:
    if n%2==0:
        cont_pares=cont_pares+1
    else: 
        cont_impares=cont_impares+1

    system("clear")
    n=int(input("\n Ingrese un numero entero positivo "))

print("\nLa cantidad de numeros pares es de: "+str(cont_pares))
print("\nLa cantidad de numeros impares es de: "+str(cont_impares))
print(" ")