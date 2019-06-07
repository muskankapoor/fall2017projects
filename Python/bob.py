def bob(str):
    if '!' in str:
            return 'Fine. Be that way!'
    elif '?' in str:
            return 'Sure.'
    elif "" in str:
            return 'Whoa, chill out!'
    else:
            return 'Whatever'
        
print (bob('you are cool you!'))
print (bob('Wassup?'))
print (bob(''))
print 