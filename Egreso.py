from prettytable import PrettyTable

#CLASE EGRESOS Y SUS RESPETIVOS METODOS
class Egresos:
    def __init__(self):
        self.tablaEgresos = PrettyTable()
        self.tablaEgresos.field_names = ["Cantidad retirada ($)"]

    def egresar (self, cantidadEgresada):
        self.cantidadEgresada = cantidadEgresada
        self.tablaEgresos.add_row([self.cantidadEgresada])

    def mostrarEgresos(self):
        egreso = self.tablaEgresos
        return egreso

        