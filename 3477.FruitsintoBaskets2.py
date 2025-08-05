fruits = [3,6,1]
baskets = [6,4,7]

#use A GREEDY ALG 
#CHANGE THE ALREADY MATCHED UP TO A NUMBER LIKE -1 

count = 0
for i in range(len(fruits)): 
    for j in range(len(baskets)): 
        if fruits[i]<baskets[j] and fruits[i]!=-1 and baskets[j]!=-1:
            fruits[i]=-1
            baskets[j]=-1
            count+=1 
print(len(fruits)-count)
        
       
        