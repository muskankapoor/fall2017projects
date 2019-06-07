"""Given a string, return a new string where the first
and last chars have been exchanged."""

def front_back(str):
  first_letter=str[0]
  last_letter=str[-1]
  str=last_letter+str[1:]+first_letter
  return str

print (front_back('candy'))
    