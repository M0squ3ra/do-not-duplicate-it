class HTFiles:
	def __init__(self):
		self.dict = dict()
		self.repP = dict() #key = path
		self.repH = dict() #key = hash

	def insert(self,hash,path):
			value = self.dict.get(hash)
			if value == None:
				self.dict[hash] = path
			else:
				self.repP[path] = hash
				self.repH[hash] = path
				return hash,value,path
