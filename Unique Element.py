

#Time Complexity=O(N)
#Space Complexity=O(1)

def UniqueElement(arr,n):
  XOR=0
  for i in range(n):
    XOR ^=arr[i]
  return XOR
arr=[2 ,3 ,1 ,6 ,3 ,6 ,2]
n=7
UniqueElement(arr,n)