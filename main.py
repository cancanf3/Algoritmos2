#! /usr/bin/env python
# Programa de prueba

from tubo import *
from vehiculo import *
from estacionamiento import *
<<<<<<< HEAD
mi_carro1 = Vehiculo("carabobo4",5,"toyota",2008,"negro",1234)
mi_carro2 = Vehiculo("caracas1",3,"toyota",2010,"blanco",8456)
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
from evento import *

x = Evento()
print(x.ProcesarLlegadas("prueba.txt"))
>>>>>>> d7e2389999584ae05a47c31bdaea024ac79201d4
