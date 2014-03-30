import ttt as t
import random as r

class GStruct:
  'Wrap class for running other game objects'


  def __init__(self):
    self.game = t.GF()
    self.human = 0
    self.comp = 0
    self.winner = ''
    self.message = 'default'
    self.current_user = ''


  def __str__(self):
    return "Construct for a game collection"


  def play(self):
    'play loop'
    
    f = True
    
    while f:

      h = raw_input("\nAre you X or O ?\n")

      if h == 'X':
        self.ai = t.Ai('O')
        self.ai.opponentmark = 'X'
        self.game.marker = 'X'
        self.game.opponentmark = 'O'
        first = self.flipCoin()
        f = False
      elif h == 'O':
        self.ai = t.Ai('X')
        self.ai.opponentmark = 'O'
        self.game.opponentmark = 'X'
        self.game.marker = 'O'
        first = self.flipCoin()
        f = False
      else:
        print "\nThat is an invald answer. Try again - X or O :  "

    if first == 0:
      self.human = 2
      self.comp = 1
    else:
      self.human = 1
      self.comp = 2

    for i in range(9):

      self.game.printBoard()

      if i % 2 == 0:
        self.current_user = 2
        print "\nLooks like its my move, I choose : \n"
        self.ai.move(self.game)
      else:
        self.current_user = 1
        print "\nLooks like its your move.\n"
        self.game.humanMove()

      if self.game.endGame() and self.game.winner != '-':
        print self.game.winner + " is the winner!!"
        break



  def flipCoin(self):
    'flip to see who goes first'
    return r.randint(0,1)

    


def main():
  'Running the program - main()'
  s = GStruct()
  s.play()



if __name__ == '__main__':
  main()






