from prettytable import PrettyTable


#CLASE FINANZAS Y SUS RESPECTIVOS METODOS
class Finanzas:
    def __init__(self):
        self.tablaFinanzas = PrettyTable()
        self.tablaFinanzas.field_names = ["Ingresos", "Engresos", "Cantidad ($)"]

    def agregarCuenta(self, ingresos, egresos, cantidad):
        self.ingresos = ingresos
        self.egresos = egresos
        self.cantidad = round(cantidad,2)
        self.tablaFinanzas.add_row([self.ingresos, self.egresos, self.cantidad])

    def mostrarCuenta(self):
        cuenta = self.tablaFinanzas
        return cuenta

