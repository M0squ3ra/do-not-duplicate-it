class Node:

	def __init__(self, label, path, parent):
		self.label = label
		self.path = path
		self.left = None
		self.right = None
		self.parent = parent

	def getLabel(self):
		return self.label

	def getPath(self):
		return self.path

	def getLeft(self):
		return self.left

	def setLeft(self, left):
		self.left = left

	def getRight(self):
		return self.right

	def setRight(self, right):
		self.right = right

	def getParent(self):
		return self.parent

	def setParent(self, parent):
		self.parent = parent

class Btree:
	def __init__(self):
		self.root = None

	def insert(self,hash,path):
		new = Node(hash,path,None)

		if self.root == None:
			self.root = new

		else:
			curr_node = self.root
			equal = False
			while (curr_node is not None) and not equal:
				if curr_node.label == new.label:
					equal = True
				else:
					parent_node = curr_node
					if new.getLabel() < curr_node.getLabel():
						curr_node = curr_node.getLeft()
					else:
						curr_node = curr_node.getRight()

			if not equal:
				if new.getLabel() < parent_node.getLabel():
					parent_node.setLeft(new)
				else:
					parent_node.setRight(new)
				new.setParent(parent_node)
		
				return None
			else:
				return (curr_node.getLabel(),curr_node.getPath(),new.getLabel(),new.getPath())
