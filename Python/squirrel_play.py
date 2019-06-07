def squirrel_play(temp, is_summer):
  if is_summer:
    if temp==[40, 101]:
     return True
  elif temp==[60, 91]:
    return True
  else:
    return False

print (squirrel_play(95, False)) 
print (squirrel_play(95, True))