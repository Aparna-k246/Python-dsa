

import queue



class BinaryTreeNode:
    
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None

        
def constructBST(lst, startIndex, endIndex):
    
    if startIndex>endIndex:
        return 
    
    mid = (startIndex+endIndex)//2

    root = BinaryTreeNode(lst[mid])
    root.left = constructBST(lst, startIndex, mid-1)
    root.right = constructBST(lst, mid+1, endIndex)
    
    return root


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    
    preOrder(root.left)
    preOrder(root.right)

    
# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst, 0, len(lst)-1)
preOrder(root)
