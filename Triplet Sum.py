

#Time Complexity : O(n^2)
#Space Complexity : O(1)
def tripletSum(arr,n,num):
  arr.sort()
  
  numTriplets=0
  for i in range(n) :
    pairSumFor = num-arr[i]

    numPairs=pairSum(arr, (i+1),(n-1), pairSumFor)
    numTriplets+=numPairs
  return numTriplets

def pairSum(arr, startIndex, endIndex, num):
  numPair=0
  while startIndex < endIndex:
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

arr=[2 ,-5 ,8 ,-6 ,0 ,5 ,10 ,11 ,-3]
n=9
num=10
tripletSum(arr,n,num)