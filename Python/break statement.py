while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':
      continue#(1)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)