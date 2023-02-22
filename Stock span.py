from sys import stdin

def stockSpan(price, n) :
    answer = [0]*n
    answer[0] = 1
    
    stack = []
    stack.append(0)
    
    for i in range(1,n):
        while(len(stack)>0 and price[stack[-1]] < price[i]):
            stack.pop()
            
        if len(stack)<=0:
            answer[i] = i + 1
        else:
            answer[i] = i - stack[-1]
            
        stack.append(i)
        
    return answer
    
    
def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")
	print()

def takeInput():
	size = int(stdin.readline().strip())
	if size == 0 :
		return list(), 0
	price = list(map(int, stdin.readline().strip().split(" ")))
	return price, size

#main
price, n = takeInput()
output = stockSpan(price, n)
printList(output)
