import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#','$', '%', '/', '(', ')', '&']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = [] # se crea el vector o lista vacio

    for i in range(1, 15):
        caracter_random = random.choice(caracteres) # la funcion choice selecciona 15 valores de el arreglo caracteres al azar
        contrasena.append(caracter_random) # le enviamos los caracteres random a la lista o vector

    contrasena = "".join(contrasena) # convierte una lista o vector en un string
    return contrasena


def run():
    contrasena = generar_contrasena()
    print(' Tu nueva contraseña es:  ' + contrasena)


if __name__ == '__main__':
    run()
