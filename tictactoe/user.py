"""
User class for tic-tac-toe game.
"""
class User:
  'this class runs the user aspect'
  
  def __init__(self, user_hash):
     
    if user_hash[0] == "Me":
      self.user = "O"
    else:
      self.user = "X"
    
  
