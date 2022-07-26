N = int(input())
result = []
for _ in range(N):
  result.append(int(input()))

result.sort(reverse = True)
print(" ".join([str(_) for _ in result]))