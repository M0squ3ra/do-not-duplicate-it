import pyinotify
from util import printRep,getHash

class EventHandler(pyinotify.ProcessEvent):
	def __init__(self,tree):
		self.tree = tree

	def process_IN_CREATE(self, event):
		state = self.tree.insert(getHash(event.pathname),event.pathname)
		if state != None:
			printRep(state[1],state[2],state[0])

	def process_IN_DELETE(self, event):
		print("Removing:", event.pathname)
		self.tree.remove(event.pathname)
