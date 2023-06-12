
## Print ou
n=int(input())
i=1
while i<=n:
    j=1
    k=ord('A')+i-1
    while j<=i:
        char=chr(k)
        print(char,end='')
        j=j+1
        
    i=i+1
    print()

    
