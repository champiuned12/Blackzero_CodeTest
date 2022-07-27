N = int(input())
arrayN = list(map(int,input().split()))
M = int(input())
arrayM = list(map(int,input().split()))

arrayN.sort()

def binarySearch(start,end,target):
  if start > end :
    return False
  mid = (start + end)//2
  if arrayN[mid] == target:
    return True
  elif arrayN[mid] > target:
    return binarySearch(start,mid-1,target)
  else :
    return binarySearch(mid+1,end,target)


for i in arrayM:
  if binarySearch(0,len(arrayN)-1,i) == True:
    print("yes", end = " ")
  else :
    print("no", end = " ")
  