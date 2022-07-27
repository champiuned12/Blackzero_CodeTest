"""
N, M = map(int,input().split())
arrayN = list(map(int,input().split()))

arrayN.sort(reverse=True)

sum = 0
result = 0
for i in range(arrayN[0],0,-1):
  for j in arrayN:
    if j - i > 0:
      sum += j - i
    else :
      break
  if (sum >= M):
    result = i
    break
  else : 
    sum = 0

print(i)
"""

n, m = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while(start<=end):
  total = 0
  mid = (start+end)//2
  for x in array:
    if x > mid:
      total += x-mid
  if total < m:
    end = mid-1
  else:
    result = mid
    start = mid+1

print(result)