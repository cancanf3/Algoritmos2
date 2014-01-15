#! /usr/bin/env python
from arbolbin import *

arbol=arbol()



arbol.add('A')
arbol.add('AA')
arbol.add('AAA')
arbol.add('T')
arbol.add('TTT')
arbol.add('TT')
arbol.add('AAT')
arbol.add('AAAA')
arbol.add('AAAT')
arbol.add('AATA')
arbol.add('AATT')
arbol.add('AAATT')
arbol.add('AATAA')
arbol.add('AATTA')
arbol.add('AATTT')
arbol.add('TTAA')
arbol.add('TTAT')
arbol.add('TTTT')
arbol.add('TTTA')
arbol.add('TTA')
arbol.changemerge('AA','TTTT')

arbol.getall()



