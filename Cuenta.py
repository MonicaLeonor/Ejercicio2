from Egreso import Egresos
from Finanza import Finanzas
from Ingresos import Ingresos
from Transacciones import Transaccion
from prettytable import PrettyTable

class Cuenta:
    def __init__(self):
        self.ingresos = 0
        self.egresos = 0
        self.cantidad = 0
        

    def crearCuenta(self):
        self.tablaIngresos = Ingresos()
        self.tablaEgresos = Egresos()
        self.tablaTransaccion = Transaccion()
        self.Finanzas = Finanzas()
        self.Finanzas.agregarCuenta(self.ingresos, self.egresos, self.cantidad)
        print("Ha iniciado una cuenta personal, dispone de $0.00")
        print("Continue navegando en el menu")

    def ingresar(self):
        cantidadIngresada = float(input("Cantidad a ingresar ($0.00): "))
        print(f"Se han ingresado ${cantidadIngresada} dolares a su cuenta")
        transaccion = "Ingreso"
        self.tablaTransaccion.agregaTransaccion(transaccion,cantidadIngresada)
        self.tablaIngresos.ingresar(cantidadIngresada)
        self.ingresos = self.ingresos + cantidadIngresada
        self.cantidad = self.cantidad + cantidadIngresada

    def egresar (self):      
        cantidadEgresada = float(input("Cantidad a egresar ($0.00): "))
        print(f"Se han retirado ${cantidadEgresada} dolares de su cuenta")
        transaccion = "Retiro"
        self.tablaTransaccion.agregaTransaccion(transaccion, cantidadEgresada)
        self.tablaEgresos.egresar(cantidadEgresada)
        self.egresos = self.egresos + cantidadEgresada
        self.cantidad = self.cantidad - cantidadEgresada

    def mostrarIngresos(self):
        print(self.tablaIngresos.mostrarIngresos())
    
    def mostrarEgresos(self):
        print(self.tablaEgresos.mostrarEgresos())

    def mostrarTransaccion(self):
        print(self.tablaTransaccion.mostrarTransaccion())

    def mostrarCuenta(self):
        self.Finanzas.agregarCuenta(self.ingresos, self.egresos, self.cantidad)
        print(self.Finanzas.mostrarCuenta())

    

   
