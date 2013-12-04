#! /usr/bin/env python
# Programa de prueba

from tubo import *
from vehiculo import *
from estacionamiento import *
#from evento import *

"""x = Evento()
print(x.ProcesarLlegadas("prueba.txt")) """

x = Vehiculo("xxd4r2", 2.5, "toyota", 2008, "azul",0)
y = Vehiculo("123145",5,"chevrolet", 2010, "negro",1)
z = Vehiculo("4321",3,"nissan",2013,"blue",2)

mi_estacionamiento = Estacionamiento("hola Vale")

mi_estacionamiento.Estacionar(x)
print(mi_estacionamiento.ticket_tubo)
mi_estacionamiento.Estacionar(y)
print(mi_estacionamiento.ticket_tubo)
mi_estacionamiento.Estacionar(z)
print(mi_estacionamiento.ticket_tubo)
print(mi_estacionamiento.ct[0].pv[0].placa)
print(mi_estacionamiento.ct[1].pv[0].placa)
print(mi_estacionamiento.ct[2].pv[0].placa)
