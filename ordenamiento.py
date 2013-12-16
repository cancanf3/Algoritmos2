#! /usr/bin/env python

def cmpf(x,y):
	if x < y:
		return -1
	elif x > y:
		return 1
	else: 
		return 0
		
# Descripción: Módulo con la implementación de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos que son comparables
#              entre sí. Al aplicar algún algoritmo de ordenamiento, la lista a ordenar
#              es copiada y se retorna una nueva lista con los elementos ordenados.
# Autor: Guillermo Palma
# email: gvpalma@usb.ve
# version 0.1


# Todos los algoritmos de ordenamiento tienen los siguentes parámetros
# Parámetros: seq: objeto lista de python que contiene elementos comparables
#
#             cmpf: Función que compara dos elementos de la lista.
#             Esta función es llamada repetidamente por los algoritmos de ordenamiento
#             para comparar dos elementos. La función cmpf toma como argumento
#             dos elementos de la lista, y retorna un número entero. Su prototipo es:
#             cmpf(x, y) --> int
#             El  número entero  define el orden
#             de los elementos de la siguiente manera:
#                 cmpf(x, y) < 0 : significa que el elemento x va antes del elemento y
#                 cmpf(x, y) > 0 : significa que el elemento x va después del elemento y
#                 cmpf(x, y) = 0 : significa que los elementos x, y son equivalentes

# Ordenamiento por Inserción
def insertion(seq, cmpf):
    n = len(seq)
    for i in range(1, n) :
        value = seq[i]
        pos = i
        while pos > 0 and cmpf(value, seq[pos - 1]) < 0 :
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value

# Ordenamiento por Quicksort
def quicksort(seq, cmpf):
   # complet
    return

# Ordenamiento por Mergeort
def mergesort(seq):
	if len(seq)==1:
		pass
	elif len(seq)==2 and seq[0]>seq[1]:
			aux=seq[0]
			seq[0]=seq[1]
			seq[1]=aux
			
	else:
		seq1=seq[:len(seq)/2]
		seq2=seq[len(seq)/2:]
		mergesort(seq1)
		mergesort(seq2)
		j=0
		k=0
		
		while j<len(seq1) and k<len(seq2):
			if seq1[j]<=seq2[k]:
				seq[k+j]=(seq1[j])

				j+=1
			elif seq1[j]>seq2[k]:
				seq[k+j]=(seq2[k])

				k+=1
				
		while j<len(seq1):
			seq[k+j]=(seq1[j])

		 	j+=1 
		while k<len(seq2):
			seq[k+j]=(seq2[k])
		 	k+=1


   # completar
    return

# Ordenamiento por Heapsort
def heapsort(seq, cmpf):
    # completar
    return

# Ordenamiento por Bubblesort0
def bubblesort0(seq, cmpf):
    # completar
    return

# Ordenamiento por Bubblesort1
def bubblesort1(seq, cmpf):
    # completar
    return
