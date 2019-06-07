#Legos
#p and q types she gives to friend
#r and s the ones she keeps
#r times s to find the no. of combinations

from collections import Counter
def solve(a, b, c, d, p, q):
    r, s = (Counter([a, b, c, d]) - Counter([p, q])).elements()
    return r * s

print (solve(20, 10, 40, 30, 10, 30))