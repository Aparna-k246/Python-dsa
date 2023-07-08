

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

i = 1
while i <= n:
    j = 1
    startP = ord('A')+n - i
    while j<= i:
        #print jth column
        
        print(chr(startP+j-1), end='')
        j = j + 1
    print()
    i = i + 1
