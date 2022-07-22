cordinates = input()
x_cordinate_dict = {}
x_cordinate_dict['a'] = 0
x_cordinate_dict['b'] = 1
x_cordinate_dict['c'] = 2
x_cordinate_dict['d'] = 3
x_cordinate_dict['e'] = 4
x_cordinate_dict['f'] = 5
x_cordinate_dict['g'] = 6
x_cordinate_dict['h'] = 7

calculatedCordinate = (x_cordinate_dict[cordinates[0]],int(cordinates[1])-1)
possibleSpots = 0
x,y = 0,0

x = calculatedCordinate[0]-2
y = calculatedCordinate[1]+1

def available(x,y):
  if x >= 0 and x <= 7:
    if y >= 0 and y <= 7:
      return True
  else :
      return False

if available(x,y) :
  possibleSpots = possibleSpots + 1

x = calculatedCordinate[0]-2
y = calculatedCordinate[1]-1

if available(x,y) :
  possibleSpots = possibleSpots + 1

x = calculatedCordinate[0]+2
y = calculatedCordinate[1]+1

if available(x,y) :
  possibleSpots = possibleSpots + 1
x = calculatedCordinate[0]+2
y = calculatedCordinate[1]-1

if available(x,y) :
  possibleSpots = possibleSpots + 1
x = calculatedCordinate[0]+1
y = calculatedCordinate[1]-2

if available(x,y) :
  possibleSpots = possibleSpots + 1
  
x = calculatedCordinate[0]+1
y = calculatedCordinate[1]+2

if available(x,y) :
  possibleSpots = possibleSpots + 1

x = calculatedCordinate[0]-1
y = calculatedCordinate[1]-2

if available(x,y) :
  possibleSpots = possibleSpots + 1

x = calculatedCordinate[0]-1
y = calculatedCordinate[1]+2

if available(x,y) :
  possibleSpots = possibleSpots + 1




print(possibleSpots)