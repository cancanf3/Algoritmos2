import sys, traceback

def Argumentos (args):
	msg = " Error en la linea de comandos: arbolbin.py  \
		<Archivo de Entrada> <Archivo de Salida> "
	if  len(args) != 3:
		print(msg)
	return str(args[1]), str(args[2])

def Procesar (fileR, fileW):
	arbol = Arbol()
	arbol.fileW = fileW
	archivo = open(fileR, "r")
	for x in archivo:
		i = x.split()
		if len(i) > 0:
			if i[0] == "ADD":
				arbol.add(i[1])
			elif i[0] == "GET":
				arbol.get(i[1])
			elif i[0] == "GETALL":
				arbol.getall()
			elif i[0] == "MAXLENGTH":
				arbol.maxlength()
			elif i[0] == "DELETE":
				arbol.delete(i[1])
			elif i[0] == "SET":
				arbol.set(i[1],int(i[2]))
			elif i[0] == "CHANGE":
				arbol.change(i[1], i[2])
			elif i[0] == "CHANGEMERGE":
				arbol.changemerge(i[1], i[2])
			elif i[0] == "PRINT":
				arbol.Print(fileW,i[1:])


class nodo(object):
	def __init__(self):
		self.cantidad=0
		self.hijo_izq=None
		self.hijo_der=None



class Arbol(object):
	def __init__(self):
		self.raiz=nodo()
		self.raiz.cantidad = None
		self.fileW = " "
	# Procedimiento que escribe las salidas en el archivo de texto
	def Print (self, archivo, arg):
		string=""
		for i in arg:
			string+=str(i)
			if arg[0][0] == '\'':
				string += ' '
		if arg[0][0] == '\'':
			string = string[1:len(string)-2]
		archivo = open(archivo,"a")
		archivo.write(string+"\n")
		archivo.close()

	


	# Agrega una secuencia al arbol y aumenta la cantidad de la misma en 1
	def add(self,secuencia):
		aux=self.raiz
		for i in secuencia:
			if i == 'A':
				if aux.hijo_izq == None:
					aux.hijo_izq = nodo()
				aux=aux.hijo_izq
			elif i == 'T':
				if aux.hijo_der == None:
					aux.hijo_der = nodo()
				aux=aux.hijo_der
		aux.cantidad+=1
		
	# Imprime la cantidad de una secuencia, de no existir retorna 0
	def get(self,secuencia):
		aux=self.raiz
		for i in secuencia:
			if i == 'A' and aux.hijo_izq != None:
				aux=aux.hijo_izq
			elif i == 'T' and aux.hijo_der != None:
				aux=aux.hijo_der
			else:
				 return [secuencia,0]
		self.Print(self.fileW,str(secuencia)+' '+str(aux.cantidad))

	# Obtiene todas las secuencias con su respectiva cantidad
	def getall(self,*args):
		listado=[]
		
		if self.raiz.hijo_der == None and self.raiz.hijo_izq == None:
			return listado
			
		elif len(args) == 0:	
			aux = self.raiz
			listado+=self.getall(aux.hijo_izq,'A')
			listado+=self.getall(aux.hijo_der,'T')
			for i in range(len(listado)//2):
				self.Print(self.fileW, str(listado[2*i])+' '+ 
					   str(listado[2*i+1]))
		else:
		
			if args[0] == None:
				return listado
				
			else:	
				if int(args[0].cantidad) > 0:
					listado=[args[1],args[0].cantidad]
			
				listado += self.getall(args[0].hijo_izq,args[1]
					   +'A')
				listado += self.getall(args[0].hijo_der,args[1]
					   +'T')
				return listado


	# Obtiene la secuencia mas larga
	def maxlength (self,*args):

		if self.raiz.hijo_der == None and self.raiz.hijo_izq == None:
			return 0

		elif len(args) == 0:
			aux = self.raiz
			max1 = self.maxlength(aux.hijo_izq)
			max2 = self.maxlength(aux.hijo_der)
			max1=max1 if max1 > max2 else max2
			
			self.Print(self.fileW,'maxlength == '+str(max1))
			

		else:
			if args[0] == None:
				return 0
			else:
				max1 = self.maxlength(args[0].hijo_izq)
				max2 = self.maxlength(args[0].hijo_der)
				return max1+1 if max1 > max2 else max2+1

	# Elimina la secuencia del arbol, eliminando los nodos si es que no
	# pertenencen a otra secuencia, sino cambia su cantidad a 0
	
	def delete (self,secuencia,*args):
		if self.raiz.hijo_der == None and self.raiz.hijo_izq == None:		
			self.Print(self.fileW,'ERROR: Cannot DELETE.')
		elif len(args) == 0:
			aux = self.raiz
			if secuencia[0] == 'A':
				self.delete(secuencia,aux.hijo_izq,1)
				if (aux.hijo_izq.cantidad == 0 and 
				    aux.hijo_izq.hijo_izq == None and 
				    aux.hijo_izq.hijo_der == None):
					aux.hijo_izq = None
			if secuencia[0] == 'T':
				self.delete(secuencia,aux.hijo_der,1)
				if (aux.hijo_der.cantidad == 0 and 
				    aux.hijo_der.hijo_izq == None and 
				    aux.hijo_der.hijo_der == None):
					aux.hijo_der = None
		else:
			if args[1] != len(secuencia) and args[0] == None:
				self.Print(self.fileW,'ERROR: Cannot DELETE.')
				return 1

			elif args[1] < len(secuencia):
				b=0
				if secuencia[args[1]] == 'A':
					b=self.delete(secuencia,
					args[0].hijo_izq,args[1]+1)
				elif secuencia[args[1]] == 'T':
					b=self.delete(secuencia,
					args[0].hijo_der,args[1]+1)
				if b == 1:
					if secuencia[args[1]] == 'A':
						args[0].hijo_izq = None
					elif secuencia[args[1]] == 'T':
						args[0].hijo_der = None
						
					if (args[0].cantidad == 0 and 
					    args[0].hijo_izq == None and 
					    args[0].hijo_der == None):
						return 1
					else:
						return 2
				elif b == 0:
					return 0	
				
			elif args[1] == len(secuencia):
				if args[0] !=None:
					args[0].cantidad = 0
					if (args[0].hijo_izq != None or
					    args[0].hijo_der != None):
						return 2
					else:
						return 1
				else:
					return 1
	
				
	# Reemplaza la cantidad de una secuencia dada por otra cantidad dada
	def set ( self, secuencia, cantidad):

		if cantidad == 0:
			self.delete(secuencia)
		else:
			aux = self.raiz
		
			for i in secuencia:
				if i == 'A':
					aux=aux.hijo_izq
				elif i == 'T':
					aux=aux.hijo_der
			aux.cantidad = cantidad
			


	# Cambia las secuencias que empiecen por secuenciaOrigen, por unas que 
	# empiecen con secuenciaDestino
	def change (self, secuenciaOrigen, secuenciaDestino):
		aux1=self.raiz
		pre=False
		nodo1=None
		aux2=self.raiz
		for i in range(len(secuenciaOrigen)-1):
			if secuenciaOrigen[i] == 'A':
				aux2=aux2.hijo_izq
			elif secuenciaOrigen[i] == 'T':
				aux2=aux2.hijo_der
		if secuenciaOrigen[len(secuenciaOrigen)-1] == 'A':
			nodo1=aux2.hijo_izq
			aux2.hijo_izq=None
		else:
			nodo1=aux2.hijo_der
			aux2.hijo_der=None
			
		ultimo1=secuenciaDestino[len(secuenciaDestino)-1]
		for i in range(len(secuenciaDestino)-1):
			if secuenciaDestino[i] == 'A':
				if aux1.hijo_izq == None:
					pre = True
					aux1.hijo_izq=nodo()
				aux1=aux1.hijo_izq
			elif secuenciaDestino[i] == 'T':
				if aux1.hijo_der == None:
					pre = True
					aux1.hijo_der = nodo()
				aux1=aux1.hijo_der
		if (not(pre) and((ultimo1 == 'A' and aux1.hijo_izq != None) 
			     or (ultimo1 == 'T' and aux1.hijo_der != None))):
			self.Print(self.fileW,'ERROR: Cannot CHANGE. \
			Use CHANGEMERGE instead.')
			if secuenciaOrigen[len(secuenciaOrigen)-1] == 'A':
				aux2.hijo_izq=nodo1
			else:
				aux2.hijo_der=nodo1
		else:	
			if ultimo1 == 'A':
			 	aux1.hijo_izq = nodo1
			else:
			 	aux1.hijo_der = nodo1
			self.delete(secuenciaOrigen)


			

	# Mapea, sincroniza y referencia los subarboles

	def __Mapeo (self, aux1, aux0):
		# aux1 y aux0 apunten a el final de secuenciaOrigen 
		# y secuenciaDestino respectivamente
		if aux1 == None:
			pass

		else:
			aux0.cantidad += aux1.cantidad
			aux1.cantidad = 0
			
			if aux1.hijo_izq != None:
				if aux0.hijo_izq != None:
					self.__Mapeo(aux1.hijo_izq,
					aux0.hijo_izq)
				else:
					aux0.hijo_izq = aux1.hijo_izq
					aux1.hijo_izq = None

			if aux1.hijo_der != None:
				if aux0.hijo_der != None:
					self.__Mapeo(aux1.hijo_der,
					aux0.hijo_der)
				else:
					aux0.hijo_der = aux1.hijo_der
					aux1.hijo_der = None

				

			

	# Cambia las secuencias que empiecen por secuenciaOrigen, por unas que
	# Empiecen con secuenciaDestino 
	def changemerge (self, secuenciaOrigen, secuenciaDestino):

		if self.raiz == None:
			pass
		else:
			aux1 = self.raiz
			for i in secuenciaOrigen[:
				 len(secuenciaOrigen)-1]:
				if i == 'A':
					aux1=aux1.hijo_izq
				elif i == 'T':
					aux1=aux1.hijo_der

			if (secuenciaOrigen[len(secuenciaOrigen)-1]  
				== 'A'):
				nodoO = aux1.hijo_izq
				aux1.hijo_izq = None
			else:
				nodoO = aux1.hijo_der
				aux1.hijo_der = None

			aux0 = self.raiz
			for i in secuenciaDestino:
				if i == 'A':
					if aux0.hijo_izq == None:
						aux0.hijo_izq=nodo()
					aux0=aux0.hijo_izq
				elif i == 'T':
					if aux0.hijo_der == None:
						aux0.hijo_der=nodo()
					aux0=aux0.hijo_der
			self.__Mapeo(nodoO, aux0)
			self.delete(secuenciaOrigen)





				
##############################################
#					     #
#	   INICIO DE LA APLICACION           #
#					     #
#					     #
##############################################


fileR, fileW = Argumentos(sys.argv)

Procesar(fileR, fileW)



