def function(N):
    for i in range(1, N+1):
        print (i)
        
print (function(7))

def list(list):
    list.insert(0, 5)
    return list
    list.remove(5)
    list.append(5)
    list.sort()
    return list
    list.pop(5)
    list[::-1]
    return list

print (list([12]))


arr = []
s = [int(x) for x in input().split()]
for i in range(1,len(s)):
    s[i] = int(s[i])
if s[0] == "append":
    arr.append(s[1])
elif s[0] == "extend":    
    arr.extend(s[1:])
elif s[0] == "insert":
    arr.insert(s[1],s[2])
elif s[0] == "remove":
    arr.remove(s[1])
elif s[0] == "pop":
    arr.pop()
elif s[0] == "index":
    print (arr.index(s[1]))
elif s[0] == "count":
    print (arr.count(s[1]))
elif s[0] == "sort":
    arr.sort()
elif s[0] == "reverse":
    arr.reverse()
elif s[0] == "print":
    print (arr)