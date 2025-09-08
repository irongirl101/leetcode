hours = [5,1,4,2,2]
target = 6
count = 0 
for i in range(len(hours)): 
    if hours[i] >= target: 
        count+=1
print(count)