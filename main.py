from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada (N números)")
    print("6. Salir")

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Introduce el número de la opción: ")

        if opcion == '1':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")

        elif opcion == '2':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {restar(a, b)}")

        elif opcion == '3':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {multiplicar(a, b)}")

        elif opcion == '4':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {dividir(a, b)}")

        elif opcion == '5':
            numeros = input("Introduce los números separados por comas: ").split(',')
            numeros = [float(n) for n in numeros]
            print(f"Resultado: {suma_avanzada(*numeros)}")

        elif opcion == '6':
            print("Saliendo de la calculadora...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

if __name__ == "__main__":
    ejecutar_calculadora()