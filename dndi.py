#!/usr/bin/env python3
#organizar en binary tree por los hashes de los archivos, si coincide mandar a una lista la ruta del nuevo y la del anterior
#trabajar con threads, uno para capturar cambios y otro para procesarlos
#agregar una opcion verbose para ver cambios en carpetas ademas de si hay duplicados (-v)

from btree import Btree
from os import listdir
from os.path import isdir,isfile
from hashlib import md5
import pyinotify
import sys
from event_handler import EventHandler
import time

def getHash(file):
	try:
		hashmd5 = md5()
		with open(file,"rb") as f:
			for block in iter(lambda: f.read(4096),b""):
				hashmd5.update(block)
		return hashmd5.hexdigest()
	except Exception as e:
		print("Error: %s" % (e))
		return ""
	except:
		print("Unknown error")
		return ""


def getFiles(path):
	dirs = []
	files = []
	for i in listdir(path):
		if isdir(i):
			dirs.append(path + "/" + i)
		else:
			if isfile(i):
				files.append(path + "/" + i)

	for j in dirs:
		files = files + getFiles(j)

	return files

def initTree(path):
	tree = Btree()
	files = getFiles(path)
	rep = []

	for i in files:
		state = tree.insert(getHash(i),i)
		if state != None:
			rep.append(state)

	return tree,rep

def printRep(parent,copy,hash):
	print("[**] " + parent + " == " + copy + " --> " + hash)

path = "."

tree,rep = initTree(path)

for i in rep:
	printRep(i[1],i[3],i[0])


wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE #| pyinotify.IN_MODIFY | pyinotify.IN_DELETE

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(path, mask, rec=True)


#for d in dirs:  para añadir varios directorios
#	wm.add_watch(d, mask)

def process(notifier):
	#deberia poder procesar los eventos, obteniendo los datos
	if(notifier.check_events()):
		print("Nuevo evento")
	#	notifier.read_events()
	#	notifier.process_events()
	#	print(notifier.read_events())
	return None #para que el loop no termine
notifier.loop(callback=process) #investigar, si retorna true, el loop termina
# - Functor called after each event processing iteration
