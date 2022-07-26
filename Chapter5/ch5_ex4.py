n,m = map(int,input().split())

graph = []
for i in range(n) : 
  graph.append(list(map(int,input())))

result=[]

def dfs(x,y,count):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return 999
  if x == n-1 and y == m-1:
    #print("flag"+str(x)+" "+str(y)+" "+str(count))
    graph[x][y] = 0
    result.append(count)
  if graph[x][y] == 1 :
    #print("flag"+str(x)+" "+str(y)+" "+str(count))
    graph[x][y] = 0
    dfs(x-1,y,count+1)
    dfs(x,y-1,count+1)
    dfs(x+1,y,count+1)
    dfs(x,y+1,count+1)
dfs(0,0,1)
print(min(result))

