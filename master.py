#Create board, an array of arrays
board=[['BR','BKn','BB','BQ','BK','BB','BKn','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WKn','WB','WQ','WK','WB','WKn','WR']]

record=['p1name','p2name']
#The record is a history of an individual game. The first two rows should contain the 
  #names of the players, to be created when we have a 'tournament' program.
  #The following elements in the record array will be the moves, which is an array itself.

#Motion checks if the proposed move fits the way a piece is meant to move. It is incomplete
"""
def motion(board,move):
  x1,y1,x2,y2=move[1],move[2],move[3],move[4]
  color=move[0]
  #Pawn
  if board[x1][y1]='BP' and 
"""

def checklegal(board,move):
  #move[0], the first element of the 'move' array, is 1 for player 1 (white), 2 for player 2
    #The next elements: (x1,y1) is the position of the piece, (x2,y2) is where you want to move it.
    #The player would pass a move to master in the form (1,2,3,4,5) for player 1 to move the piece at
    #(2,3) to position (4,5)
  x1,y1,x2,y2=move[1],move[2],move[3],move[4]
  #Is the move on the board at all?
  if x1 not in range(7) or y1 not in range(7) or x2 not in range(7) or y2 not in range(7):
   return 0
  #Is the move actually moving?
  elif x1==x2 and y1==y2:
    return 0
  #Is a piece selected?
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
    #I am returning 1 for 'legal', but at this point we are missing whether it is a proper motion
      #(the 'motion' function) and if it places the person in check (a 'check' function)
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

#Sample move. This would be passed to master from the players
move=[1,6,0,4,0]
#first number identifies player number, e.g. 1 = white

print checklegal(board,move)

if checklegal(board,move)==1:
  updaterecord(move)
  updateboard(move)

print record
print board
