nums = [2,1,4]
flag = 0
if len(nums)>1:
    for i in range(len(nums)): 

        if i+1<len(nums): 
            
            if nums[i]%2==0 and nums[i+1]%2==0: 
                flag = 0 
                break
                
            elif nums[i]%2!=0 and nums[i+1]%2!=0: 
                flag = 0 
                break
                
            elif nums[i]%2 == 0 and nums[i+1]%2!=0: 
                flag = 1
                
            elif nums[i]%2!=0 and nums[i+1]%2==0: 
                flag = 1 


   
else:
    print("True")