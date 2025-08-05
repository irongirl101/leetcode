fruits = [4,2,5]
baskets = [3,5,4]

i = 0 
count = len(fruits)
j = 0
while j<len(baskets) and i<len(fruits): 
    flag = 0 
    if flag !=0:
        count-=1
        if baskets[j]>fruits[i]: 
            flag = 0
        else: 
            flag = 1
            j+=1
            #count+=1

    i+=1
print(count)