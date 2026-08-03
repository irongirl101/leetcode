m = "xabax"
n = ""
for i in range(len(m)): 
    for j in range(len(m)):
        if n in m[i:j] and m[i]==m[j]:
            n= m[i:j+1]
        elif m[i:j] == m[j:i:-1] and len(m[i:j])>len(n): 
            n = m[i:j+1]
        
print(n)

# how to reduce this time to O(1) (palindromic thingy)