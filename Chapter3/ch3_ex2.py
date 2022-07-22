inputList = list(map(int,input().split()))                 
n = inputList[0]
m = inputList[1]
k = inputList[2]
sum = 0

numberList = list(map(int,input().split()))

biggestNumber = 0
secondBiggestNumber = 0

for _ in range(n):
  if numberList[_] > biggestNumber :
    secondBiggestNumber = biggestNumber
    biggestNumber = numberList[_]
  elif numberList[_] == biggestNumber :
    secondBiggestNumber = biggestNumber

temp_k = 0
while(m>0):
  m = m-1
  temp_k = temp_k+1
  if(temp_k > k):
    temp_k = 0
    sum = sum + secondBiggestNumber
  else:
    sum = sum + biggestNumber

print(sum)
