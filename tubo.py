#! /usr/bin/env python
#Modulo de Tubos

class Tubo:

	lista_vehiculos = [] #lista de los vehiculos
	def __init__(self,capacidad,etiqueta):
		capacidad = self.capacidad
		ocupacion = self.capacidad
		etiqueta  = self.etiqueta

	def estacionar(self,vehiculo):

		if self.cabe(self.vehiculo):
			lista_vehiculos.append(self.vehiculo)
			self.capacidad -= self.vehiculo.longitud
		else:
			return "No hay mas espacio en el Tubo"


	def retirar(self):
		lista_vehiculos.pop(0)


	def cercano(self):
		return lista_vehiculos[len(lista_vehiculos)]


	def cabe(self,vehiculo):
		if self.vehiculo < self.capacidad:
			return True
		else:
			return False
