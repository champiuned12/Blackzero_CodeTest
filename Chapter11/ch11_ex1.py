N = int(input())
countList = [0]*(N+1)

adventurerList = list(map(int,input().split()))
for j in adventurerList:
  countList[j] += 1

result = 0
leftoverAdventurer = 0
for i in range(1,len(countList)):
  if (leftoverAdventurer + countList[i]) >= i :
    result += 1
    leftoverAdventurer = leftoverAdventurer + countList[i] - i

print(result)