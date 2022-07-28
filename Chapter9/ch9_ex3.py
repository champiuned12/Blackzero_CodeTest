import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  x, y, z = map(int,input().split())
  graph[x].append((y,z))
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

dijkstra(C)
maxTime = 0
countCity = 0
for i in distance:
  if i != 0 and i != INF:
    maxTime = max(maxTime,i)
    countCity += 1
print(str(countCity)+" "+str(maxTime))