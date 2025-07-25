nums = [1,5,2,10]
diff = -1
for i in range(len(nums)): 
    for j in range(i+1, len(nums)): 
        if diff<nums[j]-nums[i]:
            diff = nums[j]-nums[i]
print(diff)

for i in range(len(nums)): 
    if i+1 < len(nums) and diff <nums[i+1]-nums[i]:
        diff = nums[i+1]-nums[i] 
print(diff)