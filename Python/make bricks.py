def make_bricks(small, big, goal):
    #failed possiblities
    if goal>(big*5+small):
        return False
    #small bricks
    elif goal%5>small:
        return False
    else:
      return True

  
