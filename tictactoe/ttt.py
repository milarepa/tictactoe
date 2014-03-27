"""
classification
"""
class GF:
  'Game field class'

  def __init__(self):

    self.prev_moves = []
    self.board = [ '-' for i in range(0,9) ]
    self.winner = None
    self.marker = ''
    self.opponentmark = ''

  def __str__(self):
    return 'Game Field Object'


  def humanMove(self):
    'manages human moves'

    flag = True
    while flag:

      choice = raw_input("please enter your postition choice : ")
      try:
        mvs = int(choice)
      except:
        mvs = -1

      if mvs not in self.gatherMoves():
        print "Move not available"
      else:
        break

    self.markBoard(self.marker, mvs)


  def printBoard(self):
    'printBoard() : prints the current board'

    for j in range(0,9,3):
      for i in range(3):
        if self.board[j+i] == '-':
          print "%d |" %(j+i),
        else:
          print "%s |" %self.board[j+i],
      print "\n",


  def gatherMoves(self):
    'gather the empty moves'
    moves = []

    for i,v in enumerate(self.board):
      if v == '-':
        moves.append(i)

    return moves


  def markBoard(self,marker,pos):
    '''Mark a position with marker X or O'''

    self.board[pos] = marker
    self.prev_moves.append(pos)


  def endGame(self):
    'For each turn we need to check if the game has win condiditons'

    win_conditions = [
      (0,1,2),
      (3,4,5),
      (6,7,8),
      (0,3,6),
      (1,4,7),
      (2,5,8),
      (0,4,8),
      (2,4,6),
      ]

    # unpack sets and compare sets with board to see if win cond has been met
    if ('x','X','X') in win_conditions and self.marker == 'X':
      self.winner = 'X'
      return True
        
    if('O','O','O') in win_conditions:
      self.winner = 'O'
      return True

    return False



class Ai:
  'AI takes on turns based on MiniMax choices'

  def __init__(self, marker):
    self.marker = marker

    if self.marker == 'X':
      self.opponentmark = 'O'
    elif self.marker == 'O':
      self.opponentmark = 'X'
    else:
      self.message = "init failed to set marks\n"

  def __str__(self):
    return self.marker


  def score(self,GFinstance):

    if GFinstance.endGame():
      if GFinstance.winner  == self.marker:
        return 10
      elif GFinstance.winner == self.opponentmark:
        return -10
      else:
        return 0

  def move(GFinstance):
    'minimax implementation'
    if GFinstance.endGame():
      return Ai.score(GFinstance)
      
    scores = []
    moves = []
    
    for move in GFinstance.gatherMoves():















