#list comphrehension syntax
#1.
new_list = [x *2 for x in range(1, 6)]
print (new_list)


#2.
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# => [6]
print (doubles_by_3)

#3.
even_squares = [x**2 for x in range(1, 11) if x%2==0]
print (even_squares)

#4.
cubes_by_four=[x**3 for x in range(1, 10) if (x**3)%4==0]
print (cubes_by_four)

#5.
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (l[2:9:2]) #start, end, and stride, negative stride reverse the list
