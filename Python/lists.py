answers=[['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
         ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
         ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
         ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
         ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
         ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
         ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
         ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
"""The program grades the test and displays the result. To do this,
the program compares each student’s answers with the key, counts
the number of correct answers, and displays it."""
for i in range(len(answers)): #row
    count=0
    for j in range(len(answers[i])): #column
        if answers[i][j]==keys[j]:
           count=count+1
    print (count)
# Grade all answers

