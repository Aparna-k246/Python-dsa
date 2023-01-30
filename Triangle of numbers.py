## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(" ",end='')
        spaces=spaces+1
    num=1
    p=i
    while num<=i:
        print(p,end='')
        num=num+1
        p=p+1
   
    p=2*i-2
    while p>=i:
        print(p,end='')
        p=p-1
        
        
    print()
    i=i+1
