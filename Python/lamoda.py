languages = ["HTML", "JavaScript", "Python", "Ruby"]

print (filter(lambda x: x == "Python", languages))


cubes = [x ** 3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)


#itenerating over dicitonaries
#a codeacademy example
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print (movies.items())

#secret mesage program
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message= garbled[::-2]
print (message)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print message