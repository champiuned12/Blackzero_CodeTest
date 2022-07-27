X = int(input())

countArray = [0]*(X+1)
countArray[0] = 0
countArray[1] = 0
countArray[2] = 1
countArray[3] = 1
countArray[4] = 2
countArray[5] = 1
for i in range(X+1):
  if i < 6 :
    continue
  else :
    minimum = countArray[i-1]
    if i % 5 == 0:
      minimum = min(minimum,countArray[i//5])
    if i % 3 == 0:
      minimum = min(minimum,countArray[i//3])
    if i % 2 == 0:
      minimum = min(minimum,countArray[i//2])
    countArray[i] = 1+minimum

print(countArray[X])
