#given array is sorted ascending 

#code under -> runtime complexity of o(n), will not be accepted 
nums = [5,7,7,8,8,10]
target = 6
ans = []
for i in range(len(nums)): 
    if nums[i] == target: 
        ans.append(i)

if ans == []: 
    ans = [-1,1]
    print(ans)
else:
    print([ans[0],ans[-1]])

#runtime complexity o(log(n))




