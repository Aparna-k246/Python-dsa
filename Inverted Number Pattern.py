    ## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i+1:
        print(n-i+1,end="")
        j=j+1
    print()
    i=i+1
