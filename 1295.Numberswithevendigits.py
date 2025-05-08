nums = [555,901,1000,1771,2,61]
count = 0
for i in range(len(nums)): 
    num = nums[i] 
    c = 1
    while num//10>0: 
        
        c+=1
        num = num//10
    if c%2==0: 
        count+=1
print(count)   

