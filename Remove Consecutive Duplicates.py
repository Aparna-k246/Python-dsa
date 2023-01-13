
from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
    i=0
    y=""
    while i<len(string):
        x=string[i]
        j=i+1
        c=1
        while j<len(string) and string[j]==x:
            j=j+1
        y=y+string[i]
        i=j
    return y



























	


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
