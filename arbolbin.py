

class nodo(object):
		cantidad=0
		hijo_izq=None
		hijo_der=None


def mostrar(listado):
	print ' - - - - - - - - - - - - - - - - '; 
	for i in range(len(listado)/2):
		print listado[2*i], listado[2*i+1];
	
	print ' - - - - - - - - - - - - - - - - ';

class arbol(object):
	raiz=nodo()
	raiz.cantidad = None
	

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
		return [secuencia,aux.cantidad]

	# Obtiene todas las secuencias con su respectiva cantidad
	def getall(self,*args):
		listado=[]
		
		if self.raiz.hijo_der == None and self.raiz.hijo_izq == None:
			return listado
			
		elif len(args) == 0:	
			aux = self.raiz
			listado+=self.getall(aux.hijo_izq,'A')
			listado+=self.getall(aux.hijo_der,'T')
			for i in range(len(listado)/2):
				self.Print(str(listado[2*i])+', '+ str(listado[2*i+1]))
		else:
		
			if args[0] == None:
				return listado
				
			else:	
			
				if args[0].cantidad > 0:
					listado=[args[1],args[0].cantidad]
			
				listado += self.getall(args[0].hijo_izq,args[1]+'A')
				listado += self.getall(args[0].hijo_der,args[1]+'T')
				return listado


	# Obtiene la secuencia mas larga
	def maxlength (self,*args):

		if self.raiz.hijo_der == None and self.raiz.hijo_izq == None:
			return 0

		elif len(args) == 0:
			aux = self.raiz
			max1 = self.maxlength(aux.hijo_izq)
			max2 = self.maxlength(aux.hijo_der)
			return max1 if max1 > max2 else max2

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
			print 'ERROR: Cannot DELETE.';
		elif len(args) == 0:
			aux = self.raiz
			if secuencia[0] == 'A':
				self.delete(secuencia,aux.hijo_izq,1)
			if secuencia[0] == 'T':
				self.delete(secuencia,aux.hijo_der,1)

		else:
			if args[1] != len(secuencia) and args[0] == None:
				print 'ERROR: Cannot DELETE.';
				return 0

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
				args[0].cantidad = 0
				if (args[0].hijo_izq != None or
				    args[0].hijo_der != None):
					return 2
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

		# Precondicion:
		aux1=self.raiz
		pre=False
		nodo1=aux1
		ultimo1=secuenciaDestino[len(secuenciaDestino)-1]
		for i in range(len(secuenciaDestino)-1):
			if secuenciaDestino[i] == 'A':
				if aux1.hijo_izq == None:
					pre = True
					break
				else:
					aux1=aux1.hijo_izq
			elif secuenciaDestino[i] == 'T':
				
				if aux1.hijo_der == None:
					pre = True
					break
				else:
					aux1=aux1.hijo_der
		if not(pre):
			
			if ultimo1 == 'A':
				 nodo1=aux1.hijo_izq
			elif ultimo1 == 'T':
				 nodo1=aux1.hijo_der
		else:
			self.add(secuenciaDestino)
			print(self.getall())
			aux1=self.raiz
			for i in range(len(secuenciaDestino)-1):
				if secuenciaDestino[i] == 'A':
					aux1=aux1.hijo_izq
				elif secuenciaDestino[i] == 'T':
					aux1=aux1.hijo_der
			
			
		
		if (nodo1 != None) and not(pre):
			print 'ERROR: Cannot CHANGE. Use CHANGEMERGE instead.';
		else:
			aux2=self.raiz
			ultimo2 = secuenciaOrigen[len(secuenciaOrigen)-1]
			for i in range(len(secuenciaOrigen)-1):
				if secuenciaOrigen[i] == 'A':
					aux2=aux2.hijo_izq
				elif secuenciaOrigen[i] == 'T':
					aux2=aux2.hijo_der

			nodo2=aux2
			if ultimo2 == 'A':
				nodo2=aux2.hijo_izq
			elif ultimo2 == 'T':
				nodo2=aux2.hijo_der
			
			if ultimo1 == 'A':
				 aux1.hijo_izq = nodo2
		        elif ultimo1 == 'T':
		       		 print nodo2.cantidad;
		        	 aux1.hijo_der = nodo2
		
		       	if ultimo2 == 'A':
				aux2.hijo_izq = None
			elif ultimo2 == 'T':
				aux2.hijo_der = None

	# Mapea los subarboles
	def __Mapeo1 (self, aux, *args): 
		sec=[]	

		if aux == None:
			return sec
		else:
			if aux.hijo_izq != None:
				if len(args) != 0:
					x= args[0] + 'A'
					sec.append(x)
					sec+=self.__Mapeo(aux.hijo_izq,x)
				else:
					x='A'
					sec+=x
					sec+=self.__Mapeo(aux.hijo_izq,x)
		
			if aux.hijo_der != None:
				if len(args) != 0:
					print(args[0])
					print('llegue')
					y=args[0] + 'T'
					sec.append(y)
					sec+=self.__Mapeo(aux.hijo_der,y)
				else:
					y='T'
					sec+=y
					sec+=self.__Mapeo(aux.hijo_der,y)
			return sec



	def __Mapeo (self, aux1, aux0):
		# aux1 y aux0 apunten a el final de secuenciaOrigen y secuenciaDestino respectivamente
		if aux1 == None:
			pass

		else:
			aux0.cantidad += aux1.cantidad
			aux1.cantidad = 0
			
			if aux1.hijo_izq != None:
				if aux0.hijo_izq != None:
					self.__Mapeo(aux1.hijo_izq,aux0.hijo_izq)
				else:
					aux0.hijo_izq = aux1.hijo_izq
					aux1.hijo_izq = None

			if aux1.hijo_der != None:
				if aux0.hijo_der != None:
					self.__Mapeo(aux1.hijo_der,aux0.hijo_der)
				else:
					aux0.hijo_der = aux1.hijo_der
					aux1.hijo_der = None

				

			

# Cambia las secuencias que empiecen por secuenciaOrigen, por unas que
# Empiecen con secuenciaDestino 
	def changemerge (self, secuenciaOrigen, secuenciaDestino):

			if self.raiz == None:
				pass
			else:
				pre=False
				aux0=self.raiz
				for i in secuenciaDestino:
					if i == 'A':
						if aux0.hijo_izq == None:
							pre=True
							break
						else:
							aux0=aux0.hijo_izq
					elif i == 'T':
						if aux0.hijo_der == None:
							pre=True
							break
						else:
							aux0=aux0.hijo_der

					if pre:
						self.add(secuenciaDestino)   # Recordar que se suma 1
						aux0=self.raiz
						for i in secuenciaDestino:
							if i == 'A':
								aux0=aux0.hijo_izq
							elif i == 'T':
								aux0=aux0.hijo_der
						aux0.cantidad -= 1


				aux0=self.raiz				# Posicionamiento de referencias
				for i in secuenciaDestino:
					if i == 'A':
						aux0=aux0.hijo_izq
					elif i == 'T':
						aux0=aux0.hijo_der
				aux1=self.raiz
				for i in secuenciaOrigen:
					if i == 'A':
						aux1=aux1.hijo_izq
					elif i == 'T':
						aux1=aux1.hijo_der
			
				self.__Mapeo(aux1, aux0)




	def Print (self, string):
		archivo = open("salida.txt","a")
		archivo.write(string+"\n")
		archivo.close()
				
		





		
