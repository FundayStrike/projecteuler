from functools import reduce

with open('largesum.txt', 'r') as f: # largesum.txt contains the large numbers
    nums = f.read()
    nums = nums.split('\n')

nums = [int(num) for num in nums]

print(sum(nums))
