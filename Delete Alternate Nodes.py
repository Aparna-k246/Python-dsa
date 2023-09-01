


import math



class Node:
	
	def _init_(self, data):
		self.data = data
		self.next = None

def deleteAlternateNodes(head):
	if (head == None):
		return
	prev = head
	now = head.next
	while (prev != None and now != None):
		prev.next = now.next
		now = None
		prev = prev.next
		if (prev != None):
			now = prev.next
