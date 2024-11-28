'''
original solution
nums = [0,0,1,1,1,2,2,3,3,4]
expectednums=[]

for i in nums:
    if i not in expectednums:
        expectednums.append(i)
print(expectednums,len(expectednums))'''

#using in place algorithms 

nums=[0,0,1,1,1,2,2,3,3,4]

for i in range(len(nums)):
    if i+1<len(nums):
        if nums[i]==nums[i+1]:
            nums.pop(i)
        elif nums[i]==nums[i-1]:
            nums.pop(i)
print(nums,len(nums))

    

