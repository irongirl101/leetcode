digits = [2, 2,8,8,2]
sums = []

for i in range(len(digits)): 
    #sum = 0
    if digits[i]%2 ==0: 
        #sum+=digits[i]
        for j in range(len(digits)): 
            if i!=j: 
                for k in range(len(digits)): 
                    if k!=j and digits[k]!=0 and k!=i:
                       if (digits[k]*100+ digits[j]*10+digits[i]) not in sums: 
                           sums.append (digits[k]*100+ digits[j]*10+digits[i])

if sums:                   
 print(sums)  
else: 
    print(0)
