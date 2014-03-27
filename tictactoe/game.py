import tictactoe as t
import random as r
import ai

class GStruct:
  'Wrap class for running other game objects'


  def __init__(self):
    self.game = t.GF()
    self.human = 0
    self.comp = 0
    self.winner = self.game.winner
    self.game_state = self.game.endGame()
    self.message = 'default'
    self.turn_count = 0

  def __str__(self):
    return "Construct for a game collection"

  def play(self):

    f = True
    while f:

      h = raw_input("\nAre you X or O ?\n")

      if h == 'X':
        self.ai = t.Ai('O')
        self.game.marker = 'X'
        first = self.flipCoin()
        f = False
      elif h == 'O':
        self.ai = t.Ai('X')
        self.game.marker = 'O'
        first = self.flipCoin()
        f = False
      else:
        print "\nThat is an invald answer. Try again - X or O :  "

    if first == 'human':
      self.human = 2
      self.comp = 1
    else:
      self.human = 1
      self.comp = 2

    for i in range(9):



      self.game.printBoard()

      if i % 2 == 0:

        print "\nLooks like its my move, I choose : \n"
        self.ai.moveMe(self.game)
      else:
        print "\nLooks like its your move.\n"
        self.game.humanMove()

      if self.game.endGame() and self.game.winner != '-':
        print self.game.winner + " is the winner!!"
        break



  def flipCoin(self):
    'flip to see who goes first'

    n = r.randint(0,1)

    if str(self.ai) == 'O':
      f = {0: "comp", 1: "Human"}
    else:
      f = {0: "human",1: "comp"}

    return f[n]


def main():
  'Running the program - main()'
  s = GStruct()
  s.play()



if __name__ == '__main__':
  main()






