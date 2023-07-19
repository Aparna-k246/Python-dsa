from sys import stdin
#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def length(head):
    len = 0
    while head is not None:
        len += 1
        head = head.next
    return len
def appendLastNToFirst(head,n) :
    len = length(head)
    if n==0:
        return head
    
    elif n>0 and n<len:
        
        newHead = head
        tail = head
        
        for i in range(len-n-1):
            tail = tail.next
            newHead = newHead.next
        newHead = newHead.next
        tail.next = None
        tail = newHead
        
        while tail.next is not None:
            tail = tail.next
                
        tail.next = head
        head  = newHead
        
        return head
    
    return


























#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 

    
