## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n=int(input())
even=0
odd=0

while(n!=0):
    d=n%10
    if(d%2==0):
        even=even+d
    else:
        odd=odd+d
    n=n//10
print(even, odd)
    
    
