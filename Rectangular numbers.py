n=int(input())
n1=(n//2)+1
n2=n1-1
for i in range(1,n1+1):
    for sp1 in range (n1-i):
        print(" ",end="")
    for str1 in range(2*i-1):
        print('*',end="")
    print()
for i in range(1,n2+1):
    for sp2 in range(1,i+1):
        print(" ",end="")
    for str2 in range(2*(n2-i)+1,0,-1):
        print("*",end="")
    print()
