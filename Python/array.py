def array_front9(nums):
  newnums=nums[0:4]
  for num in newnums:
    if num==9:
      return True
  return False