##################################################################
##################################################################

##################### PALINDROME PROGRAM ########################

# Description: This program let you know if the insert word is or not is
# a palindrome. 

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
    palabra = input('Please insert a word: ')
    if palindromo(palabra) == True:
        print('Is a Palindrome')
    else:
        print('Is not a Palindrome')


if __name__ == '__main__':
    run()
