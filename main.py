#! /usr/bin/env python
# Programa de prueba

from vehiculo import *
from tubo import *

mi_carro1 = Vehiculo("carabobo4",5,"toyota",2008,"negro","terios")
mi_carro2 = Vehiculo("caracas1",3,"toyota",2010,"blanco","yaris")
mi_carro3 = Vehiculo("valencia2",20,"ford",2012,"azul","aveo")

mi_tubo1 = Tubo(15,"roro")

mi_tubo1.estacionar(mi_carro1)
mi_tubo1.estacionar(mi_carro2)
print(mi_tubo1.estacionar(mi_carro3))
print(mi_tubo1.cercano())
print(mi_tubo1.cabe(mi_carro3))
mi_tubo1.retirar()

