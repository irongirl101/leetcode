nums =[1,2,3,4]
k = 1
flag = False 
c = 0 

for i in range(len(nums)):
    for j in range(len(nums)): 
        if i!=j and nums[i] == nums[j]: 
            num = i*j 
            flag = True
            if num%k == 0: 
                c+=1

if not flag: 
    print(0)
elif c == 0: 
    print("No pairs")
else: 
    print(c//2)