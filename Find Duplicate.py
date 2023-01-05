

#Time Complexity=O(N)
#Space Complexity=O(1)

def FindDuplicate(arr,n):
  sum=0
  for i in range(0,n):
    sum+=arr[i]
  sumOfNNaturalNumbers=((n-1)*(n-2))//2
  return sum-sumOfNNaturalNumbers

arr=[0 ,2 ,1 ,3 ,1]
n=5
FindDuplicate(arr,n)