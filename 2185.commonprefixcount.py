words = ["pay","attention","practice","attend"]
pref = "at"

count = 0 
for i in range(len(words)): 
    for j in range(len(pref)):
        if words[i][j] == pref[j]: 
            count+=1 
print(count//len(pref))