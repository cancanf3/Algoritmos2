#! /usr/bin/env python
from arbolbin import *

arbol=arbol()



arbol.add('A')
arbol.add('AA')
arbol.add('AAA')
arbol.add('T')
arbol.add('AAAA')
arbol.add('AAAAAAAT')

x=arbol.getall()
mostrar(x)




arbol.change('AAA','TTT')

mostrar(arbol.getall())

