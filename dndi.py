#!/usr/bin/env python3
#organizar en binary tree por los hashes de los archivos, si coincide mandar a una lista la ruta del nuevo y la del anterior
#trabajar con threads, uno para capturar cambios y otro para procesarlos
#agregar una opcion verbose para ver cambios en carpetas ademas de si hay duplicados (-v)

from btree import Btree
import pyinotify
import sys
from event_handler import EventHandler
import time
from queue import Queue
from util import *


def initTree(path):
	tree = Btree()
	dirs = getDirs(path)
	dirs = [path] + dirs
	files = []

	for j in dirs:
		files = files + getFiles(j)

	rep = []

	for i in files:
		state = tree.insert(getHash(i),i)
		if state != None:
			rep.append(state)

	for i in rep:
		printRep(i[1],i[3],i[0])

	return tree,rep,dirs

path = "/home/lol/Escritorio/do-not-duplicate-it/pruebas"

tree,rep,dirs = initTree(path)

wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE #| pyinotify.IN_MODIFY | pyinotify.IN_DELETE

handler = EventHandler(tree)
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(path, mask, rec=True)

def process(notifier):
	if(notifier.check_events()):
		print("Nuevo evento")
	return None #para que el loop no termine

notifier.loop(callback=None) #investigar, si retorna true, el loop termina
# - Functor called after each event processing iteration
