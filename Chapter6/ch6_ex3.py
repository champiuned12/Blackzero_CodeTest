N = int(input())
result = []
for _ in range(N):
  x, y = input().split()
  result.append((x,int(y)))

result.sort(key= lambda x:x[1])
for i in result:
  print(i[0], end=' ')

