
#time complexity: O((n*log(n)) + (m*log(m)))
#Space complexity: O(1)
def intersection(arr1,arr2,n,m):
  
  arr1.sort()
  
  arr2.sort()
  
  i=0
  
  j=0
  while i<n and j<m:
    
    if arr1[i]==arr2[j]:
      
      print(arr1[i],end=" ")
      i+=1
      
      j+=1
    elif arr1[i]<arr2[j]:
      i+=1
    else:
      j+=1
arr1=[2,4,1,6,5]
arr2=[2,3,4,1,6]
n=5
m=6
intersection(arr1,arr2,n,m)
