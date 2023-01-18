


def printTable(start,end,step):
   while start<=end:
        c=(start-32)*5
        c=int(c/9)
        print(start ,c)
        start=start+step
   

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





