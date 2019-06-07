#Test 1 Problem 1
"""def divide(A, B, U):
    unit=B/A
    cake=unit*U
    return cake

print (divide(5, 10, 2))"""

#test 1 problem 2
#"bbaaa"
"""def encode(s): #aabbcc returns a list of the letter and number of time it repeats
    list=[]
    for i in s:
         if i not in list:
            list.append(i)
            count=s.count(i)
            list.append(count)
        
    return list
         
       

print (encode("bbbaa"))
print (encode("aabcccdeeeeaaa"))"""


#Test 1 Problem 3
"""def score(w):
    value = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1,
              "N": 1, "R": 1, "S": 1, "T": 1, "C": 3, "B": 3,  "D": 2, "G": 2, 
             "F": 4,  "H": 4, "K": 5, "J": 8, "M": 3, 
              "Q": 10, "P": 3,  
            "W": 4, "W": 4, "Y": 4, 
         "X": 8, "Z": 10}
    start=0
    w=w.upper()
    for i in w:
        count=value[i]
        start=count+start
    return start
print (score("Hello"))"""
#test 2 problem 2
def overlap(t1,t2): #overlap between two ranges
    (x,y) = t1
    (a,b) = t2
    # return not (b < x or a > y)
    if  b < x or a > y:
        return False
    else:
        return True

def merge(t1, t2):
    list=[]
    (x,y) = t1
    (a,b) = t2 
    if overlap(t1, t2)==True:
      if t1[0]<t2[0]:
          list.append(t1[0])
      else:
          list.append(t2[0])
      if t1[-1]>t2[-1]:
          list.append(t1[-1])
      else:
          list.append(t2[-1])
    return list

def build_rangelist(length=10):
  l=[]
  lowval = 5
  for i in range(length):
    r = [lowval, lowval+random.randrange(1,20)]
    l.append(r)
    lowval = r[1] + random.randrange(1,20)
  return l
  
rangelist = build_rangelist()


def add_range(rangelist,newrange):