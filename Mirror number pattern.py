## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end="")
        spaces+=1
    stars=1
    while stars<=i:
        print(stars,end="")
        stars=stars+1
    print()
    i=i+1
