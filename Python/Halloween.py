#hacerank Halloween Sale problem
#game 1=p dollars
#games afterwards will be sold at d dollars the subsequent
#goes on till it reaches less than or equal to m dollars 
#afterwards every game will cost m dollars
#p, d, m, s

def games(p, d, m, s): #10, 2, 3, 35 ouptut: 10,8,6,4,2, 2 6 games
    list=[]
    list.append(p)
    while (p>m): #20>6 10>3
        p=(p-d) 
        list.append(p) #20-3 8, 6, 4, 2  
        if (p<=m):
            list.append(m)
    if sum(list)>s:
         return (len(list)-1)
    elif sum(list)<s:
        return (len(list))
print (games(20, 3, 6, 80)) #6
print (games(20, 3, 6, 85)) #7
print (games(10, 2, 3, 35))
        