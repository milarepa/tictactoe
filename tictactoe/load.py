#!/usr/bin/python3
from nose.tools import *
import ttt as t


OPERATOR = t.GF()
AGENT = t.Ai('X')


def op_tests():
  OPERATOR.printBoard()
  
  OPERATOR.markBoard('X', 4)
  
  print OPERATOR.board
  
  OPERATOR.printBoard()
  
  b = OPERATOR.endGame(AGENT.marker)
  print str(b)
  
  
def main():
  op_tests()
  
if __name__ == '__main__':
  main()
    

