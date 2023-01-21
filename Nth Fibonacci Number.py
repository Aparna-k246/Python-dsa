## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
a=0
b=1
i=2
while i<=n:
        
        c=a+b
        a=b
        b=c
        i=i+1
print(b)
