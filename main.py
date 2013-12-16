#! /usr/bin/env python
from ordenamiento import *
from random import *
def comparadorNumerico1(x, y):	# es la funcioncion cmpf
        return x - y


N = 100				# Tamano de la lista

seq = [ x for x in range(N)]	# genero una lista de [0..N)
shuffle(seq)			# Barajeo el arreglo
print(seq)
print("==================================================================================================================")
seq = quicksort(seq, comparadorNumerico1)
print(seq)

