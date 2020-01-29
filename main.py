from random import randint 

height = 10
width = 10
 
playerx = 1
playery = 8
monsterx = 1
monstery = 1

maze = [ [' ' for i in range (height) ] for j in range (width)   ]



for j in range (width):
  maze[0][j] = "x"
  maze[9][j] = "x"
for i in range (height):
  maze[i][0] = "x"
  maze[i][9] = "x"
#individual
maze[2][5] = "x"
maze[2][6] = "x"
maze[2][7] = "x"
maze[2][8] = "x"
maze[3][5] = "x"
maze[4][5] = "x"
maze[4][6] = "x"
maze[6][5] = "x"
maze[6][4] = "x"
maze[6][3] = "x"
maze[6][2] = "x"
maze[6][1] = "x"
maze[1][3] = "x"
maze[2][3] = "x"
maze[3][3] = "x"
maze[7][8] = "x"
maze[7][7] = "x"
maze[1][8] = "o"
maze[playery][playerx] = "p"
maze[monstery][monsterx] = "m"
  
def printMaze():
  global maze
  
  #prints maze
  for i in range (height):
    s = ''
    for j in range (width):
      s+= maze [i][j]
    print (s)

def playermove():
  global playerx, playery
  maze[playery][playerx] = " "
  choice = input("enter your direction(wasd)")
  if "a" == choice and maze[playery][playerx-1] != "x": 
    playerx = playerx-1
  elif "d" == choice and maze[playery][playerx+1] != "x":
    playerx = playerx+1
  elif "w" == choice and maze[playery-1][playerx] != "x":
    playery = playery-1
  elif "s" == choice and maze[playery+1][playerx] != "x":
    playery = playery+1
  
  if playerx == 8 and playery == 1: 
    print("Congratulations!!!!!")
    return False
  maze[playery][playerx] = "p"
  return True

def monstermove():
  global monsterx, monstery
  maze[monstery][monsterx] = " "
  posMoves = []
  if maze[monstery][monsterx-1] != "x":
    posMoves.append({'x':monsterx-1, 'y':monstery})
  if maze[monstery][monsterx+1] != "x":
    posMoves.append({'x':monsterx+1, 'y':monstery})
  if maze[monstery-1][monsterx] != "x":
    posMoves.append({'x':monsterx, 'y':monstery-1})
  if maze[monstery+1][monsterx] != "x":
    posMoves.append({'x':monsterx, 'y':monstery+1})
  
  r = randint(0, len(posMoves)-1)
  #print(r, posMoves)
  monsterx = posMoves[r]['x']
  monstery = posMoves[r]['y']

  
  
  
  '''
  r = randint(0,3)
  if 0 == r and maze[monstery][monsterx-1] != "x":
    monsterx = monsterx-1
  elif 1 == r and maze[monstery][monsterx+1] != "x":
    monsterx = monsterx+1
  elif 2 == r and maze[monstery-1][monsterx] != "x":
    monstery = monstery-1
  elif 3 == r and maze[monstery+1][monsterx] != "x":
    monstery = monstery+1
  '''
  maze[monstery][monsterx] = "m"
    

play = True

while play: 
  printMaze()
  play = playermove()
  monstermove()
  
  
  
  
  