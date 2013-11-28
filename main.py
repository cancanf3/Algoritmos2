#! /usr/bin/env python
# Programa de prueba

from tubo import *
from vehiculo import *
mi_carro1 = Vehiculo("carabobo4",5,"toyota",2008,"negro",1234)
mi_carro2 = Vehiculo("caracas1",3,"toyota",2010,"blanco",8456)
mi_carro3 = Vehiculo("valencia2",20,"ford",2012,"azul",123567)

mi_tubo1 = Tubo(15,"roro")
print(mi_tubo1.Cercano())
print(mi_tubo1.Retirar())
print(mi_tubo1.Estacionar(mi_carro1))
print(mi_tubo1.Estacionar(mi_carro2))
print(mi_tubo1.Estacionar(mi_carro3))
print(mi_tubo1.Cercano().modelo)
print(mi_tubo1.Existe("etiqueta",1234))
