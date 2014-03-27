# This is a Zero Sum game - two experts will always tie...
import ai

def print_promt():
  print "Here is the playing field, starting at the left top as 1 and so on"
  print_field([2,3,4,5,6,7,8,9,10])
  users = build_users()
  

def print_field(field):

  # create the playing field
  # key of this presentation is
  # i * 3 * j I would love to explore
  # i * x * j where x is larger !!
  print "Current PLaying Field. \n"

  for i in range(3):
    print " ",
    for j in range(3):
      if field[i*3+j] == 1:
        print 'X',
      elif field[i*3+j] == 0:
        print 'O',
      elif field[i*3+j] != -1:
        print field[i*3+j]-1,
      else:
        print ' ',

      if j != 2:
        print " | ",
    print

    if i != 2:
      print "----------------"
    else:
      print


def build_users():

  flag = False

  while not flag:
    try:
      user_xo = raw_input("Are You X or O ?\n")
      print "User choice : " + user_xo + "\n"

      if user_xo == "X":
        users_hash = {0: "human", 1: "machine"}
        current_user = users_hash[0]
        flag = True
      elif user_xo == "O":
        users_hash = {0: "human", 1: "machine"}
        current_user = users_hash[1]
        flag = True
      else:
        print "I am sorry, that is not a choice. Try again...\n"
        print_promt()
    except Exception as e:
      print "I am sorry, that is not a choice (e). Try again...\n"
      print_promt()
    
    return user_hash
      
      
def take_turn(user):
  sqr = raw_input("Where would you like to place your tile ?\n")
  field = [2,3,4,5,6,7,8,9,10]
  if sqr in field:
    return print_field([2,3,4,5,6,7,8,9,10])



