"""
classification
"""
class GF:
  'Game field class'

  def __init__(self):

    self.board = [ '-' for i in range(0,9) ]
    self.winner = None
    self.marker = ''
    self.opponentmark = ''
    self.marked_spaces = {}
    self.win_conditions = [
      (0,1,2),
      (3,4,5),
      (6,7,8),
      (0,3,6),
      (1,4,7),
      (2,5,8),
      (0,4,8),
      (2,4,6),
      ]

  def __str__(self):
    return 'Game Field Object'


  def humanMove(self):
    'manages human moves'

    flag = True
    
    while flag:

      choice = raw_input("please enter your postition choice : ")

      mvs = int(choice)
      
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
    self.marked_spaces[marker] = pos
    return self.gameState()
    


  def endGame(self, marker):
    'For each turn we need to check if the game has win condiditons'
    
    if marker == "X" or marker == "O":
      if (("X",) * 3) in self.win_conditions:
        self.winner = "X"
        return True
      elif (("O",) * 3) in self.win_conditions:
        self.winner = "O"
        return True
      elif len(self.gatherMoves()) == 0:
        self.winner = "Draw"
        return True
      else:
        return False

  
  def gameState(self):
    return self.board


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


  def score(self, GFinstance):

    if GFinstance.endGame(self.marker):
      return 10
    elif GFinstance.endGame(self.opponentmark):
      return -10
    else:
      return 0



  def move(self, GFinstance):
    'minimax implementation'
    
    if GFinstance.endGame(self.marker):
      return score()
      
    for move in GFinstance.gatherMoves():
      
