#! /usr/bin/env python
# Programa de prueba

from tubo import *
from vehiculo import *
from estacionamiento import *
mi_carro1 = Vehiculo("carabobo4",5,"toyota",2008,"negro",1234)
mi_carro2 = Vehiculo("caracas1",3,"toyota",2010,"blanco",8456)
<<<<<<< HEAD
mi_carro3 = Vehiculo("valencia2",7,"ford",2012,"azul",123567)

mi_tubo1 = Tubo(15,"roro")
(mi_tubo1.Cercano())
(mi_tubo1.Retirar())



estacionamiento1 = Estacionamiento(1)
(estacionamiento1.Estacionar(mi_carro1))
(estacionamiento1.Estacionar(mi_carro2))
(estacionamiento1.Estacionar(mi_carro3))
(estacionamiento1.Estacionar(mi_carro1))
(estacionamiento1.Estacionar(mi_carro2))
(estacionamiento1.Estacionar(mi_carro3))
estacionamiento1.mostrar()

estacionamiento1.Vaciar(0)
(estacionamiento1.Estacionar(mi_carro1))
estacionamiento1.mostrar()

=======
mi_carro3 = Vehiculo("valencia2",20,"ford",2012,"azul",123567)

estacionamiento1 = Estacionamiento(1)
print(estacionamiento1.Estacionar(mi_carro1))
print(estacionamiento1.Estacionar(mi_carro2))
print(estacionamiento1.Estacionar(mi_carro3))
print(estacionamiento1.ct[0].pv)
print(estacionamiento1.ct[1].pv)
print(len(estacionamiento1.ct[0].pv))
print(len(estacionamiento1.ct[1].pv))
>>>>>>> e48fdd062bd529dc19f6fe5b3122baeb2bd2cac3
