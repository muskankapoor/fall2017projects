def without_end(str):
  return str[1:-1]

print (without_end('sup'))

"""if you want to remove the central character:

midlen = len(oldstr)/2
newstr = oldstr[:midlen] + oldstr[midlen+1:]"""