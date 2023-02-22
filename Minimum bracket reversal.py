from sys import stdin

def countBracketReversals(inputString) :
    if len(inputString)%2 != 0 :
        return -1
    
    stack = []
    for char in inputString:
        if char=='{':
            stack.append(char)
        else:
            if(len(stack)>0) :
                if(stack[-1]=='{') :
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
    
    count = 0
    for i in range(len(stack)-1,-1,-2):
        if(stack[i]==stack[i-1]):
            count += 1
        else:
            count += 2
    
    return count
        
    
print(countBracketReversals(stdin.readline().strip()))
