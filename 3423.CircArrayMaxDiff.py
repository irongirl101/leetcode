nums = [1,3,2]
greatest=0
for i in range (len(nums)):
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
print(greatest)
