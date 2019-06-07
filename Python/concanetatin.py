def non_start(a, b):
  sum=a+b
  sum1=sum[1:]
  return sum1

print (non_start('Hello', 'There'))
print (non_start('java', 'code'))


#alternative
def non_start(a, b):
    return a[1:] + b[1:]