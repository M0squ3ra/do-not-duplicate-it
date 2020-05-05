import pyinotify
from util import *


#tal vez se pueda reemplazar por una funcion en lugar de una clase
class EventHandler(pyinotify.ProcessEvent):
	def __init__(self,tree):
		self.tree = tree

	def process_IN_CREATE(self, event):
		#print("Creating:", event.pathname)
		state = self.tree.insert(getHash(event.pathname),event.pathname)
		if state != None:
			printRep(state[1],state[3],state[0])


	#def process_IN_MODIFY(self, event):
	#	print('File modified: %s', event.pathname)
		#self.queue.put(event)

	def process_IN_DELETE(self, event):
		print("Removing:", event.pathname)
