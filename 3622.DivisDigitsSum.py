n = 231
n1 = n 
sum = 0 
prod = 1 
while(n>0):
    #print(n%10)
    sum+=(n%10) 
    prod*=(n%10)  
    
    n=n//10

if n1%(sum+prod)==0: 
    print("true")
else:
    print("false")