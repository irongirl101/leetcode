nums = [-5,-10,-5]
greatest=0
for i in range (len(nums)):
    if nums[i]>0:
        pos=nums[i]
    else: 
        pos = -1 * nums[i]  
    #print(pos)
    for j in range(len(nums)-1,i,-1):
        #print(nums[j])
        #diff = nums[j]
        if j!=i:
            if nums[j] >0 : 
                diff = nums[j]
            else: 
                diff = -1*nums[i]
            #print(diff)
            print(pos,diff,diff-pos)
            """if pos >= diff and pos-diff>greatest:
                greatest = pos-diff
            elif pos<diff and diff-pos>greatest:
                greatest=diff-pos"""
print(greatest)
