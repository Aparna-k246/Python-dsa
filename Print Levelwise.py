from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
    if root is None:
        return None
    q = queue.Queue()
    q.put(root)
    while(not q.empty()):
        currentNode = q.get()
        print(currentNode.data, end=':')
        
        if currentNode.left is None:
            print('L:'+'-1', end=',')
        elif currentNode.left!=-1:
            print('L:'+str(currentNode.left.data), end=',')
            q.put(currentNode.left)
            
        if currentNode.right is None:
            print('R:'+'-1')
        elif currentNode.right!=-1:
            print('R:'+str(currentNode.right.data))
            q.put(currentNode.right)
    return


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

# Main
root = takeInput()
printLevelWise(root)
