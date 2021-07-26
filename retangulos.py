import sys

def look_max_XY(rectangles):
  mX = -1
  mY = -1
  for rectangle in rectangles:
    mX = max(mX, rectangle[2])
    mY = max(mY, rectangle[3])
  return [mX, mY]

def init_board(coords):
  board = []
  mX = coords[0]
  mY = coords[1]
  for y in range(mY+1):
    board.append("c" * (mX+1))
  return board

def fill_rectangle(rectangle, board):
  fstX = rectangle[0]
  fstY = rectangle[1]
  sndX = rectangle[2]
  sndY = rectangle[3]
  for y in range(fstY, sndY+1):
    board[y] = board[y][:fstX] + "#"*(sndX-fstX+1) + board[y][sndX+1:]

def update_board(board, result):
  for rectangle in result:
    fill_rectangle(rectangle, board)

def print_board(board):
  for x in board:
    print(x)

result = []
for rectangle in sys.stdin:
  rectangle = [int(s) for s in rectangle.split()]
  result.append(rectangle)

if len(result) > 0:
  coords = look_max_XY(result)
  board = init_board(coords)
  print_board(board)