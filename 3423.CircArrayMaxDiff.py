nums = [-5,-10,-5]
greatest=0
'''for i in range (len(nums)):
    pos = nums[i] 
    #print(pos)
    for j in range(len(nums)-1,i,-1):
        #print(nums[j])
        #diff = nums[j]
        if j!=i:
            diff = nums[j]
            if pos >= diff and pos-diff>greatest:
                greatest = pos-diff
            elif pos<diff and diff-pos>greatest:
                greatest=diff-pos
print(greatest)'''

for i in range(len(nums)): 
    j = i+1
    if j == len(nums): 
        j = 0
        if nums[j]>=nums[i] and greatest<nums[j]-nums[i]: 
            greatest = nums[j]-nums[i]
        elif nums[i]>nums[j] and greatest<nums[i]-nums[j]: 
            greatest = nums[i]-nums[j]
    elif j<len(nums): 
        if nums[j]>=nums[i] and greatest<nums[j]-nums[i]: 
            greatest = nums[j]-nums[i]
        elif nums[i]>nums[j] and greatest<nums[i]-nums[j]: 
            greatest= nums[i]-nums[j]

    """if i+1==len(nums): 
        if nums[0]>=nums[i] and nums[0]-nums[i]>greatest: 
            greatest = nums[0]-nums[i]
        elif nums[0]<nums[i] and nums[i]-nums[0]>greatest: 
            greatest = nums[i]-nums[0]
    elif i+1<len(nums): 
        
        if nums[i]>=nums[i+1] and nums[i]-nums[i+1]>greatest: 
            greatest = nums[i]-nums[i+1]
        elif nums[i]<nums[i+1] and nums[i+1]-nums[1]>greatest: 
            greatest = nums[i+1]-nums[i]"""
        
print(greatest)
