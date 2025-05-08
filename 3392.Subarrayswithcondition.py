nums = [1,1,1]
arr = [0,0,0]
c = 0 
for i in range(len(nums)): 
    arr[0]=nums[i]
    for j in range(i+1,len(nums)): 
        arr[1]=nums[j]
        for k in range(j+1,len(nums)): arr[2]=nums[k] 
        if (arr[0]+arr[2])==(arr[1]/2): 
             c+=1 
print(c/2 )           
