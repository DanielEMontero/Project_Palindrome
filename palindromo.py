##################################################################
##################################################################

##################### PROGRAMA PALINDROMO ########################

# Descripción: Programa que te permite validar si la palabra ingresada
# o no un palíndromo.

###################################################################

# Author: DANIEL EDUARDO MONTERO RAMÍREZ 

###################################################################
def palindromo(palabra):
        palabra = palabra.lower()
        palabra = palabra.replace(' ','')
        if palabra[::-1] == palabra:
            return True
        else:
            return False


def run():
    palabra = input('Por favor ingrese una palabra: ')
    if palindromo(palabra) == True:
        print('Es un Palíndromo')
    else:
        print('No es un Palíndromo')


if __name__ == '__main__':
    run()
