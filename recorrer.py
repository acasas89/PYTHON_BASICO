def run():
   # nombre =input('Cual es tu nombre: ')# Se inicia el codigo para que se recorra todas las letras del  que se escriban en el imput
    #for letra in nombre:
    #    print(letra)

    frase = input('Escribe una frase: ')
    for caracter in frase: # la palabra caracter no es obligatoria puede ser cualquiera
        print(caracter.upper())


if __name__ == '__main__':
    run()
