s='luffy is still joyboy'  
s=s.split(' ')

maxl=0
for i in s:
    if i!='':
        x=len(i)
        if x>maxl:
            maxl=x
print(maxl)
