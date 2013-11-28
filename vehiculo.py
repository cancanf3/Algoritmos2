#! /usr/bin/env python
# Modulo del Vehiculo

class Vehiculo(object):
	
	def __init__(self,placa,longitud,modelo,anyo,color,etiqueta):
		self.longitud = longitud
		self.placa = placa
		self.modelo = modelo
		self.anyo = anyo
		self.color = color
		self.etiqueta = etiqueta

