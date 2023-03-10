from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class Queue :
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def enqueue(self, data) :
        newNode = Node(data)
        self.__count += 1
        if self.__head == None :
            self.__head = newNode
        else:
        	self.__tail.next = newNode
        self.__tail = newNode
        return

    def dequeue(self) :
        if self.isEmpty():
            return -1
        removedNode = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return removedNode
        
    def getSize(self) :
        return self.__count
        
    def isEmpty(self) :
        return self.__count == 0

    def front(self) :
        if self.__head == None :
            return -1
        return self.__head.data
        
#main
q = int(stdin.readline().strip())
queue = Queue()
while q > 0 :
    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])
    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)
    elif choice == 2 :
        print(queue.dequeue())
    elif choice == 3 :
        print(queue.front())
    elif choice == 4 : 
        print(queue.getSize())
    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")
    q -= 1
