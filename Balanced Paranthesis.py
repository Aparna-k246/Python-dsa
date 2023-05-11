from sys import stdin
import queue



def isBalanced(expression) :
    stck = []
    
    for char in expression:
        if char in '({[' :
            stck.append(char)
            
        elif char==')':
            if not stck or stck[-1]!='(' :
                return False
            stck.pop()
            
        elif char=='}':
            if not stck or stck[-1]!='{' :
                return False
            stck.pop()
            
        elif char==']':
            if not stck or stck[-1]!='[' :
                return False
            stck.pop()
    
    if not stck:
        return True
    
    return False

#main
expression = stdin.readline().strip()
if isBalanced(expression) :
	print("true")
else :
	print("false")
