
N,M = map(int,input().split())                 
arrayA = [[0]*M for _ in range(N)]
minArray = []
for i in range(N):
  arrayA[i] = list(map(int,input().split()))
  arrayA[i].sort()
  minArray.append(arrayA[i][0])
minArray.sort(reverse = True)
print(minArray[0])

"""
a = [1,4,3,2,5]
a.sort()
print(a)
"""
#print(arrayA)