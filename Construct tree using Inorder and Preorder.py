from sys import stdin, setrecursionlimit

import queue




setrecursionlimit(10 ** 6)

class BinaryTreeNode:
    def __init__(self, data):
	    
        self.data = data
        self.left = None
        self.right = None

def buildTree(preOrder, inOrder, n) :
	
    if n==0:
        return None
    
    rootData = preOrder[0]
    root = BinaryTreeNode(rootData)
    indexOfRoot = inOrder.index(rootData)
    
    inOrderLeft = inOrder[ : indexOfRoot]
    inOrderRight = inOrder[indexOfRoot+1 : ]
    
    lengthOfLeft = len(inOrderLeft)
    preOrderLeft = preOrder[1 : lengthOfLeft+1]
    preOrderRight = preOrder[lengthOfLeft+1 : ]
    
    leftSubTree = buildTree(preOrderLeft, inOrderLeft, len(preOrderLeft))
    rightSubTree = buildTree(preOrderRight, inOrderRight, len(preOrderRight))
    
    root.left = leftSubTree
    root.right = rightSubTree
    
    return root
	
    

def printLevelWise(root):
    if root is None :
        return
    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)
    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
        if frontNode is None :
            print()       
            if not pendingNodes.empty() :
                pendingNodes.put(None)            
        else :
            print(frontNode.data, end = " ")
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), list(), 0
    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))
    return preOrder, inOrder, n

# Main
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)
