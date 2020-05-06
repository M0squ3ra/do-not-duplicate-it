#!/usr/bin/env python3

import pyinotify
from event_handler import EventHandler
from util import *
from inittree import initTree


path = "/home/lol/Escritorio/do-not-duplicate-it/pruebas"

tree = initTree(path)

wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY | pyinotify.IN_MOVED_TO | pyinotify.IN_MOVED_FROM

handler = EventHandler(tree)
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(path, mask, rec=True)

#problema: si se agregan carpetas durante la ejecucion, este no las agrega al watch
#posible solucion: que el loop este adentro de un while
# y que en el callback se detecte que es una carpeta y se pare el loop


def process(notifier):
	if(notifier.check_events()):
		print("Nuevo evento")
	return None

notifier.loop(callback=None)
