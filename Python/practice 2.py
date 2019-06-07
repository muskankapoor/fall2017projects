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

def rle(s):
    encoded = [] #empty list
    while len(s)>1: #lenth of string is grater than 1
        runlen = 1 #instilzqtion
        runchar = s[0] #instialization
        while runlen < len(s) and s[runlen]==runchar: 
            runlen = runlen + 1 
        if runlen>1:
            encoded.append(runlen)
            encoded.append(runchar)
        s=s[runlen:]
    return encoded


s = "aabbcc"
print(s)
print(rle(s))
print(s)


#Calculate the moment when someone has lived for 10^9 seconds.

def gigasecond(int):
    hours=int/3600
    days=hours/24
    months=days/365
    return months

print (gigasecond(1000000000))


def rotation(c, r):
    l=''
    for letter in c:
        rotation=ord(letter)+r
        if (rotation > 122):
                rotation=rotation-26 #the full alphabet 
        char=chr(rotation)
        l=l+char
    return l
print (rotation('hello', 2))
print (rotation('zup', 3))
print (rotation('omg', 5))


"""Find the difference between the square of the
sum and the sum of the squares of the first N natural numbers."""

def function(n):
    result=0
    for i in n:
        s=i**2
        result=result+s
    return result

def function2(n):
    tally=0
    for i in n:
        tally=tally+i
    answer=tally**2
    return answer

def difference(n):
    return function2(n) - function(n)

print (difference([1, 2, 3]))


#def (anagram()):
   # for
word='anagram'

list=['naagmra', 'upsdie']
for i in list:
    if (''.join(sorted(i)))==(''.join(sorted(word))):
     print (i, 'is the anagram')


      
def allergy(score):
    result=0
    list=[]
    dict={'eggs': 1, 'peanuts': 2, 'shellfish': 4,
      'strawberries':8, 'tomatoes':16, 'chocolate': 32, 'pollen':64,
      'cats':128}
    for key in dict:
        if dict[key]==score:
            return key
        else:
            while result<=score:
                result=result+dict[key]
                if result==score:
                    list.append(key)
                return list
        
print (allergy(3))


def series 
