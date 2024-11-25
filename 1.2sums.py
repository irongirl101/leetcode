#problem 1 
class Solution(object):
    def twosum(nums,target):
        sumlist=[] #all the possible combinations in this list
        for value1_pos in range(len(nums)): #going over each number in the list
            value1= nums[value1_pos] #getting the value1 at value1_pos in nums
            value2= target-value1 #getting the difference  
            if value2 in nums and value1_pos != nums.index(value2): #checking if value2 is in nums, and checking if the position of value1 and value2 are same in nums (only applicable if value1=value2)
                sumlist.append([value1_pos,nums.index(value2)]) #appending the positions of the 2 values, according to problem statement
        answer=sumlist[0]#only the first answer is accepted, only in cases of multiple answers
        return answer#displaying answer wrt to problem statement

nums=[2,7,11,15]
target=9

soln =Solution(nums,target)

print(soln.twosum())

