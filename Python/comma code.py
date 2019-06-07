"""spam = ['apples', 'bananas', 'tofu', 'cats']

return 'apples, bananas, tofu, and cats'. 

def comman(list):"""
    
"""kist= ['apples', 'bananas', 'tofu', 'cats']
list[-1]='and '+ list[-1]
str=', '.join(list) 
print (str)"""

def comma(list):
    list[-1]='and ' + list[-1]
    str=' , '.join(list)
    return str

print (comma(['apples', 'bananas', 'tofu', 'cats']))

