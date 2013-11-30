'''
<<<<<<< HEAD
#Modulo main.py
#! /usr/bin/env python

from clases import*

hola=Estacionamiento(1)
l=16
p="la3774"
m="toyota"
a=1999
c="rojo"
v=vehiculo(l,p,m,a,c)

l=12
p="lhola123"
m="corola"
a=122349
c="verde"
v1=vehiculo(l,p,m,a,c)

l=1
p="toma"
m="daka"
a=1999
c="teotisto es marico"
v2=vehiculo(l,p,m,a,c)

l=11
p="rata74"
m="ford"
a=1
c="azul"
v3=vehiculo(l,p,m,a,c)




hola.Estacionar(v)
hola.Estacionar(v1)
hola.Estacionar(v2)
hola.Estacionar(v3)



hola.mostrar()
=======
'''
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
#>>>>>>> 2987ca18302ad99c4617001d1b36acbebb4fee89
