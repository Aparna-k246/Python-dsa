## Read input as specified in the que
## Print output as specified in the question.
N=int(input())

li=[int(x) for x in input().split()]
sum=0
for ele in li:
    sum=sum+ele
print(sum)
