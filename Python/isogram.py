def isogram(x):
    for i in x:
        count=x.count(i)
        #count function 
        if count>1:
            return 'is not an isogram'
        else:
            return 'isogram'
    
print (isogram('isogram-ishp-'))
print (isogram('isogram'))