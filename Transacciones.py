from prettytable import PrettyTable

#CLASE PARA TRANSACCIONES Y SUS RESPECTIVOS METODOS
class Transaccion:
    def __init__(self):
        self.tablaTransaccion = PrettyTable()
        self.tablaTransaccion.field_names = ["Transaccion", "Cantidad ($)"]

    def agregaTransaccion(self, transaccion, monto):
        self.transaccion = transaccion
        self.monto = monto
        self.tablaTransaccion.add_row([self.transaccion, self.monto])

    def mostrarTransaccion(self):
        result = self.tablaTransaccion
        return result
