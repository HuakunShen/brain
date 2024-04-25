class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
	
	def __str__(self):
		return str(self.value)

class TreeNode:
	def __init__(self, value, parent=None):
		self.value = value
		self.parent = parent
	
	def __str__(self):
		return "Value: {0}, Parent: {1}".format(self.value, self.parent)

