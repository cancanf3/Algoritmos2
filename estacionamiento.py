#! /usr/bin/env python
# Modulo Estacionamiento
from random import *
from tubo import *
from vehiculo import *
seed(0.101101)
class Estacionamiento(object):


	def __init__(self,e):
		self.etiqueta = e
		self.ct = []
		self.tamanyo_estacionamiento = 0
		self.ticket_tubo = 0
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


	def Existe(self,placa,ticket):
		existe = False
		for i in self.ct:
			if ticket == i.etiqueta:
				existe = i.Existe("placa",placa)

		return existe


	def Retirar(self,placa,ticket):
		if True == self.Existe(placa,ticket):
			while self.ct[0].etiqueta != ticket:
				self.ct.append(self.ct[0])
				self.ct.pop(0)

			aux = Tubo(self.ct[0].capacidad,self.ct[0].etiqueta)
			for i in range(len(self.ct[0].pv)):
				if placa == self.ct[0].pv[0].placa:
					x = self.ct[0].Retirar()
				else:
					aux.Estacionar_tubo(self.ct[0].Retirar())
					
			self.ct.pop(0)
			self.ct.append(aux)
		else:
			x = "El vehiculo no existe"

		return x


	def Destruir(self):
	
		self.tamanyo = self.tamanyo - 1
		self.ct.pop(1)



	def mostrar(self):
		for i in range(len(self.ct)):
			print("TUBO",self.ct[i].etiqueta,self.ct[i].capacidad,self.ct[i].ocupacion)
			print("--------------------------")
			for j in range(len(self.ct[i].pv)):
				print(self.ct[i].pv[j].placa)
			print("\n")
		

	def Vaciar(self,etiqueta): #El profesor Victor Theoktisto comento que este procedimiento no es necesario
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
		if (atributo == ( "Anyo" or "Longitud" or "Etiqueta" or "anyo" \
			or "longitud" or "etiqueta")):
			valor = int(valor)

		for i in self.ct:
			x.append([i.etiqueta, i.Busqueda(atributo,valor)])
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
			x = self.le[len(self.le) - 1].Retirar(linea[1], int(linea[2]))  
			self.mensaje = str(x) 

		elif linea[0] == "E":
			self.encabezado = ' '.join(linea) 
			x = self.le[len(self.le) - 1].Existe(linea[1], int(linea[2]))
			self.mensaje = str(x)
		elif linea[0] == "K":
			self.le.pop()
			self.encabezado = ' '.join(linea) 
			self.mensaje = " Fin \n"

		elif linea[0] == "B":
			self.encabezado = ' '.join(linea)
			self.mensaje = ("Vehiculos de " + str(linea[1]) + " " \
					+ str(linea[2]) + "\n")
			x = self.le[len(self.le) - 1].Buscar(linea[1], linea[2])
			for i in x:
				for j in i[1]:
					self.mensaje += str(i[0]) + ": "+ str(j) + \
							"\n"

		archivo = open(self.traza, "a")
		archivo.write(self.encabezado + "\n")
		archivo.write("--> " + self.mensaje + "\n")
		archivo.close()
    
