class functions:
    def __init__(self):
        self.acciones = []

    def insertarCuentas(self, identificador, factura, usuario, descripcion):
        if not factura:
            return "Error: No se ha encontrado una factura"
        if not usuario:
            return "Error: reautenticar usuario"
        self.acciones.append([identificador, factura, usuario, descripcion])
        return f'La factura {identificador} fue registrada con exito!'

    def eliminarCuentas(self, identificador):
        try:
            identificador not in self.acciones[identificador]
        except IndexError:
            return "Error: factura no encontrada"

        del self.acciones[identificador]
        return f'La factura {identificador} fue eliminada con exito!'