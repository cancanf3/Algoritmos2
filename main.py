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
