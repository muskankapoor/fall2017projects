def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
    return True
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
    return True

print (pos_neg(-4, 5, True))
