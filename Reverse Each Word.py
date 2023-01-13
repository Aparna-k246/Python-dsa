
from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
    w = string.split(" ")        
                           
    nw= [i[::-1] for i in w]
                          
    ns = " ".join(nw)
    return ns


























	



#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
