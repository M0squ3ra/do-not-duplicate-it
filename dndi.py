#!/usr/bin/env python3

import pyinotify
from event_handler import EventHandler
from util import *


path = "/home/lol/Escritorio/do-not-duplicate-it/pruebas"

tree = initTree(path)

wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE

handler = EventHandler(tree)
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(path, mask, rec=True)

#problema: si se agregan carpetas durante la ejecucion, este no las agrega al watch

def process(notifier):
	if(notifier.check_events()):
		print("Nuevo evento")
	return None

notifier.loop(callback=None)
