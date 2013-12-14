#! /usr/bin/env python

def cmpf(x,y):
	if x < y:
		return -1
	elif x > y:
		return 1
	else: 
		return 0
		
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
