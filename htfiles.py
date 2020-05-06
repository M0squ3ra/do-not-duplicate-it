class HTFiles:
	#buscar solucion a los multiples diccionarios
	def __init__(self):
		self.dictP = dict() #key = path
		self.dictH = dict() #key = hash
		self.repP = dict() #key = path
		self.repH = dict() #key = hash

	def insert(self,hash,path):
		value = self.dictH.get(hash)
		if value == None:
			self.dictH[hash] = path
			self.dictP[path] = hash
			return None
		else:
			self.repP[path] = hash
			self.repH[hash] = path
			return hash,value,path

	def remove(self,path):
		hashR = self.repP.get(path)
		if hashR == None:
			hashR = self.dictP.get(path)
			self.dictH.pop(hashR)
			self.dictP.pop(path)
			pathR = self.repH.get(hashR)
			if pathR != None:
				self.dictH[hashR] = pathR
				self.dictP[pathR] = hashR
				self.repH.pop(hashR)
				self.repP.pop(pathR)

		else:
			self.repH.pop(hashR)
			self.repP.pop(path)
