"""
board = [ '-' for i in range(0,9) ]

print "\nCurrent board:"

for j in range(0,9,3):
  for i in range(3):
    if board[j+i] == '-':
      print "%d |" %(j+i),
    else:
      print "%s |" %board[j+i],
  print "\n",
"""

def loopy():
  'returns a list of somethings'
  x = [2 % i for i in range(1,9)]
  return x
  
  
for m in loopy():
  print m,
    

