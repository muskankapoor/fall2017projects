"""#Excerise 12
def listends(list):
    newlist=[]
    newlist.append(list[0])
    newlist.append(list[-1])
    return (list[0], list[-1])

print (listends([4, 5, 6]))

#Excerise 13
def gen_fib(count): #4 expected answer is [1, 1, 2, 3]
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2: 
        fib = [1,1]
    elif count > 2: 
        fib = [1,1]
        while i < (count - 1): #1<3 2<3
            fib.append(fib[i] + fib[i-1]) #fib=1+0 [1, 3 
            i += 1

    return fib

print (gen_fib(5))

#Excerise 14
def duplicates(list):
    newlist=[]
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist
print (duplicates([1, 1, 2, 3, 4, 4]))

#this one uses sets
def duplicate(setting):
    return list(set(setting))#set removes duplicated elements

print (duplicate([1, 2, 1, 3]))

#list overlap
def common(a,b):

    c=[x for x in b if x in a]
    return set(c)

                
print (common([1, 1, 2, 3, 4, 5], [2, 3, 5, 1]))

#Excercise 15
def reverse(str):
    str=str.split(" ")
    for words in str:
        str1=str[::-1]
    return ' '.join(str1)
print (reverse('My name is Muskan'))

#Excersie 16-password generator
import random
generator=[]
upperalpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W','X', 'Y', 'Z']
loweralpha=['a', 'b', 'c', 'd', 'e', 'f', 'h', 'j', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['#', '!', '@', '$', '^']
a=random.choice(upperalpha)
generator.append(a)
b=random.choice(loweralpha)
generator.append(b)
c=random.choice(numbers)
generator.append(c)
d=random.choice(symbols)
generator.append(d)
generator="".join(generator)
print (generator)

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen))
print (p)

#Excericise 20
def function(list, number):
        if number in list:
            return True
        else:
            return False
print (function([1, 2, 3, 4], 5))

#Excercise 17, Decode a Web Page
import requests
#requests does HTTP for humans
from bs4 import BeautifulSoup
#import beautiful soup-interprets the requests 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
#above two lines how ot use the requests 
#then get request 
soup = BeautifulSoup(r.text)
#returns all the html in r text 
#the following recrodes it
#the following is a class in beautifulsoup
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: #heading use to link one page to another
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())

"""
        
#Excercise 24: tIC TAC TAC
"""def board_draw(height, width): #(3, 3)
    for x in range(height): #for x in range(3)
        print(" --- " * width) 
        print("|   |" * width)
    print(" --- " * width)


print (board_draw(3, 3))"""

def tic_tac(list):
    if [1, 1, 1] in list:
        return 'Player 1 won'
    elif [2, 2, 2] in list:
        return 'Player 2 won'
    elif 

    
print (tic_tac([[2, 1, 2],
                [1, 1, 0],
                [2, 1, 1]]))
    
