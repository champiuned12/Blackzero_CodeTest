N,M = map(int,input().split())
x,y,direction = map(int,input().split())
miniMaps = [[0]*M for _ in range(N)]
for i in range(N):
  miniMaps[i] = list(map(int,input().split()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn_left():
  global direction
  direction = direction -1
  if direction == -1:
    direction = 3

movedareas = 1
rotate_counter = 0
while(True):
  turn_left()
  if miniMaps[x+dx[direction]][y+dy[direction]] == 0:
    miniMaps[x][y] = 2
    x, y = x+dx[direction],y+dy[direction]
    movedareas = movedareas + 1
    rotate_counter = 0
  elif miniMaps[x+dx[direction]][y+dy[direction]] > 0 and rotate_counter < 4:
    rotate_counter = rotate_counter+1
  elif rotate_counter == 4:
    if miniMaps[x-dx[direction]][y-dy[direction]] == 2:
      x, y = x-dx[direction], y-dy[direction]
      rotate_counter = 0
    else :
      break

print(movedareas)
"""
movedareas = 0
def move(x_pos,y_pos,direction,rotate_counter):
  global movedareas
  rotate_counter = rotate_counter+1
  if direction == 0:
    direction = direction + 3
    if miniMaps[x_pos-1][y_pos] == 0 :
      miniMaps[x_pos][y_pos] = 2
      movedareas = movedareas+1
      move(x_pos-1,y_pos,direction,rotate_counter)
    elif miniMaps[x_pos-1][y_pos] > 0 and rotate_counter < 4:
      move(x_pos,y_pos,direction,rotate_counter)
    else :
      if miniMaps[x_pos][y_pos-1] == 2:
        move(x_pos,y_pos-1,0,0)
      else :
        return movedareas
  elif direction == 1:
    direction = direction - 1
    if miniMaps[x_pos][y_pos+1] == 0:
      miniMaps[x_pos][y_pos] = 2
      movedareas = movedareas+1
      move(x_pos,y_pos+1,direction,rotate_counter)
    elif miniMaps[x_pos][y_pos+1] > 0 and rotate_counter < 4:
      move(x_pos,y_pos,direction,rotate_counter)
    else :
      if miniMaps[x_pos-1][y_pos] == 2:
        move(x_pos-1,y_pos,1,0)
      else :
        return movedareas
  elif direction == 2:
    direction = direction - 1
    if miniMaps[x_pos+1][y_pos] == 0:
      miniMaps[x_pos][y_pos] = 2
      movedareas = movedareas+1
      move(x_pos+1,y_pos,direction,rotate_counter)
    elif miniMaps[x_pos+1][y_pos] > 0 and rotate_counter < 4:
      move(x_pos,y_pos,direction,rotate_counter)
    else :
      if miniMaps[x_pos][y_pos+1] == 2:
        move(x_pos,y_pos,2,0)
      else :
        return movedareas
  elif direction == 3:
    direction = direction - 1
    if miniMaps[x_pos][y_pos-1] == 0:
      miniMaps[x_pos][y_pos] = 2
      movedareas = movedareas+1
      move(x_pos,y_pos-1,direction,rotate_counter)
    elif miniMaps[x_pos][y_pos-1] > 0 and rotate_counter < 4:
      move(x_pos,y_pos,direction,rotate_counter)
    else :
      if miniMaps[x_pos+1][y_pos] == 2:
        move(x_pos,y_pos,3,0)
      else :
        return movedareas
        
move(coordinates[0],coordinates[1],coordinates[2],0)
print(movedareas)
"""