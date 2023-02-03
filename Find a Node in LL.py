# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    index = 0
    
    while head is not None:
        if head.data == n:
            return index
        head = head.next
        index += 1
        
    return -1
