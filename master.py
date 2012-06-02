#Okay
board=[['BR','BKn','BB','BQ','BK','BB','BKn','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WKn','WB','WQ','WK','WB','WKn','WR']]

record=['p1name','p2name']

def motion(board,move):
  x1,y1,x2,y2=move[1],move[2],move[3],move[4]
  color=move[0]
  #Pawn
  if board[x1][y1]='BP' and 
  

def checklegal(board,move):
  x1,y1,x2,y2=move[1],move[2],move[3],move[4]
  #Within range?
  if x1 not in range(7) or y1 not in range(7) or x2 not in range(7) or y2 not in range(7):
   return 0
  #Are you moving?
  elif x1==x2 and y1==y2:
    return 0
  #Are you selecting a piece?
  elif board[x1][y1]=='':
   return 0
  #Are you selecting your own piece?
  elif ( move[0]==1 and board[x1][y1][0]!='W' ) or ( move[0]==2 and board[x1][y1][0]!='B' ):
   return 0
  #Are you moving into your own piece?
  elif board[x2][y2]!='':
    if ( move[0]==1 and board[x2][y2]=='W' ) or ( move[0]==2 and board[x2][y2]=='B' ):
      return 0
  else:
    return 1

def updaterecord(move):
  global record
  record.append(move)
  return record

def updateboard(move):
  global board
  x1=move[1]
  y1=move[2]
  x2=move[3]
  y2=move[4]
  board[x2][y2]=board[x1][y1]
  board[x1][y1]=''
  return board

move=[1,6,0,4,0]
#first number identifies player number, e.g. 1 = white

print checklegal(board,move)

if checklegal(board,move)==1:
  updaterecord(move)
  updateboard(move)

print record
print board
