"""NUMBER_OF_ELEMENTS = 5 # For simplicity, use 5 instead of 100
numbers=[]# Create an empty list
sum = 0

for i in range(NUMBER_OF_ELEMENTS):
        value = eval(input("Enter a new number: "))
        numbers.append(value)
        sum += value

average = sum / NUMBER_OF_ELEMENTS

count = 0 # The number of elements above average
for i in range(NUMBER_OF_ELEMENTS):
        if numbers[i] > average:
             count += 1
print("Average is", average)
print("Number of elements above the average is", count)
list=[]
list.append(4)
list.extend([1, 43])
print (list)
list1 = [30, 1, 2, 1, 0]
a=[x for x in list1 if x > 1]
b=[x for x in range(0, 10, 2)]
c=[x for x in range(10, 0, -2)]
print (a, b, c)

def function(list):
   for i in range(99):
    if i not in list:
        return "not all the number"
    else:
        return "all the number"
    
print (function([11, 48, 51, 42, 8, 74, 1, 41, 36, 53, 52, 82, 16, 72, 19, 70, 44, 56, 29, 33]))

#list of certain rows and columns
def mat(value, row, column):
    matrix=[]
    for i in range(row):
        matrix.append(value)
    for y in range(column):
        matrix.append(value)
    return matrix
        
def accumulate(m):
    total = 0
    for row in m:
    total += sum(row)
18\
19 return total
20
21 def main():
22 m = getMatrix() # Get a list
23 print(m)
24
25 # Display sum of elements
26 print("\nSum of all elements is", accumulate(m)) 
def getMatrix():
    matrix = [] # Create an empty list
    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    for row in range(numberOfRows):
        matrix.append([]) # Add an empty new row
        for column in range(numberOfColumns):
            value = eval(input("Enter a value and press Enter: "))
            matrix[row].append(value)
    return matrix

def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)
    return total

def main():
    m = getMatrix() # Get a list
    print(m)

# Display sum of elements
    print("\nSum of all elements is", accumulate(m))
main() # Invoke main function"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for j in range(len(grid[0])):
    for i in range(0, len(grid)):
        print(grid[i][j], end='')
    print()