#find the lucky integer in an array 
#a lucky integer is one that comes up that many times in an array 
#l = [1,2,2,3]
#finally display the greatest lucky integer 

l = [2,3,3]
final = -1; 
for i in range(len(l)): 
    pos = l[i]
    count = 1
    for j in range(i+1,len(l)): 
        if pos == l[j]: 
            count+=1
    if pos == count: 
        final = pos
print(final)