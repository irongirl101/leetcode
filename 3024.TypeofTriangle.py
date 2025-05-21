#an array is given, with 3 integers. using these 3 numbers, you need to return whether its equi, isco or scalene. if it cannot form a triangle, none must be returned 

#HOW TO CHECK WHETHER A TRIANGLE CAN BE FORMED USING  
'''
sides = [3,4,5]
sides[0]+sides[1] > sides[2]
sides[1]+sides[2] > sides[0]
sides[0]+sides[2] > sides[1]

makes a triangle. 

equilateral is when each side is of the same length 
isoceles is when 2 sides are of the same length 
scalene is when neither are of the same length 
'''

def count_occurences(data,element):
    count = 0 
    for i in range(len(data)): 
        if data[i] == element: 
            count+=1 
    return count

nums = [2,3,1]
#to check whether a triangle can be formed with those sides 
if ((nums[0]+nums[1])>nums[2]) and ((nums[0]+nums[2])>nums[1]) and ((nums[1]+nums[2])>nums[0]): 
    #print("Triangle")
    #num = nums[0]
    #print("trianlge")
    counts = [0,0,0]
    for i in range(len(nums)): 
        counts[i] =  count_occurences(nums,nums[i]) 

    for i in range(len(counts)): 
        if counts[i] == 2: 
            print("isoceles")
            break
        elif counts[i] == 3: 
            print("equilateral")
            break
        elif counts[i]==1 and counts[i+1]==1: 
            print("scalene")
            break
    #print(counts)
else: 
    print("None") 