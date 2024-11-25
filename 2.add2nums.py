'''class Solution(object):
    def addTwoNumbers(self,l1,l2):
        answer_list1=[] #to make string into a list so that it becomes subscriptable
        answer_list=[]#expected result

        list1_string,list2_string='','' #changing list into string  
        for i in range(len(l1)-1,-1,-1): #going from right to left, as per the conditions
            list1_string+=str(l1[i])
        for i in range(len(l2)-1,-1,-1):
            list2_string+=str(l2[i])

        Sum= int(list1_string)+ int(list2_string)#adding the numbers
        SumStr=str(Sum)#converting to str so that each number could become its own entity
        for i in SumStr:
            answer_list1.append(i)#appending to external list

        for i in range(len(answer_list1)-1,-1,-1):
            answer_list.append(int(answer_list1[i]))#finally appeneding to final list.
        print(answer_list)
'''
'''
creating a linked list using stacks

'''
    


