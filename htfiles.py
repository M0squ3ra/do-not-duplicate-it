from util import getHash
from os.path import isdir

class HTFiles:
	#buscar solucion a los multiples diccionarios
	def __init__(self):
		self.dictP = dict() #key = path
		self.dictH = dict() #key = hash
		self.repP = dict() #key = path
		self.repH = dict() #key = hash

	def insert(self,hash,path):
		if isdir(path) != True:
			value = self.dictH.get(hash)
			if value == None:
				self.dictH[hash] = path
				self.dictP[path] = hash
				return None
			else:
				self.repP[path] = hash
				self.repH[hash] = path
				return hash,value,path

	def modify(self,path):
		if isdir(path) != True:
			newHash = getHash(path)
			self.remove(path)
			state = self.insert(newHash,path)
			return state
		else:
			return None

	def move(self,oldP,newP):
		if isdir(newP) != True:
			hash = self.dictP.get(oldP)
			if hash != None:
				self.dictP.pop(oldP)
				self.dictP[newP] = hash
				self.dictH[hash] = newP
			else:
				hash = self.repP.get(oldP)
				self.repP.pop(oldP)
				self.repP[newP] = hash
				self.repH[hash] = newP



	def remove(self,path):
		hashR = self.repP.get(path)
		if hashR == None:
			hashR = self.dictP.get(path)
			if hashR != None:
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
