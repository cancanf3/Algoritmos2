from random import *


## VEHICULO ##
class vehiculo(object):

	longitud= 0		 
	placa= "" 
	modelo= ""
	anyo= 0  
	color= ""
	etiqueta= 0 


	def __init__(self,l,p,m,a,c,e):

		self.longitud = l		 
		self.placa = p
		self.modelo = m
		self.anyo = a
		self.color = c
		self.etiqueta = e



## TUBO ## 	
class tubo(object):
	capacidad = 0
	ocupacion = 0
	etiqueta = 0

	def __init__(self,c):

		self.capacidad = c
		self.ocupacion = 0
		self.pv = [];


	def Cabe(self,vehiculo):
		if (vehiculo.longitud) <= (self.capacidad-self.ocupacion):
			return True
		else:
			return False


	def Existe(self,atributo,valor):
	
		existe=False
		if ( atributo == "longitud") and ( self.longitud == valor):
			existe=True
		elif ( atributo == "placa") and ( self.placa == valor):
			existe=True
		elif ( atributo == "modelo") and ( self.modelo == valor):
			existe=True
		elif ( atributo == "anyo") and ( self.anyo == valor):
			existe=True					
		elif ( atributo == "color") and ( self.color == valor):
			existe=True
		elif ( atributo == "etiqueta") and ( self.etiqueta == valor):
			existe=True
			
		return existe
	
	def Estacionar(self,vehiculo,e):
	
		if self.Cabe(vehiculo):
			self.ocupacion=ocupacion + vehiculo.longitud
			self.pv.insert(0,vehiculo)
			self.etiqueta=e
			return "El vehiculo se ha estacionado correctamente"

		else:
			return "El tubo no tiene capacidad para estacionar este vehiculo"





	def Retirar(self):

		self.ocupacion = self.ocupacion - self.pv[0].longitud
		self.pv.pop(0)

		if self.ocupacion == 0:
			return "El tubo esta vacio"

		else: 
			return "Se retiro el vehiculo correctamente"


	def Cercano(self):

		if self.ocupacion > 0:
			return self.pv[0]

		else:
			return "No hay vehiculos en el tubo"


##  ESTACIONAMIENTO  ##
class Estacionamiento(object):

	etiqueta=0
	ct=[]
	ticket_tubo=0
	ticket_vehiculo=0
	tamanyo_estacionamiento=0


	def __init__(self,e):
		self.etiqueta=e


	def Generar(self):

		 
		nuevo_tubo = tubo( randint(5,25) , ticket_tubo )
		self.ticket_tubo = ticket_tubo+1
		self.tamanyo_estacionamiento = tamanyo_estacionamiento+1 
		self.ct.append(nuevo_tubo)


	def Estacionar(self,vehiculo):

		if self.tamanyo_estacionamiento == 0:
			self.Generar()
			self.ct[0].Estacionar(vehiculo,ticket_vehiculo)
	      	   	

		else:
			i=0
			hay_espacio=False
			while (( i < self.tamanyo_estacionamiento) 
			      and not(hay_espacio)):

			      if self.ct[i].ocupacion >vehiculo.longitud:
			      		self.ct[i].Estacionar(vehiculo,ticket_vehiculo+1)
					hay_espacio=True
			      	   	
			      else: 
			      		i=i+1

			if not(hay_espacio):
				self.Generar()
				self.ct[i].Estacionar(vehiculo,ticket_vehiculo+1)

		ticket_vehiculo = ticket_vehiculo + 1

		return ticket_vehiculo



	def Existe(self,placa,ticket,*arg):

		i=0
		existe=False
		while  i < self.tamanyo_estacionamiento and not(existe):
		     j=0
		     while j < len(self.ct[i].pv) and not(existe):

		     		if (self.ct[i].pv[j].existe("placa",placa)
		     		and self.ct[i].pv[j].existe("etiqueta",ticket)):
		     			existe=True
		     		else:
		     			j=j+1
		     i=i+1
		
		if len(arg)==2 and existe: 
		 	arg[0]=i-1
		 	arg[1]=j
		 
		 
		return existe

	
	def Retirar(self,placa,ticket):

		i=0
		j=0
		if self.Existe(placa,ticket,i,j):
			return "falta implementar"
		
		else: 
			return "No existe un vehiculo con esos atributos"
			


	def Destruir(self):
	
		self.tamanyo = self.tamanyo - 1
		self.ct.pop(1)

	def Vaciar(self,etiqueta):
		i=0
		existe=False
		while (i < len(self.ct)) and not(existe):
			if self.ct[i].etiqueta == etiqueta:
				existe = True
			else: 
				i=i+1

		if existe:
			return "falta implementar"

		else:
			return "No existe un tubo con esta etiqueta"
			
		


