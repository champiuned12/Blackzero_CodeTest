N,M = map(int,input().split())
weight =[]
numberofBalls = [[] for _ in range(M+1)]
mylist = list(map(int,input().split()))
for i in range(1,N+1):
  if(mylist[i-1] not in weight):
    weight.append(mylist[i-1])
  numberofBalls[mylist[i-1]].append(i)

result = 0
for j in range(1,len(numberofBalls)):
  for k in range(j,len(numberofBalls)):
    if j == k :
      continue
    else :
      result = result + len(numberofBalls[j]) * len(numberofBalls[k])
    
#print(weight)
#print(numberofBalls)
print(result)