def near_hundred(n):
  if n in range(90, 111):
    return True
  elif n in range (190, 211):
    return True
  else:
    return False
    
print (near_hundred(112))