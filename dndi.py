#!/usr/bin/env python3
#organizar en binary tree por los hashes de los archivos, si coincide mandar a una lista la ruta del nuevo y la del anterior


from btree import Btree
from os import listdir
from os.path import isdir
from hashlib import md5

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






initTree(".")
