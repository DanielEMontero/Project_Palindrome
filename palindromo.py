palabra = input("Por favor ingrese una palabra: ")

palabra = palabra.replace(" ","")

if palabra[::-1] == palabra[::1]:
    print("Es un Palíndromo")
else:
    print("No es un Palíndromo")
