import random

def build_rangelist(length=10):
  l=[]
  lowval = 5
  
  for i in range(length):
    r = [lowval, lowval+random.randrange(1,20)]
    l.append(r)
    lowval = r[1] + random.randrange(1,20)
  return l
  
rangelist = build_rangelist()

def add_range(rangelist, newrange):
    newlist=rangelist+newrange
    newlist.sort()
    return newlist

print (add_range(rangelist, [4, 5]))

def overlap(t1, t2):
    for i in t2:
        if i in t1:
            return True
        else:
            return False
        
def merge(t1, t2): 
   for i in t2:
        if i in t1:
            t3=t1 + t2
            t3=t3.sort()
            return t3
    

        
print (overlap([1,5],[2, 4]))
print (merge([1,5],[2, 4]))
