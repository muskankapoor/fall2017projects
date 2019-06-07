def close_far(a, b, c):
    if abs(b-a) <= 1: #<=1
        close = b  #close=2
    elif abs(c-a) <= 1: 
        close = c #close=3
    else:
        return False
    if (close == b) and (abs(c-a) >= 2) and (abs(c-b)>=2):
        return True
    elif (close == c) and (abs(b-a) >= 2) and (abs(b-c)>=2):
        return True
    else:
        return False
    
    
print (close_far(1, 2, 3)) 
print (close_far(4, 1, 3))