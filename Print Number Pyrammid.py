## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
n1=n
n2=n-1
for i in range (1,n1+1):
    for sp1 in range(1,i):
        print(" ",end='')
    for num1 in range(i,n1+1):
        print(num1,end="")
    print()
for i in range (1,n2+1):
    for sp2 in range(n2-i,0,-1):
        print(" ",end="")
    for num2 in range (n2-i+1,n2+2):
        print(num2,end="")
    print()
