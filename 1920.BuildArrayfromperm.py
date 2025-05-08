nums = [5,0,1,2,3,4]
ans = [0,0,0,0,0,0]
for i in range(len(nums)): 
    index = nums[i]
    pos = i
    print(index, pos)
    ans[pos]= nums[index]

print(ans)

