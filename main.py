#! /usr/bin/env python
# Modulo de prueba
from ordenamiento import *
from random import *
def comparadorNumerico1(x, y):
        return x - y
N = 100

seq = [ x for x in range(N)]
shuffle(seq)
print(seq)
print("==================================================================================================================")
seq = quicksort(seq, comparadorNumerico1)
print(seq)





