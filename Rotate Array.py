

def swapElements(arr,start,end):
  arr[start],arr[end]=arr[end],arr[start]
def reverse(arr,start,end):
  while(start<end):
    swapElements(arr,start,end)
    start+=1
    end-=1
  
def rotate(arr,n,d):
  if n==0:
    return
  if d>=n and n!=0:
    d=d%n
  reverse(arr,0,n-1)
  reverse(arr,0,n-d-1)
  reverse(arr,n-d,n-1)
  return arr
arr=[1,2,3,4,5,6,7]
n=7
d=2
rotate(arr,n,d)