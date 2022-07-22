N, M = map(int,input().split())

trial = 0
while(True):
  if N == 1:
    break
  elif N % M == 0:
    N = N/M
    trial = trial+1
  else :
    N = N-1
    trial = trial+1

print(trial)