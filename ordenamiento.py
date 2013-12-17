#! /usr/bin/env python

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
	if cmpf(len(seq), 0) < 2:
		pass
	elif cmpf(len(seq), 0) >= 2:
		i, j = 1, 1
		while j != len(seq):
			if seq[j] <= seq[0]:
				seq[i],seq[j] = seq[j], seq[i]
				i += 1
			else:
				pass
			j += 1
		seq[0],seq[i-1] = seq[i-1], seq[0]
		seq1 = seq[:i-1]
		seq2 = seq[i:]
		seq1 = quicksort(seq1,cmpf)
		seq2 = quicksort(seq2,cmpf)
		seq = seq1 + [seq[i-1]] + seq2
	return seq
	

# Ordenamiento por Mergeort
def mergesort(seq, cmpf):
	if len(seq)==1:
		pass
	elif len(seq)==2 and cmpf(seq[0],seq[1])>0:
		aux=seq[0]
		seq[0]=seq[1]
		seq[1]=aux
			
	else:
		seq1=seq[:len(seq)//2]
		seq2=seq[len(seq)//2:]
		mergesort(seq1,cmpf)
		mergesort(seq2,cmpf)
		j=0
		k=0
		
		while j<len(seq1) and k<len(seq2):
			if cmpf(seq1[j],seq2[k])<=0:
				seq[k+j]=(seq1[j])
				j+=1
			elif cmpf(seq1[j],seq2[k])>0:
				seq[k+j]=(seq2[k])
				k+=1
				
		while j<len(seq1):
			seq[k+j]=(seq1[j])
			j+=1 
		while k<len(seq2):
			seq[k+j]=(seq2[k])
			k+=1


# Ordenamiento por Heapsort
def heapsort(seq, cmpf):
	def _construirHeap(n, seq, cmpf):
		k = n // 2
		while k != 0:
			k -= 1
			seq = _acomodarHeap(n,seq,k,n, cmpf)
		
		return seq


	def _acomodarHeap(n, seq, l, m, cmpf):
		k, listo = l, False
		while not listo:
			mayor = k
			if cmpf(2*k+1, m) < 0 and cmpf(seq[2*k+1], seq[mayor]) > 0:
				mayor = 2*k + 1
			if cmpf(2*k+2, m) < 0 and cmpf(seq[2*k+2], seq[mayor]) > 0:
				mayor = 2*k + 2
			if mayor == k:
				listo = True
			else:
				seq[mayor], seq[k] = seq[k], seq[mayor]
				k = mayor

		return seq


	seq = _construirHeap(len(seq),seq,cmpf)
	k = len(seq)

	while k >= 0:
		k -= 1
		seq[0], seq[k] = seq[k], seq[0]
		seq = _acomodarHeap(len(seq),seq,0,k,cmpf)

	seq[0], seq[k] = seq[k], seq[0]
	return seq

# Ordenamiento por Bubblesort0
def bubblesort0(seq, cmpf):
	n = 0
	while n != len(seq):
		k = len(seq) - 1
		while k != n:
			if cmpf(seq[k-1],seq[k]) < 0:
				pass
			else:
				seq[k-1], seq[k] = seq[k], seq[k-1]
			k -= 1
		n += 1


# Ordenamiento por Bubblesort1
def bubblesort1(seq, cmpf):
	n, b = 0, False
	while n != len(seq) and not b:
		k = len(seq) - 1
		b = True
		while k != n:
			if cmpf(seq[k-1],seq[k]) < 0:
				pass
			else:
				seq[k-1], seq[k] = seq[k], seq[k-1]
				b = False
			k -= 1
		n += 1

