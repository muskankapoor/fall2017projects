def make_chocolate(small, big, goal):
  maxBig = goal / 5 #big=5 small=1 example: 4, 1, 9  
   #1.8
  if big >= maxBig: #9>=1.8
    if small >= (goal - maxBig * 5): 1>=(9-1.8*5) 1>=0
      return goal - maxBig * 5 #0
  if big < maxBig:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1