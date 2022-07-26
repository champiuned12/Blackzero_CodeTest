N,M = map(int,input().split())
arrayA = list(map(int,input().split()))
arrayB = list(map(int,input().split()))

arrayA.sort()
arrayB.sort(reverse=True)

sum = 0
for i in range(M):
  sum = sum+max(arrayA[i],arrayB[i])
for j in range(N-1,N-M,-1):
  sum = sum+arrayA[j]

print(sum)
