import game
import ai

class GStruct:
  'Wrap class for running other TTT game objects'


  def __init__(self):
    self.gameField = game.GF()
    self.human = ''
    self.winner = ''
    self.game_state = game.GStruct.gameState()
    self.message = 'default'
    self.turn_count = 8


  def play(self):

    f = True
    while f:

      h = raw_input("Are you X or O ?")

      if h == 'X':
        self.ai = ai.Ai('O')
        f = False
      elif h == 'O':
        self.ai = ai.Ai('X')
        f = false
      else:
        print "That is an invald answer. Try again - X or O"

  for i in len(self.turn_count):











def main():
    print "here comes the game!"



if __name__ == '__main__':
  main()






