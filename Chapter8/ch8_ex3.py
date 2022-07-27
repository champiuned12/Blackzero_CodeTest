N = int(input())
inputArray = list(map(int,input().split()))
countArray = [0]*N
countArray[0] = inputArray[0]
countArray[1] = max(inputArray[0],inputArray[1])
for i in range(2,N):
  countArray[i] = max(countArray[i-1],countArray[i-2]+inputArray[i])
print(countArray[N-1])
