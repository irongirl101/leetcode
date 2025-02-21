#logic - pascals triangle
'''
1;1,1;1,2,1;1,3,3,1;1,4,6,4,1;1,5,10,5,1; ... 
the first two rows will be present regardless, and it is required for the further operations. 
note that the length of the row is the number of the row 
and each row start and ends with 1. always. 

[[1],[1,1],[1,2,1],[1,3,3,1]]
'''

'''
logc

make a sub list, start and end it with 1 

'''
n = 7
pascal = [[1]]
i = 2 
while True:
    j = 0
    sub = [] #row in pascal
    l = pascal[-1] #last row in pascal
    for k in range(i): 
        if k == 0: 
            sub.append(1)
        elif k == i-1: 
            sub.append(1)
        else: 
           sub.append(l[k-1] + l[k])
    pascal.append(sub)
    i+=1
    if i == n+1:
        break

print(pascal)
        
        

