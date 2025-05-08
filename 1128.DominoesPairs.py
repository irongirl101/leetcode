dominoes = [[1,2 ], [1,2 ], [1,1 ], [1,2 ], [2,2 ]] 
c = 0 
for i in range(len(dominoes)): 
    for j in range(len(dominoes)): 
        if i!=j: 
            if(dominoes[i][0]==dominoes[j][0]) and (dominoes[i][1]==dominoes[j][1]):
                c+=1
            elif(dominoes[i][0]==dominoes[j][1]) and (dominoes[i][1]==dominoes[j][0]) :
                c+=1
print(c//2)        
        
   
