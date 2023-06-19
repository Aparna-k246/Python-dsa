

from sys import stdin, setrecursionlimit

import queue

setrecursionlimit(10 ** 6)

class BinaryTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertDuplicateNode(root):
    if root is None:
        
        return None
    
    insertDuplicateNode(root.left)
    insertDuplicateNode(root.right)
    
   
    duplicate = BinaryTreeNode(root.data)
    duplicate.left = root.left
    root.left = duplicate
    
    return root
    

#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    length = len(levelOrder)
    if length == 1 :
        return None  
    root = BinaryTreeNode(levelOrder[start])
    start += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelOrder[start]
        start += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelOrder[start]
        start += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root
  
def printLevelWise(root):
    if root is None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():   
        while not inputQ.empty():   
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)   
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
root = takeInput()
insertDuplicateNode(root)
printLevelWise(root)
