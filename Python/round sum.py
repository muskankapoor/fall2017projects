def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
    #ADD Sum
  
def round10(num):
  mod = num % 10
  num = num-mod
  if mod >= 5: num += 10
  return num