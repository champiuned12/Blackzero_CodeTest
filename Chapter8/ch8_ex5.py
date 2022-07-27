"""
N,M = map(int,input().split())

arrayN=[]
calculatedArray = [0]*(10001)
for _ in range(N):
  arrayN.append(int(input()))
arrayN.sort()

for i in arrayN:
  calculatedArray[i] = 1

def calculate(M):
  if M < arrayN[0] :
    return None
  
  if calculatedArray[M] != 0 :
    return calculatedArray[M]
  
  minimum = 1e9
  calculatable = False
  for i in arrayN:
    if calculate(M-i) is not None:
      calculatable = True
      minimum = min(minimum, calculate(M-i))
  if calculatable:
    calculatedArray[M] = minimum+1
    return minimum+1
  else :
    return None

calculate(M)
if calculatedArray[M] == 0:
  print(-1)
else :
  print(calculatedArray[M])
"""

n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input()))

d = [10001]*(m+1)

d[0] = 0
for i in range(n):
  for j in range(array[i], m+1):
    if d[j-array[i]] != 10001:
      d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])