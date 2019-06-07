#Excerice 1-11

"""
#basic age and name program
name=input("Enter your name: ")
age=int(input("Enter your age: "))
number=int(input('How many times" '))
year=(100-age)+2017
statement=('Hi ' + str(name) + ' You will turn 100 in ' + str(year) + 'this \n')
print (statement * number)

#another simpler solution
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)

#odd or even program
user=int(input('enter a number: '))
if user%2==0:
    print ('even number')
elif user%2==1:
    print ('odd number')

check=int(input('ennter a number check: '))
user=int(input('user: '))
if check//user==0:
    print ('divides evenly')
elif user%4==0:
    print ('divides by four')
    


import sys
	
=
str = input("Please enter an integer: ")
num = int(float(str))  # force the input to an int

# Part the first
if num % 2 == 0:
    print ('Your number is even.')
else:
    print ('Your number is odd.')

if num % 4 == 0:
    print ('Your number is a multiple of 4.')


str1 = input("\nPlease enter an integer numerator: ")
str2 = input("Please enter an integer denominator: ")

numerator = int(float(str1))
denominator = int(float(str2))
if denominator == 0:
    print ('Cannot accept zero divisor. Exiting.')
    sys.exit()
else:
    if numerator % denominator == 0:
        print ("{} divides evenly into {}".format(denominator, numerator))
    else:
        print ("{} does not divide evenly into {}".format(denominator, numerator))
        
#list less than 10 list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for i in a:
	if i < 5:
		new_list.append(i)
print (new_list)

#divisors
newlist=[]
user=int(input())
for i in range(1, user+1):
    if user%i==0:
        newlist.append(i)
print (newlist)

#common values in two lists    
import random

list1 = random.sample(range(20), 13)
list2 = random.sample(range(20), 17)

newlist=[] #newlist
print ("Random List 1:", list1)
print ("Random List 2:" ,list2, "\n")

if len(list1)>len(list2):
    for i in list1:
        if i in list2:
            newlist.append(i)
elif len(list2)>len(list1):
    for i in list2:
        if i in list1:
            newlist.append(i)
print (newlist)

#palindrome is a string that reads the same forwards and backward
def palindrome(str):
    str=str.lower()
    if str[:]==str[::-1]:
        return 'is a palindrome'
    else:
        return 'not a palindrome'
   

print (palindrome('Dad'))
print (palindrome('wassup'))

#list comphrehension
def comphrenshion(list):
    b = [number for number in list if number % 2 == 0]
    return (b)
print (comphrenshion([1, 2, 4, 7, 9]))
#another solution
import random

numlist = []
list_length = random.randint(5,15) #returns a random integer

while len(numlist) < list_length:
    numlist.append(random.randint(1,75))

evenlist = [number for number in numlist if number % 2 == 0] 

print(numlist)
print(evenlist)"

#rock paper and sccisors
user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))
#import random module
import random
count=1
number=random.randint(1, 9)

while (count<=5):
    user=int(input())
    if user<number:
        print ('guess is too low')
        count=count+1
    elif user>number:
        print ('guess is too high')
        count=count+1
    elif user==number:
        count=count+1
        print ('You got it right in', count, 'guesses')
        break


#list overlap
import random
a = random.sample(range(1,50),10)
b = random.sample(range(1,50),10)

common = [i for i in a if i in b]

print(common)"""

#check primality

usernum = int(input("Please input a number: ")) #3
divisors = ([i for i in range(2,usernum) if(usernum%i == 0)]) #(2, 3) 
if(len(divisors)>0):
	print("Your number is not a prime.")
else:
	print("Your number is a prime.")