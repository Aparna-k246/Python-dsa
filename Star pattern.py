## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(' ',end="")
        space=space+1
    stars=1
    while stars<=i:
        print("*",end='')
        stars=stars+1
    stars=i-1
    while stars>=1:
        print("*",end='')
        stars=stars-1
    print()
    i=i+1
        
    
    
    
