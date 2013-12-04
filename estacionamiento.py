#! /usr/bin/env python
# Modulo Estacionamiento
from random import *
from tubo import *
from vehiculo import *
seed(0.101101)
class Estacionamiento(object):

	ticket_tubo = 0

	def __init__(self,e):
		self.etiqueta = e
		self.ct = []
		self.tamanyo_estacionamiento = 0

	def Generar(self):	 
		nuevo_tubo = Tubo(randint(5,25), self.ticket_tubo)
		self.ticket_tubo += 1
		self.tamanyo_estacionamiento += 1 
		self.ct.append(nuevo_tubo)


	def Estacionar(self, vehiculo, *arg):
		if self.tamanyo_estacionamiento == 0:
			self.Generar()
			while self.ct[0].capacidad < vehiculo.longitud:
				self.Generar()

				i = len(self.ct) - 1
				aux = self.ct[i] 
				while i != 0:
					self.ct[i] = self.ct[i - 1]
					i -= 1

				self.ct[0] = aux
			self.ct[0].Estacionar_tubo(vehiculo)
			tubo_estacionar = self.ct[0].etiqueta


		else:
			if (self.ct[0].capacidad - self.ct[0].ocupacion) >= vehiculo.longitud:
				self.ct[0].Estacionar_tubo(vehiculo)
				tubo_estacionar = self.ct[0].etiqueta
			else:
				
				while (self.ct[0].capacidad - self.ct[0].ocupacion) < vehiculo.longitud:
					self.Generar()

					i = len(self.ct) - 1
					aux = self.ct[i] 
					while i != 0:
						self.ct[i] = self.ct[i - 1]
						i -= 1

					self.ct[0] = aux
				self.ct[0].Estacionar_tubo(vehiculo)
				tubo_estacionar = self.ct[0].etiqueta

		return tubo_estacionar



	def Existe(self,placa,ticket,*arg):

		i = 0
		existe=False
		while  i < self.tamanyo_estacionamiento and not(existe):
		     j = 0
		     while j < len(self.ct[i].pv) and not(existe):

		     		if self.ct[i].Existe("placa",placa) and self.ct[i].etiqueta == ticket:
		     			existe=True
		     		else:
		     			j += 1
		     i += 1
		
		if len(arg)==2 and existe: 
		 	arg[0]=i-1
		 	arg[1]=j
		 
		 
		return existe

	
	def Retirar(self,placa,ticket):

		j=0
		
		if self.Existe(placa,ticket):
			for i in range(0,len(self.ct)):
				tubo_explota = False
				while not len(self.ct[i].pv) == 0 and self.ct[i].etiqueta == tickect:
					tubo_explota = True
					vehiculo = self.ct[i].Retirar() 
					if placa == vehiculo.placa and j == 0:
						tubo = self.ct[i].pv
						return "El vehiculo se ha retirado correctamente"
						break
					else:
						if placa == vehiculo.placa:
							return "El vehiculo se ha retirado correctamente"
						else:
							tubo = Tubo(self.ct[i].capacidad, self.ct[i].etiqueta)
							tubo.Estacionar(vehiculo)
					j += 1
			
				if tubo_explota:
					self.ct.pop(i)
					self.ct.append(tubo)						
					break	
		
		else: 
			return "No existe un vehiculo con esos atributos"
			


	def Destruir(self):
	
		self.tamanyo = self.tamanyo - 1
		self.ct.pop(1)



	def mostrar(self):
		for i in range(len(self.ct)):
			print("TUBO",self.ct[i].etiqueta,self.ct[i].capacidad,self.ct[i].ocupacion)
			print("--------------------------")
			for j in range(len(self.ct[i].pv)):
				print(self.ct[i].pv[j].etiqueta)
			print("\n")
		

	def Vaciar(self,etiqueta):
		i=0
		existe=False
		while (i < len(self.ct)) and not(existe):
			if self.ct[i].etiqueta == etiqueta:
				existe = True
				break
			else: 
				i += 1

		if existe:
			print(i)
			for j in range(len(self.ct[i].pv)-1):
				vehiculo=self.ct[i].Cercano()
				self.ct[i].Retirar()


				self.Estacionar(vehiculo)
			self.ct.pop(i)	
				
			return "Se Vacio el tubo"

		else:
			return "No existe un tubo con esta etiqueta"

	def Buscar(self, atributo, valor):
		x = []
		for i in self.ct:
			x.append([i.etiqueta, i.Existe(atributo,valor)])
		 
		return x
			
								
			
 
	def ProcesarLlegadas(self, nombreArchivo):
	    

		archivo = open(nombreArchivo,"r")
		for i in archivo:
			linea = i.split()
			if len(linea) == 0:
			    pass
			else:
				self.Procesar(linea)

#<<<<======================================================================>>>#
    
class Evento(Estacionamiento):
	ticket_estacionamiento = 0
	ticket_vehiculo = 0
	le = []	
	traza = " "

	def __init__(self):
		self.mensaje = " " 
		self.encabezado = " "
		
	def Procesar(self, linea):
		if linea[0] == "C":
			self.encabezado = ' '.join(linea) 
			estacionamiento = \
			Estacionamiento(self.ticket_estacionamiento)
			self.le.append(estacionamiento)
			self.ticket_estacionamiento += 1
			self.mensaje = "Se ha creado el Estacionamiento"
			self.traza = linea[1]	
			print(len(self.le))

		elif linea[0] == "P":
			self.encabezado = ' '.join(linea) 
			x = Vehiculo(linea[1], float(linea[2]), linea[3], \
				int(linea[4]), linea[5], self.ticket_vehiculo)
			self.ticket_vehiculo += 1
			pseudo_mensaje = self.le[len(self.le) - 1].Estacionar(x)
			self.mensaje = "Se ha Estacionado el Vehiculo, \
					su ticket: " + str(pseudo_mensaje)
		elif linea[0] == "R":
			self.encabezado = ' '.join(linea) 
			x = self.le[len(self.le) - 1].Retirar(linea[1], linea[2])  
			self.mensaje = x 

		elif linea[0] == "E":
			self.encabezado = ' '.join(linea) 
			x = self.le[len(self.le) - 1].Existe(linea[1], linea[2])
			self.mensaje = str(x)
		elif linea[0] == "K":
			self.encabezado = ' '.join(linea) 
			self.mensaje = " Fin \n"

		elif linea[0] == "B":
			self.encabezado = ' '.join(linea)
			self.mensaje = ("Vehiculos de " + str(linea[1]) + " " \
					+ str(linea[2]) + "\n")
			x = self.le[len(self.le) - 1].Buscar(linea[1], linea[2])
			for i in x:
				for j in i[1]:
					print(j)
					self.mensaje += str(i[0]) + ": "+ j + \
							"\n"

		archivo = open(self.traza, "a")
		archivo.write(self.encabezado + "\n")
		archivo.write("--> " + self.mensaje + "\n")
		archivo.close()
    
