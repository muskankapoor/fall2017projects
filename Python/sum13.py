def sum13(nums):
  if len(nums) == 0: #number and exception case
    return 0
 
  for i in range(0, len(nums)): #range of 0 to number 
    if nums[i] == 13: #if it is 13
      nums[i] = 0 #make it p 
      if i+1 < len(nums):  #check if it is on range
        nums[i+1] = 0 #iternate and make it all same
  return sum(nums) 


print (sum13([1, 2, 2, 1]))
print (sum13([13, 2, 2, 1]))