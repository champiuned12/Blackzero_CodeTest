N = int(input())

count = [0]*(N+1)
count[1] = 1
count[2] = 3
for i in range(3,N+1):
  count[i] = (count[i-1]+2*count[i-2]) % 796796
print(count[N])