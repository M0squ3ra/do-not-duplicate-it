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

def process(notifier):
	if(notifier.check_events()):
		wm.add_watch(path,mask,rec=True)
	return None

notifier.loop(callback=process)
