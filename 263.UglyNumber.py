n = 2
flag = "true"

def isprime(x):
    for i in range(2,x//2): 
        if x%i == 0: 
            return 0
        
    return 1 

for i in range(2,n): 
    if n%i == 0 and i!=2 and i!=3 and i!=5 and isprime(i)==1: 
        flag = "false"
        break 
print(flag)