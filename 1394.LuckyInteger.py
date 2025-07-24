#find the lucky integer in an array 
#a lucky integer is one that comes up that many times in an array 
#l = [1,2,2,3]
#finally display the greatest lucky integer 

l = [5,5,0,2,7,9,5,5,5,2]
#o(n2)
def nsqyare():
    final = -1
    for i in range(len(l)): 
        pos = l[i]
        count = 1
        for j in range(i+1,len(l)): 
            if pos == l[j]: 
                count+=1
        if pos == count and final<pos: 
            final = pos
    print(final)


'''final = -1 
count = 1
pos = l.pop()

for i in range(len(l)):
    x = l.pop()
    #print(x)
    if x == pos: 
        count+=1
    if pos==count: 
        final = pos
    else: 
        pos = x
        print(x)
    
print(final)'''
nsqyare()