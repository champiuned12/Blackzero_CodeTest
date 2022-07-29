N, M = map(int,input().split())

parents = [ i for i in range(N+1)]

def findParent(parents,i):
  if parents[i] != i:
    parents[i] = findParent(parents, parents[i])
  return parents[i]

def setParent(parents,i,j):
  i = findParent(parents, i)
  j = findParent(parents, j)
  if i < j :
    parents[j] = i
  else :
    parents[i] = j
  
for _ in range(M):
  a, b, c = map(int,input().split())
  if a == 1:
    if(findParent(parents,b) == findParent(parents,c)):
      print("YES")
    else:
      print("NO")
  else:
    setParent(parents,b,c)

