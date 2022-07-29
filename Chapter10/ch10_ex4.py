from collections import deque

N = int(input())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
courseTime = [0]*(N+1)
minHour = [0]*(N+1)

for i in range(1,N+1):
  course = list(map(int,input().split()))
  courseTime[i] = course[0]
  for j in course[1:] :
    if j != -1:
      graph[j].append(i)
      indegree[i] += 1

result = [0]*(N+1)
#print(indegree)

q = deque()
for i in range(1,N+1):
  if indegree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  result[now] = courseTime[now] + minHour[now]
  
  for i in graph[now] :
    indegree[i] -= 1
    minHour[i] = max(minHour[i],result[now])
    if indegree[i] == 0:
      q.append(i)

#print(courseTime)
#print(minHour)

for i in range(1,N+1):
  print(result[i])