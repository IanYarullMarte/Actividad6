# Actividad 6

Este trabajo se basa en el caso de estudio originalmente implementado, este trata sobre probar modulos de contabilidad en un sistema de facturas.

## Funciones creadas para ser evaluadas

En este sistema se crearon 2 funciones diferentes:

- `insertarCuentas()` que sirve para poder insertar cuentas en una base de datos

En este se utilizan pruebas de errores para chequear si la factura agregada cuenta con un usuario y con una factura en si.

- `eliminarCuentas()` que sirve para poder eliminar las instancias ya creadas

En este se utilizan pruebas de errores para chequear si la factura eliminada ya esta en el sistema.

Estas se encuentran dentro de ``functionTests.py``

## Funciones de prueba para evaluar

De las dos funciones creadas, se derivaron 4 funciones de prueba diferentes que son:
- `pruebaInsertar()` que prueba la insercion de una nueva entrada.
- `pruebaInsertarFallida()` que prueba la insercion de una nueva entrada con datos faltantes.
- `pruebaEliminar` que prueba la eliminacion de una entrada ya existente.
- `pruebaEliminarFallida()` que prueba la eliminacion de una entrada de manera erronea.

Estas se encuentran dentro de ``pruebasUso.py``
