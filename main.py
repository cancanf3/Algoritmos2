#! /usr/bin/env python
# Programa de prueba

from tubo import *
from vehiculo import *
from estacionamiento import *
from evento import *

x = Evento()
print(x.ProcesarLlegadas("prueba.txt"))
