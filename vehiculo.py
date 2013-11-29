#! /usr/bin/env python
# Modulo de Vehiculo

class Vehiculo(object):

	longitud= 0		 
	placa= "" 
	modelo= ""
	anyo= 0  
	color= ""
	etiqueta= 0 


	def __init__(self,p,l,m,a,c,e):
    
		self.longitud = l		 
		self.placa = p
		self.modelo = m
		self.anyo = a
		self.color = c
		self.etiqueta = e

