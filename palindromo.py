##################################################################
##################################################################

##################### PROGRAMA PALINDROMO ########################

# Descripción: Programa que te permite validar si la palabra ingresada
# o no un palíndromo.

###################################################################

# Author: DANIEL EDUARDO MONTERO RAMÍREZ 

###################################################################


palabra = input("Por favor ingrese una palabra: ")

palabra = palabra.lower()
palabra = palabra.replace(" ","")

if palabra[::-1] == palabra[::1]:
    print("Es un Palíndromo")
else:
    print("No es un Palíndromo")
