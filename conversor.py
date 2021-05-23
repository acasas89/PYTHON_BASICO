def conversor(tipo_pesos, valor_dolar):
    pesos = input("cuantos pesos " + tipo_pesos + " tines?: ")
    pesos = float(pesos)
    dolares = pesos /valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")



menu ='''

Bienvenido al conversor de monedas
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos 
Elige una opcion:'''

opcion = int(input(menu))
if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print('ingresa una opcion correcta por favor')



#Codigo inicial largo
#opcion = int(input(menu))
#if opcion == 1:
#    pesos = input("cuantos pesos Colombianos tines?: ")
#    pesos = float(pesos)
#    valor_dolar = 3875
#    dolares = pesos /valor_dolar
#    dolares = round(dolares, 2)
#    dolares = str(dolares)
#    print("Tienes $" + dolares + "dolares")
#elif opcion == 2:
#     pesos = input("cuantos pesos Argentinos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 65
#     dolares = pesos /valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + "dolares")

#elif opcion == 3:
#     pesos = input("cuantos pesos Mexicanos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 24
#     dolares = pesos /valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + "dolares")

#else:
#    print('ingresa una opcion correcta por favor')

 #pesos = input("cuantos pesos tienes?: ")
 #pesos = float(pesos)
 #valor_dolar = 3875
 #dolares = pesos /valor_dolar
 #dolares = round(dolares, 2)
 #dolares = str(dolares)
 #print("Tienes $" + dolares + "dolares")



