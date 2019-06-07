"""students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
            ['Akriti', 41], [
    'Harsh', 39]]

1. create a nested list 
2. then loop throught to see the second lowest score 
3. lowest to highest
#hackerrank problem url : https://www.hackerrank.com/challenges/nested-list
#nested lists"""

def nested(N):
 # getting test case input
    name_list = []
    mark_list = []

    for i in range(N):
        name_list.append(input()) # getting student name
        mark_list.append(input()) # getting student's mark

    min_mark = sorted(mark_list)[1:2] # getting second lowest mark
    outer_list = []

    for name in range(len(name_list)):
        inner_list = []
        inner_list.append(name_list[name])
        inner_list.append(mark_list[name])
        outer_list.append(inner_list)

    lowest_number_name_list = []
    for i in range(len(outer_list)):
        if mark_list[i] == min_mark[0]:
        #print(name_list[i])
            lowest_number_name_list.append(name_list[i])

    sorted_list = sorted(lowest_number_name_list, key=str.lower)
    for i in range(len(sorted_list)):
        print(sorted_list[i])

#print(sortedt_list)
print (nested(3))
