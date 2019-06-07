def collatz(number):
    if number % 2 == 0:
        print (number//2)
        return (number // 2)
       
    else:
        print (3 * number +1)
        return (3 * number + 1)
        
x=int(input())
try:
    while x != 1:
        x = collatz(x)
        print (x)
except ValueError:
        print ('Input must be an integer')