x = 2
y = 7
z = 4

def abs(a,b): 
    if a-b > 0: 
        return a-b 
    else: 
        return b-a 

if(abs(x,z)<abs(y,z)):
    print(1)
elif (abs(x,z)>(y,z)): 
    print(2) 
elif (abs(x,z)==abs(y,z)): 
    print(0)