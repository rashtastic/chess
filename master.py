#Create board, an array of arrays
board=[['BR','BKn','BB','BQ','BK','BB','BKn','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WKn','WB','WQ','WK','WB','WKn','WR']]

record=['p1name','p2name']
#The record is a history of an individual game. The first two rows should contain the 
  #names of the players, to be created when we have a 'tournament' program.
  #The following elements in the record array will be the moves, which is an array itself.

def updaterecord(move):
  global record
  record.append(move)
  return record

def updateboard(move):
  global board
  [p,x1,y1,x2,y2]=move;
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
