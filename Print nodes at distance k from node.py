from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesAtDistanceK(root, node, k) :
    if root is None:
        return -1
    
    if root.data==node:
        printNodesAtDistanceK(root,k)
        return 0
    
    leftDistanceFromRoot = nodesAtDistanceK(root.left, node, k)
    if leftDistanceFromRoot != -1 :
        if leftDistanceFromRoot+1 == k:
            print(root.data)
        else:
            printNodesAtDistanceK(root.right, k-leftDistanceFromRoot-2)
        return leftDistanceFromRoot+1
    
    rightDistanceFromRoot = nodesAtDistanceK(root.right, node, k)
    if rightDistanceFromRoot != -1 :
        if rightDistanceFromRoot+1 == k:
            print(root.data)
        else:
            printNodesAtDistanceK(root.left, k-rightDistanceFromRoot-2)
        return rightDistanceFromRoot+1
    
    return -1


def printNodesAtDistanceK(root, k):
    if root is None:
        return None
    
    if k==0 :
        print(root.data)
        return
    
    printNodesAtDistanceK(root.left,k-1)
    printNodesAtDistanceK(root.right,k-1)

    
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
target_k = stdin.readline().strip().split(" ")
target = int(target_k[0])
k = int(target_k[1])
nodesAtDistanceK(root, target, k)
