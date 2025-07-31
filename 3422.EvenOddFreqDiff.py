s = "abcabcab"
a1 = 0
a2 = 0
for i in range(len(s)): 
    c=0
    p = s[i] 
    for j in range(len(s)): 
        if p == s[j]: 
            c+=1
    if c%2==0 and c>a2: 
        a2 = c 
        
    elif c%2!=0: 
        if c>a1:
            a1 = c
            
if a2>a1: 
    print(a2-a1)
else: 
    print(a1-a2)
    