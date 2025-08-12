n = 2
w = 3
max_weight = 15
sum = 0
count = 0 
for i in range(n*n):
    if sum<max_weight: 
        sum+=w
        count+=1 
    else: 
        break
print(count)