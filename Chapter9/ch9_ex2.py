"""
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  x, y = map(int,input().split())
  graph[x].append((y,1))
  graph[y].append((x,1))
X, K = map(int,input().split())
distance = [INF] * (N+1)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist+i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost, i[0]))

def reset():
  for _ in range(len(distance)):
    distance[_] = INF
  
tmp = 0
dijkstra(1)
if distance[K] == INF:
  print(-1)
else :
  tmp = distance[K]
  reset()
  dijkstra(K)
  if distance[X] == INF:
    print(-1)
  else :
    print(tmp+distance[X])
"""

INF = int(1e9)

n, m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a,b = map(int,input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int,input().split())

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print(-1)
else:
  print(distance)
