import pytest
from functionTests import functions

@pytest.fixture
def functionTests():
    return functions()

def pruebaInsertar(functionTests):
    #Todos los parametros a agregar
    arrIn = [0,"OIYFJSA!1258IKH.png", "Juan" , "Compra de Gomas"]

    resultado = functionTests.insertarCuentas(0, "OIYFJSA!1258IKH.png", "Juan" , "Compra de Gomas")
    assert resultado == 'La factura 0 fue registrada con exito!'

    #Contador para el for loop
    num = 0
    for item in arrIn:

        #Chequear si se insertaron los atributos correctamente
        assert functionTests.acciones[0][num] == item
        num+=1
    print("Prueba insertar pasada")

def pruebaInsertarFallida(functionTests):

    #Prueba de no factura
    resultado = functionTests.insertarCuentas(1, False, "Juan" , "Compra de Carro")
    assert resultado == "Error: No se ha encontrado una factura"

    #Prueba de no usuario
    resultado = functionTests.insertarCuentas(1,"Factura.png",False,"Compra de Carro")
    assert resultado == "Error: reautenticar usuario"
    print("Prueba de fallos pasada")

def pruebaEliminar(functionTests):
    #Se debe insertar una entrada para poder ser eliminada
    functionTests.insertarCuentas(0, "OIYFJSA!1258IKH.png", "Juan" , "Compra de Gomas")
    resultado = functionTests.eliminarCuentas(0)

    #Chequear si fue eliminada correctamente
    assert resultado == 'La factura 0 fue eliminada con exito!'
    assert [0, "OIYFJSA!1258IKH.png", "Juan" , "Compra de Gomas"] not in functionTests.acciones
    print("Prueba de eliminacion pasada")

def pruebaEliminarFallida(functionTests):
    #No es necesario, pero como una precacion se agrega una entrada
    functionTests.insertarCuentas(0, "OIYFJSA!1258IKH.png", "Juan" , "Compra de Gomas")

    #Chequear si retorna un error, ya que esta fuera de indice
    resultado = functionTests.eliminarCuentas(1)
    assert resultado == 'Error: factura no encontrada'
    print("Prueba de eliminacion fallida pasada")

#Llamar todas las pruebas de uso
pruebaInsertar(functions())
pruebaInsertarFallida(functions())
pruebaEliminar(functions())
pruebaEliminarFallida(functions())

