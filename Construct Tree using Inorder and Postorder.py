from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

	
def buildTree(postOrder, inOrder, n) :
    if n==0:
        return None
    
    rootData = postOrder[-1]
    root = BinaryTreeNode(rootData)
    indexOfRoot = inOrder.index(rootData)
	
    inOrderLeft = inOrder[ : indexOfRoot]
    inOrderRight = inOrder[indexOfRoot+1 : ]
    
    lenghtOfLeft = len(inOrderLeft)
    postOrderLeft = postOrder[ : lenghtOfLeft]
    postOrderRight = postOrder[lenghtOfLeft : -1]
    
    leftSubTree = buildTree(postOrderLeft, inOrderLeft, len(postOrderLeft))
    rightSubTree = buildTree(postOrderRight, inOrderRight, len(postOrderRight))
    
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
    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))
    return postOrder, inOrder, n

# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)
