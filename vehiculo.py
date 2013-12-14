#! /usr/bin/env python
# Modulo de Vehiculo

class Vehiculo(object):


	def __init__(self,p,l,m,a,c,e):
    
		self.longitud = l		 
		self.placa = p
		self.modelo = m
		self.anyo = a
		self.color = c
		self.etiqueta = e

	def __str__(self):
	
		outSTR = "<< " + str(self.placa) + ", " + str(self.longitud) + \
			 ", " + str(self.modelo) + ", " + str(self.anyo) + ", "\
			 + str(self.color) + ", " + str(self.etiqueta) + " >>"

		return outSTR

