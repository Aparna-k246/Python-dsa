

#Time Complexity : O(n(logn))
#Space Complexity : O(n)
def pairSum(arr,n,num):
  arr.sort()
  startIndex=0
  endIndex=(n-1)
  numPair=0
  while startIndex<endIndex:
    if arr[startIndex] + arr[endIndex] <num:
      startIndex +=1
    elif arr[startIndex] + arr[endIndex] > num:
      endIndex -=1
    else:
      elementAtStart = arr[startIndex]
      elementAtEnd = arr[endIndex]

      if elementAtStart ==elementAtEnd:
        totalElementsFromStartToEnd=(endIndex-startIndex)+1
        numPair += (totalElementsFromStartToEnd * (totalElementsFromStartToEnd -1) //2)

        return numPair
      tempStartIndex = startIndex+1
      tempEndIndex = endIndex-1
      while (tempStartIndex <= tempEndIndex) and (arr[tempStartIndex]==elementAtStart):
        tempStartIndex+=1
      while (tempEndIndex >= tempStartIndex) and (arr[tempEndIndex] == elementAtEnd):
        tempEndIndex -=1

      totalElementsFromStart = (tempStartIndex -startIndex)
      totalElementsFromEnd = (endIndex - tempEndIndex)
      numPair+= (totalElementsFromStart * totalElementsFromEnd)

      startIndex=tempStartIndex
      endIndex=tempEndIndex
  return numPair

arr=[1 ,3 ,6 ,2 ,5 ,4 ,3 ,2 ,4]
n=9
m=7
pairSum(arr,n,m)