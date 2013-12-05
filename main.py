#! /usr/bin/env python
# Programa de prueba

from tubo import *
from vehiculo import *
from estacionamiento import *
#from evento import *

x = Evento()
x.ProcesarLlegadas("prueba.txt")
"""

mi_carro1 = Vehiculo("1234",1,"toyota",2008,"rojo",1234)
mi_carro2 = Vehiculo("45678",2,"ford",2007,"amarilo",423)

x = Estacionamiento(1234)
x.Estacionar(mi_carro1)
x.Estacionar(mi_carro2)

print(x.ct[0].etiqueta)
#print(x.ct[1].etiqueta)
print(x.Existe("1234",0)
"""
