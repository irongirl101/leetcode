# BS moment 
nums = [3,2,2,3] 
val = 3

i = 0
while i<len(nums):
    if nums[i] == val: 
        del nums[i]
    i+=1
print(nums)