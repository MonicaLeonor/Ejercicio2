from prettytable import PrettyTable
from Cuenta import Cuenta


#APLICACION DE BANCO 
print("-"*50)
print("Bienvenido a la aplicacion del banco")
while True:
    print("-"*50)
    print("0 - Salir")
    print("1 - Crear una cuenta")
    print("2 - Registrar ingreso")
    print("3 - Registrar egreso")
    print("4 - Generar reporte ingresos")
    print("5 - Generar reporte egresos")
    print("6 - Generar reporte operaciones")
    print("7 - Generar reporte cantidad")
  
    opcion = input("Seleccione una opcion del menu: ")

    if opcion == "0":
        print("Gracias por usar la aplicacion")
        break
    elif opcion == "1":
        print("-"*50)
        registro = Cuenta()
        registro.crearCuenta()
    elif opcion == "2":
        print("-"*50)
        registro.ingresar()
    elif opcion == "3":
        print("-"*50)
        registro.egresar()
    elif opcion == "4":
        print("-"*50)
        registro.mostrarIngresos()
    elif opcion == "5":
        print("-"*50)
        registro.mostrarEgresos()
    elif opcion == "6":
        print("-"*50)
        registro.mostrarTransaccion()
    elif opcion == "7":
        print("-"*50)
        registro.mostrarCuenta()

