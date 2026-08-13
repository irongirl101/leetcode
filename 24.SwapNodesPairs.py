#BS Method

head = [1,2,3]


i = 0 
j = 1 
while j < len(head) and i < len(head): 
    head[i],head[j] = head[j],head[i]
    i+=2
    j+=2 

print(head)