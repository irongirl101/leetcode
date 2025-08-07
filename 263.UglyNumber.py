n = 6
flag = "true"
for i in range(2,n): 
    if n%i == 0 and i!=2 and i!=3 and i!=5: 
        flag = "false"
        break 
print(flag)