def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)
n=int(input())
fact(n)

def sum(n):
  if n==0:
    return 0
  smallOutput=sum(n-1)
  return (smallOutput+n)
n=int(input())
sum(n)

def power(x,n):
  if n==0:
    return 1
  if n==1:
    return x
  smallOutput=power(x,n-1)
  return x*smallOutput
x,n=map(int,input().split())
print(power(x,n))

def print_1_to_n(n):
  if n==0:
    return
  print_1_to_n(n-1)
  print(n)
n=int(input())
print_1_to_n(n)

def print_n_to_1(n):
  if n==0:
    return
  print(n)
  print_n_to_1(n-1)
  return
n=int(input())
print_n_to_1(n)

def fib(n):
  if n==1 or n==2:
    return 1
  fib_n_1=fib(n-1)
  fib_n_2=fib(n-2)
  output=fib_n_1+fib_n_2
  return output
n=4
fib(n)

#copies the list everytime
def isSorted(a):
  l=len(a)
  if l==0 or l==1:
    return True
  if a[0]>a[1]:
    return False
  smallerList=a[1:]
  isSmallerListSorted=isSorted(smallerList)
  return isSmallerListSorted
a=[1,2,3,4,5,6]
isSorted(a)

#optimised soln
def isSortedBetter(a,si):
  l=len(a)
  if si==l-1 or si==l:
    return True
  if a[si] > a[si+1]:
    return False
  isSmallListSorted=isSortedBetter(a,si+1)
  return isSmallListSorted
a=[1,2,3,4,5,6]
si=0
isSortedBetter(a,si)

def sum(a):
  l=len(a)
  if l==1:
    return a[0]
  smallsum=sum(a[:l-1])
  return a[l-1]+smallsum
a=[1,2,3]
sum(a)

def checknumber(a,x):
  l=len(a)
  if l==1:
    return x==a[0]
  smalllist=checknumber(a[:l-1],x)
  return smalllist or (x==a[l-1])
a=[1,2,3,4,5,6]
x=6
checknumber(a,x)
if checknumber(a,x):
  print('true')
else:
  print('false')

#copies the list everytime
def firstIndex(a,x):
  l=len(a)
  if l==0:
    return -1
  if a[0]==x:
    return 0
  smallerList=a[1:]
  smallerListOutput=firstIndex(smallerList,x)
  if smallerListOutput==-1:
    return -1
  else:
    return smallerListOutput+1
a=[1,2,3,4,6,7,6]
firstIndex(a,6)

#optimised solution
def firstIndexBetter(a,x,si):
  l=len(a)
  if si==l:
    return -1
  if a[si]==x:
    return si
  smallerListOutput=firstIndexBetter(a,x,si+1)
  if smallerListOutput==-1:
    return -1
  else:
    return smallerListOutput
a=[1,2,3,4,6,7,6]
firstIndexBetter(a,6,0)

#copies the list every time
def lastIndex(a,x):
  l=len(a)
  if l==0:
    return -1
  smallerList=a[1:]
  smallerListOutput=lastIndex(smallerList,x)
  if smallerListOutput!=-1:
    return smallerListOutput+1
  else:
    if a[0]==x:
      return 0
    else:
      return -1

a=[1,2,3,4,5,4,6,4,7,8]
lastIndex(a,4)

#optimised way
def lastIndexBetter(a,x,si):
  l=len(a)
  if si==l:
    return -1
  smallerListOutput=lastIndexBetter(a,x,si+1)
  if smallerListOutput!=-1:
    return smallerListOutput
  else:
    if a[si]==x:
      return si
    else:
      return -1
a=[1,2,3,4,5,4,6,4,7,8]
lastIndexBetter(a,4,0)

def replaceChar(s,a,b):
  if len(s)==0:
    return s
  smallOutput=replaceChar(s[1:],a,b)
  if s[0]==a:
    return b + smallOutput
  else:
    return s[0]+smallOutput
s="dacdxcd"
replaceChar(s,'a','b')

def replaceChar(s,a,b):
  if len(s)==0:
    return s
  smallOutput=replaceChar(s[1:],a,b)
  if s[0]==a:
    return b + smallOutput
  else:
    return s[0]+smallOutput
s="dacdxcd"
replaceChar(s,'x','')

def replacePi(s):
  if len(s)==0 or len(s)==1:
    return s
  if s[0]=='p' and s[1]=='i':
    smallOutput=replacePi(s[2:])
    return "3.14"+smallOutput
  else:
    smallOutput=replacePi(s[1:])
    return s[0]+smallOutput
s="piabcd"
replacePi(s)

def removeDuplicates(s):
  if len(s)==0 or len(s)==1:
    return s
  if s[0]==s[1]:
    return removeDuplicates(s[1:])
  else:
    return s[0]+removeDuplicates(s[1:])
s="aabbccd"
removeDuplicates(s)

def binarySearch(a,x,si,ei):
  if si>ei:
    return -1
  mid=(si+ei)//2
  if a[mid]==x:
    return mid
  if a[mid]>x:
    return binarySearch(a,x,si,mid-1)
  else:
    return binarySearch(a,x,mid+1,ei)
binarySearch([2,4,6,8,9,10,11,12,16,20],10,0,9)

def merge(a1,a2,a):
  i=0
  j=0
  k=0
  while i<len(a1) and j<len(a2):
    if a1[i] < a2[j]:
      a[k]=a1[i]
      k+=1
      i+=1
    else:
      a[k]=a2[j]
      k+=1
      j+=1
  while i<len(a1):
    a[k]=a1[i]
    k+=1
    i+=1
  while j<len(a2):
    a[k]=a2[j]
    k+=1
    j+=1


def merge_sort(a):
  if len(a)==0 or len(a)==1:
    return
  mid=(len(a))//2
  a1=a[0:mid]
  a2=a[mid:]
  merge_sort(a1)
  merge_sort(a2)
  merge(a1,a2,a)
a=[1,5,4,7,10,6,12]
merge_sort(a)
a

def partition(a,si,ei):
  pivot=a[si]
  c=0
  for i in range(si,ei):
    if a[si]<pivot:
      c+=1
  a[si+c],a[si]=a[si],a[si+c]
  pivot_index=si+c

  i=si
  j=ei
  while i < j:
    if a[i]<pivot:
      i=i+1
    elif a[j] >=pivot:
      j=j-1
    else:
      a[i],a[j]=a[j],a[i]
      i=i+1 
      j=j-1
  return pivot_index



def quick_sort(a,si,ei):
  if si>=ei:
    return
  pivot_index=partition(a,si,ei)
  quick_sort(a,si,pivot_index-1)
  quick_sort(a,pivot_index+1,ei)
a=[1,4,7,3,12,2,8,10,4]
quick_sort(a,0,len(a)-1)
a

def tower_hanoi(n,a,b,c):
  if n==1:
    print("move 1st disc from ",a," to ",c)
    return
  tower_hanoi(n-1,a,c,b)
  print("move ",n," th disc from",a," to ",c)
  tower_hanoi(n-1,b,a,c)
tower_hanoi(4,"s","h","d")

def geometric_sum(n):
  if n==0:
    return 1
  return 1/pow(2,n)+geometric_sum(n-1)
geometric_sum(4)

def isPalindrome(s):
  if len(s)<=1:
    return True
  if s[0]!=s[len(s)-1]:
    return False
  return isPalindrome(s[1:-1])
s="racecar"
isPalindrome(s)

def sum(n):
  if n==0:
    return 0
  return n%10 + sum(n//10)
n=12345
sum(n)

def multiply(m,n):
  if m==0 or n==0:
    return 0
  if m==1:
    return n
  if n==1:
    return m
  return m + multiply(m,n-1)
multiply(6,6)

def count_zeros(n):
  if n==0:
    return 1
  if n<10:
    return 0
  elif n%10==0:
    return 1+count_zeros(n//10)
  return count_zeros(n//10)
count_zeros(10320)

def StringToInt(str):
    if len(str) == 1:
        return ord(str[0]) - ord('0')
    
    y = StringToInt(str[1:])
    x = ord(str[0]) - ord('0')

    x = x*(10**(len(str)-1)) + y
    return int(x)
StringToInt("1234")

def pairStar(s):
  if len(s)<=1:
    return s
  if s[0]!=s[1]:
    return s[0]+pairStar(s[1:])
  else:
    return s[0]+"*"+pairStar(s[1:])
pairStar("aabbcc")

#a. The string begins with an 'a'
#b. Each 'a' is followed by nothing or an 'a' or "bb"
#c. Each "bb" is followed by nothing or an 'a'
def check(s):

    if len(s) == 0:
        return 1
    if s[0] == 'b':
        return False
    if s[0] == 'a':
        if s[1:] == 'a' or s[1] == '' or s[1:3] == 'bb':
            return check(s[3:])
        else:
            return check(s[1:])
    else:
        return False


s = input()
if check(s):
    print('true')
else:
    print('false')

def staircase(n):
  if n==1 or n==0:
    return 1
  if n==2:
    return 2
  else:
    return staircase(n-3)+staircase(n-2)+staircase(n-1)
staircase(4)
