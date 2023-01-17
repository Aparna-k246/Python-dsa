## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j==i:
            print('*',end="")
        else:
            print(j,end="")
    print()
 
