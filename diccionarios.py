def run():
    mi_diccionarios = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,

    }

    print(mi_diccionarios['llave1'])
    print(mi_diccionarios['llave2'])
    print(mi_diccionarios['llave3'])
    
    poblacion_paises = {
        'Argentiana': 44258963,
        'Brasil': 201489325,
        'Colombia': 50372424,
      

    }

    
    #for pais in poblacion_paises.keys():# Retorna los nombres de los paises
    #    print(pais)

    #for pais in poblacion_paises.values(): # Retorna el valor de la poblacion del pais
    #    print(pais) 

    for pais, poblacion in poblacion_paises.items():# Retorna los valores
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')



if __name__ == '__main__':
    run()