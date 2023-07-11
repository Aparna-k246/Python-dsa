


from sys import stdin


def checkRedundantBrackets(expression) :
	
	
    stack = []
    
	
    for char in expression:
	    
        if char==')' :
		
            count = 0
		
            while(stack.pop() != '('):
		    
                count += 1
		    
            if count<=1:
		    
                return True
        else:
            stack.append(char)
     

    return False


#main
expression = stdin.readline().strip()
if checkRedundantBrackets(expression) :
	print("true")
else :
	print("false")

	
	
