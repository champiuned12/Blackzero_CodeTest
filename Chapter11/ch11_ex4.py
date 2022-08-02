
from itertools import combinations
"""
for i in combinations([1,1,2,3], 3):
    print(i, end=" ")
"""
N = int(input())

M = list(map(int,input().split()))
M.sort()

result = []
count = 0
for j in range(1,len(M)+1):
  for i in combinations(M,j):
    for _ in range(len(i)):
      count += i[_]
    result.append(count)
    count = 0

final_list = list(set(result))
minimum = 1
while(True):
  if minimum not in final_list:
    break
  minimum += 1
print(minimum)

