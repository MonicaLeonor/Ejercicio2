from prettytable import PrettyTable


#CLASE PARA INGRESOS Y SUS RESPECTIVO METODOS
class Ingresos:
    def __init__(self):
        self.tablaIngresos = PrettyTable()
        self.tablaIngresos.field_names = ["Cantidad ingresada ($)"]

    def ingresar (self, cantidadIngresada):
        self.cantidadIngresada = cantidadIngresada
        self.tablaIngresos.add_row([self.cantidadIngresada])

    def mostrarIngresos(self):
        ingreso = self.tablaIngresos
        return ingreso