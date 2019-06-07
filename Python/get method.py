#check whether the key and value exists

picnicItems = {'apples': 5, 'cups': 2}
print ('I am bringing ' + str((picnicItems.get('cups', 0))) + ' cups.')

#set defualt mehtod
spam = {'name': 'Pooka', 'age': 5}
print (spam.setdefault('color', 'black'))
spam.setdefault('color', 'white')
print (spam)

#black is the default value

#counts the number of occurrences of each letter in a string.
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1 #count is the dictionary

print(count)