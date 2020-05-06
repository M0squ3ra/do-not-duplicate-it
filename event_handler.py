import pyinotify
from util import printRep,getHash
from os.path import isdir

class EventHandler(pyinotify.ProcessEvent):
	def __init__(self,tree):
		self.tree = tree
		self.MF = None

	def process_IN_CREATE(self, event):
		if isdir(event.pathname):
			print("es una carpeta")
		else:
			state = self.tree.insert(getHash(event.pathname),event.pathname)
			if state != None:
				printRep(state[1],state[2],state[0])

	def process_IN_DELETE(self, event):
		print("Removed:", event.pathname,"\n")
		self.tree.remove(event.pathname)

	def process_IN_MODIFY(self, event):
		print("Modificado: ", event.pathname)
		state = self.tree.modify(event.pathname)
		if state != None:
			printRep(state[1],state[2],state[0])

	def process_IN_MOVED_FROM(self,event):
		self.MF = event.pathname

	def process_IN_MOVED_TO(self,event):
		#llama primero a IN_MOVED_FROM
		print("Moved from: ", self.MF)
		print("      to: ", event.pathname,"\n")
		self.tree.move(self.MF,event.pathname)
		self.MF = None
