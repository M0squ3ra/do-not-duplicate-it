import pyinotify

class EventHandler(pyinotify.ProcessEvent):
	def __init__(self,queue):
		self.queue = queue

	def process_IN_CREATE(self, event):
		print("Creating:", event.pathname)
		self.queue.append(event.pathname)
	#def process_IN_MODIFY(self, event):
	#	print('File modified: %s', event.pathname)
		#self.queue.put(event)

	def process_IN_DELETE(self, event):
		print("Removing:", event.pathname)
		self.queue.append(event.pathname)



#p = Process( target=notifier.loop, args=() )
#p.start()
#while True:
#	print(q.get(), "hola")

#p.join()
