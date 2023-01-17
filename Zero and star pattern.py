## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n+1):
    for j in range(1,(2*n)+2):
        if i==j or j==n+1 or j==(2*n+1)-i+1:
            print('*',end="")
        else:
            print('0',end="")
    print()
