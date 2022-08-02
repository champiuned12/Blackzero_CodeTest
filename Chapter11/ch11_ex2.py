N = input()
flagZero = False
result = int(N[0])
if result == 0:
  flagZero = True
for i in N[1:] :
  if int(i) == 0 :
    flagZero = True
  elif int(i) == 1 :
    result += 1
    flagZero = False
  else :
    if flagZero :
      result += int(i)
      flagZero = False
    else :
      result = result*int(i)

print(result)
