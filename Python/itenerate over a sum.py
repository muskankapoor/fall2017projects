#itenerate over a list

#Given an array of ints, return True if the array contains a 2 next to a 2somewhere.

def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

#LIsts2-sum67

def sum67(nums):
  count = 0
  blocked = False
  
  for n in nums:
    if n == 6:
      blocked = True
      continue #contines the loop 
    if n == 7 and blocked:
      blocked = False
      continue
    if not blocked:  
      count += n
  
  return count

#eturn the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  if len(nums) == 0:
    return 0
  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums): 
        nums[i+1] = 0
  return sum(nums)

