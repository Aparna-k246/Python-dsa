
#Time Complexity=O(N)

#Space Complexity=O(1)
def arrayEquilibriumIndex(arr,n):
  
  rightSum,leftSum=0,0
  
  for i in range(n):
    
    rightSum+=arr[i]
    
  for i in range(n):
    
    rightSum-=arr[i]
    
   if rightSum==leftSum:
     
      return i
     
    leftSum+=arr[i]

  return -1
arr=[1, 4, 9, 3 ,2]
n=5

arrayEquilibriumIndex(arr,n)
