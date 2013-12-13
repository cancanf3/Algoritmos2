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
    def ordenar(seq, izq, der, cmpf):
	if cmpf(der, izq) < 2:
	    pass
	elif cmpf(der, izq) > 2:
	    pivote = der - 1
	    seq = particionar(seq, izq, der, pivote, cmpf)
	    seq = ordenar(seq, izq, pivote, cmpf)
	    seq = ordenar(seq, pivote + 1, der, cmpf)
	    
	return seq
    
    def particionar(seq, izq, der, cmpf):
	i = izq
	j = izq
	while j != der:
	    if cmpf(seq[j],seq[pivote]) < 0:
		seq[i], seq[j] = seq[j], seq[i]
		i += 1
	    elif cmpf(seq[j], seq[pivote]) > 0:
		pass
	    j += 1

    seq = ordenar(seq, 0, len(seq), cmpf)
    return seq

# Ordenamiento por Mergeort
def mergesort(seq, cmpf):
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



def ordenar(ordenamiento, lista, izq, der):
    if der - izq < 2:
	pass
    elif der - izq > 2:
	med = (izq + der) div 2
	
