#! /usr/bin/env python
#Modulo de Tubos

class Tubo:

	lista_vehiculos = [] #lista de los vehiculos
	def __init__(self,capacidad,etiqueta):
		self.capacidad = capacidad
		self.ocupacion = capacidad
		self.etiqueta = etiqueta

	def estacionar(self,vehiculo):

		if self.cabe(vehiculo):
			self.lista_vehiculos.append(vehiculo)
			self.capacidad -= vehiculo.longitud
		else:
			return "No hay mas espacio en el Tubo"


	def retirar(self):
		self.lista_vehiculos.pop(0)


	def cercano(self):
		return self.lista_vehiculos[len(self.lista_vehiculos) - 1]


	def cabe(self,vehiculo):
		if vehiculo.longitud < self.capacidad:
			return True
		else:
			return False
