def centered_average(nums):
  nums=sorted(nums)
  del nums[0]
  del nums[-1]
  count=0
  for num in nums:
    count=count+num
  answer=count/len(nums)
  return answer


print (centered_average([1, 2, 3, 4, 100]))
print (centered_average([1, 1, 5, 5, 10, 8, 7]))



