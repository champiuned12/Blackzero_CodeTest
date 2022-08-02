N = input()

coordinate = [0]

for i in range(1,len(N)):
  if N[i-1] != N[i] :
    coordinate.append(i)

print(len(coordinate)//2)