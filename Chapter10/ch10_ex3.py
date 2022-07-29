import heapq
N, M = map(int,input().split())
q = []

result = 0
maxRoad = 0

parent = [i for i in range(N+1)]

def findparent(parent, i):
  if(parent[i] != i):
    parent[i] = findparent(parent,parent[i])
  return parent[i]

def unionparent(parent, i, j):
  i = findparent(parent, i)
  j = findparent(parent, j)
  if(i < j):
    parent[j] = i
  else :
    parent[i] = j

for _ in range(M):
  A, B, Cost = map(int,input().split())
  heapq.heappush(q,(Cost,A,B))

for _ in range(N-1):
  (Cost, A, B) = heapq.heappop(q)
  while(findparent(parent, A) == findparent(parent, B)):
    (Cost, A, B) = heapq.heappop(q)
  maxRoad = max(Cost,maxRoad)
  unionparent(parent,A,B)
  result = result + Cost

print(result-max)
  
