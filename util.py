from hashlib import md5
from os import listdir
from os.path import isdir,isfile
from btree import Btree

def printRep(parent,copy,hash):
	print("[**] Duplicated file detected: \n" +
		"Old: "+ parent + "\n" +
		"New: " + copy + "\n" +
		 "Hash: " + hash + "\n")

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


def getDirs(path):
	dirs = []
	for i in listdir(path):
		if isdir(path + "/" + i):
			dirs.append(path + "/" + i)

	for j in dirs:
		dirs = dirs + getDirs(j)

	return dirs

def getFiles(path):
	files = []
	for i in listdir(path):
		if isfile(path + "/" + i):
			files.append(path + "/" + i)

	return files

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
