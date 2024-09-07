from funciones_calculadora import sumar_n_numeros
from funciones_calculadora import multiplicacion_n_numeros
from funciones_calculadora import division_2_numeros

while True:
    print('''
    Bienvenido a mi calculadora, por favor ingresa la opcion que desees.
    1) Hacer una suma de N números
    2) Hacer multiplicacion de N números
    3) Hacer una division de 2 números

    0) Salir del programa
    ''')
    
    opcion = int(input('> '))

    match opcion:

        case 1:
            resultado = sumar_n_numeros()
            print(resultado)
        case 2:
            resultado = multiplicacion_n_numeros()
            print(resultado)
        case 3:
            resultado = division_2_numeros()
            print(resultado)
        case 0:
            break 
        case _:
            print(f'Por favor ingresa una opcion válida')