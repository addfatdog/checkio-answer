from fractions import gcd as getgcd

def greatest_common_divisor(*nums):
  length = len(nums)
  gcd = 1
  gcd = getgcd(nums[0], nums[1])
  data = list(nums)
  for i in data[2:]:
    gcd = getgcd(i, gcd)
  return gcd

